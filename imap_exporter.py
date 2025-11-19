# imap_exporter.py
import imaplib
import hashlib
import os
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk, messagebox
import re
import time
import sys
import threading
import queue
import platform

from common_utils import (
    sha256_from_bytes,
    sha256_file,
    safe_folder_name,
    get_base_dir,
    get_tool_path,
)

# =========================
#      VERSION OUTIL
# =========================

VERSION = "1.0.3"


# =========================
#      UTILITAIRES IMAP
# =========================


def parse_french_date(date_str: str):
    """
    Prend une date JJ/MM/AAAA en entrée et renvoie un objet datetime.date.
    Lève ValueError si le format est invalide.
    """
    return datetime.strptime(date_str, "%d/%m/%Y").date()


def to_imap_date(d):
    """
    Convertit une date Python en format IMAP anglais: DD-Mon-YYYY
    Exemple : 01-Jan-2025
    """
    return d.strftime("%d-%b-%Y")


def decode_imap_mailbox(raw_line: bytes) -> str:
    """
    Extrait correctement le nom IMAP d'un dossier à partir de la ligne LIST.

    Exemple de lignes LIST :
      b'(\\HasNoChildren \\UnMarked \\Sent) "." "Sent"'
      b'(\\HasNoChildren \\UnMarked \\Trash) "." "Trash"'
      b'(\\HasNoChildren \\UnMarked) "/" "INBOX"'
    """
    line = raw_line.decode("utf-8", errors="replace").strip()

    # Patron classique IMAP : (FLAGS) "DELIM" NAME
    m = re.match(r'\((?P<flags>.*?)\)\s+"(?P<delim>.*)"\s+(?P<name>.*)$', line)
    if not m:
        return line

    name = m.group("name").strip()

    if name.startswith('"') and name.endswith('"'):
        name = name[1:-1]

    # Décodage UTF-7 IMAP pour les dossiers avec accents
    try:
        decoded = imaplib.IMAP4._utf7_decode(name)[0]
    except Exception:
        decoded = name

    return decoded


# =========================
#   RAPPORT FORENSIC
# =========================


