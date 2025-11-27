from __future__ import annotations

import hashlib
import imaplib
import os
import platform
import queue
import re
import sys
import threading
import time
from datetime import datetime, timedelta

import tkinter as tk
from tkinter import messagebox, ttk

from eml_forensic_suite.ui.i18n import t, Language

from eml_forensic_suite.core.common_utils import (
    get_base_dir,
    get_tool_path,
    safe_folder_name,
    sha256_file,
    sha256_from_bytes,
)

try:
    from eml_forensic_suite import __version__ as APP_VERSION
except Exception:
    APP_VERSION = "Unknown"


def parse_french_date(date_str: str):
    return datetime.strptime(date_str, "%d/%m/%Y").date()


def to_imap_date(d: datetime.date):
    return d.strftime("%d-%b-%Y")


def decode_imap_mailbox(raw_line: bytes) -> str:
    line = raw_line.decode("utf-8", errors="replace").strip()

    m = re.match(r'\((?P<flags>.*?)\)\s+"(?P<delim>.*)"\s+(?P<name>.*)$', line)
    if not m:
        return line

    name = m.group("name").strip()

    if name.startswith('"') and name.endswith('"'):
        name = name[1:-1]

    try:
        decoded = imaplib.IMAP4._utf7_decode(name)[0]
    except Exception:
        decoded = name

    return decoded


