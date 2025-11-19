# common_utils.py
"""
Fonctions utilitaires communes pour la suite forensic EML/IMAP.

- Hash (sha256_from_bytes, sha256_file)
- Gestion des chemins (safe_folder_name, get_base_dir, get_tool_path)
- Dates (parse_french_date, to_imap_date)
- IMAP (decode_imap_mailbox)
- EML (read_raw_headers, read_message_bodies, scan_eml_files, parse_eml_headers)
- Hashes d'export (load_hashes)
- Rapport forensic IMAP (write_report)
"""

from __future__ import annotations

import os
import re
import sys
import hashlib
import imaplib
import platform
from datetime import datetime
from typing import Any, Dict, List, Tuple

from email import policy
from email.parser import BytesParser
import json

def load_version_info():
    try:
        path = resource_path("VERSION.json")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"version": "Unknown"}

VERSION_INFO = load_version_info()
VERSION = VERSION_INFO.get("version", "Unknown")


def resource_path(relative_path: str) -> str:
    """
    Retourne un chemin vers une ressource embarquée, compatible
    avec le mode PyInstaller --onefile (sys._MEIPASS).
    """
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# ==========================================================
#   Hash utilitaires
# ==========================================================


def sha256_from_bytes(data: bytes) -> str:
    """Calcule le SHA-256 d'un buffer en mémoire."""
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def sha256_file(path: str) -> str:
    """Calcule le SHA-256 d'un fichier sur disque."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


# ==========================================================
#   DATES & IMAP
# ==========================================================


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


# ==========================================================
#   CHEMINS & ENVIRONNEMENT
# ==========================================================


def safe_folder_name(name: str) -> str:
    """
    Convertit un nom de dossier IMAP en nom de dossier sûr pour le système de fichiers.
    On garde une trace du vrai nom dans les logs / hashes.
    """
    forbidden = '<>:"/\\|?*'
    out = name
    for ch in forbidden:
        out = out.replace(ch, "_")
    out = out.strip()
    if not out:
        out = "MAILBOX"
    return out


def get_base_dir() -> str:
    """
    Renvoie le vrai dossier depuis lequel le script .exe est lancé,
    même lorsque PyInstaller utilise un dossier temporaire _MEIxxxx.
    """
    if getattr(sys, "frozen", False):
        # Exécution en .exe PyInstaller
        return os.path.dirname(sys.executable)
    # Exécution en .py normal
    return os.path.dirname(os.path.abspath(__file__))


def get_tool_path() -> str:
    """
    Renvoie le chemin de l'outil (script .py ou .exe).
    """
    if getattr(sys, "frozen", False):
        return os.path.abspath(sys.executable)
    return os.path.abspath(__file__)


# ==========================================================
#   EML : headers & corps (lecture seule)
# ==========================================================


def read_raw_headers(path: str) -> str:
    """
    Retourne les en-têtes "brutes" du .eml (tout avant la première ligne vide).
    Lecture en binaire puis décodage texte.
    NE MODIFIE JAMAIS LE FICHIER SUR DISQUE.
    """
    with open(path, "rb") as f:
        data = f.read()

    sep = data.find(b"\r\n\r\n")
    if sep == -1:
        sep = data.find(b"\n\n")

    if sep == -1:
        headers = data
    else:
        headers = data[:sep]

    return headers.decode("utf-8", errors="replace")


def read_message_bodies(path: str) -> tuple[str, str]:
    """
    Lit un .eml en lecture seule et extrait :
      - corps text/plain concaténé
      - corps text/html concaténé (brut, non rendu)

    Retourne (text_body, html_body). Les deux peuvent être vides.
    """
    with open(path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    text_parts: list[str] = []
    html_parts: list[str] = []

    for part in msg.walk():
        # On ignore les parties multipart "container"
        if part.is_multipart():
            continue

        ctype = part.get_content_type()
        # get_content() avec policy.default renvoie déjà du str
        try:
            content = part.get_content()
        except Exception:
            # fallback ultra basique
            payload = part.get_payload(decode=True)
            if isinstance(payload, bytes):
                content = payload.decode("utf-8", errors="replace")
            else:
                content = str(payload)

        if ctype == "text/plain":
            text_parts.append(content)
        elif ctype == "text/html":
            html_parts.append(content)

    text_body = "\n\n----- PARTIE SUIVANTE -----\n\n".join(text_parts).strip()
    html_body = "\n\n----- PARTIE SUIVANTE (HTML) -----\n\n".join(html_parts).strip()

    return text_body, html_body


# ==========================================================
#   EML : scan & parsing d’en-têtes
# ==========================================================


def scan_eml_files(root_dir: str) -> list[tuple[str, str]]:
    """
    Parcourt récursivement root_dir et renvoie une liste de (full_path, rel_path)
    pour tous les fichiers .eml trouvés.
    """
    eml_files: list[tuple[str, str]] = []
    for current_root, dirs, files in os.walk(root_dir):
        for name in files:
            if name.lower().endswith(".eml"):
                full_path = os.path.join(current_root, name)
                rel_path = os.path.relpath(full_path, root_dir)
                eml_files.append((full_path, rel_path))
    return eml_files


def parse_eml_headers(path: str) -> dict[str, str]:
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


# ==========================================================
#   HASHES D’EXPORT (hashes.txt)
# ==========================================================


def load_hashes(root_dir: str) -> tuple[dict[str, str], str | None]:
    """
    Charge hashes.txt s'il existe dans root_dir.
    Retourne un dict { chemin_relatif_disque_posix : sha256 } et le hash global éventuel.

    IMPORTANT : on adapte les chemins de hashes.txt (basés sur le nom IMAP)
    pour retrouver les chemins réels sur disque (basés sur safe_folder_name).
    """
    hashes_path = os.path.join(root_dir, "hashes.txt")
    hash_map: dict[str, str] = {}
    global_hash: str | None = None

    if not os.path.isfile(hashes_path):
        return hash_map, global_hash

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
            if not (
                all(c in "0123456789abcdefABCDEF" for c in right)
                and len(right) >= 32
            ):
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

    # Essai basique pour retrouver le hash global : dernière ligne non vide
    with open(hashes_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        if lines:
            last = lines[-1]
            if all(c in "0123456789abcdefABCDEF" for c in last) and len(last) >= 32:
                global_hash = last

    return hash_map, global_hash


# ==========================================================
#   RAPPORT FORENSIC IMAP
# ==========================================================


def write_report(export_dir: str, stats: dict, hashes_path: str) -> None:
    """
    Écrit rapport_imap_export.txt + ajoute son hash dans hashes.txt
    (sans modifier le hash global des messages).

    stats doit contenir (entre autres) :
      - version
      - analysis_start_utc / analysis_end_utc
      - analysis_start_local / analysis_end_local
      - host, user
      - date_start_text, date_end_text
      - search_criteria
      - dossiers_selectionnes
      - folders (détails par dossier)
      - tool_path, tool_hash
      - env (os_system, os_release, os_version, machine, python_version)
      - imap_greeting, imap_capability
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
        f.write("Outil      : imap_eml_downloader.py\n")
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