def write_report(export_dir: str, stats: dict, hashes_path: str) -> None:
    """
    Écrit rapport_imap_export.txt + ajoute son hash dans hashes.txt
    (sans modifier le hash global des messages).
    """
    rapport_path = os.path.join(export_dir, "rapport_imap_export.txt")

    start_utc = stats.get("analysis_start_utc")
    end_utc = stats.get("analysis_end_utc")
    start_local = stats.get("analysis_start_local")
    end_local = stats.get("analysis_end_local")
    duration = None
    if start_utc and end_utc:
        duration = end_utc - start_utc

    env = stats.get("env", {})
    folders = stats.get("folders", {})

    with open(rapport_path, "w", encoding="utf-8") as f:
        f.write("=== Rapport d'export IMAP (lecture seule) ===\n\n")
        f.write(f"Outil      : imap_eml_downloader.py\n")
        f.write(f"Version    : {stats.get('version')}\n")
        f.write(f"Dossier    : {export_dir}\n\n")

        # Outil / intégrité
        f.write("---- Informations sur l'outil ----\n")
        f.write(f"Chemin de l'outil       : {stats.get('tool_path')}\n")
        f.write(f"SHA-256 de l'outil      : {stats.get('tool_hash')}\n\n")

        # Environnement d'exécution
        f.write("---- Environnement d'exécution ----\n")
        f.write(
            "Système d'exploitation : "
            f"{env.get('os_system')} {env.get('os_release')} "
            f"({env.get('os_version')}) / {env.get('machine')}\n"
        )
        f.write(f"Version Python          : {env.get('python_version')}\n\n")

        # Contexte IMAP / compte
        f.write("---- Contexte IMAP / compte ----\n")
        f.write(f"Serveur IMAP : {stats.get('host')}\n")
        f.write(f"Compte      : {stats.get('user')}\n")
        f.write(f"Date début demandée : {stats.get('date_start_text')}\n")
        f.write(f"Date fin demandée   : {stats.get('date_end_text')}\n")
        f.write(
            f"Critères IMAP       : {stats.get('search_criteria')} "
            "(tels qu'envoyés au serveur)\n"
        )
        f.write("\nDossiers sélectionnés :\n")
        for mb in stats.get("dossiers_selectionnes", []):
            f.write(f"  - {mb}\n")
        f.write("\n")

        # Infos serveur IMAP
        f.write("---- Informations serveur IMAP ----\n")
        greeting = stats.get("imap_greeting")
        capability = stats.get("imap_capability")
        if greeting:
            f.write(f"Bannière IMAP : {greeting}\n")
        if capability:
            f.write(f"CAPABILITY    : {capability}\n")
        f.write("\n")

        # Horodatage analyse
        f.write("---- Horodatage de l'analyse ----\n")
        if start_utc:
            f.write(f"Début analyse (UTC)   : {start_utc.isoformat()}Z\n")
        if start_local:
            f.write(f"Début analyse (local) : {start_local.isoformat()}\n")
        if end_utc:
            f.write(f"Fin analyse (UTC)     : {end_utc.isoformat()}Z\n")
        if end_local:
            f.write(f"Fin analyse (local)   : {end_local.isoformat()}\n")
        if duration is not None:
            f.write(f"Durée totale          : {duration}\n")
        f.write("\n")

        # Dossiers analysés
        f.write("---- Dossiers analysés ----\n")
        f.write(
            f"Nombre de dossiers sélectionnés : "
            f"{len(folders)}\n\n"
        )

        global_msgs = 0
        global_exported = 0
        global_errors = 0
        global_bytes = 0

        for name, info in folders.items():
            msgs = info.get("messages", 0)
            exported = info.get("exported", 0)
            errors = info.get("errors", 0)
            size_bytes = info.get("bytes", 0)
            min_size = info.get("min_size")
            max_size = info.get("max_size")
            sum_size = info.get("sum_size", 0)
            error_uids = info.get("error_uids", [])
            first_int = info.get("first_internaldate")
            last_int = info.get("last_internaldate")

            global_msgs += msgs
            global_exported += exported
            global_errors += errors
            global_bytes += size_bytes

            f.write(f"Dossier : {name}\n")
            f.write(f"  Messages trouvés (période) : {msgs}\n")
            f.write(f"  Messages exportés          : {exported}\n")
            f.write(f"  Erreurs de fetch           : {errors}\n")
            f.write(f"  Volume téléchargé          : {size_bytes} octets\n")

            if min_size is not None and max_size is not None and exported > 0:
                avg_size = sum_size / exported
                f.write(
                    "  Taille min / max / moyenne : "
                    f"{min_size} / {max_size} / {int(avg_size)} octets\n"
                )

            if first_int and last_int:
                try:
                    first_str = first_int.isoformat()
                except Exception:
                    first_str = str(first_int)
                try:
                    last_str = last_int.isoformat()
                except Exception:
                    last_str = str(last_int)
                f.write(
                    "  Période couverte (INTERNALDATE) : "
                    f"{first_str} → {last_str}\n"
                )

            if error_uids:
                f.write(
                    "  UIDs en erreur (liste non exhaustive) : "
                    + ", ".join(error_uids)
                    + "\n"
                )

            f.write("\n")

        # Totaux globaux
        f.write("---- Totaux globaux ----\n")
        f.write(
            f"Messages trouvés (tous dossiers) : "
            f"{global_msgs}\n"
        )
        f.write(
            f"Messages exportés                : "
            f"{global_exported}\n"
        )
        f.write(
            f"Erreurs de fetch                 : "
            f"{global_errors}\n"
        )
        f.write(
            f"Volume total téléchargé          : "
            f"{global_bytes} octets\n"
        )
        f.write("\n")

        # Méthodologie (texte fixe)
        f.write("---- Méthodologie et garanties forensic ----\n")
        f.write(
            "- L'outil n'a utilisé que des commandes IMAP en lecture seule "
            "(SELECT en readonly, SEARCH, FETCH). Aucun message n'a été "
            "modifié, supprimé ou marqué comme lu pendant l'analyse.\n"
        )
        f.write(
            "- Les messages ont été exportés tels que fournis par le serveur IMAP, "
            "et écrits sur disque en format .eml sans altération du contenu.\n"
        )
        f.write(
            "- Chaque message exporté est associé à un hash SHA-256, listé dans "
            "le fichier hashes.txt, ainsi qu'à un hash global calculé sur la "
            "concaténation de tous les hashes individuels.\n"
        )
        f.write(
            "- Le présent rapport d'analyse est lui-même hashé en SHA-256, et "
            "ce hash est ajouté à hashes.txt pour garantir l'intégrité du "
            "rapport.\n"
        )

    # Hash du rapport
    report_hash = sha256_file(rapport_path)

    # Ajout dans hashes.txt (sans toucher au hash global des messages)
    with open(hashes_path, "a", encoding="utf-8") as f:
        f.write("\nRAPPORT D'ANALYSE :\n")
        f.write(f"rapport_imap_export.txt : {report_hash}\n")