def write_report(
    export_dir: str,
    stats: dict,
    hashes_path: str,
    lang: Language = Language.FR,
) -> None:
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
        f.write(t("imap.report.title", lang) + "\n\n")
        f.write(t("imap.report.tool_line", lang) + "\n")
        f.write(
            t("imap.report.version_line", lang).format(
                version=stats.get("version")
            )
            + "\n"
        )
        f.write(
            t("imap.report.folder_line", lang).format(
                export_dir=export_dir
            )
            + "\n\n"
        )

        f.write(t("imap.report.section_tool", lang) + "\n")
        f.write(
            t("imap.report.tool_path", lang).format(
                tool_path=stats.get("tool_path")
            )
            + "\n"
        )
        f.write(
            t("imap.report.tool_hash", lang).format(
                tool_hash=stats.get("tool_hash")
            )
            + "\n\n"
        )

        f.write(t("imap.report.section_env", lang) + "\n")
        f.write(
            t("imap.report.env_os", lang).format(
                os_system=env.get("os_system"),
                os_release=env.get("os_release"),
                os_version=env.get("os_version"),
                machine=env.get("machine"),
            )
            + "\n"
        )
        f.write(
            t("imap.report.env_python", lang).format(
                python_version=env.get("python_version")
            )
            + "\n\n"
        )

        f.write(t("imap.report.section_context", lang) + "\n")
        f.write(
            t("imap.report.context_host", lang).format(
                host=stats.get("host")
            )
            + "\n"
        )
        f.write(
            t("imap.report.context_user", lang).format(
                user=stats.get("user")
            )
            + "\n"
        )
        f.write(
            t("imap.report.context_date_start", lang).format(
                date_start=stats.get("date_start_text")
            )
            + "\n"
        )
        f.write(
            t("imap.report.context_date_end", lang).format(
                date_end=stats.get("date_end_text")
            )
            + "\n"
        )
        f.write(
            t("imap.report.context_criteria", lang).format(
                search_criteria=stats.get("search_criteria")
            )
            + "\n"
        )
        f.write("\n")
        f.write(t("imap.report.selected_folders_title", lang) + "\n")
        for mb in stats.get("dossiers_selectionnes", []):
            f.write(
                t("imap.report.selected_folder_item", lang).format(
                    folder=mb
                )
                + "\n"
            )
        f.write("\n")

        f.write(t("imap.report.section_server", lang) + "\n")
        greeting = stats.get("imap_greeting")
        capability = stats.get("imap_capability")
        if greeting:
            f.write(
                t("imap.report.server_greeting", lang).format(
                    greeting=greeting
                )
                + "\n"
            )
        if capability:
            f.write(
                t("imap.report.server_capability", lang).format(
                    capability=capability
                )
                + "\n"
            )
        f.write("\n")

        f.write(t("imap.report.section_timestamps", lang) + "\n")
        if start_utc:
            f.write(
                t("imap.report.timestamp_start_utc", lang).format(
                    dt=start_utc.isoformat() + "Z"
                )
                + "\n"
            )
        if start_local:
            f.write(
                t("imap.report.timestamp_start_local", lang).format(
                    dt=start_local.isoformat()
                )
                + "\n"
            )
        if end_utc:
            f.write(
                t("imap.report.timestamp_end_utc", lang).format(
                    dt=end_utc.isoformat() + "Z"
                )
                + "\n"
            )
        if end_local:
            f.write(
                t("imap.report.timestamp_end_local", lang).format(
                    dt=end_local.isoformat()
                )
                + "\n"
            )
        if duration is not None:
            f.write(
                t("imap.report.duration", lang).format(
                    duration=str(duration)
                )
                + "\n"
            )
        f.write("\n")

        f.write(t("imap.report.section_folders", lang) + "\n")
        f.write(
            t("imap.report.folders_count", lang).format(
                count=len(folders)
            )
            + "\n\n"
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

            f.write(
                t("imap.report.folder_header", lang).format(name=name)
                + "\n"
            )
            f.write(
                t("imap.report.folder_messages", lang).format(
                    count=msgs
                )
                + "\n"
            )
            f.write(
                t("imap.report.folder_exported", lang).format(
                    count=exported
                )
                + "\n"
            )
            f.write(
                t("imap.report.folder_errors", lang).format(
                    count=errors
                )
                + "\n"
            )
            f.write(
                t("imap.report.folder_bytes", lang).format(
                    bytes=size_bytes
                )
                + "\n"
            )

            if min_size is not None and max_size is not None and exported > 0:
                avg_size = sum_size / exported
                f.write(
                    t("imap.report.folder_size_stats", lang).format(
                        min_size=min_size,
                        max_size=max_size,
                        avg_size=int(avg_size),
                    )
                    + "\n"
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
                    t("imap.report.folder_period", lang).format(
                        first=first_str,
                        last=last_str,
                    )
                    + "\n"
                )

            if error_uids:
                f.write(
                    t("imap.report.folder_error_uids", lang).format(
                        uids=", ".join(error_uids)
                    )
                    + "\n"
                )

            f.write("\n")

        f.write(t("imap.report.section_totals", lang) + "\n")
        f.write(
            t("imap.report.total_messages", lang).format(
                count=global_msgs
            )
            + "\n"
        )
        f.write(
            t("imap.report.total_exported", lang).format(
                count=global_exported
            )
            + "\n"
        )
        f.write(
            t("imap.report.total_errors", lang).format(
                count=global_errors
            )
            + "\n"
        )
        f.write(
            t("imap.report.total_bytes", lang).format(
                bytes=global_bytes
            )
            + "\n"
        )
        f.write("\n")

        f.write(t("imap.report.section_forensic", lang) + "\n")
        f.write(t("imap.report.forensic_item_readonly", lang) + "\n")
        f.write(t("imap.report.forensic_item_eml", lang) + "\n")
        f.write(t("imap.report.forensic_item_hashes", lang) + "\n")
        f.write(t("imap.report.forensic_item_report_hash", lang) + "\n")

    report_hash = sha256_file(rapport_path)

    with open(hashes_path, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(t("imap.report.hashes_report_header", lang) + "\n")
        f.write(
            t("imap.report.hashes_report_line", lang).format(
                filename="rapport_imap_export.txt",
                file_hash=report_hash,
            )
            + "\n"
        )


def export_imap_worker(
    host: str,
    user: str,
    password: str,
    date_debut,
    date_fin,
    mailboxes: list[str],
    q: "queue.Queue[tuple[str, object]]",
    stop_event: threading.Event | None = None,
    export_root_dir: str | None = None,
    auth_mode: str = "password",
    oauth_provider: str | None = None,
    lang: Language = Language.FR,
) -> None:

    def send(kind: str, payload: object):
        q.put((kind, payload))

    def log(msg: str):
        send("log", msg)

    if not mailboxes:
        send("error", t("imap.worker.error_no_folder_selected", lang))
        send("done", None)
        return

    if export_root_dir:
        base_dir = export_root_dir
    else:
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

    log(
        t("imap.worker.log_export_dir", lang).format(
            export_dir=export_dir
        )
    )
    send("export_dir", export_dir)

    tool_path = get_tool_path()
    tool_hash = ""
    try:
        if os.path.isfile(tool_path):
            tool_hash = sha256_file(tool_path)
    except Exception:
        tool_hash = t("imap.worker.tool_hash_error", lang)

    stats: dict = {
        "version": APP_VERSION,
        "analysis_start_utc": datetime.utcnow(),
        "analysis_start_local": datetime.now(),
        "analysis_end_utc": None,
        "analysis_end_local": None,
        "host": host,
        "user": user,
        "dossiers_selectionnes": list(mailboxes),
        "folders": {},
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
        log(t("imap.worker.log_connecting", lang))
        M = imaplib.IMAP4_SSL(host)

        try:
            greeting = getattr(M, "welcome", None)
            if isinstance(greeting, bytes):
                greeting_str = greeting.decode("utf-8", errors="replace")
            else:
                greeting_str = str(greeting) if greeting is not None else ""
            stats["imap_greeting"] = greeting_str
        except Exception:
            stats["imap_greeting"] = t(
                "imap.worker.greeting_not_available", lang
            )

        #if auth_mode == "oauth":
        #    log("Authentification OAuth2...")

        #    provider = oauth_provider
        #    if provider == "google":
        #        from eml_forensic_suite.core.oauth.google_oauth import GoogleOAuthClient
        #        client = GoogleOAuthClient()
        #    elif provider == "microsoft":
        #        from eml_forensic_suite.core.oauth.microsoft_oauth import MicrosoftOAuthClient
        #        client = MicrosoftOAuthClient()
        #    elif provider == "yahoo":
        #        from eml_forensic_suite.core.oauth.yahoo_oauth import YahooOAuthClient
        #        client = YahooOAuthClient()
        #    else:
        #        raise RuntimeError("Aucun fournisseur OAuth2 configuré pour l’export IMAP.")

        #    access_token = client.get_valid_access_token()
        #    auth_string = f"user={user}\x01auth=Bearer {access_token}\x01\x01"

        #    try:
        #        M.authenticate("XOAUTH2", lambda _: auth_string)
        #    except Exception as e:
        #        q.put(("error", f"Erreur d'authentification OAuth2 : {e}"))
        #        raise
        #else:


        log(t("imap.worker.log_auth_classic", lang))
        try:
            M.login(user, password)
        except Exception as e:
            q.put(
                (
                    "error",
                    t("imap.worker.error_auth_failed", lang).format(
                        error=str(e)
                    ),
                )
            )
            raise

        try:
            typ_cap, caps = M.capability()
            if typ_cap == "OK":
                if isinstance(caps, list):
                    joined = b" ".join(caps)
                else:
                    joined = caps
                stats["imap_capability"] = joined.decode(
                    "utf-8", errors="replace"
                )
        except Exception:
            stats["imap_capability"] = t(
                "imap.worker.capability_error", lang
            )

        search_criteria: list[str] = []

        if date_debut is not None:
            since_str = to_imap_date(date_debut)
            log(
                t("imap.worker.log_date_start_inclusive", lang).format(
                    date=date_debut.strftime("%d/%m/%Y"),
                    imap_since=since_str,
                )
            )
            search_criteria.extend(["SINCE", since_str])
            stats["date_start_text"] = date_debut.strftime("%d/%m/%Y")
        else:
            log(t("imap.worker.log_date_start_unset", lang))
            stats["date_start_text"] = t(
                "imap.worker.date_start_unset_label", lang
            )

        if date_fin is not None:
            date_fin_plus_1 = date_fin + timedelta(days=1)
            before_str = to_imap_date(date_fin_plus_1)
            log(
                t("imap.worker.log_date_end_inclusive", lang).format(
                    date=date_fin.strftime("%d/%m/%Y"),
                    imap_before=before_str,
                )
            )
            search_criteria.extend(["BEFORE", before_str])
            stats["date_end_text"] = date_fin.strftime("%d/%m/%Y")
        else:
            log(t("imap.worker.log_date_end_unset", lang))
            stats["date_end_text"] = t(
                "imap.worker.date_end_unset_label", lang
            )

        if not search_criteria:
            search_criteria = ["ALL"]

        stats["search_criteria"] = " ".join(search_criteria)

        log(
            t("imap.worker.log_criteria", lang).format(
                criteria=" ".join(search_criteria)
            )
        )
        log("")
        log(
            t("imap.worker.log_selected_folders_header", lang).format(
                count=len(mailboxes)
            )
        )
        for mb in mailboxes:
            log(
                t("imap.worker.log_selected_folder_item", lang).format(
                    folder=mb
                )
            )
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

        mailbox_to_msgs: dict[str, list[bytes]] = {}
        total_to_download = 0

        for mb_name in mailboxes:
            if stop_event and stop_event.is_set():
                log(t("imap.worker.log_stop_during_count", lang))
                send("done", None)
                return

            log(
                t("imap.worker.log_phase1_count", lang).format(
                    folder=mb_name
                )
            )
            quoted_name = f'"{mb_name}"'

            typ, _ = M.select(quoted_name, readonly=True)
            if typ != "OK":
                log(t("imap.worker.log_select_folder_failed", lang))
                continue

            typ, msgnums = M.search(None, *search_criteria)
            if typ != "OK":
                log(t("imap.worker.log_search_folder_failed", lang))
                continue

            msg_list = msgnums[0].split()
            mailbox_to_msgs[mb_name] = msg_list
            total_in_folder = len(msg_list)
            total_to_download += total_in_folder

            mb_stats = stats["folders"].get(mb_name)
            if mb_stats is not None:
                mb_stats["messages"] = total_in_folder

            log(
                t("imap.worker.log_messages_to_process", lang).format(
                    count=total_in_folder,
                    folder=mb_name,
                )
            )

        log("")
        log(
            t("imap.worker.log_total_messages_to_download", lang).format(
                count=total_to_download
            )
        )
        log("")

        send("progress_total", total_to_download)
        downloaded_count = 0

        for mb_name, msg_list in mailbox_to_msgs.items():
            if stop_event and stop_event.is_set():
                log(t("imap.worker.log_stop_during_export", lang))
                break

            log(
                t("imap.worker.log_folder_header", lang).format(
                    folder=mb_name
                )
            )

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
                log(
                    t("imap.worker.log_no_messages_in_period", lang).format(
                        folder=mb_name
                    )
                )
                log("")
                continue

            safe_mb = safe_folder_name(mb_name)
            mb_dir = os.path.join(export_dir, safe_mb)
            os.makedirs(mb_dir, exist_ok=True)

            total_in_folder = len(msg_list)
            log(
                t("imap.worker.log_folder_message_count", lang).format(
                    count=total_in_folder,
                    folder=mb_name,
                )
            )

            try:
                first_uid = msg_list[0]
                last_uid = msg_list[-1]

                for label, uid in (
                    ("first_internaldate", first_uid),
                    ("last_internaldate", last_uid),
                ):
                    typ_int, data_int = M.fetch(uid, "(INTERNALDATE)")
                    if (
                        typ_int == "OK"
                        and data_int
                        and isinstance(data_int[0], tuple)
                    ):
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
                                pass
            except Exception:
                pass

            quoted_name = f'"{mb_name}"'
            typ, _ = M.select(quoted_name, readonly=True)
            if typ != "OK":
                log(t("imap.worker.log_reselect_folder_failed", lang))
                continue

            for idx, num in enumerate(msg_list, start=1):
                if stop_event and stop_event.is_set():
                    log(t("imap.worker.log_stop_during_export", lang))
                    break

                num_str = num.decode()

                if idx == 1:
                    log(
                        t(
                            "imap.worker.log_first_message_download",
                            lang,
                        ).format(uid=num_str)
                    )
                elif idx % 500 == 0 or idx == total_in_folder:
                    log(
                        t(
                            "imap.worker.log_folder_progress",
                            lang,
                        ).format(
                            folder=mb_name,
                            current=idx,
                            total=total_in_folder,
                            last_uid=num_str,
                        )
                    )

                typ, msg_data = M.fetch(num, "(RFC822)")
                if typ != "OK":
                    log(
                        t(
                            "imap.worker.log_fetch_error_message",
                            lang,
                        ).format(uid=num_str)
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
                    if (
                        mb_stats["min_size"] is None
                        or size_bytes < mb_stats["min_size"]
                    ):
                        mb_stats["min_size"] = size_bytes
                    if (
                        mb_stats["max_size"] is None
                        or size_bytes > mb_stats["max_size"]
                    ):
                        mb_stats["max_size"] = size_bytes

                downloaded_count += 1
                send("progress", downloaded_count)

                if downloaded_count % 200 == 0:
                    time.sleep(0.01)

            log(
                t("imap.worker.log_folder_end", lang).format(
                    folder=mb_name
                )
            )
            log("")

        global_hash = hashlib.sha256()
        for _, h in all_hashes:
            global_hash.update(h.encode())

        hashes_path = os.path.join(export_dir, "hashes.txt")
        with open(hashes_path, "w", encoding="utf-8") as f:
            f.write(t("imap.worker.hashes_header", lang) + "\n\n")
            for rel_path, h in all_hashes:
                f.write(
                    t("imap.worker.hashes_file_line", lang).format(
                        path=rel_path, file_hash=h
                    )
                    + "\n"
                )
            f.write("\n")
            f.write(
                t("imap.worker.hashes_global_header", lang) + "\n"
            )
            f.write(global_hash.hexdigest() + "\n")

        log("")
        log(t("imap.worker.log_export_done_header", lang))
        log(
            t("imap.worker.log_export_done_count", lang).format(
                count=total_msgs
            )
        )
        log(
            t("imap.worker.log_export_done_hashes_file", lang).format(
                path=hashes_path
            )
        )
        log(
            t("imap.worker.log_export_done_hash", lang).format(
                file_hash=global_hash.hexdigest()
            )
        )

        summary = t("imap.worker.summary", lang).format(
            count=total_msgs,
            export_dir=export_dir,
            file_hash=global_hash.hexdigest(),
        )
        send("info", summary)

        stats["analysis_end_utc"] = datetime.utcnow()
        stats["analysis_end_local"] = datetime.now()
        try:
            write_report(export_dir, stats, hashes_path, lang)
            log(t("imap.worker.log_report_generated", lang))
        except Exception as e:
            log(
                t("imap.worker.log_report_failed", lang).format(
                    error=str(e)
                )
            )

    except Exception as e:
        send(
            "error",
            t("imap.worker.error_generic", lang).format(error=str(e)),
        )

    finally:
        if M is not None:
            try:
                M.logout()
            except Exception:
                pass
        send("done", None)


def fetch_mailboxes(
    host: str,
    user: str,
    password: str,
    log_widget: tk.Text,
    shared_state: dict,
):

    if isinstance(shared_state, dict):
        raw_lang = shared_state.get("lang", Language.FR)
    else:
        raw_lang = Language.FR

    if isinstance(raw_lang, Language):
        lang = raw_lang
    else:
        try:
            lang = Language(raw_lang)
        except Exception:
            lang = Language.FR

    def log(msg: str) -> None:
        log_widget.insert(tk.END, msg + "\n")
        log_widget.see(tk.END)
        log_widget.update_idletasks()

    M = None
    mailboxes = []

    try:
        log(t("imap.tk.log_connecting", lang))
        M = imaplib.IMAP4_SSL(host)

    #    if shared_state.get("auth_mode") == "oauth":

    #        log("Authentification OAuth2...")
    #        from eml_forensic_suite.core.oauth.google_oauth import GoogleOAuthClient

    #        oauth = GoogleOAuthClient(
    #            client_id="TON_CLIENT_ID",
    #            client_secret="TON_SECRET",
    #            token_path="google_token.json"
    #        )

    #        access_token = oauth.get_valid_access_token()
    #        auth_string = f"user={user}\x01auth=Bearer {access_token}\x01\x01"

    #        M.authenticate("XOAUTH2", lambda _: auth_string)

    #    else:
        log(t("imap.tk.log_auth_classic", lang))
        M.login(user, password)

        typ, data = M.list()
        if typ != "OK":
            raise RuntimeError(
                t("imap.tk.error_list_mailboxes_failed", lang)
            )

        log(t("imap.tk.log_folders_found_header", lang))
        for raw in data:
            if raw is None:
                continue
            name = decode_imap_mailbox(raw)
            mailboxes.append(name)
            log(
                t("imap.tk.log_folder_item", lang).format(folder=name)
            )

        log("")
        log(
            t("imap.tk.log_folders_count", lang).format(
                count=len(mailboxes)
            )
        )

        return mailboxes

    except Exception as e:
        messagebox.showerror(
            t("imap.tk.msgbox_error_title", lang),
            t("imap.tk.msgbox_error_fetch_mailboxes", lang).format(
                error=str(e)
            ),
        )
        log(
            t("imap.tk.log_error_fetch_mailboxes", lang).format(
                error=str(e)
            )
        )
        return []

    finally:
        if M is not None:
            try:
                M.logout()
            except Exception:
                pass


def build_imap_tab(notebook: ttk.Notebook, shared_state: dict) -> None:
    root = notebook.winfo_toplevel()

    if isinstance(shared_state, dict):
        raw_lang = shared_state.get("lang", Language.FR)
    else:
        raw_lang = Language.FR

    if isinstance(raw_lang, Language):
        lang = raw_lang
    else:
        try:
            lang = Language(raw_lang)
        except Exception:
            lang = Language.FR

    tab = ttk.Frame(notebook)
    notebook.add(tab, text=t("imap.tk.tab_title", lang))

    main_frame = ttk.Frame(tab, padding=10)
    main_frame.pack(fill=tk.BOTH, expand=True)

    mailbox_vars: list[tuple[str, tk.BooleanVar]] = []
    select_all_var = tk.BooleanVar(value=False)
    progress_var = tk.DoubleVar(value=0.0)
    progress_total = {"value": 0}
    worker_thread: dict[str, threading.Thread | None] = {"t": None}
    stop_event = threading.Event()
    q: "queue.Queue[tuple[str, object]]" = queue.Queue()

    ttk.Label(
        main_frame,
        text=t("imap.tk.label_server", lang),
    ).grid(row=0, column=0, sticky=tk.W, pady=5)
    entry_host = ttk.Entry(main_frame, width=40)
    entry_host.grid(row=0, column=1, sticky=tk.W, pady=5)
    entry_host.insert(0, "imap.exemple.com")

    ttk.Label(
        main_frame,
        text=t("imap.tk.label_email", lang),
    ).grid(row=1, column=0, sticky=tk.W, pady=5)
    entry_user = ttk.Entry(main_frame, width=40)
    entry_user.grid(row=1, column=1, sticky=tk.W, pady=5)

    ttk.Label(
        main_frame,
        text=t("imap.tk.label_password", lang),
    ).grid(row=2, column=0, sticky=tk.W, pady=5)
    entry_password = ttk.Entry(main_frame, width=40, show="*")
    entry_password.grid(row=2, column=1, sticky=tk.W, pady=5)

    ttk.Label(
        main_frame,
        text=t("imap.tk.label_date_start", lang),
    ).grid(row=3, column=0, sticky=tk.W, pady=5)
    entry_date_start = ttk.Entry(main_frame, width=20)
    entry_date_start.grid(row=3, column=1, sticky=tk.W, pady=5)

    ttk.Label(
        main_frame,
        text=t("imap.tk.label_date_end", lang),
    ).grid(row=4, column=0, sticky=tk.W, pady=5)
    entry_date_end = ttk.Entry(main_frame, width=20)
    entry_date_end.grid(row=4, column=1, sticky=tk.W, pady=5)

    ttk.Label(
        main_frame,
        text=t("imap.tk.label_log", lang),
    ).grid(row=5, column=0, columnspan=3, sticky=tk.W, pady=(10, 0))
    text_log = tk.Text(main_frame, height=10, wrap="word")
    text_log.grid(row=6, column=0, columnspan=3, sticky="nsew", pady=5)

    scrollbar = ttk.Scrollbar(
        main_frame, orient="vertical", command=text_log.yview
    )
    scrollbar.grid(row=6, column=3, sticky="ns")
    text_log.configure(yscrollcommand=scrollbar.set)

    ttk.Label(
        main_frame,
        text=t("imap.tk.label_mailboxes", lang),
    ).grid(row=7, column=0, columnspan=3, sticky=tk.W, pady=(10, 0))

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

    def on_toggle_select_all():
        if not mailbox_vars:
            return

        all_checked = all(var.get() for _, var in mailbox_vars)
        new_value = not all_checked

        select_all_var.set(new_value)
        for _, var in mailbox_vars:
            var.set(new_value)

    chk_select_all = ttk.Checkbutton(
        main_frame,
        text=t("imap.tk.checkbox_select_all", lang),
        variable=select_all_var,
        command=on_toggle_select_all,
    )
    chk_select_all.grid(row=9, column=0, columnspan=3, pady=5, sticky=tk.W)

    ttk.Label(
        main_frame,
        text=t("imap.tk.label_progress", lang),
    ).grid(row=10, column=0, sticky=tk.W, pady=(5, 0))
    progress_bar = ttk.Progressbar(
        main_frame,
        variable=progress_var,
        maximum=100.0,
        mode="determinate",
        length=400,
    )
    progress_bar.grid(row=10, column=1, sticky="w", pady=(5, 0))

    def on_fetch_mailboxes():
        host = entry_host.get().strip()
        user = entry_user.get().strip()
        password = entry_password.get().strip()

        if not host or not user or not password:
            messagebox.showwarning(
                t("imap.tk.msgbox_missing_fields_title", lang),
                t("imap.tk.msgbox_missing_fields_text", lang),
            )
            return

        for child in mailbox_frame_inner.winfo_children():
            child.destroy()
        mailbox_vars.clear()
        select_all_var.set(False)

        text_log.delete("1.0", tk.END)
        text_log.insert(
            tk.END,
            t("imap.tk.log_fetch_mailboxes_start", lang) + "\n",
        )
        text_log.update_idletasks()

        mailboxes = fetch_mailboxes(
            host, user, password, text_log, shared_state
        )

        for mb in mailboxes:
            var = tk.BooleanVar(value=False)
            chk = ttk.Checkbutton(
                mailbox_frame_inner, text=mb, variable=var
            )
            chk.pack(anchor="w")
            mailbox_vars.append((mb, var))

        if not mailboxes:
            text_log.insert(
                tk.END,
                t("imap.tk.log_no_mailboxes_or_error", lang) + "\n",
            )
        else:
            text_log.insert(
                tk.END,
                t("imap.tk.log_select_mailboxes_hint", lang) + "\n",
            )

    btn_fetch = ttk.Button(
        main_frame,
        text=t("imap.tk.button_list_mailboxes", lang),
        command=on_fetch_mailboxes,
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
                t("imap.tk.msgbox_missing_fields_title", lang),
                t("imap.tk.msgbox_missing_fields_text", lang),
            )
            return

        date_debut = None
        if date_start_str:
            try:
                date_debut = parse_french_date(date_start_str)
            except ValueError:
                messagebox.showerror(
                    t("imap.tk.msgbox_date_start_invalid_title", lang),
                    t("imap.tk.msgbox_date_start_invalid_text", lang),
                )
                return

        date_fin = None
        if date_end_str:
            try:
                date_fin = parse_french_date(date_end_str)
            except ValueError:
                messagebox.showerror(
                    t("imap.tk.msgbox_date_end_invalid_title", lang),
                    t("imap.tk.msgbox_date_end_invalid_text", lang),
                )
                return

            if date_debut is not None and date_fin < date_debut:
                messagebox.showerror(
                    t("imap.tk.msgbox_date_range_invalid_title", lang),
                    t("imap.tk.msgbox_date_range_invalid_text", lang),
                )
                return

        selected_mailboxes = [mb for mb, var in mailbox_vars if var.get()]

        if not selected_mailboxes:
            messagebox.showwarning(
                t("imap.tk.msgbox_no_mailbox_selected_title", lang),
                t("imap.tk.msgbox_no_mailbox_selected_text", lang),
            )
            return

        btn_run.config(state=tk.DISABLED)
        btn_fetch.config(state=tk.DISABLED)
        stop_event.clear()
        progress_var.set(0.0)
        progress_total["value"] = 0
        text_log.delete("1.0", tk.END)
        text_log.insert(
            tk.END,
            t("imap.tk.log_export_start", lang) + "\n",
        )
        text_log.update_idletasks()

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
                lang=lang,
            )

        t_thread = threading.Thread(target=worker, daemon=True)
        worker_thread["t"] = t_thread
        t_thread.start()

    btn_run = ttk.Button(
        main_frame,
        text=t("imap.tk.button_run_export", lang),
        command=on_run,
    )
    btn_run.grid(row=11, column=0, columnspan=2, pady=10, sticky=tk.W)

    def on_stop():
        if worker_thread["t"] and worker_thread["t"].is_alive():
            stop_event.set()
            text_log.insert(
                tk.END,
                t("imap.tk.log_stop_requested", lang) + "\n",
            )
            text_log.see(tk.END)

    btn_stop = ttk.Button(
        main_frame,
        text=t("imap.tk.button_stop_export", lang),
        command=on_stop,
    )
    btn_stop.grid(row=11, column=2, pady=10, sticky=tk.E)

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
                    messagebox.showinfo(
                        t("imap.tk.msgbox_export_done_title", lang),
                        str(payload),
                    )
                elif kind == "error":
                    messagebox.showerror(
                        t("imap.tk.msgbox_error_title", lang),
                        str(payload),
                    )
                elif kind == "export_dir":
                    shared_state["last_export_dir"] = str(payload)
                elif kind == "done":
                    btn_run.config(state=tk.NORMAL)
                    btn_fetch.config(state=tk.NORMAL)
        except queue.Empty:
            pass

        root.after(100, poll_queue)

    main_frame.rowconfigure(6, weight=1)
    main_frame.rowconfigure(8, weight=1)
    main_frame.columnconfigure(1, weight=1)

    root.after(100, poll_queue)
