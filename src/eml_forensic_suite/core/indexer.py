from __future__ import annotations

from typing import Callable, Dict, List, Tuple, Optional
import os
import csv
from email import policy
from email.parser import BytesParser
from email.message import EmailMessage

from eml_forensic_suite.core.common_utils import safe_folder_name
from eml_forensic_suite.core.email_analysis import analyze_email




def scan_eml_files(root_dir: str) -> List[Tuple[str, str]]:
    eml_files: List[Tuple[str, str]] = []
    for current_root, _, files in os.walk(root_dir):
        for name in files:
            if name.lower().endswith(".eml"):
                full_path = os.path.join(current_root, name)
                rel_path = os.path.relpath(full_path, root_dir)
                eml_files.append((full_path, rel_path))
    return eml_files


def parse_eml_headers(path: str) -> Tuple[Dict[str, str], EmailMessage]:
    with open(path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    subject = msg["subject"] or ""
    from_ = msg["from"] or ""
    to = msg["to"] or ""
    cc = msg["cc"] or ""
    bcc = msg["bcc"] or ""
    date = msg["date"] or ""
    msg_id = msg["message-id"] or msg["message-id".title()] or ""

    headers = {
        "subject": subject,
        "from": from_,
        "to": to,
        "cc": cc,
        "bcc": bcc,
        "date": date,
        "message_id": msg_id,
    }
    return headers, msg




def load_hashes(root_dir: str) -> Tuple[Dict[str, str], Optional[str]]:
    hashes_path = os.path.join(root_dir, "hashes.txt")
    hash_map: Dict[str, str] = {}
    global_hash: Optional[str] = None

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

            if not (all(c in "0123456789abcdefABCDEF" for c in right) and len(right) >= 32):
                continue

            rel_posix_imap = left.replace("\\", "/")
            folder_imap_orig, filename = os.path.split(rel_posix_imap)
            if folder_imap_orig:
                safe_mb = safe_folder_name(folder_imap_orig)
                disk_rel = f"{safe_mb}/{filename}"
            else:
                disk_rel = filename

            hash_map[disk_rel] = right

    with open(hashes_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        if lines:
            last = lines[-1]
            if all(c in "0123456789abcdefABCDEF" for c in last) and len(last) >= 32:
                global_hash = last

    return hash_map, global_hash




def build_index_csv(
    root_dir: str,
    log_callback: Callable[[str], None],
    progress_callback: Optional[Callable[[float], None]] = None,
) -> Tuple[str, List[Dict[str, str]]]:
    eml_files = scan_eml_files(root_dir)
    total = len(eml_files)
    if total == 0:
        raise RuntimeError("Aucun fichier .eml trouvé dans ce dossier.")

    log_path = os.path.join(root_dir, "forensic_analysis_log.txt")
    log_file = open(log_path, "w", encoding="utf-8")

    def log(msg: str) -> None:
        log_callback(msg)
        log_file.write(msg + "\n")

    stats_suspicion_levels: Dict[str, int] = {}
    stats_integrity_flags: Dict[str, int] = {}
    stats_received_anomalies: Dict[str, int] = {}
    stats_dkim: Dict[str, int] = {}
    stats_spf: Dict[str, int] = {}
    stats_dmarc: Dict[str, int] = {}
    error_count = 0

    suspicious_samples: List[Dict[str, str]] = []

    try:
        log(f"{total} fichiers .eml trouvés. Chargement des hashes (si présents)...")

        hash_map, global_hash = load_hashes(root_dir)
        log(f"{len(hash_map)} entrées de hash individuelles trouvées dans hashes.txt.")
        if global_hash:
            log(f"Hash global (dans hashes.txt) : {global_hash}")

        log("Début de l'indexation...\n")

        if progress_callback is not None:
            progress_callback(0.0)

        index_path = os.path.join(root_dir, "index_eml.csv")
        index_entries: List[Dict[str, str]] = []

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
            "has_attachments",
            "attachment_count",
            "attachment_filenames",
            "dkim_result",
            "spf_result",
            "dmarc_result",
            "auth_comment",
            "received_count",
            "received_anomalies",
            "integrity_flags",
            "suspicion_score",
            "suspicion_level",
            "suspicion_reasons",
            "relative_path",
            "filename",
        ]

        with open(index_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i, (full_path, rel_path) in enumerate(eml_files, start=1):
                log(f"[{i}/{total}] Lecture des en-têtes : {rel_path}")

                headers, msg = parse_eml_headers(full_path)
                with open(full_path, "rb") as f:
                    raw_bytes = f.read()

                analysis = analyze_email(msg, raw_email_bytes=raw_bytes)


                folder_imap, filename = os.path.split(rel_path)
                if not folder_imap:
                    folder_imap = "(racine)"

                seq = ""
                if filename.lower().endswith(".eml"):
                    base = filename[:-4]
                    if base.isdigit():
                        seq = base

                rel_posix_disk = rel_path.replace("\\", "/")
                sha256 = hash_map.get(rel_posix_disk, "")

                row: Dict[str, str] = {
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
                    "has_attachments": "1" if analysis.has_attachments else "0",
                    "attachment_count": str(analysis.attachment_count),
                    "attachment_filenames": analysis.attachment_filenames,
                    "dkim_result": analysis.dkim_result,
                    "spf_result": analysis.spf_result,
                    "dmarc_result": analysis.dmarc_result,
                    "auth_comment": analysis.auth_comment,
                    "received_count": str(analysis.received_count),
                    "received_anomalies": analysis.received_anomalies,
                    "integrity_flags": analysis.integrity_flags,
                    "suspicion_score": str(analysis.suspicion_score),
                    "suspicion_level": analysis.suspicion_level,
                    "suspicion_reasons": analysis.suspicion_reasons,
                    "relative_path": rel_path,
                    "filename": filename,
                }

                writer.writerow(row)

                entry = dict(row)
                entry["full_path"] = full_path
                index_entries.append(entry)

                log_line = (
                    f"  -> score={analysis.suspicion_score} "
                    f"level={analysis.suspicion_level or 'NONE'} "
                    f"received=[{analysis.received_anomalies}] "
                    f"integrity=[{analysis.integrity_flags}]"
                )

                if analysis.suspicion_level == "ERROR":
                    log_line += f" error_reason=[{analysis.suspicion_reasons}]"

                log(log_line)


                level = analysis.suspicion_level or "NONE"
                stats_suspicion_levels[level] = stats_suspicion_levels.get(level, 0) + 1

                if level == "ERROR":
                    error_count += 1

                stats_dkim[analysis.dkim_result or "none"] = stats_dkim.get(analysis.dkim_result or "none", 0) + 1
                stats_spf[analysis.spf_result or "none"] = stats_spf.get(analysis.spf_result or "none", 0) + 1
                stats_dmarc[analysis.dmarc_result or "none"] = stats_dmarc.get(analysis.dmarc_result or "none", 0) + 1

                if analysis.integrity_flags:
                    for flag in analysis.integrity_flags.split(";"):
                        f = flag.strip()
                        if not f:
                            continue
                        stats_integrity_flags[f] = stats_integrity_flags.get(f, 0) + 1

                if analysis.received_anomalies:
                    for flag in analysis.received_anomalies.split(";"):
                        f = flag.strip()
                        if not f:
                            continue
                        stats_received_anomalies[f] = stats_received_anomalies.get(f, 0) + 1

                try:
                    if analysis.suspicion_score >= 50 and len(suspicious_samples) < 10:
                        suspicious_samples.append(
                            {
                                "relative_path": rel_path,
                                "from": headers["from"],
                                "subject": headers["subject"],
                                "score": str(analysis.suspicion_score),
                                "level": analysis.suspicion_level or "NONE",
                                "reasons": analysis.suspicion_reasons,
                                "received_anomalies": analysis.received_anomalies,
                                "integrity_flags": analysis.integrity_flags,
                            }
                        )
                except Exception:
                    pass

                if progress_callback is not None and total > 0:
                    progress_callback(i / total * 100.0)

        log("\n=== SYNTHÈSE FORENSIC PROVISOIRE (DEBUG) ===")
        log(f"Total de messages analysés : {total}")
        log(f"Nombre de messages avec erreur d’analyse avancée : {error_count}")

        log("\nRépartition par niveau de suspicion :")
        for lvl, cnt in sorted(stats_suspicion_levels.items(), key=lambda x: x[0]):
            log(f"  - {lvl}: {cnt}")

        log("\nDKIM (résumé simple dkim_result du CSV) :")
        for val, cnt in sorted(stats_dkim.items(), key=lambda x: x[0]):
            log(f"  - {val}: {cnt}")

        log("\nSPF (résumé simple spf_result du CSV) :")
        for val, cnt in sorted(stats_spf.items(), key=lambda x: x[0]):
            log(f"  - {val}: {cnt}")

        log("\nDMARC (résumé simple dmarc_result du CSV) :")
        for val, cnt in sorted(stats_dmarc.items(), key=lambda x: x[0]):
            log(f"  - {val}: {cnt}")

        log("\nFlags d’intégrité les plus fréquents :")
        if not stats_integrity_flags:
            log("  (aucun flag d’intégrité)")
        else:
            for flag, cnt in sorted(stats_integrity_flags.items(), key=lambda x: -x[1]):
                log(f"  - {flag}: {cnt}")

        log("\nAnomalies Received les plus fréquentes :")
        if not stats_received_anomalies:
            log("  (aucune anomalie Received)")
        else:
            for flag, cnt in sorted(stats_received_anomalies.items(), key=lambda x: -x[1]):
                log(f"  - {flag}: {cnt}")

        log("\nExemples de messages suspects (score >= 50) :")
        if not suspicious_samples:
            log("  (aucun message avec score >= 50)")
        else:
            for sample in suspicious_samples:
                log("  ---")
                log(f"  Chemin : {sample['relative_path']}")
                log(f"  From   : {sample['from']}")
                log(f"  Sujet  : {sample['subject']}")
                log(f"  Score  : {sample['score']} (niveau {sample['level']})")
                log(f"  Raisons: {sample['reasons']}")
                log(f"  Received anomalies: {sample['received_anomalies']}")
                log(f"  Integrity flags   : {sample['integrity_flags']}")

        log(f"\nIndexation terminée. Fichier créé : {index_path}")
        log(f"Nombre de messages indexés : {len(index_entries)}")
        log(f"Log détaillé d'analyse : {log_path}")

        return index_path, index_entries
    finally:
        try:
            log_file.close()
        except Exception:
            pass