# =========================
#   TRAVAILLEUR IMAP
# =========================


def export_imap_worker(
    host: str,
    user: str,
    password: str,
    date_debut,          # datetime.date | None
    date_fin,            # datetime.date | None
    mailboxes: list[str],
    q: "queue.Queue[tuple[str, object]]",
    stop_event: threading.Event | None = None,
) -> None:
    """
    Fonction exécutée dans un thread de fond.
    Elle NE TOUCHE JAMAIS à Tkinter directement.
    Toutes les infos passent par la queue q.

    Messages envoyés dans q :
      ("log", str)              : ligne de log
      ("progress_total", int)   : nombre total de messages
      ("progress", int)         : nombre de messages déjà téléchargés
      ("info", str)             : message d'info (popup)
      ("error", str)            : message d'erreur (popup)
      ("export_dir", str)       : chemin du dossier d'export
      ("done", None)            : traitement terminé (succès ou erreur)
    """

    def send(kind: str, payload: object):
        q.put((kind, payload))

    def log(msg: str):
        send("log", msg)

    if not mailboxes:
        send("error", "Aucun dossier sélectionné.")
        send("done", None)
        return

    base_dir = get_base_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_user = (
        user.replace("@", "_at_")
        .replace(":", "_")
        .replace("\\", "_")
        .replace("/", "_")
    )
    export_dir = os.path.join(base_dir, f"export_{safe_user}_{timestamp}")
    os.makedirs(export_dir, exist_ok=True)

    log(f"Dossier d'export : {export_dir}")
    # Permet aux autres onglets de récupérer le dossier d'export
    send("export_dir", export_dir)

    # --- Stats globales pour le rapport ---
    tool_path = get_tool_path()
    tool_hash = ""
    try:
        if os.path.isfile(tool_path):
            tool_hash = sha256_file(tool_path)
    except Exception:
        tool_hash = "(erreur lors du calcul du hash de l'outil)"

    stats: dict = {
        "version": VERSION,
        "analysis_start_utc": datetime.utcnow(),
        "analysis_start_local": datetime.now(),
        "analysis_end_utc": None,
        "analysis_end_local": None,
        "host": host,
        "user": user,
        "dossiers_selectionnes": list(mailboxes),
        "folders": {},  # {mb_name: {...}}
        "search_criteria": None,
        "date_start_text": None,
        "date_end_text": None,
        "tool_path": tool_path,
        "tool_hash": tool_hash,
        "env": {
            "os_system": platform.system(),
            "os_release": platform.release(),
            "os_version": platform.version(),
            "machine": platform.machine(),
            "python_version": sys.version.replace("\n", " "),
        },
        "imap_greeting": None,
        "imap_capability": None,
    }

    M = None
    all_hashes: list[tuple[str, str]] = []
    total_msgs = 0

    try:
        log("Connexion au serveur IMAP...")
        M = imaplib.IMAP4_SSL(host)

        # Bannière IMAP (si dispo)
        try:
            greeting = getattr(M, "welcome", None)
            if isinstance(greeting, bytes):
                greeting_str = greeting.decode("utf-8", errors="replace")
            else:
                greeting_str = str(greeting) if greeting is not None else ""
            stats["imap_greeting"] = greeting_str
        except Exception:
            stats["imap_greeting"] = "(non disponible)"

        log("Authentification...")
        M.login(user, password)

        # CAPABILITY
        try:
            typ_cap, caps = M.capability()
            if typ_cap == "OK":
                if isinstance(caps, list):
                    joined = b" ".join(caps)
                else:
                    joined = caps
                stats["imap_capability"] = joined.decode("utf-8", errors="replace")
        except Exception:
            stats["imap_capability"] = "(erreur lors de CAPABILITY)"

        # Préparation des critères de recherche communs
        search_criteria: list[str] = []

        if date_debut is not None:
            since_str = to_imap_date(date_debut)
            log(
                "Date de début (incluse) : "
                f"{date_debut.strftime('%d/%m/%Y')} → IMAP SINCE {since_str}"
            )
            search_criteria.extend(["SINCE", since_str])
            stats["date_start_text"] = date_debut.strftime("%d/%m/%Y")
        else:
            log(
                "Date de début : non renseignée → extraction depuis le "
                "premier message disponible."
            )
            stats["date_start_text"] = (
                "Premier message disponible (pas de limite basse)"
            )

        if date_fin is not None:
            date_fin_plus_1 = date_fin + timedelta(days=1)
            before_str = to_imap_date(date_fin_plus_1)
            log(
                "Date de fin (incluse) : "
                f"{date_fin.strftime('%d/%m/%Y')} → IMAP BEFORE {before_str}"
            )
            search_criteria.extend(["BEFORE", before_str])
            stats["date_end_text"] = date_fin.strftime("%d/%m/%Y")
        else:
            log(
                "Date de fin : non renseignée → jusqu'à la dernière date "
                "disponible sur le serveur."
            )
            stats["date_end_text"] = (
                "Dernier message disponible (pas de limite haute)"
            )

        if not search_criteria:
            # Ni SINCE ni BEFORE : on prend tout
            search_criteria = ["ALL"]

        stats["search_criteria"] = " ".join(search_criteria)

        log(f"Critères IMAP utilisés : {search_criteria}")
        log("")
        log(f"Dossiers sélectionnés ({len(mailboxes)}) :")
        for mb in mailboxes:
            log(f"  - {mb}")
            stats["folders"][mb] = {
                "messages": 0,
                "exported": 0,
                "errors": 0,
                "bytes": 0,
                "min_size": None,
                "max_size": None,
                "sum_size": 0,
                "first_internaldate": None,
                "last_internaldate": None,
                "error_uids": [],
            }
        log("")

        # ---------- Phase 1 : comptage des messages ----------
        mailbox_to_msgs: dict[str, list[bytes]] = {}
        total_to_download = 0

        for mb_name in mailboxes:
            if stop_event and stop_event.is_set():
                log("Arrêt demandé pendant la phase de comptage.")
                send("done", None)
                return

            log(f"[Phase 1] Comptage des messages dans {mb_name}...")
            quoted_name = f'"{mb_name}"'  # important pour les noms avec espaces

            typ, _ = M.select(quoted_name, readonly=True)
            if typ != "OK":
                log(
                    "  ⚠️ Impossible de sélectionner ce dossier, "
                    "on passe au suivant."
                )
                continue

            typ, msgnums = M.search(None, *search_criteria)
            if typ != "OK":
                log(
                    "  ⚠️ Erreur lors de la recherche dans ce dossier, "
                    "on passe au suivant."
                )
                continue

            msg_list = msgnums[0].split()
            mailbox_to_msgs[mb_name] = msg_list
            total_in_folder = len(msg_list)
            total_to_download += total_in_folder

            mb_stats = stats["folders"].get(mb_name)
            if mb_stats is not None:
                mb_stats["messages"] = total_in_folder

            log(f"  → {total_in_folder} messages à traiter dans {mb_name}")

        log("")
        log(
            "Nombre total de messages à télécharger (tous dossiers) : "
            f"{total_to_download}"
        )
        log("")

        send("progress_total", total_to_download)
        downloaded_count = 0

        # ---------- Phase 2 : téléchargement + hashing ----------
        for mb_name, msg_list in mailbox_to_msgs.items():
            if stop_event and stop_event.is_set():
                log("Arrêt demandé : on interrompt l'extraction.")
                break

            log(f"=== Dossier : {mb_name} ===")

            mb_stats = stats["folders"].get(mb_name)
            if mb_stats is None:
                mb_stats = {
                    "messages": 0,
                    "exported": 0,
                    "errors": 0,
                    "bytes": 0,
                    "min_size": None,
                    "max_size": None,
                    "sum_size": 0,
                    "first_internaldate": None,
                    "last_internaldate": None,
                    "error_uids": [],
                }
                stats["folders"][mb_name] = mb_stats

            if not msg_list:
                log(f"  Aucun message dans {mb_name} pour cette période.")
                log("")
                continue

            safe_mb = safe_folder_name(mb_name)
            mb_dir = os.path.join(export_dir, safe_mb)
            os.makedirs(mb_dir, exist_ok=True)

            total_in_folder = len(msg_list)
            log(f"  Nombre de messages trouvés dans {mb_name} : {total_in_folder}")

            # Période couverte (INTERNALDATE) : on regarde seulement 1er et dernier
            try:
                first_uid = msg_list[0]
                last_uid = msg_list[-1]

                for label, uid in (
                    ("first_internaldate", first_uid),
                    ("last_internaldate", last_uid),
                ):
                    typ_int, data_int = M.fetch(uid, "(INTERNALDATE)")
                    if typ_int == "OK" and data_int and isinstance(data_int[0], tuple):
                        header_bytes = data_int[0][0]
                        if isinstance(header_bytes, bytes):
                            header_str = header_bytes.decode(
                                "utf-8", errors="replace"
                            )
                        else:
                            header_str = str(header_bytes)
                        m_int = re.search(
                            r'INTERNALDATE "([^"]+)"', header_str
                        )
                        if m_int:
                            date_str = m_int.group(1)
                            try:
                                dt_int = datetime.strptime(
                                    date_str, "%d-%b-%Y %H:%M:%S %z"
                                )
                                mb_stats[label] = dt_int
                            except Exception:
                                # en cas de parse raté, on laisse None
                                pass
            except Exception:
                # on ne bloque pas l'export si INTERNALDATE pose problème
                pass

            quoted_name = f'"{mb_name}"'
            typ, _ = M.select(quoted_name, readonly=True)
            if typ != "OK":
                log(
                    "  ⚠️ Impossible de re-sélectionner ce dossier, "
                    "on passe au suivant."
                )
                continue

            for idx, num in enumerate(msg_list, start=1):
                if stop_event and stop_event.is_set():
                    log("Arrêt demandé : on interrompt l'extraction.")
                    break

                num_str = num.decode()

                # Log allégé
                if idx == 1:
                    log(f"  Téléchargement du premier message ({num_str})...")
                elif idx % 500 == 0 or idx == total_in_folder:
                    log(
                        f"  Progression dossier {mb_name} : "
                        f"{idx}/{total_in_folder} (dernier : {num_str})"
                    )

                typ, msg_data = M.fetch(num, "(RFC822)")
                if typ != "OK":
                    log(
                        "    ⚠️ Erreur lors du fetch du message "
                        f"{num_str}, on continue."
                    )
                    if mb_stats is not None:
                        mb_stats["errors"] += 1
                        if len(mb_stats["error_uids"]) < 50:
                            mb_stats["error_uids"].append(num_str)
                    continue

                raw = msg_data[0][1]
                size_bytes = len(raw)

                file_hash = sha256_from_bytes(raw)

                filename = os.path.join(mb_dir, f"{num_str}.eml")
                with open(filename, "wb") as f:
                    f.write(raw)

                rel_path = f"{mb_name}/{num_str}.eml"
                all_hashes.append((rel_path, file_hash))
                total_msgs += 1

                if mb_stats is not None:
                    mb_stats["exported"] += 1
                    mb_stats["bytes"] += size_bytes
                    mb_stats["sum_size"] += size_bytes
                    if mb_stats["min_size"] is None or size_bytes < mb_stats["min_size"]:
                        mb_stats["min_size"] = size_bytes
                    if mb_stats["max_size"] is None or size_bytes > mb_stats["max_size"]:
                        mb_stats["max_size"] = size_bytes

                downloaded_count += 1
                send("progress", downloaded_count)

                # Petite pause toutes les 200 itérations pour laisser respirer la machine
                if downloaded_count % 200 == 0:
                    time.sleep(0.01)

            log(f"  Fin du dossier {mb_name}")
            log("")

        # ---------- Hash global des messages ----------
        global_hash = hashlib.sha256()
        for _, h in all_hashes:
            global_hash.update(h.encode())

        hashes_path = os.path.join(export_dir, "hashes.txt")
        with open(hashes_path, "w", encoding="utf-8") as f:
            f.write("Liste des fichiers exportés et leurs hashes SHA-256\n\n")
            for rel_path, h in all_hashes:
                f.write(f"{rel_path} : {h}\n")
            f.write("\nHASH GLOBAL (messages uniquement) :\n")
            f.write(global_hash.hexdigest() + "\n")

        log("")
        log("=== Export terminé ===")
        log(f"Nombre total de messages exportés : {total_msgs}")
        log(f"Fichier des hashes : {hashes_path}")
        log(f"HASH GLOBAL : {global_hash.hexdigest()}")

        summary = (
            "Extraction terminée.\n\n"
            f"Messages exportés : {total_msgs}\n"
            f"Dossier : {export_dir}\n\n"
            f"Hash global (messages) :\n{global_hash.hexdigest()}"
        )
        send("info", summary)

        # ---------- Rapport forensic ----------
        stats["analysis_end_utc"] = datetime.utcnow()
        stats["analysis_end_local"] = datetime.now()
        try:
            write_report(export_dir, stats, hashes_path)
            log("Rapport d'analyse généré et hashé (voir rapport_imap_export.txt et hashes.txt).")
        except Exception as e:
            log(f"⚠️ Impossible de générer le rapport d'analyse : {e}")

    except Exception as e:
        send("error", f"Une erreur est survenue : {e}")

    finally:
        if M is not None:
            try:
                M.logout()
            except Exception:
                pass
        send("done", None)


