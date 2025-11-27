from __future__ import annotations

from typing import Dict

TRANSLATIONS_IT: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Applicazione
    # ------------------------------------------------------------------
    "app.title": "Suite forense EML / IMAP (sola lettura)",

    # ------------------------------------------------------------------
    # Menu
    # ------------------------------------------------------------------
    "menu.file": "File",
    "menu.view": "Visualizzazione",
    "menu.help": "Aiuto",

    "menu.file.settings": "Impostazioni…",
    "menu.file.quit": "Esci",

    "menu.view.theme.dark": "Tema scuro",
    "menu.view.theme.light": "Tema chiaro",

    "menu.help.about": "Informazioni…",

    # ------------------------------------------------------------------
    # Tab
    # ------------------------------------------------------------------
    "tab.imap": "1. Export IMAP",
    "tab.index": "2. Indicizzazione EML",
    "tab.viewer": "3. Viewer forense",
    "tab.dashboard": "4. Dashboard forense",

    # ------------------------------------------------------------------
    # Finestra impostazioni
    # ------------------------------------------------------------------
    "settings.title": "Impostazioni",
    "settings.reports_dir.label": "Cartella di lavoro / rapporti:",
    "settings.reports_dir.browse": "Sfoglia…",
    "settings.language.label": "Lingua dell’interfaccia:",
    "settings.reports_dir.dialog_title": (
        "Seleziona la cartella di lavoro / rapporti"
    ),

    # ------------------------------------------------------------------
    # Stato / Varie
    # ------------------------------------------------------------------
    "status.ready": "Pronto.",
    "status.settings.saved": "Impostazioni salvate.",

    # ------------------------------------------------------------------
    # Tab Index (indicizzazione EML)
    # ------------------------------------------------------------------
    "index.folder_label": "Cartella di export EML:",
    "index.browse": "Sfoglia…",
    "index.use_last_export": "Usa l’ultimo export IMAP",
    "index.log_placeholder": (
        "Log di indicizzazione EML (sola lettura)…"
    ),
    "index.start_button": "Avvia indicizzazione EML",
    "index.dialog_select_folder": "Seleziona la cartella di export EML",
    "index.no_last_export": (
        "Nessun export IMAP noto al momento (tab 1)."
    ),
    "index.error_already_running_title": "Indicizzazione già in corso",
    "index.error_already_running_body": (
        "È già in corso un’operazione di indicizzazione EML."
    ),
    "index.error_no_folder_title": "Cartella mancante",
    "index.error_no_folder_body": (
        "Seleziona una cartella che contenga file .eml."
    ),
    "index.error_invalid_folder_title": "Cartella non valida",
    "index.error_invalid_folder_body": (
        "La cartella specificata non esiste:\n{folder}"
    ),
    "index.status_selected_folder": (
        "Cartella selezionata per l’indicizzazione: {folder}"
    ),
    "index.error_indexing_title": "Errore durante l’indicizzazione",
    "index.error_log": "❌ Errore: {error}",
    "index.done_log_success": "\nIndicizzazione completata con successo.",
    "index.done_log_path": "Percorso CSV: {csv_path}",
    "index.done_log_count": "Numero di voci indicizzate: {count}",
    "index.done_msg_title": "Indicizzazione completata",
    "index.done_msg_body": (
        "Indicizzazione EML completata.\n\nFile CSV: {csv_path}\nVoci: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard – base
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "Usa l’ultimo indice",
    "dashboard.open_csv": "Apri un indice CSV…",
    "dashboard.placeholder": (
        "Riepilogo statistico forense basato sull’indice EML…"
    ),
    "dashboard.source_memory": (
        "Sorgente: indice in memoria (ultima indicizzazione della sessione)."
    ),
    "dashboard.source_csv": "Sorgente: {path}",
    "dashboard.no_index_title": "Nessun indice",
    "dashboard.no_index_body": (
        "Nessun indice è disponibile in questa sessione.\n"
        "Genera un indice nel tab 2 oppure apri manualmente un file CSV."
    ),
    "dashboard.dialog_open_csv": "Apri un file di indice CSV",
    "dashboard.error_csv_missing_title": "File non trovato",
    "dashboard.error_csv_missing_body": (
        "Il file specificato non esiste:\n{path}"
    ),
    "dashboard.error_csv_read_title": "Errore di lettura CSV",
    "dashboard.error_csv_read_body": (
        "Impossibile leggere il file CSV: {path}"
    ),
    "dashboard.empty_csv_title": "Indice vuoto",
    "dashboard.empty_csv_body": (
        "Il file CSV non contiene alcuna voce utilizzabile."
    ),
    "dashboard.no_data": "Nessun dato da analizzare.",

    "dashboard.section_overview": "Panoramica",
    "dashboard.overview_line": (
        "Email totali: {total} – Mittenti distinti: {senders}"
    ),
    "dashboard.dates_line": "Periodo coperto: {date_min} → {date_max}",
    "dashboard.dates_unknown": (
        "Date non disponibili o non interpretabili."
    ),

    "dashboard.section_folders": "Distribuzione per cartella IMAP",
    "dashboard.no_folders": "Nessuna cartella IMAP rilevata.",

    "dashboard.section_domains": "Distribuzione per dominio (mittente)",
    "dashboard.no_domains": "Nessun dominio rilevato.",

    "dashboard.section_attachments": "Allegati",
    "dashboard.attachments_line": (
        "Email con allegati: {with_att}/{total} – "
        "Totale stimato allegati: {total_att}"
    ),

    "dashboard.section_auth": "Autenticazione (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "Risultati DKIM:",
    "dashboard.auth_header_spf": "Risultati SPF:",
    "dashboard.auth_header_dmarc": "Risultati DMARC:",

    "dashboard.section_integrity": "Integrità / header mancanti",
    "dashboard.integrity_flags_title": "Flag di integrità rilevati:",
    "dashboard.no_integrity_flags": (
        "Nessun flag di integrità specifico rilevato."
    ),

    "dashboard.section_received": "Anomalie nella catena Received",
    "dashboard.no_received_anomalies": (
        "Nessuna anomalia Received rilevata (con le regole attuali)."
    ),

    # ------------------------------------------------------------------
    # Viewer – colonne principali
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "Cartella IMAP",
    "viewer.col.sequence_number": "Sequenza",
    "viewer.col.date_header": "Data",
    "viewer.col.from_header": "From",
    "viewer.col.to_header": "To",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Bcc",
    "viewer.col.subject": "Oggetto",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "Allegati?",
    "viewer.col.attachment_count": "Numero allegati",
    "viewer.col.attachment_filenames": "Nomi allegati",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (estratto)",
    "viewer.col.received_count": "Numero Received",
    "viewer.col.received_anomalies": "Anomalie Received",
    "viewer.col.integrity_flags": "Flag di integrità",
    "viewer.col.relative_path": "Percorso relativo",
    "viewer.col.filename": "Nome file",

    # ------------------------------------------------------------------
    # Viewer – ricerca & aree
    # ------------------------------------------------------------------
    "viewer.search_label": "Ricerca:",
    "viewer.search_placeholder": (
        "Filtra nell’indice (tutte le colonne)…"
    ),
    "viewer.search_clear": "Pulisci",

    "viewer.headers_label": "Header",
    "viewer.headers_placeholder": (
        "Header del messaggio selezionato…"
    ),

    "viewer.body_label": "Corpo (testo)",
    "viewer.body_placeholder": (
        "Corpo text/plain (o HTML grezzo come fallback) del messaggio selezionato…"
    ),

    "viewer.btn_load_last": "Usa l’ultimo export IMAP",
    "viewer.btn_open_csv": "Apri un indice CSV...",
    "viewer.attachments_label": "Allegati",

    # ------------------------------------------------------------------
    # Viewer – errori EML
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "File EML non trovato",
    "viewer.error_missing_eml_body": (
        "Impossibile trovare il file EML sul disco:\n{path}"
    ),
    "viewer.error_parse_eml_title": "Errore di lettura EML",
    "viewer.error_parse_eml_body": (
        "Impossibile effettuare il parsing del file EML: {path}"
    ),

    # ------------------------------------------------------------------
    # Viewer – colonne allegati
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "Nome",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "Dimensione (byte)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "Sospetto?",

    "viewer.attach.yes": "Sì",
    "viewer.attach.no": "No",

    # ------------------------------------------------------------------
    # IMAP – connessione / campi
    # ------------------------------------------------------------------
    "imap.group.connection": "Server IMAP (fonte di prova)",
    "imap.label.host": "Indirizzo del server IMAP",
    "imap.label.user": "Identificativo della casella analizzata",
    "imap.label.password": "Password (mai memorizzata)",
    "imap.label.date_start": "Data di inizio (filtro forense)",
    "imap.label.date_end": "Data di fine (filtro forense)",

    "imap.placeholder.host": "es. imap.example.com",
    "imap.placeholder.user": "es. incident@azienda.it",
    "imap.placeholder.password": "Password dell’account analizzato",
    "imap.placeholder.date_start": "GG/MM/AAAA (opzionale)",
    "imap.placeholder.date_end": "GG/MM/AAAA (opzionale)",

    "imap.button.fetch_mailboxes": "Ispeziona cartelle IMAP…",
    "imap.button.start_export": "Avvia estrazione forense",
    "imap.button.cancel_export": "Annulla estrazione",

    "imap.label.mailboxes_title": (
        "Cartelle IMAP da estrarre (fonte di prova):"
    ),
    "imap.checkbox.select_all": "Seleziona tutte le cartelle",

    "imap.log.placeholder": (
        "Log dell’estrazione IMAP (sola lettura, con timestamp)…"
    ),

    # ------------------------------------------------------------------
    # IMAP – errori / informazioni
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "Parametri incompleti",
    "imap.error.missing_fields.body": (
        "Inserisci server IMAP, nome utente e password."
    ),

    "imap.info.export_running.title": "Estrazione già in corso",
    "imap.info.export_running.body": (
        "Un’estrazione IMAP è già in esecuzione."
    ),

    "imap.error.date_invalid.title": "Data non valida",
    "imap.error.date_invalid.body": (
        "Errore nelle date inserite: {error}"
    ),
    "imap.error.date_end_before_start.body": (
        "La data di fine non può essere precedente alla data di inizio."
    ),

    "imap.error.no_mailbox_selected.title": "Nessuna cartella selezionata",
    "imap.error.no_mailbox_selected.body": (
        "Seleziona almeno una cartella IMAP da estrarre."
    ),

    "imap.error.fetch_mailboxes.title": "Errore IMAP",
    "imap.error.fetch_mailboxes.body": (
        "Impossibile recuperare l’elenco delle cartelle IMAP:\n{error}"
    ),

    "imap.info.generic.title": "Informazione",
    "imap.error.generic.title": "Errore",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "Connessione a {host}:{port} (SSL={use_ssl})...",
    "imap.log.connected": "Connesso al server IMAP.",
    "imap.log.select_folder": "Selezione della cartella \"{folder}\"...",
    "imap.log.folder_selected": "Cartella \"{folder}\" selezionata.",
    "imap.log.message_count": "{count} messaggi da esportare.",
    "imap.log.fetching": "Recupero dei messaggi IMAP...",
    "imap.log.export_done": "Esportazione IMAP completata.",
    "imap.log.saving_to": "Salvataggio dei messaggi in \"{output_dir}\"...",
    "imap.log.progress": "Esportazione del messaggio {current}/{total}...",
    "imap.log.skip_existing": "Il file \"{path}\" esiste già, ignorato.",

    "imap.error.connect_failed": "Impossibile connettersi a {host}:{port}: {error}",
    "imap.error.login_failed": "Errore di autenticazione IMAP: {error}",
    "imap.error.select_failed": "Impossibile selezionare la cartella \"{folder}\": {error}",
    "imap.error.fetch_failed": "Errore durante il recupero dei messaggi: {error}",
    "imap.error.generic": "Errore durante l'esportazione IMAP: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== Rapporto di esportazione IMAP (solo lettura) ===",
    "imap.report.tool_line": "Strumento  : eml_forensic_suite – Esportazione IMAP",
    "imap.report.version_line": "Versione  : {version}",
    "imap.report.folder_line": "Cartella  : {export_dir}",

    "imap.report.section_tool": "---- Informazioni sullo strumento ----",
    "imap.report.tool_path": "Percorso dello strumento   : {tool_path}",
    "imap.report.tool_hash": "SHA-256 dello strumento    : {tool_hash}",

    "imap.report.section_env": "---- Ambiente di esecuzione ----",
    "imap.report.env_os": "Sistema operativo          : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Versione di Python         : {python_version}",

    "imap.report.section_context": "---- Contesto IMAP / account ----",
    "imap.report.context_host": "Server IMAP : {host}",
    "imap.report.context_user": "Account     : {user}",
    "imap.report.context_date_start": "Data di inizio richiesta : {date_start}",
    "imap.report.context_date_end": "Data di fine richiesta   : {date_end}",
    "imap.report.context_criteria": "Criteri di ricerca IMAP  : {search_criteria} (così come inviati al server)",

    "imap.report.selected_folders_title": "Cartelle selezionate:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- Informazioni sul server IMAP ----",
    "imap.report.server_greeting": "Banner IMAP   : {greeting}",
    "imap.report.server_capability": "CAPABILITY   : {capability}",

    "imap.report.section_timestamps": "---- Marcature temporali dell'analisi ----",
    "imap.report.timestamp_start_utc": "Inizio analisi (UTC)     : {dt}",
    "imap.report.timestamp_start_local": "Inizio analisi (locale)  : {dt}",
    "imap.report.timestamp_end_utc": "Fine analisi (UTC)       : {dt}",
    "imap.report.timestamp_end_local": "Fine analisi (locale)    : {dt}",
    "imap.report.duration": "Durata totale            : {duration}",

    "imap.report.section_folders": "---- Cartelle analizzate ----",
    "imap.report.folders_count": "Numero di cartelle selezionate : {count}",

    "imap.report.folder_header": "Cartella : {name}",
    "imap.report.folder_messages": "  Messaggi trovati (periodo)  : {count}",
    "imap.report.folder_exported": "  Messaggi esportati          : {count}",
    "imap.report.folder_errors": "  Errori di recupero          : {count}",
    "imap.report.folder_bytes": "  Volume scaricato            : {bytes} byte",
    "imap.report.folder_size_stats": "  Dimensione min / max / media: {min_size} / {max_size} / {avg_size} byte",
    "imap.report.folder_period": "  Periodo coperto (INTERNALDATE) : {first} → {last}",
    "imap.report.folder_error_uids": "  UIDs in errore (elenco non esaustivo) : {uids}",

    "imap.report.section_totals": "---- Totali globali ----",
    "imap.report.total_messages": "Messaggi trovati (tutte le cartelle) : {count}",
    "imap.report.total_exported": "Messaggi esportati                   : {count}",
    "imap.report.total_errors": "Errori di recupero                   : {count}",
    "imap.report.total_bytes": "Volume totale scaricato              : {bytes} byte",

    "imap.report.section_forensic": "---- Metodologia e garanzie forensi ----",
    "imap.report.forensic_item_readonly": "- Lo strumento ha utilizzato solo comandi IMAP in sola lettura (SELECT readonly, SEARCH, FETCH). Nessun messaggio è stato modificato, eliminato o marcato come letto durante l'analisi.",
    "imap.report.forensic_item_eml": "- I messaggi sono stati esportati esattamente come forniti dal server IMAP e scritti su disco come file .eml senza alterarne il contenuto.",
    "imap.report.forensic_item_hashes": "- Ogni messaggio esportato è associato a un hash SHA-256 elencato in hashes.txt, oltre a un hash globale calcolato dalla concatenazione di tutti gli hash individuali.",
    "imap.report.forensic_item_report_hash": "- Questo stesso rapporto di analisi è stato sottoposto a hash SHA-256 e tale hash è stato aggiunto a hashes.txt per garantire l'integrità del rapporto.",

    "imap.report.hashes_report_header": "RAPPORTO DI ANALISI:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "Nessuna cartella selezionata.",
    "imap.worker.log_export_dir": "Cartella di esportazione: {export_dir}",
    "imap.worker.tool_hash_error": "(errore durante il calcolo dell'hash dello strumento)",

    "imap.worker.log_connecting": "Connessione al server IMAP...",
    "imap.worker.greeting_not_available": "(banner IMAP non disponibile)",
    "imap.worker.log_auth_classic": "Autenticazione IMAP classica...",
    "imap.worker.error_auth_failed": "Errore di autenticazione IMAP: {error}",
    "imap.worker.capability_error": "(errore durante il comando CAPABILITY)",

    "imap.worker.log_date_start_inclusive": "Data di inizio (inclusa): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "Data di inizio: non impostata → estrazione dal primo messaggio disponibile.",
    "imap.worker.date_start_unset_label": "Primo messaggio disponibile (nessun limite inferiore)",

    "imap.worker.log_date_end_inclusive": "Data di fine (inclusa): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "Data di fine: non impostata → fino all'ultima data disponibile sul server.",
    "imap.worker.date_end_unset_label": "Ultimo messaggio disponibile (nessun limite superiore)",

    "imap.worker.log_criteria": "Criteri di ricerca IMAP utilizzati: {criteria}",
    "imap.worker.log_selected_folders_header": "Cartelle selezionate ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "Interruzione richiesta durante la fase di conteggio.",
    "imap.worker.log_phase1_count": "[Fase 1] Conteggio dei messaggi in {folder}...",
    "imap.worker.log_select_folder_failed": "  ⚠️ Impossibile selezionare questa cartella, verrà ignorata.",
    "imap.worker.log_search_folder_failed": "  ⚠️ Errore durante la ricerca in questa cartella, verrà ignorata.",
    "imap.worker.log_messages_to_process": "  → {count} messaggi da elaborare in {folder}",

    "imap.worker.log_total_messages_to_download": "Numero totale di messaggi da scaricare (tutte le cartelle): {count}",

    "imap.worker.log_stop_during_export": "Interruzione richiesta: esportazione in corso di arresto.",
    "imap.worker.log_folder_header": "=== Cartella: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  Nessun messaggio in {folder} per questo periodo.",
    "imap.worker.log_folder_message_count": "  Numero di messaggi trovati in {folder}: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ Impossibile riselezionare questa cartella, verrà ignorata.",

    "imap.worker.log_first_message_download": "  Download del primo messaggio ({uid})...",
    "imap.worker.log_folder_progress": "  Avanzamento cartella {folder}: {current}/{total} (ultimo: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ Errore durante il recupero del messaggio {uid}, si continua.",
    "imap.worker.log_folder_end": "  Fine della cartella {folder}",

    "imap.worker.hashes_header": "Elenco dei file esportati e dei rispettivi hash SHA-256",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "HASH GLOBALE (solo messaggi):",

    "imap.worker.log_export_done_header": "=== Esportazione completata ===",
    "imap.worker.log_export_done_count": "Numero totale di messaggi esportati: {count}",
    "imap.worker.log_export_done_hashes_file": "File degli hash: {path}",
    "imap.worker.log_export_done_hash": "Hash globale: {file_hash}",

    "imap.worker.summary": (
        "Esportazione completata.\n\n"
        "Messaggi esportati: {count}\n"
        "Cartella: {export_dir}\n\n"
        "Hash globale (messaggi):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "Rapporto di analisi generato e sottoposto a hash (vedi rapport_imap_export.txt e hashes.txt).",
    "imap.worker.log_report_failed": "⚠️ Impossibile generare il rapporto di analisi: {error}",

    "imap.worker.error_generic": "Si è verificato un errore: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "Connessione al server IMAP...",
    "imap.tk.log_auth_classic": "Autenticazione IMAP classica...",
    "imap.tk.error_list_mailboxes_failed": "Impossibile elencare le cartelle IMAP.",

    "imap.tk.log_folders_found_header": "Cartelle trovate sul server:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "Numero totale di cartelle IMAP: {count}",

    "imap.tk.msgbox_error_title": "Errore",
    "imap.tk.msgbox_error_fetch_mailboxes": "Errore durante il recupero delle cartelle IMAP: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ Errore durante il recupero delle cartelle: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. Esportazione IMAP",

    "imap.tk.label_server": "Server IMAP:",
    "imap.tk.label_email": "Indirizzo email:",
    "imap.tk.label_password": "Password:",
    "imap.tk.label_date_start": "Data di inizio (GG/MM/AAAA, opzionale):",
    "imap.tk.label_date_end": "Data di fine (GG/MM/AAAA, opzionale):",
    "imap.tk.label_log": "Log:",
    "imap.tk.label_mailboxes": "Cartelle IMAP da esportare:",
    "imap.tk.checkbox_select_all": "Seleziona tutto / Deseleziona tutto",
    "imap.tk.label_progress": "Avanzamento:",

    "imap.tk.msgbox_missing_fields_title": "Campi mancanti",
    "imap.tk.msgbox_missing_fields_text": "Compila server, email e password.",

    "imap.tk.log_fetch_mailboxes_start": "Recupero delle cartelle IMAP...",
    "imap.tk.log_no_mailboxes_or_error": "Nessuna cartella trovata o si è verificato un errore.",
    "imap.tk.log_select_mailboxes_hint": "Seleziona le cartelle da esportare.",

    "imap.tk.button_list_mailboxes": "Elenca le cartelle IMAP",

    "imap.tk.msgbox_date_start_invalid_title": "Data di inizio non valida",
    "imap.tk.msgbox_date_start_invalid_text": "La data di inizio deve essere nel formato GG/MM/AAAA.",

    "imap.tk.msgbox_date_end_invalid_title": "Data di fine non valida",
    "imap.tk.msgbox_date_end_invalid_text": "La data di fine deve essere nel formato GG/MM/AAAA.",

    "imap.tk.msgbox_date_range_invalid_title": "Intervallo di date non valido",
    "imap.tk.msgbox_date_range_invalid_text": (
        "La data di fine non può essere precedente alla data di inizio."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "Nessuna cartella selezionata",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "Seleziona almeno una cartella IMAP (tramite 'Elenca le cartelle IMAP')."
    ),

    "imap.tk.log_export_start": "Avvio dell'esportazione...",
    "imap.tk.button_run_export": "Avvia esportazione (cartelle selezionate)",

    "imap.tk.log_stop_requested": (
        "Interruzione richiesta, l'esportazione terminerà correttamente..."
    ),
    "imap.tk.button_stop_export": "Interrompi esportazione",

    "imap.tk.msgbox_export_done_title": "Esportazione completata",


    # ------------------------------------------------------------------
    # IMAP – log
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "Connessione al server IMAP per enumerare le cartelle…"
    ),
    "imap.log.fetch_error": "❌ Errore durante il recupero delle cartelle:",
    "imap.log.no_mailboxes": (
        "Nessuna cartella IMAP trovata su questo account."
    ),
    "imap.log.mailboxes_found": "Cartelle trovate sul server:",
    "imap.log.mailboxes_total": "Totale cartelle IMAP: {count}",
    "imap.log.mailboxes_select_hint": (
        "Seleziona le cartelle da estrarre in modalità sola lettura."
    ),
    "imap.log.start_export": (
        "Avvio dell’estrazione IMAP (modalità forense, sola lettura)…"
    ),
    "imap.log.cancel_requested": (
        "Richiesta di annullamento inviata al worker IMAP…"
    ),
    "imap.log.export_dir_saved": "Cartella di export salvata: {path}",
    "imap.log.done": "Elaborazione IMAP completata.",

    # ------------------------------------------------------------------
    # Dashboard v3 – sezioni / tab
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "Livelli di sospetto",
    "dashboard.tab_text": "Riepilogo indice EML",
    "dashboard.tab_graphs": "Grafici",
    "dashboard.section_charts": "Visualizzazioni grafiche",

    "dashboard.chart_suspicion_title": (
        "Distribuzione dei livelli di sospetto"
    ),
    "dashboard.chart_folders_title": "Messaggi per cartella IMAP",
    "dashboard.chart_domains_title": (
        "Domini mittenti più frequenti"
    ),
    "dashboard.chart_attachments_title": "Presenza di allegati",
    "dashboard.chart_axis_count": "Conteggio",
    "dashboard.chart_attachments_with": "Con allegati",
    "dashboard.chart_attachments_without": "Senza allegati",

    # Testo intorno allo scoring
    "dashboard.suspicion_distribution_line": (
        "Distribuzione delle email per livello di sospetto:"
    ),
    "dashboard.suspicion_level.LOW": "Basso",
    "dashboard.suspicion_level.MEDIUM": "Medio",
    "dashboard.suspicion_level.HIGH": "Alto",
    "dashboard.suspicion_level.CRITICAL": "Critico",
    "dashboard.suspicion_level.UNKNOWN": "Sconosciuto",

    # Titoli grafici (nuova nomenclatura)
    "dashboard.chart.folders.title": "Email per cartella IMAP",
    "dashboard.chart.domains.title": "Domini mittenti principali",
    "dashboard.chart.attachments.title": "Presenza di allegati",
    "dashboard.chart.auth.title": "Risultati DKIM / SPF / DMARC",
    "dashboard.chart.suspicion.title": "Distribuzione per livello di sospetto",

    # Grafici – assi / stati
    "dashboard.chart.no_data": (
        "Dati insufficienti per visualizzare questo grafico."
    ),
    "dashboard.chart.axis.emails": "Numero di email",
    "dashboard.chart.axis.folders": "Cartelle IMAP",
    "dashboard.chart.axis.domains": "Domini",
    "dashboard.chart.axis.levels": "Livelli",

    # Piccola legenda colori
    "dashboard.legend.safe": "Area considerata tendenzialmente sicura",
    "dashboard.legend.suspicious": "Area da esaminare con priorità",

    # ------------------------------------------------------------------
    # Viewer – colonne scoring & sospetto
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "Punteggio sospetto",
    "viewer.col.suspicion_level": "Livello",
    "viewer.col.suspicion_reasons": "Motivi (riepilogo)",

    # Tooltips scoring
    "viewer.score.tooltip.base": (
        "Punteggio di sospetto globale calcolato da DKIM/SPF/DMARC, "
        "anomalie Received, integrità degli header e allegati."
    ),
    "viewer.score.level.LOW": (
        "Sospetto basso: nulla di anomalo rilevato con le regole attuali."
    ),
    "viewer.score.level.MEDIUM": (
        "Sospetto medio: alcuni elementi dovrebbero essere verificati "
        "(header, autenticazione o allegati)."
    ),
    "viewer.score.level.HIGH": (
        "Sospetto alto: diversi indicatori tecnici sono incoerenti o pericolosi."
    ),
    "viewer.score.level.CRITICAL": (
        "Sospetto critico: l’email è molto probabilmente malevola o falsificata."
    ),

    # ------------------------------------------------------------------
    # IMAP – testo su limitazioni OAuth
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "Questo account sembra essere gestito da un provider che richiede "
        "meccanismi moderni (OAuth2, export ufficiali) per accedere ai messaggi "
        "(ad es. Gmail, Outlook/Microsoft 365, Yahoo).\n\n"
        "Per motivi di conformità e per evitare di aggirare tali regole, questa "
        "versione di eml_forensic_suite non esegue un’estrazione IMAP diretta "
        "per questi servizi.\n\n"
        "Per recuperare i messaggi in modo compatibile:\n"
        "  • Gmail: utilizzare Google Takeout per esportare la casella (MBOX),\n"
        "    oppure un client come Thunderbird per creare una copia locale.\n"
        "  • Outlook / Microsoft 365: utilizzare l’export del client Outlook\n"
        "    (PST) o gli strumenti di archiviazione dell’organizzazione.\n"
        "  • Yahoo, ecc.: utilizzare gli strumenti di export forniti dal provider.\n\n"
        "Le future versioni di eml_forensic_suite mireranno ad analizzare "
        "direttamente tali export (MBOX, PST, ecc.) per restare compatibili "
        "con queste piattaforme."
    ),

    # ------------------------------------------------------------------
    # Viewer – mini-linguaggio di ricerca
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "Mini-linguaggio forense:\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "Operatori: AND implicito, OR, NOT, parentesi."
    ),

    # ------------------------------------------------------------------
    # Viewer – messaggi generici indice / CSV
    # ------------------------------------------------------------------
    "viewer.no_index_title": "Nessun indice disponibile",
    "viewer.no_index_body": (
        "Nessun indice è disponibile in questa sessione.\n"
        "Genera un indice nel tab 2 oppure apri un file CSV."
    ),
    "viewer.open_csv_title": "Apri un file di indice CSV",
    "viewer.error_csv_title": "Errore di lettura CSV",
    "viewer.error_csv_body": (
        "Impossibile leggere il file CSV: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – anteprima (sola lettura)
    # ------------------------------------------------------------------
    "viewer.attach.preview": "Anteprima sola lettura",
    "viewer.attach.preview_failed_title": "Anteprima non riuscita",
    "viewer.attach.preview_failed_body": (
        "Impossibile visualizzare un’anteprima di questo allegato."
    ),
    "viewer.attach.preview_unsupported_title": "Tipo non supportato",
    "viewer.attach.preview_unsupported_body": (
        "Nessuna anteprima integrata disponibile per questo tipo MIME: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – estrazione allegati
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "Nessun messaggio",
    "viewer.attach.no_msg_body": (
        "Nessun messaggio è attualmente selezionato."
    ),
    "viewer.attach.no_selection_title": "Nessun allegato selezionato",
    "viewer.attach.no_selection_body": (
        "Seleziona un allegato nell’elenco."
    ),
    "viewer.attach.no_root_title": "Cartella di lavoro non trovata",
    "viewer.attach.no_root_body": (
        "Nessuna cartella forense / indice è configurata per l’estrazione."
    ),
    "viewer.attach.extract_one_title": "Allegato estratto",
    "viewer.attach.extract_one_body": (
        "L’allegato è stato estratto in:\n{path}"
    ),
    "viewer.attach.extract_all_title": "Allegati estratti",
    "viewer.attach.extract_all_body": (
        "{count} allegati sono stati estratti in:\n{paths}"
    ),

    # Pulsanti allegati
    "viewer.attach.extract_one": "Estrai l’allegato selezionato",
    "viewer.attach.extract_all": "Estrai tutti gli allegati",

    # ------------------------------------------------------------------
    # About box
    # ------------------------------------------------------------------
    "about.version_label": "Versione:",
    "about.description": (
        "Strumento in sola lettura per l’analisi forense di email EML/IMAP."
    ),
}
