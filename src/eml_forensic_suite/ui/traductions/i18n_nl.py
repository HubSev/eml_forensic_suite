from __future__ import annotations

from typing import Dict

TRANSLATIONS_NL: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Applicatie
    # ------------------------------------------------------------------
    "app.title": "EML / IMAP Forensic Suite (alleen-lezen)",

    # ------------------------------------------------------------------
    # Menu
    # ------------------------------------------------------------------
    "menu.file": "Bestand",
    "menu.view": "Beeld",
    "menu.help": "Help",

    "menu.file.settings": "Instellingen…",
    "menu.file.quit": "Afsluiten",

    "menu.view.theme.dark": "Donker thema",
    "menu.view.theme.light": "Licht thema",

    "menu.help.about": "Over…",

    # ------------------------------------------------------------------
    # Tabbladen
    # ------------------------------------------------------------------
    "tab.imap": "1. IMAP-export",
    "tab.index": "2. EML-indexering",
    "tab.viewer": "3. Forensische viewer",
    "tab.dashboard": "4. Forensische dashboard",

    # ------------------------------------------------------------------
    # Instellingenvenster
    # ------------------------------------------------------------------
    "settings.title": "Instellingen",
    "settings.reports_dir.label": "Werk- / rapportmap:",
    "settings.reports_dir.browse": "Bladeren…",
    "settings.language.label": "Interfacetaal:",
    "settings.reports_dir.dialog_title": (
        "Werk- / rapportmap kiezen"
    ),

    # ------------------------------------------------------------------
    # Status / Diversen
    # ------------------------------------------------------------------
    "status.ready": "Gereed.",
    "status.settings.saved": "Instellingen opgeslagen.",

    # ------------------------------------------------------------------
    # Tab Index (EML-indexering)
    # ------------------------------------------------------------------
    "index.folder_label": "EML-exportmap:",
    "index.browse": "Bladeren…",
    "index.use_last_export": "Laatste IMAP-export gebruiken",
    "index.log_placeholder": (
        "EML-indexeringslog (alleen-lezen)…"
    ),
    "index.start_button": "EML-indexering starten",
    "index.dialog_select_folder": "EML-exportmap selecteren",
    "index.no_last_export": (
        "Nog geen IMAP-export bekend (tab 1)."
    ),
    "index.error_already_running_title": "Indexering al bezig",
    "index.error_already_running_body": (
        "Er wordt al een EML-indexering uitgevoerd."
    ),
    "index.error_no_folder_title": "Map ontbreekt",
    "index.error_no_folder_body": (
        "Selecteer een map die .eml-bestanden bevat."
    ),
    "index.error_invalid_folder_title": "Ongeldige map",
    "index.error_invalid_folder_body": (
        "De opgegeven map bestaat niet:\n{folder}"
    ),
    "index.status_selected_folder": (
        "Geselecteerde map voor indexering: {folder}"
    ),
    "index.error_indexing_title": "Fout tijdens indexering",
    "index.error_log": "❌ Fout: {error}",
    "index.done_log_success": "\nIndexering succesvol voltooid.",
    "index.done_log_path": "CSV-pad: {csv_path}",
    "index.done_log_count": "Aantal geïndexeerde items: {count}",
    "index.done_msg_title": "Indexering voltooid",
    "index.done_msg_body": (
        "EML-indexering voltooid.\n\nCSV-bestand: {csv_path}\nItems: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard – basis
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "Laatste index gebruiken",
    "dashboard.open_csv": "Een CSV-index openen…",
    "dashboard.placeholder": (
        "Forensisch statistisch overzicht op basis van de EML-index…"
    ),
    "dashboard.source_memory": (
        "Bron: index in geheugen (laatste indexering van de sessie)."
    ),
    "dashboard.source_csv": "Bron: {path}",
    "dashboard.no_index_title": "Geen index",
    "dashboard.no_index_body": (
        "Er is geen index beschikbaar in deze sessie.\n"
        "Genereer een index in tab 2 of open handmatig een CSV-bestand."
    ),
    "dashboard.dialog_open_csv": "Een CSV-indexbestand openen",
    "dashboard.error_csv_missing_title": "Bestand niet gevonden",
    "dashboard.error_csv_missing_body": (
        "Het opgegeven bestand bestaat niet:\n{path}"
    ),
    "dashboard.error_csv_read_title": "CSV-leesfout",
    "dashboard.error_csv_read_body": (
        "Kan het CSV-bestand niet lezen: {path}"
    ),
    "dashboard.empty_csv_title": "Lege index",
    "dashboard.empty_csv_body": (
        "Het CSV-bestand bevat geen bruikbare records."
    ),
    "dashboard.no_data": "Geen gegevens om te analyseren.",

    "dashboard.section_overview": "Overzicht",
    "dashboard.overview_line": (
        "Totaal e-mails: {total} – Unieke afzenders: {senders}"
    ),
    "dashboard.dates_line": "Gedekte periode: {date_min} → {date_max}",
    "dashboard.dates_unknown": (
        "Datums niet beschikbaar of niet te parseren."
    ),

    "dashboard.section_folders": "Verdeling per IMAP-map",
    "dashboard.no_folders": "Geen IMAP-mappen gedetecteerd.",

    "dashboard.section_domains": "Verdeling per domein (afzender)",
    "dashboard.no_domains": "Geen domeinen gedetecteerd.",

    "dashboard.section_attachments": "Bijlagen",
    "dashboard.attachments_line": (
        "E-mails met bijlagen: {with_att}/{total} – "
        "Geschat totaal aantal bijlagen: {total_att}"
    ),

    "dashboard.section_auth": "Authenticatie (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "DKIM-resultaten:",
    "dashboard.auth_header_spf": "SPF-resultaten:",
    "dashboard.auth_header_dmarc": "DMARC-resultaten:",

    "dashboard.section_integrity": "Integriteit / ontbrekende headers",
    "dashboard.integrity_flags_title": "Gedetecteerde integriteitsflags:",
    "dashboard.no_integrity_flags": (
        "Geen specifieke integriteitsflags gedetecteerd."
    ),

    "dashboard.section_received": "Afwijkingen in de Received-keten",
    "dashboard.no_received_anomalies": (
        "Geen Received-afwijkingen gedetecteerd (onder de huidige regels)."
    ),

    # ------------------------------------------------------------------
    # Viewer – hoofdkolommen
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "IMAP-map",
    "viewer.col.sequence_number": "Volgnummer",
    "viewer.col.date_header": "Datum",
    "viewer.col.from_header": "From",
    "viewer.col.to_header": "To",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Bcc",
    "viewer.col.subject": "Onderwerp",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "Bijlagen?",
    "viewer.col.attachment_count": "Aantal bijlagen",
    "viewer.col.attachment_filenames": "Bijlagennamen",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (uittreksel)",
    "viewer.col.received_count": "Aantal Received",
    "viewer.col.received_anomalies": "Received-afwijkingen",
    "viewer.col.integrity_flags": "Integriteitsflags",
    "viewer.col.relative_path": "Relatief pad",
    "viewer.col.filename": "Bestandsnaam",

    # ------------------------------------------------------------------
    # Viewer – zoeken & zones
    # ------------------------------------------------------------------
    "viewer.search_label": "Zoeken:",
    "viewer.search_placeholder": (
        "Filteren in de index (alle kolommen)…"
    ),
    "viewer.search_clear": "Wissen",

    "viewer.headers_label": "Headers",
    "viewer.headers_placeholder": (
        "Headers van het geselecteerde bericht…"
    ),

    "viewer.body_label": "Body (tekst)",
    "viewer.body_placeholder": (
        "text/plain-body (of ruwe HTML als fallback) van het geselecteerde bericht…"
    ),

    "viewer.btn_load_last": "Laatste IMAP-export gebruiken",
    "viewer.btn_open_csv": "Een CSV-index openen...",
    "viewer.attachments_label": "Bijlagen",

    # ------------------------------------------------------------------
    # Viewer – EML-fouten
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "EML-bestand niet gevonden",
    "viewer.error_missing_eml_body": (
        "Kan het EML-bestand niet op schijf vinden:\n{path}"
    ),
    "viewer.error_parse_eml_title": "Leessfout EML",
    "viewer.error_parse_eml_body": (
        "Kan het EML-bestand niet parsen: {path}"
    ),

    # ------------------------------------------------------------------
    # Viewer – bijlagekolommen
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "Naam",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "Grootte (bytes)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "Verdacht?",

    "viewer.attach.yes": "Ja",
    "viewer.attach.no": "Nee",

    # ------------------------------------------------------------------
    # IMAP – verbinding / velden
    # ------------------------------------------------------------------
    "imap.group.connection": "IMAP-server (bewijsbron)",
    "imap.label.host": "Adres van de IMAP-server",
    "imap.label.user": "Identificatie van de geanalyseerde mailbox",
    "imap.label.password": "Wachtwoord (wordt nooit opgeslagen)",
    "imap.label.date_start": "Startdatum (forensische filter)",
    "imap.label.date_end": "Einddatum (forensische filter)",

    "imap.placeholder.host": "bv. imap.example.com",
    "imap.placeholder.user": "bv. incident@bedrijf.be",
    "imap.placeholder.password": "Wachtwoord van de geanalyseerde account",
    "imap.placeholder.date_start": "DD/MM/JJJJ (optioneel)",
    "imap.placeholder.date_end": "DD/MM/JJJJ (optioneel)",

    "imap.button.fetch_mailboxes": "IMAP-mappen inspecteren…",
    "imap.button.start_export": "Forensische extractie starten",
    "imap.button.cancel_export": "Extractie annuleren",

    "imap.label.mailboxes_title": (
        "IMAP-mappen die geëxtraheerd moeten worden (bewijsbron):"
    ),
    "imap.checkbox.select_all": "Alle mappen selecteren",

    "imap.log.placeholder": (
        "IMAP-extractielog (alleen-lezen, met tijdstempel)…"
    ),

    # ------------------------------------------------------------------
    # IMAP – fouten / info
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "Onvolledige instellingen",
    "imap.error.missing_fields.body": (
        "Geef IMAP-server, gebruikersnaam en wachtwoord op."
    ),

    "imap.info.export_running.title": "Extractie al bezig",
    "imap.info.export_running.body": (
        "Er wordt al een IMAP-extractie uitgevoerd."
    ),

    "imap.error.date_invalid.title": "Ongeldige datum",
    "imap.error.date_invalid.body": (
        "Fout in de ingevoerde datums: {error}"
    ),
    "imap.error.date_end_before_start.body": (
        "De einddatum mag niet eerder zijn dan de startdatum."
    ),

    "imap.error.no_mailbox_selected.title": "Geen map geselecteerd",
    "imap.error.no_mailbox_selected.body": (
        "Selecteer minstens één IMAP-map om te extraheren."
    ),

    "imap.error.fetch_mailboxes.title": "IMAP-fout",
    "imap.error.fetch_mailboxes.body": (
        "Kan de lijst met IMAP-mappen niet ophalen:\n{error}"
    ),

    "imap.info.generic.title": "Informatie",
    "imap.error.generic.title": "Fout",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "Verbinden met {host}:{port} (SSL={use_ssl})...",
    "imap.log.connected": "Verbonden met de IMAP-server.",
    "imap.log.select_folder": "Map \"{folder}\" selecteren...",
    "imap.log.folder_selected": "Map \"{folder}\" geselecteerd.",
    "imap.log.message_count": "{count} berichten om te exporteren.",
    "imap.log.fetching": "IMAP-berichten worden opgehaald...",
    "imap.log.export_done": "IMAP-export voltooid.",
    "imap.log.saving_to": "Berichten worden opgeslagen in \"{output_dir}\"...",
    "imap.log.progress": "Bericht {current}/{total} wordt geëxporteerd...",
    "imap.log.skip_existing": "Bestand \"{path}\" bestaat al, wordt overgeslagen.",

    "imap.error.connect_failed": "Kan geen verbinding maken met {host}:{port}: {error}",
    "imap.error.login_failed": "IMAP-authenticatiefout: {error}",
    "imap.error.select_failed": "Kan map \"{folder}\" niet selecteren: {error}",
    "imap.error.fetch_failed": "Fout bij het ophalen van berichten: {error}",
    "imap.error.generic": "Fout tijdens IMAP-export: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== IMAP-exportrapport (alleen-lezen) ===",
    "imap.report.tool_line": "Tool      : eml_forensic_suite – IMAP-export",
    "imap.report.version_line": "Versie    : {version}",
    "imap.report.folder_line": "Map       : {export_dir}",

    "imap.report.section_tool": "---- Toolinformatie ----",
    "imap.report.tool_path": "Toolpad             : {tool_path}",
    "imap.report.tool_hash": "Tool SHA-256        : {tool_hash}",

    "imap.report.section_env": "---- Uitvoeringsomgeving ----",
    "imap.report.env_os": "Besturingssysteem   : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Python-versie       : {python_version}",

    "imap.report.section_context": "---- IMAP- / accountcontext ----",
    "imap.report.context_host": "IMAP-server : {host}",
    "imap.report.context_user": "Account     : {user}",
    "imap.report.context_date_start": "Gevraagde startdatum : {date_start}",
    "imap.report.context_date_end": "Gevraagde einddatum   : {date_end}",
    "imap.report.context_criteria": "IMAP-zoekcriteria    : {search_criteria} (zoals naar de server gestuurd)",

    "imap.report.selected_folders_title": "Geselecteerde mappen:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- IMAP-serverinformatie ----",
    "imap.report.server_greeting": "IMAP-banner  : {greeting}",
    "imap.report.server_capability": "CAPABILITY   : {capability}",

    "imap.report.section_timestamps": "---- Analyse-tijdstempels ----",
    "imap.report.timestamp_start_utc": "Start analyse (UTC)    : {dt}",
    "imap.report.timestamp_start_local": "Start analyse (lokaal) : {dt}",
    "imap.report.timestamp_end_utc": "Einde analyse (UTC)    : {dt}",
    "imap.report.timestamp_end_local": "Einde analyse (lokaal) : {dt}",
    "imap.report.duration": "Totale duur            : {duration}",

    "imap.report.section_folders": "---- Geanalyseerde mappen ----",
    "imap.report.folders_count": "Aantal geselecteerde mappen  : {count}",

    "imap.report.folder_header": "Map    : {name}",
    "imap.report.folder_messages": "  Gevonden berichten (periode) : {count}",
    "imap.report.folder_exported": "  Geëxporteerde berichten      : {count}",
    "imap.report.folder_errors": "  Ophaalfouten                 : {count}",
    "imap.report.folder_bytes": "  Gedownload volume            : {bytes} bytes",
    "imap.report.folder_size_stats": "  Min. / max. / gem. grootte   : {min_size} / {max_size} / {avg_size} bytes",
    "imap.report.folder_period": "  Gedekte periode (INTERNALDATE) : {first} → {last}",
    "imap.report.folder_error_uids": "  UID's met fouten (niet-uitputtende lijst) : {uids}",

    "imap.report.section_totals": "---- Globale totalen ----",
    "imap.report.total_messages": "Gevonden berichten (alle mappen)   : {count}",
    "imap.report.total_exported": "Geëxporteerde berichten            : {count}",
    "imap.report.total_errors": "Ophaalfouten                       : {count}",
    "imap.report.total_bytes": "Totaal gedownload volume           : {bytes} bytes",

    "imap.report.section_forensic": "---- Methodologie en forensische waarborgen ----",
    "imap.report.forensic_item_readonly": "- De tool gebruikte uitsluitend IMAP-commando's in alleen-lezen modus (SELECT readonly, SEARCH, FETCH). Geen enkel bericht werd gewijzigd, verwijderd of als gelezen gemarkeerd tijdens de analyse.",
    "imap.report.forensic_item_eml": "- Berichten werden exact zoals door de IMAP-server geleverd geëxporteerd en als .eml-bestanden op schijf geschreven, zonder hun inhoud te wijzigen.",
    "imap.report.forensic_item_hashes": "- Elk geëxporteerd bericht is gekoppeld aan een SHA-256-hash die in hashes.txt is opgenomen, plus een globale hash die wordt berekend uit de concatenatie van alle individuele hashes.",
    "imap.report.forensic_item_report_hash": "- Dit analyserapport zelf wordt gehasht met SHA-256 en deze hash wordt aan hashes.txt toegevoegd om de integriteit van het rapport te waarborgen.",

    "imap.report.hashes_report_header": "ANALYSERAPPORT:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "Geen map geselecteerd.",
    "imap.worker.log_export_dir": "Exportmap: {export_dir}",
    "imap.worker.tool_hash_error": "(fout bij het berekenen van de tool-hash)",

    "imap.worker.log_connecting": "Verbinden met de IMAP-server...",
    "imap.worker.greeting_not_available": "(IMAP-banner niet beschikbaar)",
    "imap.worker.log_auth_classic": "Klassieke IMAP-authenticatie...",
    "imap.worker.error_auth_failed": "IMAP-authenticatiefout: {error}",
    "imap.worker.capability_error": "(fout tijdens CAPABILITY-commando)",

    "imap.worker.log_date_start_inclusive": "Begindatum (inclusief): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "Begindatum: niet ingesteld → extractie vanaf het eerste beschikbare bericht.",
    "imap.worker.date_start_unset_label": "Eerste beschikbare bericht (geen ondergrens)",

    "imap.worker.log_date_end_inclusive": "Einddatum (inclusief): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "Einddatum: niet ingesteld → tot de laatste beschikbare datum op de server.",
    "imap.worker.date_end_unset_label": "Laatste beschikbare bericht (geen bovengrens)",

    "imap.worker.log_criteria": "Gebruikte IMAP-zoekcriteria: {criteria}",
    "imap.worker.log_selected_folders_header": "Geselecteerde mappen ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "Stop aangevraagd tijdens de tel-fase.",
    "imap.worker.log_phase1_count": "[Fase 1] Berichten tellen in {folder}...",
    "imap.worker.log_select_folder_failed": "  ⚠️ Kan deze map niet selecteren, wordt overgeslagen.",
    "imap.worker.log_search_folder_failed": "  ⚠️ Fout bij het zoeken in deze map, wordt overgeslagen.",
    "imap.worker.log_messages_to_process": "  → {count} te verwerken berichten in {folder}",

    "imap.worker.log_total_messages_to_download": "Totaal aantal te downloaden berichten (alle mappen): {count}",

    "imap.worker.log_stop_during_export": "Stop aangevraagd: export wordt onderbroken.",
    "imap.worker.log_folder_header": "=== Map: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  Geen berichten in {folder} voor deze periode.",
    "imap.worker.log_folder_message_count": "  Aantal gevonden berichten in {folder}: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ Kan deze map niet opnieuw selecteren, wordt overgeslagen.",

    "imap.worker.log_first_message_download": "  Eerste bericht wordt gedownload ({uid})...",
    "imap.worker.log_folder_progress": "  Voortgang map {folder}: {current}/{total} (laatste: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ Fout bij het ophalen van bericht {uid}, wordt verdergegaan.",
    "imap.worker.log_folder_end": "  Einde van map {folder}",

    "imap.worker.hashes_header": "Lijst van geëxporteerde bestanden en hun SHA-256-hashes",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "GLOBALE HASH (alleen berichten):",

    "imap.worker.log_export_done_header": "=== Export voltooid ===",
    "imap.worker.log_export_done_count": "Totaal aantal geëxporteerde berichten: {count}",
    "imap.worker.log_export_done_hashes_file": "Hashes-bestand: {path}",
    "imap.worker.log_export_done_hash": "Globale hash: {file_hash}",

    "imap.worker.summary": (
        "Export voltooid.\n\n"
        "Geëxporteerde berichten: {count}\n"
        "Map: {export_dir}\n\n"
        "Globale hash (berichten):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "Analyserapport gegenereerd en gehasht (zie rapport_imap_export.txt en hashes.txt).",
    "imap.worker.log_report_failed": "⚠️ Kan het analyserapport niet genereren: {error}",

    "imap.worker.error_generic": "Er is een fout opgetreden: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "Verbinden met de IMAP-server...",
    "imap.tk.log_auth_classic": "Klassieke IMAP-authenticatie...",
    "imap.tk.error_list_mailboxes_failed": "Kan IMAP-mappen niet weergeven.",

    "imap.tk.log_folders_found_header": "Op de server gevonden mappen:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "Totaal aantal IMAP-mappen: {count}",

    "imap.tk.msgbox_error_title": "Fout",
    "imap.tk.msgbox_error_fetch_mailboxes": "Fout bij het ophalen van IMAP-mappen: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ Fout bij het ophalen van mappen: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. IMAP-export",

    "imap.tk.label_server": "IMAP-server:",
    "imap.tk.label_email": "E-mailadres:",
    "imap.tk.label_password": "Wachtwoord:",
    "imap.tk.label_date_start": "Begindatum (DD/MM/YYYY, optioneel):",
    "imap.tk.label_date_end": "Einddatum (DD/MM/YYYY, optioneel):",
    "imap.tk.label_log": "Logboek:",
    "imap.tk.label_mailboxes": "Te exporteren IMAP-mappen:",
    "imap.tk.checkbox_select_all": "Alles selecteren / alles deselecteren",
    "imap.tk.label_progress": "Voortgang:",

    "imap.tk.msgbox_missing_fields_title": "Ontbrekende velden",
    "imap.tk.msgbox_missing_fields_text": "Vul de server, het e-mailadres en het wachtwoord in.",

    "imap.tk.log_fetch_mailboxes_start": "IMAP-mappen worden opgehaald...",
    "imap.tk.log_no_mailboxes_or_error": "Geen map gevonden of er is een fout opgetreden.",
    "imap.tk.log_select_mailboxes_hint": "Selecteer de mappen die je wilt exporteren.",

    "imap.tk.button_list_mailboxes": "IMAP-mappen weergeven",

    "imap.tk.msgbox_date_start_invalid_title": "Ongeldige begindatum",
    "imap.tk.msgbox_date_start_invalid_text": "De begindatum moet in het formaat DD/MM/YYYY staan.",

    "imap.tk.msgbox_date_end_invalid_title": "Ongeldige einddatum",
    "imap.tk.msgbox_date_end_invalid_text": "De einddatum moet in het formaat DD/MM/YYYY staan.",

    "imap.tk.msgbox_date_range_invalid_title": "Ongeldig datumbereik",
    "imap.tk.msgbox_date_range_invalid_text": (
        "De einddatum kan niet vóór de begindatum liggen."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "Geen map geselecteerd",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "Selecteer minstens één IMAP-map (via 'IMAP-mappen weergeven')."
    ),

    "imap.tk.log_export_start": "Export wordt gestart...",
    "imap.tk.button_run_export": "Export uitvoeren (geselecteerde mappen)",

    "imap.tk.log_stop_requested": (
        "Stop aangevraagd, de export wordt netjes beëindigd..."
    ),
    "imap.tk.button_stop_export": "Export stoppen",

    "imap.tk.msgbox_export_done_title": "Export voltooid",


    # ------------------------------------------------------------------
    # IMAP – logteksten
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "Verbinding maken met IMAP-server om mappen op te sommen…"
    ),
    "imap.log.fetch_error": "❌ Fout bij het ophalen van mappen:",
    "imap.log.no_mailboxes": (
        "Geen IMAP-mappen gevonden voor deze account."
    ),
    "imap.log.mailboxes_found": "Mappen gevonden op de server:",
    "imap.log.mailboxes_total": "Totaal aantal IMAP-mappen: {count}",
    "imap.log.mailboxes_select_hint": (
        "Selecteer de mappen die in alleen-lezen modus moeten worden geëxtraheerd."
    ),
    "imap.log.start_export": (
        "Starten van IMAP-extractie (forensische modus, alleen-lezen)…"
    ),
    "imap.log.cancel_requested": (
        "Annuleringsverzoek naar IMAP-worker verzonden…"
    ),
    "imap.log.export_dir_saved": "Exportmap opgeslagen: {path}",
    "imap.log.done": "IMAP-verwerking voltooid.",

    # ------------------------------------------------------------------
    # Dashboard v3 – secties / tabbladen
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "Niveaus van verdenking",
    "dashboard.tab_text": "EML-indexoverzicht",
    "dashboard.tab_graphs": "Grafieken",
    "dashboard.section_charts": "Grafische visualisaties",

    "dashboard.chart_suspicion_title": (
        "Verdeling van verdachtingsniveaus"
    ),
    "dashboard.chart_folders_title": "Berichten per IMAP-map",
    "dashboard.chart_domains_title": (
        "Meest voorkomende afzenderdomeinen"
    ),
    "dashboard.chart_attachments_title": "Aanwezigheid van bijlagen",
    "dashboard.chart_axis_count": "Aantal",
    "dashboard.chart_attachments_with": "Met bijlagen",
    "dashboard.chart_attachments_without": "Zonder bijlagen",

    # Tekst rond scoring
    "dashboard.suspicion_distribution_line": (
        "Verdeling van e-mails per verdachtingsniveau:"
    ),
    "dashboard.suspicion_level.LOW": "Laag",
    "dashboard.suspicion_level.MEDIUM": "Middel",
    "dashboard.suspicion_level.HIGH": "Hoog",
    "dashboard.suspicion_level.CRITICAL": "Critiek",
    "dashboard.suspicion_level.UNKNOWN": "Onbekend",

    # Grafiektitels (nieuwe naamgeving)
    "dashboard.chart.folders.title": "E-mails per IMAP-map",
    "dashboard.chart.domains.title": "Belangrijkste afzenderdomeinen",
    "dashboard.chart.attachments.title": "Aanwezigheid van bijlagen",
    "dashboard.chart.auth.title": "DKIM / SPF / DMARC-resultaten",
    "dashboard.chart.suspicion.title": "Verdeling per verdachtingsniveau",

    # Grafieken – assen / toestand
    "dashboard.chart.no_data": (
        "Onvoldoende gegevens om deze grafiek weer te geven."
    ),
    "dashboard.chart.axis.emails": "Aantal e-mails",
    "dashboard.chart.axis.folders": "IMAP-mappen",
    "dashboard.chart.axis.domains": "Domeinen",
    "dashboard.chart.axis.levels": "Niveaus",

    # Kleine kleurlegenda
    "dashboard.legend.safe": "Gebied dat als relatief veilig wordt beschouwd",
    "dashboard.legend.suspicious": "Gebied dat prioriteit heeft voor onderzoek",

    # ------------------------------------------------------------------
    # Viewer – scoring & verdachting
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "Verdachtingsscore",
    "viewer.col.suspicion_level": "Niveau",
    "viewer.col.suspicion_reasons": "Redenen (samenvatting)",

    # Tooltips scoring
    "viewer.score.tooltip.base": (
        "Globale verdachtingsscore berekend op basis van DKIM/SPF/DMARC, "
        "Received-afwijkingen, headerintegriteit en bijlagen."
    ),
    "viewer.score.level.LOW": (
        "Laag verdachtingsniveau: geen opvallende anomalieën onder de huidige regels."
    ),
    "viewer.score.level.MEDIUM": (
        "Middelmatig verdachtingsniveau: enkele elementen verdienen controle "
        "(headers, authenticatie of bijlagen)."
    ),
    "viewer.score.level.HIGH": (
        "Hoog verdachtingsniveau: meerdere technische indicatoren zijn incoherent of riskant."
    ),
    "viewer.score.level.CRITICAL": (
        "Critiek verdachtingsniveau: de e-mail is zeer waarschijnlijk kwaadaardig of vervalst."
    ),

    # ------------------------------------------------------------------
    # IMAP – tekst over OAuth-beperkingen
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "Deze account lijkt beheerd te worden door een provider die moderne "
        "mechanismen (OAuth2, officiële export) vereist om toegang te krijgen "
        "tot berichten (bijv. Gmail, Outlook/Microsoft 365, Yahoo).\n\n"
        "Om conform te blijven en het omzeilen van deze regels te vermijden, "
        "voert deze versie van eml_forensic_suite geen directe IMAP-extractie "
        "uit voor deze diensten.\n\n"
        "Om berichten op een compatibele manier te verkrijgen:\n"
        "  • Gmail: gebruik Google Takeout om de mailbox te exporteren (MBOX),\n"
        "    of een client zoals Thunderbird om een lokale kopie te maken.\n"
        "  • Outlook / Microsoft 365: gebruik de exportfunctie van Outlook\n"
        "    (PST) of de archiveringstools van uw organisatie.\n"
        "  • Yahoo, enz.: gebruik de exporttools die de provider aanbiedt.\n\n"
        "Toekomstige versies van eml_forensic_suite zullen proberen deze exports "
        "(MBOX, PST, enz.) rechtstreeks te analyseren om compatibel te blijven "
        "met deze platformen."
    ),

    # ------------------------------------------------------------------
    # Viewer – zoek mini-taal
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "Forensische mini-taal:\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "Operatoren: impliciete AND, OR, NOT, haakjes."
    ),

    # ------------------------------------------------------------------
    # Viewer – generieke CSV / indexmeldingen
    # ------------------------------------------------------------------
    "viewer.no_index_title": "Geen index beschikbaar",
    "viewer.no_index_body": (
        "Er is geen index beschikbaar in deze sessie.\n"
        "Genereer een index in tab 2 of open handmatig een CSV-bestand."
    ),
    "viewer.open_csv_title": "Een CSV-indexbestand openen",
    "viewer.error_csv_title": "CSV-leesfout",
    "viewer.error_csv_body": (
        "Kan het CSV-bestand niet lezen: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – alleen-lezen preview
    # ------------------------------------------------------------------
    "viewer.attach.preview": "Alleen-lezen preview",
    "viewer.attach.preview_failed_title": "Preview mislukt",
    "viewer.attach.preview_failed_body": (
        "Kan geen preview van deze bijlage weergeven."
    ),
    "viewer.attach.preview_unsupported_title": "Niet ondersteund type",
    "viewer.attach.preview_unsupported_body": (
        "Geen ingebouwde preview beschikbaar voor dit MIME-type: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – bijlage-extractie
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "Geen bericht",
    "viewer.attach.no_msg_body": (
        "Er is momenteel geen bericht geselecteerd."
    ),
    "viewer.attach.no_selection_title": "Geen bijlage geselecteerd",
    "viewer.attach.no_selection_body": (
        "Selecteer een bijlage in de lijst."
    ),
    "viewer.attach.no_root_title": "Werkmap niet gevonden",
    "viewer.attach.no_root_body": (
        "Er is geen forensische / indexmap geconfigureerd voor extractie."
    ),
    "viewer.attach.extract_one_title": "Bijlage geëxtraheerd",
    "viewer.attach.extract_one_body": (
        "De bijlage is geëxtraheerd naar:\n{path}"
    ),
    "viewer.attach.extract_all_title": "Bijlagen geëxtraheerd",
    "viewer.attach.extract_all_body": (
        "{count} bijlagen zijn geëxtraheerd naar:\n{paths}"
    ),

    # Knoppen bijlagen
    "viewer.attach.extract_one": "Geselecteerde bijlage extraheren",
    "viewer.attach.extract_all": "Alle bijlagen extraheren",

    # ------------------------------------------------------------------
    # Over-venster
    # ------------------------------------------------------------------
    "about.version_label": "Versie:",
    "about.description": (
        "Alleen-lezen tool voor forensische analyse van EML/IMAP-e-mails."
    ),
}
