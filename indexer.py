# indexer.py
import os
import csv
import threading
import queue
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from email import policy
from email.parser import BytesParser
from datetime import datetime

from common_utils import safe_folder_name, read_raw_headers


# --- Utilitaires EML & Hashes ---


def scan_eml_files(root_dir):
    """
    Parcourt récursivement root_dir et renvoie une liste de (full_path, rel_path)
    pour tous les fichiers .eml trouvés.
    """
    eml_files = []
    for current_root, _, files in os.walk(root_dir):
        for name in files:
            if name.lower().endswith(".eml"):
                full_path = os.path.join(current_root, name)
                rel_path = os.path.relpath(full_path, root_dir)
                eml_files.append((full_path, rel_path))
    return eml_files


def parse_eml_headers(path):
    """
    Lit un fichier .eml en lecture seule et extrait quelques en-têtes.
    NE MODIFIE JAMAIS LE FICHIER.
    """
    with open(path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    subject = msg["subject"] or ""
    from_ = msg["from"] or ""
    to = msg["to"] or ""
    cc = msg["cc"] or ""
    bcc = msg["bcc"] or ""
    date = msg["date"] or ""
    msg_id = msg["message-id"] or ""

    return {
        "subject": subject,
        "from": from_,
        "to": to,
        "cc": cc,
        "bcc": bcc,
        "date": date,
        "message_id": msg_id,
    }


def load_hashes(root_dir):
    """
    Charge hashes.txt s'il existe dans root_dir.
    Retourne un dict { chemin_relatif_disque_posix : sha256 } et le hash global éventuel.

    IMPORTANT : on adapte les chemins de hashes.txt (basés sur le nom IMAP)
    pour retrouver les chemins réels sur disque (basés sur safe_folder_name).
    """
    hashes_path = os.path.join(root_dir, "hashes.txt")
    hash_map = {}
    global_hash = None

    if not os.path.isfile(hashes_path):
        return hash_map, global_hash

    # Première passe : lignes individuelles "chemin : hash"
    with open(hashes_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "HASH GLOBAL" in line:
                continue
            if ":" not in line:
                continue

            left, right = line.split(":", 1)
            left = left.strip()
            right = right.strip()

            # On ne garde que ce qui ressemble vraiment à un hash
            if not (all(c in "0123456789abcdefABCDEF" for c in right) and len(right) >= 32):
                continue

            # left = chemin IMAP tel qu'écrit lors de l'export, ex : "INBOX/Secretariat/6829.eml"
            rel_posix_imap = left.replace("\\", "/")

            folder_imap_orig, filename = os.path.split(rel_posix_imap)
            if folder_imap_orig:
                safe_mb = safe_folder_name(folder_imap_orig)  # ex: "INBOX_Secretariat"
                disk_rel = f"{safe_mb}/{filename}"
            else:
                disk_rel = filename

            # Clé = chemin relatif tel qu'on le verra via os.walk (style POSIX)
            hash_map[disk_rel] = right

    # Deuxième passe : dernière ligne non vide = hash global (si format standard)
    with open(hashes_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        if lines:
            last = lines[-1]
            if all(c in "0123456789abcdefABCDEF" for c in last) and len(last) >= 32:
                global_hash = last

    return hash_map, global_hash


def build_index_csv(root_dir, log_callback, progress_callback=None):
    """
    Construit un fichier CSV index_eml.csv dans root_dir.
    Lit hashes.txt si présent pour ajouter la colonne sha256.
    Retourne (chemin_csv, liste_entries) où chaque entry contient aussi full_path.

    log_callback(msg: str) et progress_callback(pct: float) NE DOIVENT PAS
    toucher à Tkinter depuis ce thread.
    """
    eml_files = scan_eml_files(root_dir)
    total = len(eml_files)
    if total == 0:
        raise RuntimeError("Aucun fichier .eml trouvé dans ce dossier.")

    log_callback(f"{total} fichiers .eml trouvés. Chargement des hashes (si présents)...")

    hash_map, global_hash = load_hashes(root_dir)
    log_callback(f"{len(hash_map)} entrées de hash individuelles trouvées dans hashes.txt.")
    if global_hash:
        log_callback(f"Hash global (dans hashes.txt) : {global_hash}")

    log_callback("Début de l'indexation...\n")

    if progress_callback is not None:
        progress_callback(0.0)

    index_path = os.path.join(root_dir, "index_eml.csv")
    index_entries = []

    with open(index_path, "w", newline="", encoding="utf-8") as csvfile:
        # ordre plus humain
        fieldnames = [
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
            # infos de chemin à la fin
            "relative_path",
            "filename",
        ]

        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames,
            delimiter=";",          # IMPORTANT : ; pour Excel FR
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writeheader()

        for i, (full_path, rel_path) in enumerate(eml_files, start=1):
            log_callback(f"[{i}/{total}] Lecture des en-têtes : {rel_path}")

            headers = parse_eml_headers(full_path)

            folder_imap, filename = os.path.split(rel_path)
            if not folder_imap:
                folder_imap = "(racine)"

            seq = ""
            if filename.lower().endswith(".eml"):
                base = filename[:-4]
                if base.isdigit():
                    seq = base  # ex: "6829"

            # Chemin relatif disque en style POSIX pour lookup dans hash_map
            rel_posix_disk = rel_path.replace("\\", "/")
            sha256 = hash_map.get(rel_posix_disk, "")

            row = {
                "folder_imap": folder_imap,
                "sequence_number": seq,
                "date_header": headers["date"],
                "from_header": headers["from"],
                "to_header": headers["to"],
                "cc_header": headers["cc"],
                "cci_header": headers["bcc"],
                "subject": headers["subject"],
                "message_id": headers["message_id"],
                "sha256": sha256,
                "relative_path": rel_path,
                "filename": filename,
            }

            writer.writerow(row)

            # On mémorise aussi full_path pour le viewer interne
            entry = dict(row)
            entry["full_path"] = full_path
            index_entries.append(entry)

            # Mise à jour progression
            if progress_callback is not None and total > 0:
                pct = i / total * 100.0
                progress_callback(pct)

    return index_path, index_entries


# --- Interface graphique sous forme d’onglet ---


def build_indexer_tab(notebook: ttk.Notebook, shared_state: dict) -> None:
    """
    Construit l’onglet d’indexation EML dans le Notebook principal.
    shared_state est un dict partagé entre les onglets (export, index, viewer).
    On y stocke notamment :
      - last_export_dir    : dernier dossier d’export IMAP
      - last_index_dir     : dernier dossier indexé
      - last_index_csv     : chemin du CSV généré
      - last_index_entries : entries en mémoire (pour un éventuel usage ultérieur)
    """
    root = notebook.winfo_toplevel()

    tab = ttk.Frame(notebook)
    notebook.add(tab, text="2. Indexation EML")

    main_frame = ttk.Frame(tab, padding=10)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Stockage de l'index en mémoire pour le viewer interne (par séquence)
    index_entries: list[dict] = []
    progress_var = tk.DoubleVar(value=0.0)

    # Queues pour la communication thread worker -> thread UI
    log_queue: "queue.Queue[str]" = queue.Queue()
    progress_queue: "queue.Queue[float]" = queue.Queue()
    result_queue: "queue.Queue[tuple]" = queue.Queue()

    # ---------- Choix du dossier ----------
    ttk.Label(main_frame, text="Dossier d'export EML :").grid(
        row=0, column=0, sticky=tk.W, pady=5
    )
    entry_folder = ttk.Entry(main_frame, width=60)
    entry_folder.grid(row=0, column=1, sticky=tk.W, pady=5)

    def browse_folder():
        path = filedialog.askdirectory(title="Sélectionner le dossier d'export EML")
        if path:
            entry_folder.delete(0, tk.END)
            entry_folder.insert(0, path)

    btn_browse = ttk.Button(main_frame, text="Parcourir...", command=browse_folder)
    btn_browse.grid(row=0, column=2, padx=5, pady=5)

    def use_last_export():
        """
        Utilise le dernier dossier d'export IMAP connu (onglet 1),
        s'il est présent dans shared_state.
        """
        last_export = shared_state.get("last_export_dir")
        if not last_export:
            messagebox.showinfo(
                "Aucun export connu",
                "Aucun dossier d'export IMAP n'a encore été enregistré.\n"
                "Lance d'abord un export IMAP dans l'onglet 1.",
            )
            return
        if not os.path.isdir(last_export):
            messagebox.showwarning(
                "Dossier introuvable",
                f"Le dossier enregistré comme dernier export IMAP n'existe plus :\n{last_export}",
            )
            return
        entry_folder.delete(0, tk.END)
        entry_folder.insert(0, last_export)

    btn_use_last = ttk.Button(
        main_frame,
        text="Utiliser le dernier export IMAP",
        command=use_last_export,
    )
    btn_use_last.grid(row=1, column=1, sticky=tk.W, pady=(0, 5))

    # ---------- Zone de log ----------
    ttk.Label(main_frame, text="Journal :").grid(
        row=2, column=0, columnspan=3, sticky=tk.W, pady=(10, 0)
    )
    text_log = tk.Text(main_frame, height=12, wrap="word")
    text_log.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=5)

    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=text_log.yview)
    scrollbar.grid(row=3, column=3, sticky="ns")
    text_log.configure(yscrollcommand=scrollbar.set)

    def log(msg: str):
        """Log côté UI (thread principal uniquement)."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        text_log.insert(tk.END, f"[{timestamp}] {msg}\n")
        text_log.see(tk.END)
        text_log.update_idletasks()

    # ---------- Barre de progression ----------
    ttk.Label(main_frame, text="Progression :").grid(
        row=4, column=0, sticky=tk.W, pady=(5, 0)
    )
    progress_bar = ttk.Progressbar(
        main_frame,
        variable=progress_var,
        maximum=100.0,
        mode="determinate",
        length=400,
    )
    progress_bar.grid(row=4, column=1, sticky="w", pady=(5, 0))

    # ---------- Zone viewer interne (en-têtes bruts) ----------
    viewer_frame = ttk.LabelFrame(
        main_frame, text="Viewer en-têtes bruts (sans modifier les .eml)"
    )
    viewer_frame.grid(row=5, column=0, columnspan=3, sticky="ew", pady=(10, 0))

    ttk.Label(viewer_frame, text="Numéro de séquence (ex: 6829) :").grid(
        row=0, column=0, sticky=tk.W, pady=5
    )
    entry_seq = ttk.Entry(viewer_frame, width=10)
    entry_seq.grid(row=0, column=1, sticky=tk.W, pady=5)

    ttk.Label(viewer_frame, text="Dossier IMAP (optionnel) :").grid(
        row=0, column=2, sticky=tk.W, pady=5
    )
    entry_folder_filter = ttk.Entry(viewer_frame, width=20)
    entry_folder_filter.grid(row=0, column=3, sticky=tk.W, pady=5)

    def show_headers():
        seq = entry_seq.get().strip()
        folder_filter = entry_folder_filter.get().strip()

        if not index_entries:
            messagebox.showwarning(
                "Index manquant",
                "Aucun index en mémoire. Merci de construire l'index d'abord.",
            )
            return

        if not seq:
            messagebox.showwarning(
                "Séquence manquante",
                "Merci de renseigner un numéro de séquence (ex: 6829).",
            )
            return

        # Recherche de l'entrée correspondante
        matches = []
        for entry in index_entries:
            if entry.get("sequence_number") == seq:
                if folder_filter:
                    if entry.get("folder_imap") == folder_filter:
                        matches.append(entry)
                else:
                    matches.append(entry)

        if not matches:
            messagebox.showinfo(
                "Aucun résultat",
                "Aucun message trouvé pour cette séquence (et ce dossier, si précisé).",
            )
            return

        if len(matches) > 1:
            msg_info = "\n".join(
                f"- {m.get('folder_imap')} / {m.get('relative_path')}" for m in matches
            )
            if not messagebox.askyesno(
                "Plusieurs résultats",
                "Plusieurs messages correspondent à cette séquence.\n"
                "Afficher le premier trouvé ?\n\n" + msg_info,
            ):
                return

        entry = matches[0]
        full_path = entry["full_path"]
        try:
            raw_headers = read_raw_headers(full_path)
        except Exception as e:
            messagebox.showerror("Erreur de lecture", f"Impossible de lire les en-têtes : {e}")
            return

        viewer = tk.Toplevel(root)
        viewer.title(f"En-têtes bruts - {entry['folder_imap']} / {entry['filename']}")
        viewer.geometry("800x600")

        txt = tk.Text(viewer, wrap="none")
        txt.pack(fill="both", expand=True)

        scroll_y = ttk.Scrollbar(viewer, orient="vertical", command=txt.yview)
        scroll_y.pack(side="right", fill="y")
        txt.configure(yscrollcommand=scroll_y.set)

        scroll_x = ttk.Scrollbar(viewer, orient="horizontal", command=txt.xview)
        scroll_x.pack(side="bottom", fill="x")
        txt.configure(xscrollcommand=scroll_x.set)

        txt.insert("1.0", raw_headers)
        txt.config(state="disabled")

    btn_view = ttk.Button(viewer_frame, text="Afficher les en-têtes", command=show_headers)
    btn_view.grid(row=0, column=4, padx=10, pady=5)

    # ---------- Bouton de lancement de l'indexation ----------

    def on_run():
        nonlocal index_entries

        folder = entry_folder.get().strip()
        if not folder:
            messagebox.showwarning("Dossier manquant", "Merci de sélectionner un dossier d'export EML.")
            return
        if not os.path.isdir(folder):
            messagebox.showerror("Erreur", "Ce dossier n'existe pas.")
            return

        text_log.delete("1.0", tk.END)
        log(f"Dossier sélectionné : {folder}")
        log("Démarrage de l'indexation (lecture seule)...")
        progress_var.set(0.0)

        # Désactivation des contrôles pendant le traitement
        btn_run.config(state="disabled")
        btn_browse.config(state="disabled")
        btn_use_last.config(state="disabled")
        entry_folder.config(state="disabled")

        # Fonctions utilisées par le thread worker (ne touchent pas à Tkinter)
        def log_from_thread(msg: str):
            log_queue.put(msg)

        def progress_from_thread(pct: float):
            progress_queue.put(pct)

        def worker():
            try:
                index_path, entries = build_index_csv(
                    folder, log_from_thread, progress_from_thread
                )
                result_queue.put(("ok", index_path, entries, folder))
            except Exception as e:
                result_queue.put(("err", e))

        threading.Thread(target=worker, daemon=True).start()

    btn_run = ttk.Button(main_frame, text="Construire l'index (CSV)", command=on_run)
    btn_run.grid(row=6, column=0, columnspan=3, pady=10)

    # Layout responsive
    main_frame.rowconfigure(3, weight=1)
    main_frame.columnconfigure(1, weight=1)

    # ---------- Boucle de traitement des queues (UI) ----------

    def process_queues():
        nonlocal index_entries

        # Logs
        try:
            while True:
                msg = log_queue.get_nowait()
                log(msg)
        except queue.Empty:
            pass

        # Progression
        try:
            while True:
                pct = progress_queue.get_nowait()
                progress_var.set(pct)
        except queue.Empty:
            pass

        # Résultat final
        try:
            status, payload, *rest = result_queue.get_nowait()

            # Réactiver les contrôles
            btn_run.config(state="normal")
            btn_browse.config(state="normal")
            btn_use_last.config(state="normal")
            entry_folder.config(state="normal")

            if status == "ok":
                index_path = payload
                entries = rest[0]
                folder_used = rest[1]
                index_entries = entries

                # Mémoriser dans l'état partagé (pour le viewer global)
                shared_state["last_index_dir"] = folder_used
                shared_state["last_index_csv"] = index_path
                shared_state["last_index_entries"] = index_entries

                log("")
                log(f"Indexation terminée. Fichier CSV généré : {index_path}")
                log(f"{len(index_entries)} messages indexés en mémoire pour le viewer interne.")
                messagebox.showinfo(
                    "Indexation terminée",
                    f"L'index des fichiers EML a été généré.\n\nFichier :\n{index_path}\n\n"
                    "Vous pouvez l'ouvrir dans Excel / LibreOffice pour filtrer, trier et rechercher.\n"
                    "Le viewer interne peut maintenant afficher les en-têtes bruts via le numéro de séquence.\n"
                    "L'onglet '3. Viewer CSV/EML' peut également utiliser ce dossier.",
                )
            else:
                err = payload
                log(f"❌ Erreur : {err}")
                messagebox.showerror("Erreur pendant l'indexation", str(err))

        except queue.Empty:
            pass

        # Reprogrammer l'appel
        root.after(100, process_queues)

    # Démarrage du polling
    process_queues()
