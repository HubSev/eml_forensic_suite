# viewer.py
import os
import csv
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from common_utils import read_raw_headers, read_message_bodies


class EmlCsvViewerTab:
    """
    Onglet de visualisation forensic CSV / EML (lecture seule).

    Utilise shared_state pour récupérer éventuellement :
      - last_index_dir
      - last_index_csv
      - last_index_entries
    """

    def __init__(self, parent: ttk.Frame, shared_state: dict) -> None:
        self.parent = parent
        self.root = parent.winfo_toplevel()
        self.shared_state = shared_state

        # Dossier d’analyse courant (export IMAP)
        self.current_folder: str | None = None

        # Données de l'index en mémoire : liste de dicts (lignes CSV + full_path)
        self.index_entries: list[dict] = []

        # État de la recherche
        self.search_matches: list[int] = []  # indices de lignes dans index_entries
        self.search_current_idx: int = -1
        self.search_term: str = ""
        self.search_total_occurrences: int = 0

        self._build_ui()

        # Pré-remplir avec le dernier index connu, si dispo
        last_dir = self.shared_state.get("last_index_dir")
        if last_dir and os.path.isdir(last_dir):
            self.entry_folder.insert(0, last_dir)
        elif self.shared_state.get("last_export_dir") and os.path.isdir(
            self.shared_state["last_export_dir"]
        ):
            # fallback : dernier export IMAP si pas encore indexé
            self.entry_folder.insert(0, self.shared_state["last_export_dir"])

    # ------------------------------------------------------
    #   Construction UI
    # ------------------------------------------------------
    def _build_ui(self) -> None:
        main_frame = ttk.Frame(self.parent, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # ---------- Ligne choix dossier ----------
        folder_frame = ttk.Frame(main_frame)
        folder_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(folder_frame, text="Dossier d'analyse (export IMAP) :").pack(
            side=tk.LEFT
        )
        self.entry_folder = ttk.Entry(folder_frame, width=80)
        self.entry_folder.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        btn_browse = ttk.Button(
            folder_frame, text="Parcourir…", command=self.browse_folder
        )
        btn_browse.pack(side=tk.LEFT, padx=5)

        btn_load = ttk.Button(
            folder_frame, text="Charger index CSV", command=self.load_index_from_folder
        )
        btn_load.pack(side=tk.LEFT, padx=5)

        btn_use_last = ttk.Button(
            folder_frame,
            text="Utiliser le dernier index généré",
            command=self.use_last_index,
        )
        btn_use_last.pack(side=tk.LEFT, padx=5)

        # ---------- Résumé / infos ----------
        self.label_summary = ttk.Label(
            main_frame,
            text="Aucun index chargé.",
            foreground="gray",
            anchor="w",
        )
        self.label_summary.pack(fill=tk.X, pady=(0, 10))

        # ---------- Notebook : Tableau / Hashes / Rapport ----------
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Onglet 1 : tableau index
        self.tab_table = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_table, text="Index CSV")

        # Onglet 2 : hashes
        self.tab_hashes = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_hashes, text="hashes.txt")

        # Onglet 3 : rapport IMAP
        self.tab_rapport = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_rapport, text="rapport_imap_export.txt")

        # === Onglet tableau ===
        self._build_table_tab()

        # === Onglet hashes ===
        self._build_hashes_tab()

        # === Onglet rapport ===
        self._build_rapport_tab()

    # ------------------------------------------------------
    #   Construction onglets
    # ------------------------------------------------------
    def _build_table_tab(self) -> None:
        # Frame recherche + actions
        search_frame = ttk.LabelFrame(
            self.tab_table, text="Recherche dans l'index (lecture seule)"
        )
        search_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Label(search_frame, text="Texte à rechercher :").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        self.entry_search = ttk.Entry(search_frame, width=40)
        self.entry_search.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(search_frame, text="Champ :").grid(
            row=0, column=2, sticky="w", padx=5, pady=5
        )
        self.combo_field = ttk.Combobox(
            search_frame,
            state="readonly",
            values=[
                "Tous les champs",
                "folder_imap",
                "sequence_number",
                "date_header",
                "from_header",
                "to_header",
                "cc_header",
                "cci_header",
                "subject",
                "message_id",
                "sha256",
                "relative_path",
                "filename",
            ],
        )
        self.combo_field.current(0)
        self.combo_field.grid(row=0, column=3, sticky="w", padx=5, pady=5)

        self.var_case_sensitive = tk.BooleanVar(value=False)
        chk_case = ttk.Checkbutton(
            search_frame,
            text="Respecter la casse",
            variable=self.var_case_sensitive,
        )
        chk_case.grid(row=0, column=4, sticky="w", padx=5, pady=5)

        btn_search = ttk.Button(
            search_frame, text="Rechercher", command=self.run_search
        )
        btn_search.grid(row=0, column=5, sticky="w", padx=5, pady=5)

        btn_prev = ttk.Button(
            search_frame, text="⬆ Précédent", command=self.goto_prev_match
        )
        btn_prev.grid(row=0, column=6, sticky="w", padx=5, pady=5)

        btn_next = ttk.Button(
            search_frame, text="⬇ Suivant", command=self.goto_next_match
        )
        btn_next.grid(row=0, column=7, sticky="w", padx=5, pady=5)

        self.label_search_status = ttk.Label(
            search_frame,
            text="Aucune recherche.",
            foreground="gray",
        )
        self.label_search_status.grid(
            row=1, column=0, columnspan=8, sticky="w", padx=5, pady=(0, 5)
        )

        # Frame tableau
        table_frame = ttk.Frame(self.tab_table)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))

        # Colonnes du CSV (dans le même ordre que eml_indexer.py)
        columns = [
            "folder_imap",
            "sequence_number",
            "date_header",
            "from_header",
            "to_header",
            "cc_header",
            "cci_header",
            "subject",
            "message_id",
            "sha256",
            "relative_path",
            "filename",
        ]

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse",
        )

        headers_pretty = {
            "folder_imap": "Dossier IMAP",
            "sequence_number": "Séquence",
            "date_header": "Date",
            "from_header": "From",
            "to_header": "To",
            "cc_header": "Cc",
            "cci_header": "Cci",
            "subject": "Sujet",
            "message_id": "Message-ID",
            "sha256": "SHA-256",
            "relative_path": "Chemin relatif",
            "filename": "Nom de fichier",
        }

        for col in columns:
            self.tree.heading(col, text=headers_pretty.get(col, col))
            if col in ("folder_imap", "relative_path"):
                width = 200
            elif col in ("subject", "from_header", "to_header"):
                width = 250
            elif col in ("sha256", "message_id"):
                width = 260
            else:
                width = 120
            self.tree.column(col, width=width, anchor="w")

        vsb = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.tree.yview
        )
        hsb = ttk.Scrollbar(
            table_frame, orient="horizontal", command=self.tree.xview
        )
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        # Boutons actions sous le tableau
        action_frame = ttk.Frame(self.tab_table)
        action_frame.pack(fill=tk.X, padx=5, pady=(0, 5))

        btn_view_headers = ttk.Button(
            action_frame,
            text="Afficher les en-têtes bruts du message sélectionné",
            command=self.show_selected_headers,
        )
        btn_view_headers.pack(side=tk.LEFT, padx=5, pady=5)

        btn_view_full = ttk.Button(
            action_frame,
            text="Afficher le message complet (headers + corps)",
            command=self.show_selected_message,
        )
        btn_view_full.pack(side=tk.LEFT, padx=5, pady=5)

    def _build_hashes_tab(self) -> None:
        label = ttk.Label(
            self.tab_hashes,
            text="Contenu de hashes.txt (lecture seule).",
            anchor="w",
        )
        label.pack(fill=tk.X, padx=5, pady=(5, 0))

        frame = ttk.Frame(self.tab_hashes)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.text_hashes = tk.Text(frame, wrap="none", state="disabled")
        self.text_hashes.grid(row=0, column=0, sticky="nsew")

        vsb = ttk.Scrollbar(
            frame, orient="vertical", command=self.text_hashes.yview
        )
        hsb = ttk.Scrollbar(
            frame, orient="horizontal", command=self.text_hashes.xview
        )

        self.text_hashes.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

    def _build_rapport_tab(self) -> None:
        label = ttk.Label(
            self.tab_rapport,
            text="Contenu de rapport_imap_export.txt (lecture seule).",
            anchor="w",
        )
        label.pack(fill=tk.X, padx=5, pady=(5, 0))

        frame = ttk.Frame(self.tab_rapport)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.text_rapport = tk.Text(frame, wrap="word", state="disabled")
        self.text_rapport.grid(row=0, column=0, sticky="nsew")

        vsb = ttk.Scrollbar(
            frame, orient="vertical", command=self.text_rapport.yview
        )
        self.text_rapport.configure(yscrollcommand=vsb.set)
        vsb.grid(row=0, column=1, sticky="ns")

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

    # ------------------------------------------------------
    #   Choix dossier & chargement fichiers
    # ------------------------------------------------------
    def browse_folder(self) -> None:
        path = filedialog.askdirectory(
            title="Sélectionner le dossier d'analyse (export IMAP)"
        )
        if path:
            self.entry_folder.delete(0, tk.END)
            self.entry_folder.insert(0, path)

    def use_last_index(self) -> None:
        """
        Utilise directement le dernier index généré par l’onglet Indexer
        via shared_state (sans redemander de CSV si possible).
        """
        entries = self.shared_state.get("last_index_entries")
        folder = self.shared_state.get("last_index_dir")
        csv_path = self.shared_state.get("last_index_csv")

        if not entries or not folder:
            messagebox.showinfo(
                "Aucun index en mémoire",
                "Aucun index EML n'a encore été généré dans l'onglet 'Indexation EML'.",
            )
            return

        if not os.path.isdir(folder):
            messagebox.showwarning(
                "Dossier introuvable",
                f"Le dossier enregistré comme dernier index n'existe plus :\n{folder}",
            )
            return

        self.entry_folder.delete(0, tk.END)
        self.entry_folder.insert(0, folder)

        # On peuple directement à partir des entries en mémoire
        self._populate_from_entries(entries, folder, csv_path)

    def load_index_from_folder(self) -> None:
        folder = self.entry_folder.get().strip()
        if not folder:
            messagebox.showwarning(
                "Dossier manquant",
                "Merci de sélectionner un dossier d'analyse (export IMAP).",
            )
            return

        if not os.path.isdir(folder):
            messagebox.showerror("Erreur", "Ce dossier n'existe pas.")
            return

        self.current_folder = folder

        # 1) Charger index_eml.csv (ou autre fichier choisi par l'utilisateur)
        index_path = os.path.join(folder, "index_eml.csv")
        if not os.path.isfile(index_path):
            answer = messagebox.askyesno(
                "index_eml.csv introuvable",
                "Le fichier index_eml.csv n'a pas été trouvé dans ce dossier.\n"
                "Voulez-vous sélectionner manuellement un fichier CSV ?",
            )
            if not answer:
                return

            index_path = filedialog.askopenfilename(
                title="Sélectionner le fichier CSV d'index EML",
                initialdir=folder,
                filetypes=[("CSV", "*.csv"), ("Tous fichiers", "*.*")],
            )
            if not index_path:
                return

        try:
            with open(index_path, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f, delimiter=";")
                rows = list(reader)
        except Exception as e:
            messagebox.showerror(
                "Erreur lors du chargement CSV", f"{e}"
            )
            return

        # On convertit les rows CSV en entries compatibles (avec full_path)
        entries: list[dict] = []
        for row in rows:
            def get(col: str) -> str:
                return row.get(col, "") or ""

            folder_imap = get("folder_imap")
            seq = get("sequence_number")
            date_header = get("date_header")
            from_header = get("from_header")
            to_header = get("to_header")
            cc_header = get("cc_header")
            cci_header = get("cci_header")
            subject = get("subject")
            msgid = get("message_id")
            sha256 = get("sha256")
            rel_path = get("relative_path")
            filename = get("filename")

            full_path = ""
            if folder and rel_path:
                full_path = os.path.join(folder, rel_path)

            entry = {
                "folder_imap": folder_imap,
                "sequence_number": seq,
                "date_header": date_header,
                "from_header": from_header,
                "to_header": to_header,
                "cc_header": cc_header,
                "cci_header": cci_header,
                "subject": subject,
                "message_id": msgid,
                "sha256": sha256,
                "relative_path": rel_path,
                "filename": filename,
                "full_path": full_path,
            }
            entries.append(entry)

        # Mémoriser dans le shared_state pour les autres parties éventuelles
        self.shared_state["last_index_dir"] = folder
        self.shared_state["last_index_csv"] = index_path
        self.shared_state["last_index_entries"] = entries

        self._populate_from_entries(entries, folder, index_path)

    def _populate_from_entries(
        self, entries: list[dict], folder: str, index_path: str | None
    ) -> None:
        self.current_folder = folder
        self.index_entries = entries

        # Vider le tableau
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Reset recherche
        self.search_matches.clear()
        self.search_current_idx = -1
        self.search_term = ""
        self.search_total_occurrences = 0
        self.label_search_status.config(text="Aucune recherche.", foreground="gray")

        nb_messages = 0
        folders = set()
        with_sha = 0

        for i, entry in enumerate(entries):
            folder_imap = entry.get("folder_imap", "")
            seq = entry.get("sequence_number", "")
            date_header = entry.get("date_header", "")
            from_header = entry.get("from_header", "")
            to_header = entry.get("to_header", "")
            cc_header = entry.get("cc_header", "")
            cci_header = entry.get("cci_header", "")
            subject = entry.get("subject", "")
            msgid = entry.get("message_id", "")
            sha256 = entry.get("sha256", "")
            rel_path = entry.get("relative_path", "")
            filename = entry.get("filename", "")

            iid = str(i)
            self.tree.insert(
                "",
                "end",
                iid=iid,
                values=[
                    folder_imap,
                    seq,
                    date_header,
                    from_header,
                    to_header,
                    cc_header,
                    cci_header,
                    subject,
                    msgid,
                    sha256,
                    rel_path,
                    filename,
                ],
            )

            nb_messages += 1
            if folder_imap:
                folders.add(folder_imap)
            if sha256:
                with_sha += 1

        index_name = os.path.basename(index_path) if index_path else "(en mémoire)"
        summary = (
            f"Index chargé : {index_name}  |  "
            f"Messages indexés : {nb_messages}  |  "
            f"Dossiers IMAP distincts : {len(folders)}  |  "
            f"Messages avec SHA-256 : {with_sha}"
        )
        self.label_summary.config(text=summary, foreground="black")

        # Recharger hashes.txt et rapport pour ce dossier
        self._load_hashes_txt()
        self._load_rapport_txt()

    def _load_hashes_txt(self) -> None:
        self.text_hashes.config(state="normal")
        self.text_hashes.delete("1.0", tk.END)

        if not self.current_folder:
            self.text_hashes.insert(
                "1.0", "Aucun dossier d'analyse sélectionné.\n"
            )
        else:
            hashes_path = os.path.join(self.current_folder, "hashes.txt")
            if not os.path.isfile(hashes_path):
                self.text_hashes.insert(
                    "1.0",
                    "Fichier hashes.txt introuvable dans ce dossier.\n",
                )
            else:
                try:
                    with open(hashes_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    self.text_hashes.insert("1.0", content)
                except Exception as e:
                    self.text_hashes.insert(
                        "1.0",
                        f"Erreur lors de la lecture de hashes.txt : {e}\n",
                    )

        self.text_hashes.config(state="disabled")

    def _load_rapport_txt(self) -> None:
        self.text_rapport.config(state="normal")
        self.text_rapport.delete("1.0", tk.END)

        if not self.current_folder:
            self.text_rapport.insert(
                "1.0", "Aucun dossier d'analyse sélectionné.\n"
            )
        else:
            rapport_path = os.path.join(self.current_folder, "rapport_imap_export.txt")
            if not os.path.isfile(rapport_path):
                self.text_rapport.insert(
                    "1.0",
                    "Fichier rapport_imap_export.txt introuvable dans ce dossier.\n",
                )
            else:
                try:
                    with open(rapport_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    self.text_rapport.insert("1.0", content)
                except Exception as e:
                    self.text_rapport.insert(
                        "1.0",
                        f"Erreur lors de la lecture de rapport_imap_export.txt : {e}\n",
                    )

        self.text_rapport.config(state="disabled")

    # ------------------------------------------------------
    #   Recherche dans l'index CSV
    # ------------------------------------------------------
    def run_search(self) -> None:
        term = self.entry_search.get()
        if not term:
            messagebox.showinfo(
                "Recherche",
                "Merci de saisir un texte à rechercher.",
            )
            return

        if not self.index_entries:
            messagebox.showwarning(
                "Index manquant",
                "Aucun index en mémoire. Merci de charger un dossier / CSV d'abord.",
            )
            return

        field = self.combo_field.get()
        case_sensitive = self.var_case_sensitive.get()

        if not case_sensitive:
            term_cmp = term.lower()
        else:
            term_cmp = term

        matches: list[int] = []
        total_occurrences = 0

        for idx, entry in enumerate(self.index_entries):
            if field == "Tous les champs":
                values = [
                    str(v) for k, v in entry.items()
                    if k in (
                        "folder_imap",
                        "sequence_number",
                        "date_header",
                        "from_header",
                        "to_header",
                        "cc_header",
                        "cci_header",
                        "subject",
                        "message_id",
                        "sha256",
                        "relative_path",
                        "filename",
                    )
                ]
                haystack = " | ".join(values)
            else:
                haystack = str(entry.get(field, ""))

            if not case_sensitive:
                haystack_cmp = haystack.lower()
            else:
                haystack_cmp = haystack

            occ = haystack_cmp.count(term_cmp)
            if occ > 0:
                matches.append(idx)
                total_occurrences += occ

        self.search_matches = matches
        self.search_term = term
        self.search_total_occurrences = total_occurrences

        if not matches:
            self.search_current_idx = -1
            self.label_search_status.config(
                text=f"Aucun résultat pour « {term} ».",
                foreground="red",
            )
            return

        self.search_current_idx = 0
        self.label_search_status.config(
            text=(
                f"Recherche « {term} » : {len(matches)} lignes trouvées, "
                f"{total_occurrences} occurrence(s) au total."
            ),
            foreground="blue",
        )
        self._select_match_at_index(self.search_current_idx)

    def _select_match_at_index(self, match_index: int) -> None:
        if not self.search_matches:
            return
        if match_index < 0 or match_index >= len(self.search_matches):
            return

        row_idx = self.search_matches[match_index]
        iid = str(row_idx)

        self.tree.selection_remove(*self.tree.selection())
        self.tree.selection_set(iid)
        self.tree.focus(iid)
        self.tree.see(iid)

        self.label_search_status.config(
            text=(
                f"Recherche « {self.search_term} » : "
                f"résultat {match_index + 1}/{len(self.search_matches)} "
                f"– {self.search_total_occurrences} occurrence(s) au total."
            ),
            foreground="blue",
        )

    def goto_next_match(self) -> None:
        if not self.search_matches:
            messagebox.showinfo(
                "Recherche",
                "Aucun résultat à parcourir. Lance d'abord une recherche.",
            )
            return
        self.search_current_idx = (self.search_current_idx + 1) % len(
            self.search_matches
        )
        self._select_match_at_index(self.search_current_idx)

    def goto_prev_match(self) -> None:
        if not self.search_matches:
            messagebox.showinfo(
                "Recherche",
                "Aucun résultat à parcourir. Lance d'abord une recherche.",
            )
            return
        self.search_current_idx = (self.search_current_idx - 1) % len(
            self.search_matches
        )
        self._select_match_at_index(self.search_current_idx)

    # ------------------------------------------------------
    #   Affichage en-têtes bruts du message sélectionné
    # ------------------------------------------------------
    def _get_selected_entry(self) -> dict | None:
        if not self.index_entries:
            messagebox.showwarning(
                "Index manquant",
                "Aucun index en mémoire. Merci de charger un dossier / CSV d'abord.",
            )
            return None

        selection = self.tree.selection()
        if not selection:
            messagebox.showinfo(
                "Sélection manquante",
                "Merci de sélectionner une ligne dans le tableau.",
            )
            return None

        iid = selection[0]
        try:
            row_idx = int(iid)
        except ValueError:
            messagebox.showerror(
                "Erreur interne",
                "Impossible de retrouver la ligne sélectionnée.",
            )
            return None

        if row_idx < 0 or row_idx >= len(self.index_entries):
            messagebox.showerror(
                "Erreur interne",
                "Index de ligne hors limites.",
            )
            return None

        return self.index_entries[row_idx]

    def show_selected_headers(self) -> None:
        entry = self._get_selected_entry()
        if entry is None:
            return

        full_path = entry.get("full_path") or ""
        if not full_path or not os.path.isfile(full_path):
            messagebox.showerror(
                "Fichier introuvable",
                "Impossible de retrouver le fichier .eml sur disque "
                f"pour ce message.\n\nChemin attendu :\n{full_path}",
            )
            return

        try:
            raw_headers = read_raw_headers(full_path)
        except Exception as e:
            messagebox.showerror(
                "Erreur de lecture",
                f"Impossible de lire les en-têtes du fichier .eml : {e}",
            )
            return

        viewer = tk.Toplevel(self.root)
        viewer.title(
            f"En-têtes bruts – {entry.get('folder_imap', '')} / {entry.get('filename', '')}"
        )
        viewer.geometry("900x600")

        txt = tk.Text(viewer, wrap="none")
        txt.pack(fill="both", expand=True)

        scroll_y = ttk.Scrollbar(
            viewer, orient="vertical", command=txt.yview
        )
        scroll_x = ttk.Scrollbar(
            viewer, orient="horizontal", command=txt.xview
        )
        txt.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")

        txt.insert("1.0", raw_headers)
        txt.config(state="disabled")

    # ------------------------------------------------------
    #   Affichage message complet (headers + corps)
    # ------------------------------------------------------
    def show_selected_message(self) -> None:
        entry = self._get_selected_entry()
        if entry is None:
            return

        full_path = entry.get("full_path") or ""
        if not full_path or not os.path.isfile(full_path):
            messagebox.showerror(
                "Fichier introuvable",
                "Impossible de retrouver le fichier .eml sur disque "
                f"pour ce message.\n\nChemin attendu :\n{full_path}",
            )
            return

        try:
            raw_headers = read_raw_headers(full_path)
            text_body, html_body = read_message_bodies(full_path)
        except Exception as e:
            messagebox.showerror(
                "Erreur de lecture",
                f"Impossible de lire le message : {e}",
            )
            return

        viewer = tk.Toplevel(self.root)
        viewer.title(
            f"Message complet – {entry.get('folder_imap', '')} / {entry.get('filename', '')}"
        )
        viewer.geometry("1000x700")

        notebook = ttk.Notebook(viewer)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Onglet 1 : Résumé & texte
        tab_text = ttk.Frame(notebook)
        notebook.add(tab_text, text="Résumé & texte")

        frame_text = ttk.Frame(tab_text)
        frame_text.pack(fill=tk.BOTH, expand=True)

        txt_text = tk.Text(frame_text, wrap="word")
        txt_text.grid(row=0, column=0, sticky="nsew")

        vsb_text = ttk.Scrollbar(
            frame_text, orient="vertical", command=txt_text.yview
        )
        txt_text.configure(yscrollcommand=vsb_text.set)
        vsb_text.grid(row=0, column=1, sticky="ns")

        frame_text.rowconfigure(0, weight=1)
        frame_text.columnconfigure(0, weight=1)

        header_summary = (
            f"From   : {entry.get('from_header', '')}\n"
            f"To     : {entry.get('to_header', '')}\n"
            f"Cc     : {entry.get('cc_header', '')}\n"
            f"Date   : {entry.get('date_header', '')}\n"
            f"Sujet  : {entry.get('subject', '')}\n"
            f"Msg-ID : {entry.get('message_id', '')}\n"
            f"SHA256 : {entry.get('sha256', '')}\n"
            "\n"
            "===== Corps du message (text/plain) =====\n\n"
        )

        if text_body:
            txt_text.insert("1.0", header_summary + text_body)
        else:
            txt_text.insert(
                "1.0",
                header_summary
                + "[Aucun corps text/plain détecté dans ce message.]\n",
            )

        txt_text.config(state="disabled")

        # Onglet 2 : HTML brut
        tab_html = ttk.Frame(notebook)
        notebook.add(tab_html, text="HTML brut")

        frame_html = ttk.Frame(tab_html)
        frame_html.pack(fill=tk.BOTH, expand=True)

        txt_html = tk.Text(frame_html, wrap="none")
        txt_html.grid(row=0, column=0, sticky="nsew")

        vsb_html = ttk.Scrollbar(
            frame_html, orient="vertical", command=txt_html.yview
        )
        hsb_html = ttk.Scrollbar(
            frame_html, orient="horizontal", command=txt_html.xview
        )
        txt_html.configure(yscrollcommand=vsb_html.set, xscrollcommand=hsb_html.set)

        vsb_html.grid(row=0, column=1, sticky="ns")
        hsb_html.grid(row=1, column=0, sticky="ew")

        frame_html.rowconfigure(0, weight=1)
        frame_html.columnconfigure(0, weight=1)

        if html_body:
            txt_html.insert("1.0", html_body)
        else:
            txt_html.insert(
                "1.0",
                "[Aucun corps text/html détecté dans ce message.]\n",
            )
        txt_html.config(state="disabled")

        # Onglet 3 : En-têtes bruts
        tab_headers = ttk.Frame(notebook)
        notebook.add(tab_headers, text="En-têtes bruts")

        frame_headers = ttk.Frame(tab_headers)
        frame_headers.pack(fill=tk.BOTH, expand=True)

        txt_headers = tk.Text(frame_headers, wrap="none")
        txt_headers.grid(row=0, column=0, sticky="nsew")

        vsb_headers = ttk.Scrollbar(
            frame_headers, orient="vertical", command=txt_headers.yview
        )
        hsb_headers = ttk.Scrollbar(
            frame_headers, orient="horizontal", command=txt_headers.xview
        )
        txt_headers.configure(yscrollcommand=vsb_headers.set, xscrollcommand=hsb_headers.set)

        vsb_headers.grid(row=0, column=1, sticky="ns")
        hsb_headers.grid(row=1, column=0, sticky="ew")

        frame_headers.rowconfigure(0, weight=1)
        frame_headers.columnconfigure(0, weight=1)

        txt_headers.insert("1.0", raw_headers)
        txt_headers.config(state="disabled")


def build_viewer_tab(notebook: ttk.Notebook, shared_state: dict) -> None:
    """
    Construit l’onglet Viewer CSV/EML dans le Notebook principal.
    """
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="3. Viewer CSV / EML")
    EmlCsvViewerTab(tab, shared_state)