# =========================
#       INTERFACE TK
# =========================


def fetch_mailboxes(host: str, user: str, password: str, log_widget: tk.Text):
    """
    Se connecte au serveur IMAP, récupère la liste des dossiers (LIST)
    et les renvoie.
    """

    def log(msg: str) -> None:
        log_widget.insert(tk.END, msg + "\n")
        log_widget.see(tk.END)
        log_widget.update_idletasks()

    M = None
    mailboxes = []

    try:
        log("Connexion au serveur IMAP pour énumérer les dossiers...")
        M = imaplib.IMAP4_SSL(host)
        log("Authentification...")
        M.login(user, password)

        typ, data = M.list()
        if typ != "OK":
            raise RuntimeError("Impossible de lister les dossiers IMAP.")

        log("Dossiers trouvés sur le serveur :")
        for raw in data:
            if raw is None:
                continue
            name = decode_imap_mailbox(raw)
            mailboxes.append(name)
            log(f"  - {name}")

        log("")
        log(f"Total dossiers IMAP : {len(mailboxes)}")

        return mailboxes

    except Exception as e:
        messagebox.showerror(
            "Erreur", f"Erreur lors de la récupération des dossiers IMAP : {e}"
        )
        log(f"❌ Erreur lors de la récupération des dossiers : {e}")
        return []

    finally:
        if M is not None:
            try:
                M.logout()
            except Exception:
                pass


