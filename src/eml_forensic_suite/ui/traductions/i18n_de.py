from __future__ import annotations

from typing import Dict

TRANSLATIONS_DE: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Anwendung
    # ------------------------------------------------------------------
    "app.title": "EML / IMAP Forensic Suite (Nur-Lese-Modus)",

    # ------------------------------------------------------------------
    # Menüs
    # ------------------------------------------------------------------
    "menu.file": "Datei",
    "menu.view": "Ansicht",
    "menu.help": "Hilfe",

    "menu.file.settings": "Einstellungen…",
    "menu.file.quit": "Beenden",

    "menu.view.theme.dark": "Dunkles Thema",
    "menu.view.theme.light": "Helles Thema",

    "menu.help.about": "Info…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. IMAP-Export",
    "tab.index": "2. EML-Indexierung",
    "tab.viewer": "3. Forensischer Viewer",
    "tab.dashboard": "4. Forensisches Dashboard",

    # ------------------------------------------------------------------
    # Einstellungsdialog
    # ------------------------------------------------------------------
    "settings.title": "Einstellungen",
    "settings.reports_dir.label": "Arbeits- / Berichtverzeichnis:",
    "settings.reports_dir.browse": "Durchsuchen…",
    "settings.language.label": "Sprache der Oberfläche:",
    "settings.reports_dir.dialog_title": (
        "Arbeits- / Berichtverzeichnis auswählen"
    ),

    # ------------------------------------------------------------------
    # Status / Verschiedenes
    # ------------------------------------------------------------------
    "status.ready": "Bereit.",
    "status.settings.saved": "Einstellungen gespeichert.",

    # ------------------------------------------------------------------
    # Index-Tab (EML-Indexierung)
    # ------------------------------------------------------------------
    "index.folder_label": "EML-Exportverzeichnis:",
    "index.browse": "Durchsuchen…",
    "index.use_last_export": "Letzten IMAP-Export verwenden",
    "index.log_placeholder": "Protokoll der EML-Indexierung (Nur-Lese-Modus)…",
    "index.start_button": "EML-Indexierung starten",
    "index.dialog_select_folder": "EML-Exportverzeichnis auswählen",
    "index.no_last_export": (
        "Noch kein IMAP-Export bekannt (Tab 1)."
    ),
    "index.error_already_running_title": "Indexierung läuft bereits",
    "index.error_already_running_body": (
        "Eine EML-Indexierung ist bereits im Gange."
    ),
    "index.error_no_folder_title": "Verzeichnis fehlt",
    "index.error_no_folder_body": (
        "Bitte wählen Sie ein Verzeichnis mit .eml-Dateien aus."
    ),
    "index.error_invalid_folder_title": "Ungültiges Verzeichnis",
    "index.error_invalid_folder_body": (
        "Das angegebene Verzeichnis existiert nicht:\n{folder}"
    ),
    "index.status_selected_folder": (
        "Für die Indexierung ausgewähltes Verzeichnis: {folder}"
    ),
    "index.error_indexing_title": "Fehler bei der Indexierung",
    "index.error_log": "❌ Fehler: {error}",
    "index.done_log_success": "\nIndexierung erfolgreich abgeschlossen.",
    "index.done_log_path": "CSV-Pfad: {csv_path}",
    "index.done_log_count": "Anzahl indexierter Einträge: {count}",
    "index.done_msg_title": "Indexierung abgeschlossen",
    "index.done_msg_body": (
        "EML-Indexierung abgeschlossen.\n\nCSV-Datei: {csv_path}\nEinträge: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard-Tab (Basis)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "Letzten Index verwenden",
    "dashboard.open_csv": "CSV-Index öffnen…",
    "dashboard.placeholder": (
        "Forensische Statistikzusammenfassung basierend auf dem EML-Index…"
    ),
    "dashboard.source_memory": (
        "Quelle: Index im Speicher (letzte Indexierung dieser Sitzung)."
    ),
    "dashboard.source_csv": "Quelle: {path}",
    "dashboard.no_index_title": "Kein Index",
    "dashboard.no_index_body": (
        "In dieser Sitzung ist kein Index verfügbar.\n"
        "Erstellen Sie einen Index in Tab 2 oder öffnen Sie eine CSV-Datei."
    ),
    "dashboard.dialog_open_csv": "CSV-Indexdatei öffnen",
    "dashboard.error_csv_missing_title": "Datei nicht gefunden",
    "dashboard.error_csv_missing_body": (
        "Die angegebene Datei existiert nicht:\n{path}"
    ),
    "dashboard.error_csv_read_title": "CSV-Lesefehler",
    "dashboard.error_csv_read_body": (
        "Die CSV-Datei kann nicht gelesen werden: {path}"
    ),
    "dashboard.empty_csv_title": "Leerer Index",
    "dashboard.empty_csv_body": (
        "Die CSV-Datei enthält keine verwertbaren Einträge."
    ),
    "dashboard.no_data": "Keine Daten zu analysieren.",

    "dashboard.section_overview": "Übersicht",
    "dashboard.overview_line": (
        "Gesamtzahl E-Mails: {total} – Unterschiedliche Absender: {senders}"
    ),
    "dashboard.dates_line": "Abgedeckter Zeitraum: {date_min} → {date_max}",
    "dashboard.dates_unknown": (
        "Datumsangaben nicht verfügbar oder nicht auswertbar."
    ),

    "dashboard.section_folders": "Verteilung nach IMAP-Ordner",
    "dashboard.no_folders": "Keine IMAP-Ordner erkannt.",

    "dashboard.section_domains": "Verteilung nach Domain (Absender)",
    "dashboard.no_domains": "Keine Domains erkannt.",

    "dashboard.section_attachments": "Anhänge",
    "dashboard.attachments_line": (
        "E-Mails mit Anhängen: {with_att}/{total} – "
        "Geschätzte Gesamtzahl der Anhänge: {total_att}"
    ),

    "dashboard.section_auth": "Authentifizierung (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "DKIM-Ergebnisse:",
    "dashboard.auth_header_spf": "SPF-Ergebnisse:",
    "dashboard.auth_header_dmarc": "DMARC-Ergebnisse:",

    "dashboard.section_integrity": "Integrität / fehlende Header",
    "dashboard.integrity_flags_title": "Erkannte Integritäts-Flags:",
    "dashboard.no_integrity_flags": (
        "Keine speziellen Integritäts-Flags erkannt."
    ),

    "dashboard.section_received": "Anomalien in der Received-Kette",
    "dashboard.no_received_anomalies": (
        "Keine Received-Anomalien erkannt (mit den aktuellen Regeln)."
    ),

    # ------------------------------------------------------------------
    # Viewer – Spalten (Basis)
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "IMAP-Ordner",
    "viewer.col.sequence_number": "Sequenz",
    "viewer.col.date_header": "Datum",
    "viewer.col.from_header": "From",
    "viewer.col.to_header": "To",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Bcc",
    "viewer.col.subject": "Betreff",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "Anhänge?",
    "viewer.col.attachment_count": "Anzahl Anhänge",
    "viewer.col.attachment_filenames": "Anhangsnamen",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (Auszug)",
    "viewer.col.received_count": "Anzahl Received",
    "viewer.col.received_anomalies": "Received-Anomalien",
    "viewer.col.integrity_flags": "Integritäts-Flags",
    "viewer.col.relative_path": "Relativer Pfad",
    "viewer.col.filename": "Dateiname",

    # ------------------------------------------------------------------
    # Viewer – Suche & Bereiche
    # ------------------------------------------------------------------
    "viewer.search_label": "Suche:",
    "viewer.search_placeholder": (
        "Im Index filtern (alle Spalten)…"
    ),
    "viewer.search_clear": "Löschen",

    "viewer.headers_label": "Header",
    "viewer.headers_placeholder": (
        "Header der ausgewählten Nachricht…"
    ),

    "viewer.body_label": "Textkörper",
    "viewer.body_placeholder": (
        "text/plain-Body (oder Roh-HTML als Fallback) der ausgewählten Nachricht…"
    ),

    "viewer.btn_load_last": "Letzten IMAP-Export verwenden",
    "viewer.btn_open_csv": "CSV-Index öffnen...",
    "viewer.attachments_label": "Anhänge",

    # ------------------------------------------------------------------
    # Viewer – EML-Fehler
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "EML-Datei nicht gefunden",
    "viewer.error_missing_eml_body": (
        "Die EML-Datei konnte auf der Festplatte nicht gefunden werden:\n{path}"
    ),
    "viewer.error_parse_eml_title": "EML-Lesefehler",
    "viewer.error_parse_eml_body": (
        "Die EML-Datei konnte nicht geparst werden: {path}"
    ),

    # ------------------------------------------------------------------
    # Viewer – Spalten für Anhänge
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "Name",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "Größe (Bytes)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "Verdächtig?",

    "viewer.attach.yes": "Ja",
    "viewer.attach.no": "Nein",

    # ------------------------------------------------------------------
    # IMAP – Verbindung / Felder
    # ------------------------------------------------------------------
    "imap.group.connection": "IMAP-Server (Beweisquelle)",
    "imap.label.host": "Adresse des IMAP-Servers",
    "imap.label.user": "Kennung des analysierten Postfachs",
    "imap.label.password": "Passwort (nie gespeichert)",
    "imap.label.date_start": "Startdatum (forensischer Filter)",
    "imap.label.date_end": "Enddatum (forensischer Filter)",

    "imap.placeholder.host": "z. B. imap.example.com",
    "imap.placeholder.user": "z. B. incident@firma.de",
    "imap.placeholder.password": "Passwort des analysierten Kontos",
    "imap.placeholder.date_start": "TT/MM/JJJJ (optional)",
    "imap.placeholder.date_end": "TT/MM/JJJJ (optional)",

    "imap.button.fetch_mailboxes": "IMAP-Ordner inspizieren…",
    "imap.button.start_export": "Forensische Extraktion starten",
    "imap.button.cancel_export": "Extraktion abbrechen",

    "imap.label.mailboxes_title": (
        "Zu extrahierende IMAP-Ordner (Beweisquelle):"
    ),
    "imap.checkbox.select_all": "Alle Ordner auswählen",

    "imap.log.placeholder": (
        "Protokoll der IMAP-Extraktion (Nur-Lese-Modus, mit Zeitstempeln)…"
    ),

    # ------------------------------------------------------------------
    # IMAP – Fehlermeldungen / Infos
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "Unvollständige Parameter",
    "imap.error.missing_fields.body": (
        "Bitte IMAP-Server, Benutzername und Passwort angeben."
    ),

    "imap.info.export_running.title": "Extraktion läuft bereits",
    "imap.info.export_running.body": (
        "Es läuft bereits eine IMAP-Extraktion."
    ),

    "imap.error.date_invalid.title": "Ungültiges Datum",
    "imap.error.date_invalid.body": (
        "Fehler in den angegebenen Daten: {error}"
    ),
    "imap.error.date_end_before_start.body": (
        "Das Enddatum darf nicht vor dem Startdatum liegen."
    ),

    "imap.error.no_mailbox_selected.title": "Kein Ordner ausgewählt",
    "imap.error.no_mailbox_selected.body": (
        "Bitte wählen Sie mindestens einen IMAP-Ordner für die Extraktion."
    ),

    "imap.error.fetch_mailboxes.title": "IMAP-Fehler",
    "imap.error.fetch_mailboxes.body": (
        "Die Liste der IMAP-Ordner konnte nicht abgerufen werden:\n{error}"
    ),

    "imap.info.generic.title": "Information",
    "imap.error.generic.title": "Fehler",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "Verbindung zu {host}:{port} wird hergestellt (SSL={use_ssl})...",
    "imap.log.connected": "Mit dem IMAP-Server verbunden.",
    "imap.log.select_folder": "Ordner \"{folder}\" wird ausgewählt...",
    "imap.log.folder_selected": "Ordner \"{folder}\" ausgewählt.",
    "imap.log.message_count": "{count} Nachrichten zu exportieren.",
    "imap.log.fetching": "IMAP-Nachrichten werden abgerufen...",
    "imap.log.export_done": "IMAP-Export abgeschlossen.",
    "imap.log.saving_to": "Nachrichten werden in \"{output_dir}\" gespeichert...",
    "imap.log.progress": "Nachricht {current}/{total} wird exportiert...",
    "imap.log.skip_existing": "Datei \"{path}\" ist bereits vorhanden, wird übersprungen.",

    "imap.error.connect_failed": "Verbindung zu {host}:{port} nicht möglich: {error}",
    "imap.error.login_failed": "IMAP-Authentifizierungsfehler: {error}",
    "imap.error.select_failed": "Ordner \"{folder}\" kann nicht ausgewählt werden: {error}",
    "imap.error.fetch_failed": "Fehler beim Abrufen der Nachrichten: {error}",
    "imap.error.generic": "Fehler während des IMAP-Exports: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== IMAP-Exportbericht (schreibgeschützt) ===",
    "imap.report.tool_line": "Werkzeug   : eml_forensic_suite – IMAP-Export",
    "imap.report.version_line": "Version   : {version}",
    "imap.report.folder_line": "Ordner    : {export_dir}",

    "imap.report.section_tool": "---- Werkzeuginformationen ----",
    "imap.report.tool_path": "Werkzeugpfad         : {tool_path}",
    "imap.report.tool_hash": "Werkzeug-SHA-256     : {tool_hash}",

    "imap.report.section_env": "---- Laufzeitumgebung ----",
    "imap.report.env_os": "Betriebssystem       : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Python-Version       : {python_version}",

    "imap.report.section_context": "---- IMAP- / Konto-Kontext ----",
    "imap.report.context_host": "IMAP-Server : {host}",
    "imap.report.context_user": "Konto       : {user}",
    "imap.report.context_date_start": "Angeforderter Starttermin : {date_start}",
    "imap.report.context_date_end": "Angefordertes Enddatum   : {date_end}",
    "imap.report.context_criteria": "IMAP-Suchkriterien : {search_criteria} (wie an den Server gesendet)",

    "imap.report.selected_folders_title": "Ausgewählte Ordner:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- IMAP-Serverinformationen ----",
    "imap.report.server_greeting": "IMAP-Banner  : {greeting}",
    "imap.report.server_capability": "CAPABILITY   : {capability}",

    "imap.report.section_timestamps": "---- Analysezeitstempel ----",
    "imap.report.timestamp_start_utc": "Analysestart (UTC)     : {dt}",
    "imap.report.timestamp_start_local": "Analysestart (lokal)   : {dt}",
    "imap.report.timestamp_end_utc": "Analyseende (UTC)      : {dt}",
    "imap.report.timestamp_end_local": "Analyseende (lokal)    : {dt}",
    "imap.report.duration": "Gesamtdauer           : {duration}",

    "imap.report.section_folders": "---- Analysierte Ordner ----",
    "imap.report.folders_count": "Anzahl ausgewählter Ordner : {count}",

    "imap.report.folder_header": "Ordner : {name}",
    "imap.report.folder_messages": "  Gefundene Nachrichten (Zeitraum) : {count}",
    "imap.report.folder_exported": "  Exportierte Nachrichten          : {count}",
    "imap.report.folder_errors": "  Abruffehler                      : {count}",
    "imap.report.folder_bytes": "  Heruntergeladenes Volumen        : {bytes} Bytes",
    "imap.report.folder_size_stats": "  Min. / max. / durchschn. Größe   : {min_size} / {max_size} / {avg_size} Bytes",
    "imap.report.folder_period": "  Abgedeckter Zeitraum (INTERNALDATE) : {first} → {last}",
    "imap.report.folder_error_uids": "  UIDs mit Fehlern (nicht abschließende Liste) : {uids}",

    "imap.report.section_totals": "---- Gesamtsummen ----",
    "imap.report.total_messages": "Gefundene Nachrichten (alle Ordner) : {count}",
    "imap.report.total_exported": "Exportierte Nachrichten              : {count}",
    "imap.report.total_errors": "Abruffehler                          : {count}",
    "imap.report.total_bytes": "Gesamt heruntergeladenes Volumen     : {bytes} Bytes",

    "imap.report.section_forensic": "---- Methodik und forensische Garantien ----",
    "imap.report.forensic_item_readonly": "- Das Werkzeug hat ausschließlich schreibgeschützte IMAP-Befehle (SELECT readonly, SEARCH, FETCH) verwendet. Während der Analyse wurde keine Nachricht geändert, gelöscht oder als gelesen markiert.",
    "imap.report.forensic_item_eml": "- Nachrichten wurden exakt so exportiert, wie sie vom IMAP-Server geliefert wurden, und unverändert als .eml-Dateien auf die Festplatte geschrieben.",
    "imap.report.forensic_item_hashes": "- Jede exportierte Nachricht ist einem SHA-256-Hash zugeordnet, der in hashes.txt aufgeführt ist, sowie einem globalen Hash, der aus der Verkettung aller Einzel-Hashes berechnet wird.",
    "imap.report.forensic_item_report_hash": "- Dieser Analysebericht selbst wird mit SHA-256 gehasht; dieser Hash wird in hashes.txt aufgenommen, um die Integrität des Berichts zu gewährleisten.",

    "imap.report.hashes_report_header": "ANALYSEBERICHT:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "Kein Ordner ausgewählt.",
    "imap.worker.log_export_dir": "Exportordner: {export_dir}",
    "imap.worker.tool_hash_error": "(Fehler bei der Berechnung des Werkzeug-Hashes)",

    "imap.worker.log_connecting": "Verbindung zum IMAP-Server wird hergestellt...",
    "imap.worker.greeting_not_available": "(IMAP-Banner nicht verfügbar)",
    "imap.worker.log_auth_classic": "Klassische IMAP-Authentifizierung...",
    "imap.worker.error_auth_failed": "IMAP-Authentifizierungsfehler: {error}",
    "imap.worker.capability_error": "(Fehler beim CAPABILITY-Befehl)",

    "imap.worker.log_date_start_inclusive": "Startdatum (einschließlich): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "Startdatum: nicht gesetzt → Extraktion ab der ersten verfügbaren Nachricht.",
    "imap.worker.date_start_unset_label": "Erste verfügbare Nachricht (keine Untergrenze)",

    "imap.worker.log_date_end_inclusive": "Enddatum (einschließlich): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "Enddatum: nicht gesetzt → bis zur letzten auf dem Server verfügbaren Nachricht.",
    "imap.worker.date_end_unset_label": "Letzte verfügbare Nachricht (keine Obergrenze)",

    "imap.worker.log_criteria": "Verwendete IMAP-Suchkriterien: {criteria}",
    "imap.worker.log_selected_folders_header": "Ausgewählte Ordner ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "Stoppanforderung während der Zählphase.",
    "imap.worker.log_phase1_count": "[Phase 1] Nachrichten in {folder} werden gezählt...",
    "imap.worker.log_select_folder_failed": "  ⚠️ Ordner kann nicht ausgewählt werden, wird übersprungen.",
    "imap.worker.log_search_folder_failed": "  ⚠️ Fehler bei der Suche in diesem Ordner, wird übersprungen.",
    "imap.worker.log_messages_to_process": "  → {count} zu verarbeitende Nachrichten in {folder}",

    "imap.worker.log_total_messages_to_download": "Gesamtzahl der herunterzuladenden Nachrichten (alle Ordner): {count}",

    "imap.worker.log_stop_during_export": "Stoppanforderung: Export wird abgebrochen.",
    "imap.worker.log_folder_header": "=== Ordner: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  Keine Nachrichten in {folder} für diesen Zeitraum.",
    "imap.worker.log_folder_message_count": "  Anzahl gefundener Nachrichten in {folder}: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ Ordner kann nicht erneut ausgewählt werden, wird übersprungen.",

    "imap.worker.log_first_message_download": "  Erste Nachricht wird heruntergeladen ({uid})...",
    "imap.worker.log_folder_progress": "  Fortschritt Ordner {folder}: {current}/{total} (letzte: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ Fehler beim Abrufen der Nachricht {uid}, es wird fortgefahren.",
    "imap.worker.log_folder_end": "  Ende des Ordners {folder}",

    "imap.worker.hashes_header": "Liste der exportierten Dateien und ihrer SHA-256-Hashes",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "GLOBALER HASH (nur Nachrichten):",

    "imap.worker.log_export_done_header": "=== Export abgeschlossen ===",
    "imap.worker.log_export_done_count": "Gesamtzahl der exportierten Nachrichten: {count}",
    "imap.worker.log_export_done_hashes_file": "Hashes-Datei: {path}",
    "imap.worker.log_export_done_hash": "Globaler Hash: {file_hash}",

    "imap.worker.summary": (
        "Export abgeschlossen.\n\n"
        "Exportierte Nachrichten: {count}\n"
        "Ordner: {export_dir}\n\n"
        "Globaler Hash (Nachrichten):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "Analysebericht erzeugt und gehasht (siehe rapport_imap_export.txt und hashes.txt).",
    "imap.worker.log_report_failed": "⚠️ Analysebericht konnte nicht erzeugt werden: {error}",

    "imap.worker.error_generic": "Es ist ein Fehler aufgetreten: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "Verbindung zum IMAP-Server wird hergestellt...",
    "imap.tk.log_auth_classic": "Klassische IMAP-Authentifizierung...",
    "imap.tk.error_list_mailboxes_failed": "IMAP-Ordner können nicht aufgelistet werden.",

    "imap.tk.log_folders_found_header": "Auf dem Server gefundene Ordner:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "IMAP-Ordner insgesamt: {count}",

    "imap.tk.msgbox_error_title": "Fehler",
    "imap.tk.msgbox_error_fetch_mailboxes": "Fehler beim Abrufen der IMAP-Ordner: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ Fehler beim Abrufen der Ordner: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. IMAP-Export",

    "imap.tk.label_server": "IMAP-Server:",
    "imap.tk.label_email": "E-Mail-Adresse:",
    "imap.tk.label_password": "Passwort:",
    "imap.tk.label_date_start": "Startdatum (TT/MM/JJJJ, optional):",
    "imap.tk.label_date_end": "Enddatum (TT/MM/JJJJ, optional):",
    "imap.tk.label_log": "Protokoll:",
    "imap.tk.label_mailboxes": "Zu exportierende IMAP-Ordner:",
    "imap.tk.checkbox_select_all": "Alle auswählen / Auswahl aufheben",
    "imap.tk.label_progress": "Fortschritt:",

    "imap.tk.msgbox_missing_fields_title": "Fehlende Felder",
    "imap.tk.msgbox_missing_fields_text": "Bitte Server, E-Mail-Adresse und Passwort ausfüllen.",

    "imap.tk.log_fetch_mailboxes_start": "IMAP-Ordner werden abgerufen...",
    "imap.tk.log_no_mailboxes_or_error": "Kein Ordner gefunden oder es ist ein Fehler aufgetreten.",
    "imap.tk.log_select_mailboxes_hint": "Wählen Sie die zu exportierenden Ordner aus.",

    "imap.tk.button_list_mailboxes": "IMAP-Ordner auflisten",

    "imap.tk.msgbox_date_start_invalid_title": "Ungültiges Startdatum",
    "imap.tk.msgbox_date_start_invalid_text": "Das Startdatum muss im Format TT/MM/JJJJ vorliegen.",

    "imap.tk.msgbox_date_end_invalid_title": "Ungültiges Enddatum",
    "imap.tk.msgbox_date_end_invalid_text": "Das Enddatum muss im Format TT/MM/JJJJ vorliegen.",

    "imap.tk.msgbox_date_range_invalid_title": "Ungültiger Datumsbereich",
    "imap.tk.msgbox_date_range_invalid_text": (
        "Das Enddatum darf nicht vor dem Startdatum liegen."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "Kein Ordner ausgewählt",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "Bitte wählen Sie mindestens einen IMAP-Ordner aus (über „IMAP-Ordner auflisten“)."
    ),

    "imap.tk.log_export_start": "Export wird gestartet...",
    "imap.tk.button_run_export": "Export starten (ausgewählte Ordner)",

    "imap.tk.log_stop_requested": (
        "Stoppanforderung, der Export wird sauber beendet..."
    ),
    "imap.tk.button_stop_export": "Export stoppen",

    "imap.tk.msgbox_export_done_title": "Export abgeschlossen",


    # ------------------------------------------------------------------
    # IMAP – Protokolle
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "Verbindung zum IMAP-Server zur Ordner-Aufzählung wird hergestellt…"
    ),
    "imap.log.fetch_error": "❌ Fehler beim Abrufen der Ordner:",
    "imap.log.no_mailboxes": (
        "Auf diesem Konto wurden keine IMAP-Ordner gefunden."
    ),
    "imap.log.mailboxes_found": "Auf dem Server gefundene Ordner:",
    "imap.log.mailboxes_total": "Anzahl IMAP-Ordner: {count}",
    "imap.log.mailboxes_select_hint": (
        "Wählen Sie die Ordner, die im Nur-Lese-Modus extrahiert werden sollen."
    ),
    "imap.log.start_export": (
        "IMAP-Extraktion wird gestartet (forensischer Modus, Nur-Lese)…"
    ),
    "imap.log.cancel_requested": (
        "Abbruchanforderung an IMAP-Worker gesendet…"
    ),
    "imap.log.export_dir_saved": "Exportverzeichnis gespeichert: {path}",
    "imap.log.done": "IMAP-Verarbeitung abgeschlossen.",

    # ------------------------------------------------------------------
    # Dashboard v3 – Sektionen / Tabs
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "Verdachtsstufen",
    "dashboard.tab_text": "EML-Index-Zusammenfassung",
    "dashboard.tab_graphs": "Diagramme",
    "dashboard.section_charts": "Grafische Visualisierungen",

    "dashboard.chart_suspicion_title": (
        "Verteilung der Verdachtsstufen"
    ),
    "dashboard.chart_folders_title": "Nachrichten pro IMAP-Ordner",
    "dashboard.chart_domains_title": (
        "Häufigste Absender-Domains"
    ),
    "dashboard.chart_attachments_title": "Vorhandensein von Anhängen",
    "dashboard.chart_axis_count": "Anzahl",
    "dashboard.chart_attachments_with": "Mit Anhängen",
    "dashboard.chart_attachments_without": "Ohne Anhänge",

    # Legende / Text rund um das Scoring
    "dashboard.suspicion_distribution_line": (
        "Verteilung der E-Mails nach Verdachtsstufe:"
    ),
    "dashboard.suspicion_level.LOW": "Niedrig",
    "dashboard.suspicion_level.MEDIUM": "Mittel",
    "dashboard.suspicion_level.HIGH": "Hoch",
    "dashboard.suspicion_level.CRITICAL": "Kritisch",
    "dashboard.suspicion_level.UNKNOWN": "Unbekannt",

    # Diagramm-Titel (neue Namensgebung)
    "dashboard.chart.folders.title": "E-Mails pro IMAP-Ordner",
    "dashboard.chart.domains.title": "Top Absender-Domains",
    "dashboard.chart.attachments.title": "Vorhandensein von Anhängen",
    "dashboard.chart.auth.title": "DKIM / SPF / DMARC-Ergebnisse",
    "dashboard.chart.suspicion.title": "Verteilung nach Verdachtsstufe",

    # Diagramme – Achsen / Zustände
    "dashboard.chart.no_data": (
        "Nicht genügend Daten, um dieses Diagramm anzuzeigen."
    ),
    "dashboard.chart.axis.emails": "Anzahl E-Mails",
    "dashboard.chart.axis.folders": "IMAP-Ordner",
    "dashboard.chart.axis.domains": "Domains",
    "dashboard.chart.axis.levels": "Stufen",

    # Kleine visuelle Hilfe zu den Farben
    "dashboard.legend.safe": "Bereich, der eher als sicher gilt",
    "dashboard.legend.suspicious": "Bereich, der vorrangig untersucht werden sollte",

    # ------------------------------------------------------------------
    # Viewer – Scoring- & Verdachtsspalten
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "Verdachtsscore",
    "viewer.col.suspicion_level": "Stufe",
    "viewer.col.suspicion_reasons": "Gründe (Kurzfassung)",

    # Tooltips Scoring
    "viewer.score.tooltip.base": (
        "Globaler Verdachtsscore, berechnet aus DKIM/SPF/DMARC, "
        "Received-Anomalien, Header-Integrität und Anhängen."
    ),
    "viewer.score.level.LOW": (
        "Niedriger Verdacht: Nach den aktuellen Regeln wurde nichts Auffälliges erkannt."
    ),
    "viewer.score.level.MEDIUM": (
        "Mittlerer Verdacht: Einige Elemente sollten überprüft werden "
        "(Header, Authentifizierung oder Anhänge)."
    ),
    "viewer.score.level.HIGH": (
        "Hoher Verdacht: Mehrere technische Indikatoren sind inkonsistent oder gefährlich."
    ),
    "viewer.score.level.CRITICAL": (
        "Kritischer Verdacht: Die E-Mail ist sehr wahrscheinlich bösartig oder gefälscht."
    ),

    # ------------------------------------------------------------------
    # IMAP – Text zu OAuth-Beschränkungen
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "Dieses Konto scheint von einem Anbieter verwaltet zu werden, der moderne "
        "Mechanismen (OAuth2, offizielle Exporte) für den Nachrichtenzugriff verlangt "
        "(z. B. Gmail, Outlook/Microsoft 365, Yahoo).\n\n"
        "Um konform zu bleiben und diese Regeln nicht zu umgehen, führt diese Version von "
        "eml_forensic_suite keine direkte IMAP-Extraktion für diese Dienste durch.\n\n"
        "Um Nachrichten kompatibel zu exportieren:\n"
        "  • Gmail: Verwenden Sie Google Takeout, um das Postfach (MBOX) zu exportieren,\n"
        "    oder einen Client wie Thunderbird, um eine lokale Kopie zu erstellen.\n"
        "  • Outlook / Microsoft 365: Verwenden Sie den Export Ihres Outlook-Clients\n"
        "    (PST) oder die Archivierungstools Ihrer Organisation.\n"
        "  • Yahoo usw.: Verwenden Sie die vom Anbieter bereitgestellten Exportwerkzeuge.\n\n"
        "Zukünftige Versionen von eml_forensic_suite sollen diese Exporte "
        "(MBOX, PST usw.) direkt analysieren, um mit diesen Plattformen kompatibel zu bleiben."
    ),

    # ------------------------------------------------------------------
    # Viewer – Mini-Suchsprache
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "Forensische Mini-Sprache:\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "Operatoren: implizites AND, OR, NOT, Klammern."
    ),

    # ------------------------------------------------------------------
    # Viewer – generische Index-/CSV-Meldungen
    # ------------------------------------------------------------------
    "viewer.no_index_title": "Kein Index verfügbar",
    "viewer.no_index_body": (
        "In dieser Sitzung ist kein Index verfügbar.\n"
        "Erstellen Sie einen Index in Tab 2 oder öffnen Sie eine CSV-Datei."
    ),
    "viewer.open_csv_title": "CSV-Indexdatei öffnen",
    "viewer.error_csv_title": "CSV-Lesefehler",
    "viewer.error_csv_body": (
        "Die CSV-Datei kann nicht gelesen werden: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – Vorschau (Nur-Lese)
    # ------------------------------------------------------------------
    "viewer.attach.preview": "Nur-Lese-Vorschau",
    "viewer.attach.preview_failed_title": "Vorschau nicht möglich",
    "viewer.attach.preview_failed_body": (
        "Für diesen Anhang kann keine Vorschau angezeigt werden."
    ),
    "viewer.attach.preview_unsupported_title": "Nicht unterstützter Typ",
    "viewer.attach.preview_unsupported_body": (
        "Für diesen MIME-Typ steht keine integrierte Vorschau zur Verfügung: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – Extraktion von Anhängen
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "Keine Nachricht",
    "viewer.attach.no_msg_body": (
        "Derzeit ist keine Nachricht ausgewählt."
    ),
    "viewer.attach.no_selection_title": "Kein Anhang ausgewählt",
    "viewer.attach.no_selection_body": (
        "Bitte wählen Sie einen Anhang in der Liste aus."
    ),
    "viewer.attach.no_root_title": "Arbeitsverzeichnis nicht gefunden",
    "viewer.attach.no_root_body": (
        "Es ist kein forensisches / Indexverzeichnis für die Extraktion konfiguriert."
    ),
    "viewer.attach.extract_one_title": "Anhang extrahiert",
    "viewer.attach.extract_one_body": (
        "Der Anhang wurde extrahiert nach:\n{path}"
    ),
    "viewer.attach.extract_all_title": "Anhänge extrahiert",
    "viewer.attach.extract_all_body": (
        "{count} Anhänge wurden extrahiert nach:\n{paths}"
    ),

    # Buttons für Anhänge
    "viewer.attach.extract_one": "Ausgewählten Anhang extrahieren",
    "viewer.attach.extract_all": "Alle Anhänge extrahieren",

    # ------------------------------------------------------------------
    # About-Box
    # ------------------------------------------------------------------
    "about.version_label": "Version:",
    "about.description": (
        "Nur-Lese-Werkzeug für die forensische Analyse von EML/IMAP-E-Mails."
    ),
}
