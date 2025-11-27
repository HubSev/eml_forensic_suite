from __future__ import annotations

from typing import Dict

TRANSLATIONS_EN: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "EML / IMAP Forensic Suite (read only)",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "File",
    "menu.view": "View",
    "menu.help": "Help",

    "menu.file.settings": "Settings…",
    "menu.file.quit": "Quit",

    "menu.view.theme.dark": "Dark theme",
    "menu.view.theme.light": "Light theme",

    "menu.help.about": "About…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. IMAP export",
    "tab.index": "2. EML indexing",
    "tab.viewer": "3. Forensic viewer",
    "tab.dashboard": "4. Forensic dashboard",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "Settings",
    "settings.reports_dir.label": "Working / reports directory:",
    "settings.reports_dir.browse": "Browse…",
    "settings.language.label": "Interface language:",
    "settings.reports_dir.dialog_title": "Choose working / reports directory",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "Ready.",
    "status.settings.saved": "Settings saved.",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "EML export directory:",
    "index.browse": "Browse…",
    "index.use_last_export": "Use last IMAP export",
    "index.log_placeholder": "EML indexing log (read only)…",
    "index.start_button": "Start EML indexing",
    "index.dialog_select_folder": "Select EML export folder",
    "index.no_last_export": "No IMAP export known yet (tab 1).",
    "index.error_already_running_title": "Indexing already running",
    "index.error_already_running_body": "An EML indexing operation is already running.",
    "index.error_no_folder_title": "Missing folder",
    "index.error_no_folder_body": "Please select a folder containing .eml files.",
    "index.error_invalid_folder_title": "Invalid folder",
    "index.error_invalid_folder_body": "The specified folder does not exist:\n{folder}",
    "index.status_selected_folder": "Selected folder for indexing: {folder}",
    "index.error_indexing_title": "Error during indexing",
    "index.error_log": "❌ Error: {error}",
    "index.done_log_success": "\nIndexing completed successfully.",
    "index.done_log_path": "CSV path: {csv_path}",
    "index.done_log_count": "Number of indexed entries: {count}",
    "index.done_msg_title": "Indexing finished",
    "index.done_msg_body": (
        "EML indexing completed.\n\nCSV file: {csv_path}\nEntries: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "Use last index",
    "dashboard.open_csv": "Open index CSV…",
    "dashboard.placeholder": "Forensic statistical summary based on the EML index…",
    "dashboard.source_memory": "Source: in-memory index (last indexing in this session).",
    "dashboard.source_csv": "Source: {path}",
    "dashboard.no_index_title": "No index",
    "dashboard.no_index_body": (
        "No index is available in this session.\n"
        "Generate an index in tab 2 or open a CSV manually."
    ),
    "dashboard.dialog_open_csv": "Open index CSV file",
    "dashboard.error_csv_missing_title": "File not found",
    "dashboard.error_csv_missing_body": "The specified file does not exist:\n{path}",
    "dashboard.error_csv_read_title": "CSV read error",
    "dashboard.error_csv_read_body": "Unable to read CSV file: {path}",
    "dashboard.empty_csv_title": "Empty index",
    "dashboard.empty_csv_body": "The CSV file does not contain any usable entries.",
    "dashboard.no_data": "No data to analyze.",

    "dashboard.section_overview": "Overview",
    "dashboard.overview_line": (
        "Total emails: {total} – Distinct senders: {senders}"
    ),
    "dashboard.dates_line": "Covered period: {date_min} → {date_max}",
    "dashboard.dates_unknown": "Dates not available or not parsable.",

    "dashboard.section_folders": "Distribution by IMAP folder",
    "dashboard.no_folders": "No IMAP folders detected.",

    "dashboard.section_domains": "Distribution by domain (sender)",
    "dashboard.no_domains": "No domains detected.",

    "dashboard.section_attachments": "Attachments",
    "dashboard.attachments_line": (
        "Emails with attachments: {with_att}/{total} – Estimated total attachments: {total_att}"
    ),

    "dashboard.section_auth": "Authentication (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "DKIM results:",
    "dashboard.auth_header_spf": "SPF results:",
    "dashboard.auth_header_dmarc": "DMARC results:",

    "dashboard.section_integrity": "Integrity / missing headers",
    "dashboard.integrity_flags_title": "Detected integrity flags:",
    "dashboard.no_integrity_flags": "No specific integrity flags detected.",

    "dashboard.section_received": "Anomalies on the Received chain",
    "dashboard.no_received_anomalies": (
        "No Received anomalies detected (under current rules)."
    ),

    # ------------------------------------------------------------------
    # Viewer tab – columns de base
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "IMAP folder",
    "viewer.col.sequence_number": "Sequence",
    "viewer.col.date_header": "Date",
    "viewer.col.from_header": "From",
    "viewer.col.to_header": "To",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Bcc",
    "viewer.col.subject": "Subject",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "Attachments?",
    "viewer.col.attachment_count": "Attachments count",
    "viewer.col.attachment_filenames": "Attachment names",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (excerpt)",
    "viewer.col.received_count": "Received count",
    "viewer.col.received_anomalies": "Received anomalies",
    "viewer.col.integrity_flags": "Integrity flags",
    "viewer.col.relative_path": "Relative path",
    "viewer.col.filename": "Filename",

    # ------------------------------------------------------------------
    # Viewer tab – search + zones
    # ------------------------------------------------------------------
    "viewer.search_label": "Search:",
    "viewer.search_placeholder": "Filter in index (all columns)…",
    "viewer.search_clear": "Clear",

    "viewer.headers_label": "Headers",
    "viewer.headers_placeholder": "Headers of the selected message…",

    "viewer.body_label": "Body (text)",
    "viewer.body_placeholder": (
        "text/plain body (or raw HTML fallback) of the selected message…"
    ),

    "viewer.btn_load_last": "Use last IMAP export",
    "viewer.btn_open_csv": "Open index CSV...",
    "viewer.attachments_label": "Attachments",

    # ------------------------------------------------------------------
    # Viewer – erreurs EML
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "EML file not found",
    "viewer.error_missing_eml_body": "Unable to find the EML file on disk:\n{path}",
    "viewer.error_parse_eml_title": "EML read error",
    "viewer.error_parse_eml_body": "Unable to parse EML file: {path}",

    # ------------------------------------------------------------------
    # Viewer – colonnes PJ
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "Name",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "Size (bytes)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "Suspicious?",

    "viewer.attach.yes": "Yes",
    "viewer.attach.no": "No",

    # ------------------------------------------------------------------
    # IMAP tab – connexion & champs
    # ------------------------------------------------------------------
    "imap.group.connection": "IMAP server (evidence source)",
    "imap.label.host": "IMAP server address",
    "imap.label.user": "Analyzed mailbox identifier",
    "imap.label.password": "Password (never stored)",
    "imap.label.date_start": "Start date (forensic filter)",
    "imap.label.date_end": "End date (forensic filter)",

    "imap.placeholder.host": "e.g. imap.example.com",
    "imap.placeholder.user": "e.g. incident@company.com",
    "imap.placeholder.password": "Password of the analyzed account",
    "imap.placeholder.date_start": "DD/MM/YYYY (optional)",
    "imap.placeholder.date_end": "DD/MM/YYYY (optional)",

    "imap.button.fetch_mailboxes": "Inspect IMAP folders…",
    "imap.button.start_export": "Start forensic extraction",
    "imap.button.cancel_export": "Cancel extraction",

    "imap.label.mailboxes_title": (
        "IMAP folders to extract (evidence source):"
    ),
    "imap.checkbox.select_all": "Select all folders",

    "imap.log.placeholder": (
        "IMAP extraction log (read-only, timestamped)…"
    ),

    # ------------------------------------------------------------------
    # IMAP tab – erreurs / infos génériques
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "Incomplete settings",
    "imap.error.missing_fields.body": (
        "Please provide IMAP server, username and password."
    ),

    "imap.info.export_running.title": "Extraction already running",
    "imap.info.export_running.body": "An IMAP extraction is already running.",

    "imap.error.date_invalid.title": "Invalid date",
    "imap.error.date_invalid.body": "Error in provided dates: {error}",
    "imap.error.date_end_before_start.body": (
        "End date cannot be earlier than start date."
    ),

    "imap.error.no_mailbox_selected.title": "No folder selected",
    "imap.error.no_mailbox_selected.body": (
        "Please select at least one IMAP folder to extract."
    ),

    "imap.error.fetch_mailboxes.title": "IMAP error",
    "imap.error.fetch_mailboxes.body": (
        "Unable to retrieve IMAP folders:\n{error}"
    ),

    "imap.info.generic.title": "Information",
    "imap.error.generic.title": "Error",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "Connecting to {host}:{port} (SSL={use_ssl})...",
    "imap.log.connected": "Connected to the IMAP server.",
    "imap.log.select_folder": "Selecting folder \"{folder}\"...",
    "imap.log.folder_selected": "Folder \"{folder}\" selected.",
    "imap.log.message_count": "{count} messages to export.",
    "imap.log.fetching": "Fetching IMAP messages...",
    "imap.log.export_done": "IMAP export completed.",
    "imap.log.saving_to": "Saving messages to \"{output_dir}\"...",
    "imap.log.progress": "Exporting message {current}/{total}...",
    "imap.log.skip_existing": "File \"{path}\" already exists, skipping.",

    "imap.error.connect_failed": "Cannot connect to {host}:{port}: {error}",
    "imap.error.login_failed": "IMAP authentication error: {error}",
    "imap.error.select_failed": "Cannot select folder \"{folder}\": {error}",
    "imap.error.fetch_failed": "Error while fetching messages: {error}",
    "imap.error.generic": "Error during IMAP export: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== IMAP export report (read only) ===",
    "imap.report.tool_line": "Tool      : eml_forensic_suite – IMAP export",
    "imap.report.version_line": "Version   : {version}",
    "imap.report.folder_line": "Folder    : {export_dir}",

    "imap.report.section_tool": "---- Tool information ----",
    "imap.report.tool_path": "Tool path           : {tool_path}",
    "imap.report.tool_hash": "Tool SHA-256        : {tool_hash}",

    "imap.report.section_env": "---- Runtime environment ----",
    "imap.report.env_os": "Operating system    : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Python version      : {python_version}",

    "imap.report.section_context": "---- IMAP / account context ----",
    "imap.report.context_host": "IMAP server : {host}",
    "imap.report.context_user": "Account     : {user}",
    "imap.report.context_date_start": "Requested start date : {date_start}",
    "imap.report.context_date_end": "Requested end date   : {date_end}",
    "imap.report.context_criteria": "IMAP search criteria : {search_criteria} (as sent to the server)",

    "imap.report.selected_folders_title": "Selected folders:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- IMAP server information ----",
    "imap.report.server_greeting": "IMAP banner  : {greeting}",
    "imap.report.server_capability": "CAPABILITY   : {capability}",

    "imap.report.section_timestamps": "---- Analysis timestamps ----",
    "imap.report.timestamp_start_utc": "Analysis start (UTC)   : {dt}",
    "imap.report.timestamp_start_local": "Analysis start (local) : {dt}",
    "imap.report.timestamp_end_utc": "Analysis end (UTC)     : {dt}",
    "imap.report.timestamp_end_local": "Analysis end (local)   : {dt}",
    "imap.report.duration": "Total duration         : {duration}",

    "imap.report.section_folders": "---- Analysed folders ----",
    "imap.report.folders_count": "Number of selected folders : {count}",

    "imap.report.folder_header": "Folder : {name}",
    "imap.report.folder_messages": "  Messages found (period) : {count}",
    "imap.report.folder_exported": "  Messages exported       : {count}",
    "imap.report.folder_errors": "  Fetch errors            : {count}",
    "imap.report.folder_bytes": "  Downloaded volume       : {bytes} bytes",
    "imap.report.folder_size_stats": "  Min / max / avg size    : {min_size} / {max_size} / {avg_size} bytes",
    "imap.report.folder_period": "  Covered period (INTERNALDATE) : {first} → {last}",
    "imap.report.folder_error_uids": "  UIDs in error (non-exhaustive list) : {uids}",

    "imap.report.section_totals": "---- Global totals ----",
    "imap.report.total_messages": "Messages found (all folders) : {count}",
    "imap.report.total_exported": "Messages exported            : {count}",
    "imap.report.total_errors": "Fetch errors                 : {count}",
    "imap.report.total_bytes": "Total downloaded volume      : {bytes} bytes",

    "imap.report.section_forensic": "---- Methodology and forensic guarantees ----",
    "imap.report.forensic_item_readonly": "- The tool only used read-only IMAP commands (SELECT readonly, SEARCH, FETCH). No message was modified, deleted or marked as read during the analysis.",
    "imap.report.forensic_item_eml": "- Messages were exported exactly as provided by the IMAP server, and written to disk as .eml files without altering their content.",
    "imap.report.forensic_item_hashes": "- Each exported message is associated with a SHA-256 hash listed in hashes.txt, as well as a global hash computed from the concatenation of all individual hashes.",
    "imap.report.forensic_item_report_hash": "- This analysis report itself is hashed with SHA-256, and this hash is added to hashes.txt to guarantee the integrity of the report.",

    "imap.report.hashes_report_header": "ANALYSIS REPORT:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "No folder selected.",
    "imap.worker.log_export_dir": "Export folder: {export_dir}",
    "imap.worker.tool_hash_error": "(error while computing the tool hash)",

    "imap.worker.log_connecting": "Connecting to the IMAP server...",
    "imap.worker.greeting_not_available": "(IMAP banner not available)",
    "imap.worker.log_auth_classic": "Classic IMAP authentication...",
    "imap.worker.error_auth_failed": "IMAP authentication error: {error}",
    "imap.worker.capability_error": "(error during CAPABILITY command)",

    "imap.worker.log_date_start_inclusive": "Start date (inclusive): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "Start date: not set → extracting from the first available message.",
    "imap.worker.date_start_unset_label": "First available message (no lower limit)",

    "imap.worker.log_date_end_inclusive": "End date (inclusive): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "End date: not set → up to the last date available on the server.",
    "imap.worker.date_end_unset_label": "Last available message (no upper limit)",

    "imap.worker.log_criteria": "IMAP search criteria used: {criteria}",
    "imap.worker.log_selected_folders_header": "Selected folders ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "Stop requested during the counting phase.",
    "imap.worker.log_phase1_count": "[Phase 1] Counting messages in {folder}...",
    "imap.worker.log_select_folder_failed": "  ⚠️ Unable to select this folder, skipping.",
    "imap.worker.log_search_folder_failed": "  ⚠️ Error while searching in this folder, skipping.",
    "imap.worker.log_messages_to_process": "  → {count} messages to process in {folder}",

    "imap.worker.log_total_messages_to_download": "Total number of messages to download (all folders): {count}",

    "imap.worker.log_stop_during_export": "Stop requested: interrupting the export.",
    "imap.worker.log_folder_header": "=== Folder: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  No messages in {folder} for this period.",
    "imap.worker.log_folder_message_count": "  Number of messages found in {folder}: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ Unable to reselect this folder, skipping.",

    "imap.worker.log_first_message_download": "  Downloading first message ({uid})...",
    "imap.worker.log_folder_progress": "  Folder {folder} progress: {current}/{total} (last: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ Error while fetching message {uid}, continuing.",
    "imap.worker.log_folder_end": "  End of folder {folder}",

    "imap.worker.hashes_header": "List of exported files and their SHA-256 hashes",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "GLOBAL HASH (messages only):",

    "imap.worker.log_export_done_header": "=== Export completed ===",
    "imap.worker.log_export_done_count": "Total number of exported messages: {count}",
    "imap.worker.log_export_done_hashes_file": "Hashes file: {path}",
    "imap.worker.log_export_done_hash": "Global hash: {file_hash}",

    "imap.worker.summary": (
        "Export completed.\n\n"
        "Messages exported: {count}\n"
        "Folder: {export_dir}\n\n"
        "Global hash (messages):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "Analysis report generated and hashed (see rapport_imap_export.txt and hashes.txt).",
    "imap.worker.log_report_failed": "⚠️ Unable to generate the analysis report: {error}",

    "imap.worker.error_generic": "An error occurred: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "Connecting to the IMAP server...",
    "imap.tk.log_auth_classic": "Classic IMAP authentication...",
    "imap.tk.error_list_mailboxes_failed": "Unable to list IMAP folders.",

    "imap.tk.log_folders_found_header": "Folders found on the server:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "Total IMAP folders: {count}",

    "imap.tk.msgbox_error_title": "Error",
    "imap.tk.msgbox_error_fetch_mailboxes": "Error while retrieving IMAP folders: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ Error while retrieving folders: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. IMAP export",

    "imap.tk.label_server": "IMAP server:",
    "imap.tk.label_email": "Email address:",
    "imap.tk.label_password": "Password:",
    "imap.tk.label_date_start": "Start date (DD/MM/YYYY, optional):",
    "imap.tk.label_date_end": "End date (DD/MM/YYYY, optional):",
    "imap.tk.label_log": "Log:",
    "imap.tk.label_mailboxes": "IMAP folders to export:",
    "imap.tk.checkbox_select_all": "Select all / Deselect all",
    "imap.tk.label_progress": "Progress:",

    "imap.tk.msgbox_missing_fields_title": "Missing fields",
    "imap.tk.msgbox_missing_fields_text": "Please fill in the server, email and password.",

    "imap.tk.log_fetch_mailboxes_start": "Retrieving IMAP folders...",
    "imap.tk.log_no_mailboxes_or_error": "No folder found or an error occurred.",
    "imap.tk.log_select_mailboxes_hint": "Select the folders to export.",

    "imap.tk.button_list_mailboxes": "List IMAP folders",

    "imap.tk.msgbox_date_start_invalid_title": "Invalid start date",
    "imap.tk.msgbox_date_start_invalid_text": "The start date must be in DD/MM/YYYY format.",

    "imap.tk.msgbox_date_end_invalid_title": "Invalid end date",
    "imap.tk.msgbox_date_end_invalid_text": "The end date must be in DD/MM/YYYY format.",

    "imap.tk.msgbox_date_range_invalid_title": "Invalid date range",
    "imap.tk.msgbox_date_range_invalid_text": (
        "The end date cannot be earlier than the start date."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "No folder selected",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "Please select at least one IMAP folder (via 'List IMAP folders')."
    ),

    "imap.tk.log_export_start": "Starting export...",
    "imap.tk.button_run_export": "Run export (selected folders)",

    "imap.tk.log_stop_requested": (
        "Stop requested, the export will terminate cleanly..."
    ),
    "imap.tk.button_stop_export": "Stop export",

    "imap.tk.msgbox_export_done_title": "Export completed",


    # ------------------------------------------------------------------
    # IMAP tab – logs
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "Connecting to IMAP server to enumerate folders…"
    ),
    "imap.log.fetch_error": "❌ Error while fetching folders:",
    "imap.log.no_mailboxes": "No IMAP folders found on this account.",
    "imap.log.mailboxes_found": "Folders found on the server:",
    "imap.log.mailboxes_total": "Total IMAP folders: {count}",
    "imap.log.mailboxes_select_hint": (
        "Select folders to extract in read-only mode."
    ),
    "imap.log.start_export": (
        "Starting IMAP extraction (forensic mode, read-only)…"
    ),
    "imap.log.cancel_requested": (
        "Cancellation request sent to IMAP worker…"
    ),
    "imap.log.export_dir_saved": "Export directory saved: {path}",
    "imap.log.done": "IMAP processing finished.",

    # ------------------------------------------------------------------
    # Dashboard v3 – sections / onglets
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "Suspicion levels",
    "dashboard.tab_text": "Eml index summary",
    "dashboard.tab_graphs": "Graphs",
    "dashboard.section_charts": "Graphical visualizations",

    "dashboard.chart_suspicion_title": "Suspicion level distribution",
    "dashboard.chart_folders_title": "Messages per IMAP folder",
    "dashboard.chart_domains_title": "Top sender domains",
    "dashboard.chart_attachments_title": "Attachment presence",
    "dashboard.chart_axis_count": "Count",
    "dashboard.chart_attachments_with": "With attachments",
    "dashboard.chart_attachments_without": "Without attachments",

    # Légende / texte autour du scoring
    "dashboard.suspicion_distribution_line": (
        "Distribution of emails by suspicion level:"
    ),
    "dashboard.suspicion_level.LOW": "Low",
    "dashboard.suspicion_level.MEDIUM": "Medium",
    "dashboard.suspicion_level.HIGH": "High",
    "dashboard.suspicion_level.CRITICAL": "Critical",
    "dashboard.suspicion_level.UNKNOWN": "Unknown",

    # Graphes – titres (nouvelle nomenclature)
    "dashboard.chart.folders.title": "Emails per IMAP folder",
    "dashboard.chart.domains.title": "Top sender domains",
    "dashboard.chart.attachments.title": "Attachments presence",
    "dashboard.chart.auth.title": "DKIM / SPF / DMARC results",
    "dashboard.chart.suspicion.title": "Distribution by suspicion level",

    # Graphes – libellés / états
    "dashboard.chart.no_data": (
        "Not enough data to display this chart."
    ),
    "dashboard.chart.axis.emails": "Number of emails",
    "dashboard.chart.axis.folders": "IMAP folders",
    "dashboard.chart.axis.domains": "Domains",
    "dashboard.chart.axis.levels": "Levels",

    # Petite aide visuelle sur les couleurs
    "dashboard.legend.safe": "Area considered mostly safe",
    "dashboard.legend.suspicious": "Area to investigate first",

    # ------------------------------------------------------------------
    # Viewer – colonnes de scoring & suspicion
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "Suspicion score",
    "viewer.col.suspicion_level": "Level",
    "viewer.col.suspicion_reasons": "Reasons (summary)",

    # Tooltips scoring
    "viewer.score.tooltip.base": (
        "Global suspicion score computed from DKIM/SPF/DMARC, Received "
        "anomalies, header integrity and attachments."
    ),
    "viewer.score.level.LOW": (
        "Low suspicion: nothing abnormal detected under current rules."
    ),
    "viewer.score.level.MEDIUM": (
        "Medium suspicion: some elements should be checked "
        "(headers, authentication or attachments)."
    ),
    "viewer.score.level.HIGH": (
        "High suspicion: multiple technical indicators are inconsistent or dangerous."
    ),
    "viewer.score.level.CRITICAL": (
        "Critical suspicion: email is very likely malicious or forged."
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth / providers restrictions
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "This account appears to be managed by a provider that requires modern "
        "mechanisms (OAuth2, official exports) to access messages "
        "(e.g. Gmail, Outlook/Microsoft 365, Yahoo).\n\n"
        "To remain compliant and avoid bypassing these rules, this version of "
        "eml_forensic_suite does not perform direct IMAP extraction for these services.\n\n"
        "To retrieve messages in a compatible way:\n"
        "  • Gmail: use Google Takeout to export the mailbox (MBOX),\n"
        "    or a client like Thunderbird to create a local copy.\n"
        "  • Outlook / Microsoft 365: use your Outlook client export (PST)\n"
        "    or your organisation's archiving tools.\n"
        "  • Yahoo, etc.: use the export tools offered by the provider.\n\n"
        "Future versions of eml_forensic_suite will aim to analyze these exports "
        "(MBOX, PST, etc.) directly to stay compatible with these platforms."
    ),

    # ------------------------------------------------------------------
    # Viewer – mini langage de recherche
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "Forensic mini-language:\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "Operators: implicit AND, OR, NOT, parentheses."
    ),

    # ------------------------------------------------------------------
    # Viewer – CSV / index generic messages
    # ------------------------------------------------------------------
    "viewer.no_index_title": "No index available",
    "viewer.no_index_body": (
        "No index is available in this session.\n"
        "Generate an index in tab 2 or open a CSV file manually."
    ),
    "viewer.open_csv_title": "Open index CSV file",
    "viewer.error_csv_title": "CSV read error",
    "viewer.error_csv_body": (
        "Unable to read CSV file: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – preview (version finale, lecture seule)
    # ------------------------------------------------------------------
    "viewer.attach.preview": "Read-only preview",
    "viewer.attach.preview_failed_title": "Preview failed",
    "viewer.attach.preview_failed_body": (
        "Unable to show a preview of this attachment."
    ),
    "viewer.attach.preview_unsupported_title": "Unsupported type",
    "viewer.attach.preview_unsupported_body": (
        "No built-in preview is available for this MIME type: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – extraction PJ (version finale)
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "No message",
    "viewer.attach.no_msg_body": "No message is currently selected.",
    "viewer.attach.no_selection_title": "No attachment selected",
    "viewer.attach.no_selection_body": (
        "Please select an attachment in the list."
    ),
    "viewer.attach.no_root_title": "Working directory not found",
    "viewer.attach.no_root_body": (
        "No forensic / index directory is configured for extraction."
    ),
    "viewer.attach.extract_one_title": "Attachment extracted",
    "viewer.attach.extract_one_body": (
        "The attachment has been extracted to:\n{path}"
    ),
    "viewer.attach.extract_all_title": "Attachments extracted",
    "viewer.attach.extract_all_body": (
        "{count} attachments have been extracted:\n{paths}"
    ),

    # ------------------------------------------------------------------
    # Actions PJ (boutons – déjà couverts par les textes ci-dessus)
    # ------------------------------------------------------------------
    "viewer.attach.extract_one": "Extract selected attachment",
    "viewer.attach.extract_all": "Extract all attachments",

    # ------------------------------------------------------------------
    # About box
    # ------------------------------------------------------------------
    "about.version_label": "Version:",
    "about.description": (
        "Read-only tool for forensic analysis of EML/IMAP emails."
    ),
}