def build_imap_tab(notebook: ttk.Notebook, shared_state: dict) -> None:
    """
    Construit l'onglet 'Export IMAP forensic (lecture seule)' dans le Notebook
    principal. shared_state est un dict partagé entre onglets.
    """
    root = notebook.winfo_toplevel()

    tab = ttk.Frame(notebook)
    notebook.add(tab, text="1. Export IMAP")

    main_frame = ttk.Frame(tab, padding=10)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Variables partagées
    mailbox_vars: list[tuple[str, tk.BooleanVar]] = []
    select_all_var = tk.BooleanVar(value=False)
    progress_var = tk.DoubleVar(value=0.0)
    progress_total = {"value": 0}
    worker_thread: dict[str, threading.Thread | None] = {"t": None}
    stop_event = threading.Event()
    q: "queue.Queue[tuple[str, object]]" = queue.Queue()

    # Ligne 0 : serveur
    ttk.Label(main_frame, text="Serveur IMAP :").grid(
        row=0, column=0, sticky=tk.W, pady=5
    )
    entry_host = ttk.Entry(main_frame, width=40)
    entry_host.grid(row=0, column=1, sticky=tk.W, pady=5)
    entry_host.insert(0, "imap.exemple.com")  # valeur par défaut

    # Ligne 1 : email
    ttk.Label(main_frame, text="Adresse e-mail :").grid(
        row=1, column=0, sticky=tk.W, pady=5
    )
    entry_user = ttk.Entry(main_frame, width=40)
    entry_user.grid(row=1, column=1, sticky=tk.W, pady=5)

    # Ligne 2 : mot de passe
    ttk.Label(main_frame, text="Mot de passe :").grid(
        row=2, column=0, sticky=tk.W, pady=5
    )
    entry_password = ttk.Entry(main_frame, width=40, show="*")
    entry_password.grid(row=2, column=1, sticky=tk.W, pady=5)

    # Ligne 3 : date de début (optionnelle)
    ttk.Label(
        main_frame,
        text="Date de début (JJ/MM/AAAA, optionnelle) :",
    ).grid(row=3, column=0, sticky=tk.W, pady=5)
    entry_date_start = ttk.Entry(main_frame, width=20)
    entry_date_start.grid(row=3, column=1, sticky=tk.W, pady=5)
    # Pas de valeur par défaut → vide = tout l'historique

    # Ligne 4 : date de fin
    ttk.Label(
        main_frame,
        text="Date de fin (JJ/MM/AAAA, optionnelle) :",
    ).grid(row=4, column=0, sticky=tk.W, pady=5)
    entry_date_end = ttk.Entry(main_frame, width=20)
    entry_date_end.grid(row=4, column=1, sticky=tk.W, pady=5)

    # Zone de log
    ttk.Label(main_frame, text="Journal :").grid(
        row=5, column=0, columnspan=3, sticky=tk.W, pady=(10, 0)
    )
    text_log = tk.Text(main_frame, height=10, wrap="word")
    text_log.grid(row=6, column=0, columnspan=3, sticky="nsew", pady=5)

    scrollbar = ttk.Scrollbar(
        main_frame, orient="vertical", command=text_log.yview
    )
    scrollbar.grid(row=6, column=3, sticky="ns")
    text_log.configure(yscrollcommand=scrollbar.set)

    # Ligne 7 : cadre des dossiers avec cases à cocher
    ttk.Label(main_frame, text="Dossiers IMAP à exporter :").grid(
        row=7, column=0, columnspan=3, sticky=tk.W, pady=(10, 0)
    )

    mailbox_frame = ttk.Frame(main_frame, borderwidth=1, relief="solid")
    mailbox_frame.grid(row=8, column=0, columnspan=3, sticky="nsew", pady=5)

    canvas = tk.Canvas(mailbox_frame)
    scrollbar_mb = ttk.Scrollbar(
        mailbox_frame, orient="vertical", command=canvas.yview
    )
    mailbox_frame_inner = ttk.Frame(canvas)

    mailbox_frame_inner.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
    )

    canvas.create_window((0, 0), window=mailbox_frame_inner, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar_mb.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_mb.pack(side="right", fill="y")

    # Case à cocher "Tout cocher / Tout décocher"
    def on_toggle_select_all():
        val = select_all_var.get()
        for _, var in mailbox_vars:
            var.set(val)

    chk_select_all = ttk.Checkbutton(
        main_frame,
        text="Tout cocher / Tout décocher",
        variable=select_all_var,
        command=on_toggle_select_all,
    )
    chk_select_all.grid(row=9, column=0, columnspan=3, pady=5, sticky=tk.W)

    # Barre de progression
    ttk.Label(main_frame, text="Progression :").grid(
        row=10, column=0, sticky=tk.W, pady=(5, 0)
    )
    progress_bar = ttk.Progressbar(
        main_frame,
        variable=progress_var,
        maximum=100.0,
        mode="determinate",
        length=400,
    )
    progress_bar.grid(row=10, column=1, sticky="w", pady=(5, 0))

    # Boutons (fetch / run / stop)
    def on_fetch_mailboxes():
        host = entry_host.get().strip()
        user = entry_user.get().strip()
        password = entry_password.get().strip()

        if not host or not user or not password:
            messagebox.showwarning(
                "Champs manquants",
                "Merci de remplir le serveur, l'e-mail et le mot de passe.",
            )
            return

        for child in mailbox_frame_inner.winfo_children():
            child.destroy()
        mailbox_vars.clear()
        select_all_var.set(False)

        text_log.delete("1.0", tk.END)
        text_log.insert(tk.END, "Récupération des dossiers IMAP...\n")
        text_log.update_idletasks()

        mailboxes = fetch_mailboxes(host, user, password, text_log)

        for mb in mailboxes:
            var = tk.BooleanVar(value=False)
            chk = ttk.Checkbutton(mailbox_frame_inner, text=mb, variable=var)
            chk.pack(anchor="w")
            mailbox_vars.append((mb, var))

        if not mailboxes:
            text_log.insert(tk.END, "Aucun dossier trouvé ou erreur.\n")
        else:
            text_log.insert(
                tk.END, "\nSélectionnez les dossiers à exporter.\n"
            )

    btn_fetch = ttk.Button(
        main_frame, text="Lister les dossiers IMAP", command=on_fetch_mailboxes
    )
    btn_fetch.grid(row=0, column=2, pady=5, padx=5, sticky=tk.E)

    def on_run():
        host = entry_host.get().strip()
        user = entry_user.get().strip()
        password = entry_password.get().strip()
        date_start_str = entry_date_start.get().strip()
        date_end_str = entry_date_end.get().strip()

        if not host or not user or not password:
            messagebox.showwarning(
                "Champs manquants",
                "Merci de remplir le serveur, l'e-mail et le mot de passe.",
            )
            return

        # Parsing des dates
        date_debut = None
        if date_start_str:
            try:
                date_debut = parse_french_date(date_start_str)
            except ValueError:
                messagebox.showerror(
                    "Date de début invalide",
                    "La date de début doit être au format JJ/MM/AAAA.",
                )
                return

        date_fin = None
        if date_end_str:
            try:
                date_fin = parse_french_date(date_end_str)
            except ValueError:
                messagebox.showerror(
                    "Date de fin invalide",
                    "La date de fin doit être au format JJ/MM/AAAA.",
                )
                return

            if date_debut is not None and date_fin < date_debut:
                messagebox.showerror(
                    "Plage de dates invalide",
                    "La date de fin ne peut pas être antérieure "
                    "à la date de début.",
                )
                return

        selected_mailboxes = [mb for mb, var in mailbox_vars if var.get()]

        if not selected_mailboxes:
            messagebox.showwarning(
                "Aucun dossier sélectionné",
                "Merci de sélectionner au moins un dossier IMAP "
                "(via 'Lister les dossiers IMAP').",
            )
            return

        # Préparation interface
        btn_run.config(state=tk.DISABLED)
        btn_fetch.config(state=tk.DISABLED)
        stop_event.clear()
        progress_var.set(0.0)
        progress_total["value"] = 0
        text_log.delete("1.0", tk.END)
        text_log.insert(tk.END, "Démarrage de l'extraction...\n")
        text_log.update_idletasks()

        # Lancer le thread travailleur
        def worker():
            export_imap_worker(
                host,
                user,
                password,
                date_debut,
                date_fin,
                selected_mailboxes,
                q,
                stop_event,
            )

        t = threading.Thread(target=worker, daemon=True)
        worker_thread["t"] = t
        t.start()

    btn_run = ttk.Button(
        main_frame, text="Lancer l'extraction (dossiers cochés)", command=on_run
    )
    btn_run.grid(row=11, column=0, columnspan=2, pady=10, sticky=tk.W)

    def on_stop():
        if worker_thread["t"] and worker_thread["t"].is_alive():
            stop_event.set()
            text_log.insert(
                tk.END,
                "Arrêt demandé, l'extraction va se terminer proprement...\n",
            )
            text_log.see(tk.END)

    btn_stop = ttk.Button(
        main_frame, text="Arrêter l'extraction", command=on_stop
    )
    btn_stop.grid(row=11, column=2, pady=10, sticky=tk.E)

    # Polling de la queue pour garder l'UI responsive
    def poll_queue():
        try:
            while True:
                kind, payload = q.get_nowait()
                if kind == "log":
                    text_log.insert(tk.END, payload + "\n")
                    text_log.see(tk.END)
                elif kind == "progress_total":
                    progress_total["value"] = int(payload) if payload else 0
                    progress_var.set(0.0)
                elif kind == "progress":
                    total = progress_total["value"] or 1
                    pct = int(payload) / total * 100.0
                    progress_var.set(pct)
                elif kind == "info":
                    messagebox.showinfo("Extraction terminée", str(payload))
                elif kind == "error":
                    messagebox.showerror("Erreur", str(payload))
                elif kind == "export_dir":
                    # Stocker le dossier d'export dans l'état partagé
                    shared_state["last_export_dir"] = str(payload)
                elif kind == "done":
                    btn_run.config(state=tk.NORMAL)
                    btn_fetch.config(state=tk.NORMAL)
        except queue.Empty:
            pass

        root.after(100, poll_queue)

    # Layout responsive
    main_frame.rowconfigure(6, weight=1)   # log
    main_frame.rowconfigure(8, weight=1)   # liste dossiers
    main_frame.columnconfigure(1, weight=1)

    root.after(100, poll_queue)
