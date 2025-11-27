from __future__ import annotations

from typing import Dict

TRANSLATIONS_HI: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "EML / IMAP फोरेंसिक सूट (केवल-पठन)",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "फ़ाइल",
    "menu.view": "दृश्य",
    "menu.help": "सहायता",

    "menu.file.settings": "सेटिंग्स…",
    "menu.file.quit": "बंद करें",

    "menu.view.theme.dark": "डार्क थीम",
    "menu.view.theme.light": "लाइट थीम",

    "menu.help.about": "के बारे में…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. IMAP एक्सपोर्ट",
    "tab.index": "2. EML इंडेक्सिंग",
    "tab.viewer": "3. फोरेंसिक व्यूअर",
    "tab.dashboard": "4. फोरेंसिक डैशबोर्ड",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "सेटिंग्स",
    "settings.reports_dir.label": "वर्किंग / रिपोर्ट्स डायरेक्टरी:",
    "settings.reports_dir.browse": "ब्राउज़…",
    "settings.language.label": "इंटरफ़ेस भाषा:",
    "settings.reports_dir.dialog_title": "वर्किंग / रिपोर्ट्स डायरेक्टरी चुनें",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "तैयार।",
    "status.settings.saved": "सेटिंग्स सहेजी गई हैं।",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "EML एक्सपोर्ट डायरेक्टरी:",
    "index.browse": "ब्राउज़…",
    "index.use_last_export": "अंतिम IMAP एक्सपोर्ट का उपयोग करें",
    "index.log_placeholder": "EML इंडेक्सिंग लॉग (केवल-पठन)…",
    "index.start_button": "EML इंडेक्सिंग शुरू करें",
    "index.dialog_select_folder": "EML एक्सपोर्ट फ़ोल्डर चुनें",
    "index.no_last_export": "अभी तक कोई IMAP एक्सपोर्ट ज्ञात नहीं (टैब 1)।",
    "index.error_already_running_title": "इंडेक्सिंग पहले से चल रही है",
    "index.error_already_running_body": "एक EML इंडेक्सिंग प्रक्रिया पहले से चल रही है।",
    "index.error_no_folder_title": "फ़ोल्डर गायब",
    "index.error_no_folder_body": "कृपया .eml फ़ाइलों वाला कोई फ़ोल्डर चुनें।",
    "index.error_invalid_folder_title": "अमान्य फ़ोल्डर",
    "index.error_invalid_folder_body": "दर्शाया गया फ़ोल्डर मौजूद नहीं है:\n{folder}",
    "index.status_selected_folder": "इंडेक्सिंग के लिए चयनित फ़ोल्डर: {folder}",
    "index.error_indexing_title": "इंडेक्सिंग के दौरान त्रुटि",
    "index.error_log": "❌ त्रुटि: {error}",
    "index.done_log_success": "\nइंडेक्सिंग सफलतापूर्वक पूर्ण हुई।",
    "index.done_log_path": "CSV पथ: {csv_path}",
    "index.done_log_count": "इंडेक्स की गई प्रविष्टियों की संख्या: {count}",
    "index.done_msg_title": "इंडेक्सिंग समाप्त",
    "index.done_msg_body": (
        "EML इंडेक्सिंग पूर्ण हो गई।\n\nCSV फ़ाइल: {csv_path}\nप्रविष्टियाँ: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "अंतिम इंडेक्स का उपयोग करें",
    "dashboard.open_csv": "इंडेक्स CSV खोलें…",
    "dashboard.placeholder": "EML इंडेक्स के आधार पर फोरेंसिक सांख्यिकीय सारांश…",
    "dashboard.source_memory": "स्रोत: इन-मेमोरी इंडेक्स (इस सत्र की अंतिम इंडेक्सिंग)।",
    "dashboard.source_csv": "स्रोत: {path}",
    "dashboard.no_index_title": "कोई इंडेक्स नहीं",
    "dashboard.no_index_body": (
        "इस सत्र में कोई इंडेक्स उपलब्ध नहीं है।\n"
        "टैब 2 में इंडेक्स जनरेट करें या मैन्युअली कोई CSV खोलें।"
    ),
    "dashboard.dialog_open_csv": "इंडेक्स CSV फ़ाइल खोलें",
    "dashboard.error_csv_missing_title": "फ़ाइल नहीं मिली",
    "dashboard.error_csv_missing_body": "निर्दिष्ट फ़ाइल मौजूद नहीं है:\n{path}",
    "dashboard.error_csv_read_title": "CSV पढ़ने में त्रुटि",
    "dashboard.error_csv_read_body": "CSV फ़ाइल पढ़ने में असमर्थ: {path}",
    "dashboard.empty_csv_title": "रिक्त इंडेक्स",
    "dashboard.empty_csv_body": "CSV फ़ाइल में कोई उपयोगी प्रविष्टि नहीं है।",
    "dashboard.no_data": "विश्लेषण हेतु कोई डेटा नहीं।",

    "dashboard.section_overview": "सारांश",
    "dashboard.overview_line": (
        "कुल ईमेल: {total} – अलग-अलग प्रेषक: {senders}"
    ),
    "dashboard.dates_line": "कवर की गई अवधि: {date_min} → {date_max}",
    "dashboard.dates_unknown": "तिथियाँ उपलब्ध नहीं या पार्स नहीं हो सकीं।",

    "dashboard.section_folders": "IMAP फ़ोल्डर के अनुसार वितरण",
    "dashboard.no_folders": "कोई IMAP फ़ोल्डर नहीं मिला।",

    "dashboard.section_domains": "डोमेन के अनुसार वितरण (प्रेषक)",
    "dashboard.no_domains": "कोई डोमेन नहीं मिला।",

    "dashboard.section_attachments": "संलग्नक",
    "dashboard.attachments_line": (
        "संलग्नक वाले ईमेल: {with_att}/{total} – अनुमानित कुल संलग्नक: {total_att}"
    ),

    "dashboard.section_auth": "प्रमाणीकरण (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "DKIM परिणाम:",
    "dashboard.auth_header_spf": "SPF परिणाम:",
    "dashboard.auth_header_dmarc": "DMARC परिणाम:",

    "dashboard.section_integrity": "अखंडता / गुम हेडर",
    "dashboard.integrity_flags_title": "पता चली अखंडता फ्लैग्स:",
    "dashboard.no_integrity_flags": "कोई विशिष्ट अखंडता फ्लैग नहीं मिला।",

    "dashboard.section_received": "Received चेन पर विसंगतियाँ",
    "dashboard.no_received_anomalies": (
        "वर्तमान नियमों के अनुसार कोई Received विसंगति नहीं मिली।"
    ),

    # ------------------------------------------------------------------
    # Viewer tab – colonnes de base
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "IMAP फ़ोल्डर",
    "viewer.col.sequence_number": "सीक्वेन्स",
    "viewer.col.date_header": "तिथि",
    "viewer.col.from_header": "प्रेषक (From)",
    "viewer.col.to_header": "प्राप्तकर्ता (To)",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Bcc",
    "viewer.col.subject": "विषय",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "संलग्नक?",
    "viewer.col.attachment_count": "संलग्नकों की संख्या",
    "viewer.col.attachment_filenames": "संलग्नक के नाम",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (अंश)",
    "viewer.col.received_count": "Received की संख्या",
    "viewer.col.received_anomalies": "Received विसंगतियाँ",
    "viewer.col.integrity_flags": "अखंडता फ्लैग्स",
    "viewer.col.relative_path": "रिलेटिव पथ",
    "viewer.col.filename": "फ़ाइल नाम",

    # ------------------------------------------------------------------
    # Viewer tab – search + zones
    # ------------------------------------------------------------------
    "viewer.search_label": "खोज:",
    "viewer.search_placeholder": "इंडेक्स में फ़िल्टर करें (सभी कॉलम)…",
    "viewer.search_clear": "साफ़ करें",

    "viewer.headers_label": "हेडर",
    "viewer.headers_placeholder": "चयनित संदेश के हेडर…",

    "viewer.body_label": "बॉडी (टेक्स्ट)",
    "viewer.body_placeholder": (
        "चयनित संदेश का text/plain बॉडी (या कच्चा HTML फ़ॉलबैक)…"
    ),

    "viewer.btn_load_last": "अंतिम IMAP एक्सपोर्ट का उपयोग करें",
    "viewer.btn_open_csv": "इंडेक्स CSV खोलें...",
    "viewer.attachments_label": "संलग्नक",

    # ------------------------------------------------------------------
    # Viewer – erreurs EML
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "EML फ़ाइल नहीं मिली",
    "viewer.error_missing_eml_body": "डिस्क पर EML फ़ाइल नहीं मिल सकी:\n{path}",
    "viewer.error_parse_eml_title": "EML पढ़ने में त्रुटि",
    "viewer.error_parse_eml_body": "EML फ़ाइल पार्स करने में असमर्थ: {path}",

    # ------------------------------------------------------------------
    # Viewer – colonnes PJ
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "नाम",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "आकार (बाइट्स)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "संदिग्ध?",

    "viewer.attach.yes": "हाँ",
    "viewer.attach.no": "नहीं",

    # ------------------------------------------------------------------
    # IMAP tab – connexion & champs
    # ------------------------------------------------------------------
    "imap.group.connection": "IMAP सर्वर (सबूत स्रोत)",
    "imap.label.host": "IMAP सर्वर पता",
    "imap.label.user": "विश्लेषित मेलबॉक्स पहचानकर्ता",
    "imap.label.password": "पासवर्ड (कभी सहेजा नहीं जाता)",
    "imap.label.date_start": "प्रारंभ तिथि (फोरेंसिक फ़िल्टर)",
    "imap.label.date_end": "समाप्ति तिथि (फोरेंसिक फ़िल्टर)",

    "imap.placeholder.host": "उदा. imap.example.com",
    "imap.placeholder.user": "उदा. incident@company.com",
    "imap.placeholder.password": "विश्लेषित खाते का पासवर्ड",
    "imap.placeholder.date_start": "DD/MM/YYYY (वैकल्पिक)",
    "imap.placeholder.date_end": "DD/MM/YYYY (वैकल्पिक)",

    "imap.button.fetch_mailboxes": "IMAP फ़ोल्डर निरीक्षण…",
    "imap.button.start_export": "फोरेंसिक एक्सट्रैक्शन शुरू करें",
    "imap.button.cancel_export": "एक्सट्रैक्शन रद्द करें",

    "imap.label.mailboxes_title": (
        "निकालने हेतु IMAP फ़ोल्डर (सबूत स्रोत):"
    ),
    "imap.checkbox.select_all": "सभी फ़ोल्डर चुनें",

    "imap.log.placeholder": (
        "IMAP एक्सट्रैक्शन लॉग (केवल-पठन, टाइमस्टैम्प्ड)…"
    ),

    # ------------------------------------------------------------------
    # IMAP tab – erreurs / infos génériques
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "अधूरी सेटिंग्स",
    "imap.error.missing_fields.body": (
        "कृपया IMAP सर्वर, उपयोगकर्ता नाम और पासवर्ड प्रदान करें।"
    ),

    "imap.info.export_running.title": "एक्सट्रैक्शन पहले से चल रहा है",
    "imap.info.export_running.body": "एक IMAP एक्सट्रैक्शन पहले से चल रहा है।",

    "imap.error.date_invalid.title": "अमान्य तिथि",
    "imap.error.date_invalid.body": "दर्ज की गई तिथियों में त्रुटि: {error}",
    "imap.error.date_end_before_start.body": (
        "समाप्ति तिथि प्रारंभ तिथि से पहले नहीं हो सकती।"
    ),

    "imap.error.no_mailbox_selected.title": "कोई फ़ोल्डर चयनित नहीं",
    "imap.error.no_mailbox_selected.body": (
        "कृपया कम से कम एक IMAP फ़ोल्डर चयनित करें।"
    ),

    "imap.error.fetch_mailboxes.title": "IMAP त्रुटि",
    "imap.error.fetch_mailboxes.body": (
        "IMAP फ़ोल्डर प्राप्त करने में असमर्थ:\n{error}"
    ),

    "imap.info.generic.title": "सूचना",
    "imap.error.generic.title": "त्रुटि",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "{host}:{port} से कनेक्ट किया जा रहा है (SSL={use_ssl})...",
    "imap.log.connected": "IMAP सर्वर से कनेक्शन स्थापित हुआ।",
    "imap.log.select_folder": "\"{folder}\" फ़ोल्डर चुना जा रहा है...",
    "imap.log.folder_selected": "\"{folder}\" फ़ोल्डर चुना गया।",
    "imap.log.message_count": "निर्यात करने के लिए {count} संदेश।",
    "imap.log.fetching": "IMAP संदेश प्राप्त किए जा रहे हैं...",
    "imap.log.export_done": "IMAP निर्यात पूरा हुआ।",
    "imap.log.saving_to": "संदेश \"{output_dir}\" में सहेजे जा रहे हैं...",
    "imap.log.progress": "संदेश निर्यात किया जा रहा है {current}/{total}...",
    "imap.log.skip_existing": "फ़ाइल \"{path}\" पहले से मौजूद है, छोड़ दिया गया।",

    "imap.error.connect_failed": "{host}:{port} से कनेक्ट नहीं हो सका: {error}",
    "imap.error.login_failed": "IMAP प्रमाणीकरण त्रुटि: {error}",
    "imap.error.select_failed": "\"{folder}\" फ़ोल्डर चुना नहीं जा सका: {error}",
    "imap.error.fetch_failed": "संदेश प्राप्त करते समय त्रुटि: {error}",
    "imap.error.generic": "IMAP निर्यात के दौरान त्रुटि: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== IMAP निर्यात रिपोर्ट (सिर्फ़ पढ़ने के लिए) ===",
    "imap.report.tool_line": "टूल       : eml_forensic_suite – IMAP निर्यात",
    "imap.report.version_line": "संस्करण   : {version}",
    "imap.report.folder_line": "फ़ोल्डर    : {export_dir}",

    "imap.report.section_tool": "---- टूल जानकारी ----",
    "imap.report.tool_path": "टूल पथ            : {tool_path}",
    "imap.report.tool_hash": "टूल SHA-256       : {tool_hash}",

    "imap.report.section_env": "---- रनटाइम वातावरण ----",
    "imap.report.env_os": "ऑपरेटिंग सिस्टम   : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Python संस्करण     : {python_version}",

    "imap.report.section_context": "---- IMAP / खाता संदर्भ ----",
    "imap.report.context_host": "IMAP सर्वर  : {host}",
    "imap.report.context_user": "खाता       : {user}",
    "imap.report.context_date_start": "मांगी गई प्रारंभ तिथि : {date_start}",
    "imap.report.context_date_end": "मांगी गई समाप्ति तिथि : {date_end}",
    "imap.report.context_criteria": "IMAP खोज मापदंड     : {search_criteria} (सर्वर को भेजे गए अनुसार)",

    "imap.report.selected_folders_title": "चयनित फ़ोल्डर:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- IMAP सर्वर जानकारी ----",
    "imap.report.server_greeting": "IMAP बैनर   : {greeting}",
    "imap.report.server_capability": "CAPABILITY  : {capability}",

    "imap.report.section_timestamps": "---- विश्लेषण टाइमस्टैम्प ----",
    "imap.report.timestamp_start_utc": "विश्लेषण प्रारंभ (UTC)    : {dt}",
    "imap.report.timestamp_start_local": "विश्लेषण प्रारंभ (स्थानीय) : {dt}",
    "imap.report.timestamp_end_utc": "विश्लेषण समाप्ति (UTC)    : {dt}",
    "imap.report.timestamp_end_local": "विश्लेषण समाप्ति (स्थानीय) : {dt}",
    "imap.report.duration": "कुल अवधि                  : {duration}",

    "imap.report.section_folders": "---- विश्लेषित फ़ोल्डर ----",
    "imap.report.folders_count": "चयनित फ़ोल्डर की संख्या : {count}",

    "imap.report.folder_header": "फ़ोल्डर : {name}",
    "imap.report.folder_messages": "  मिले संदेश (अवधि के भीतर) : {count}",
    "imap.report.folder_exported": "  निर्यात किए गए संदेश       : {count}",
    "imap.report.folder_errors": "  फ़ेच त्रुटियाँ              : {count}",
    "imap.report.folder_bytes": "  डाउनलोड किया गया वॉल्यूम    : {bytes} बाइट",
    "imap.report.folder_size_stats": "  न्यूनतम / अधिकतम / औसत आकार : {min_size} / {max_size} / {avg_size} बाइट",
    "imap.report.folder_period": "  कवर की गई अवधि (INTERNALDATE) : {first} → {last}",
    "imap.report.folder_error_uids": "  त्रुटि वाले UIDs (अपूर्ण सूची) : {uids}",

    "imap.report.section_totals": "---- कुल आँकड़े ----",
    "imap.report.total_messages": "मिले संदेश (सभी फ़ोल्डर)    : {count}",
    "imap.report.total_exported": "निर्यात किए गए संदेश          : {count}",
    "imap.report.total_errors": "फ़ेच त्रुटियाँ                : {count}",
    "imap.report.total_bytes": "कुल डाउनलोड वॉल्यूम           : {bytes} बाइट",

    "imap.report.section_forensic": "---- कार्यविधि और फोरेंसिक गारंटी ----",
    "imap.report.forensic_item_readonly": "- टूल ने केवल पढ़ने वाले IMAP कमांड (SELECT readonly, SEARCH, FETCH) का उपयोग किया। विश्लेषण के दौरान कोई संदेश बदला, हटाया या पढ़ा हुआ के रूप में चिह्नित नहीं किया गया।",
    "imap.report.forensic_item_eml": "- संदेशों को IMAP सर्वर से जैसे प्राप्त किया गया, ठीक वैसे ही .eml फ़ाइलों के रूप में डिस्क पर लिखा गया, बिना उनकी सामग्री बदले।",
    "imap.report.forensic_item_hashes": "- प्रत्येक निर्यात किए गए संदेश के साथ SHA-256 हैश जुड़ा है, जो hashes.txt में सूचीबद्ध है, और सभी व्यक्तिगत हैशों के संयोजन से एक वैश्विक हैश भी तैयार किया गया है।",
    "imap.report.forensic_item_report_hash": "- स्वयं यह विश्लेषण रिपोर्ट SHA-256 से हैश की गई है और इसकी अखंडता सुनिश्चित करने के लिए यह हैश hashes.txt में जोड़ा गया है।",

    "imap.report.hashes_report_header": "विश्लेषण रिपोर्ट:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "कोई फ़ोल्डर चयनित नहीं है।",
    "imap.worker.log_export_dir": "निर्यात फ़ोल्डर: {export_dir}",
    "imap.worker.tool_hash_error": "(टूल हैश की गणना करते समय त्रुटि)",

    "imap.worker.log_connecting": "IMAP सर्वर से कनेक्ट किया जा रहा है...",
    "imap.worker.greeting_not_available": "(IMAP बैनर उपलब्ध नहीं है)",
    "imap.worker.log_auth_classic": "क्लासिक IMAP प्रमाणीकरण...",
    "imap.worker.error_auth_failed": "IMAP प्रमाणीकरण त्रुटि: {error}",
    "imap.worker.capability_error": "(CAPABILITY कमांड के दौरान त्रुटि)",

    "imap.worker.log_date_start_inclusive": "प्रारंभ तिथि (समावेशी): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "प्रारंभ तिथि: नहीं दी गई → पहले उपलब्ध संदेश से निर्यात।",
    "imap.worker.date_start_unset_label": "पहला उपलब्ध संदेश (कोई निचली सीमा नहीं)",

    "imap.worker.log_date_end_inclusive": "समाप्ति तिथि (समावेशी): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "समाप्ति तिथि: नहीं दी गई → सर्वर पर उपलब्ध अंतिम तिथि तक।",
    "imap.worker.date_end_unset_label": "अंतिम उपलब्ध संदेश (कोई ऊपरी सीमा नहीं)",

    "imap.worker.log_criteria": "उपयोग किए गए IMAP खोज मापदंड: {criteria}",
    "imap.worker.log_selected_folders_header": "चयनित फ़ोल्डर ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "गिनती चरण के दौरान रोकने का अनुरोध किया गया।",
    "imap.worker.log_phase1_count": "[चरण 1] {folder} में संदेशों की गिनती...",
    "imap.worker.log_select_folder_failed": "  ⚠️ यह फ़ोल्डर चुना नहीं जा सका, छोड़ दिया गया।",
    "imap.worker.log_search_folder_failed": "  ⚠️ इस फ़ोल्डर में खोज के दौरान त्रुटि, छोड़ दिया गया।",
    "imap.worker.log_messages_to_process": "  → {folder} में संसाधित करने के लिए {count} संदेश",

    "imap.worker.log_total_messages_to_download": "डाउनलोड करने के लिए कुल संदेश (सभी फ़ोल्डर): {count}",

    "imap.worker.log_stop_during_export": "रोकने का अनुरोध: निर्यात प्रक्रिया रोकी जा रही है।",
    "imap.worker.log_folder_header": "=== फ़ोल्डर: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  इस अवधि में {folder} में कोई संदेश नहीं।",
    "imap.worker.log_folder_message_count": "  {folder} में मिले संदेशों की संख्या: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ यह फ़ोल्डर दोबारा चुना नहीं जा सका, छोड़ दिया गया।",

    "imap.worker.log_first_message_download": "  पहला संदेश डाउनलोड हो रहा है ({uid})...",
    "imap.worker.log_folder_progress": "  फ़ोल्डर {folder} प्रगति: {current}/{total} (अंतिम: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ संदेश {uid} प्राप्त करते समय त्रुटि, आगे जारी।",
    "imap.worker.log_folder_end": "  फ़ोल्डर {folder} समाप्त।",

    "imap.worker.hashes_header": "निर्यात की गई फ़ाइलों और उनके SHA-256 हैश की सूची",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "वैश्विक हैश (केवल संदेश):",

    "imap.worker.log_export_done_header": "=== निर्यात पूरा हुआ ===",
    "imap.worker.log_export_done_count": "कुल निर्यात किए गए संदेश: {count}",
    "imap.worker.log_export_done_hashes_file": "हैश फ़ाइल: {path}",
    "imap.worker.log_export_done_hash": "वैश्विक हैश: {file_hash}",

    "imap.worker.summary": (
        "निर्यात पूरा हुआ।\n\n"
        "निर्यात किए गए संदेश: {count}\n"
        "फ़ोल्डर: {export_dir}\n\n"
        "वैश्विक हैश (संदेश):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "विश्लेषण रिपोर्ट तैयार की गई और हैश की गई (rapport_imap_export.txt और hashes.txt देखें)।",
    "imap.worker.log_report_failed": "⚠️ विश्लेषण रिपोर्ट तैयार नहीं की जा सकी: {error}",

    "imap.worker.error_generic": "एक त्रुटि हुई: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "IMAP सर्वर से कनेक्ट किया जा रहा है...",
    "imap.tk.log_auth_classic": "क्लासिक IMAP प्रमाणीकरण...",
    "imap.tk.error_list_mailboxes_failed": "IMAP फ़ोल्डर सूचीबद्ध नहीं किए जा सके।",

    "imap.tk.log_folders_found_header": "सर्वर पर मिले फ़ोल्डर:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "कुल IMAP फ़ोल्डर: {count}",

    "imap.tk.msgbox_error_title": "त्रुटि",
    "imap.tk.msgbox_error_fetch_mailboxes": "IMAP फ़ोल्डर प्राप्त करते समय त्रुटि: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ फ़ोल्डर प्राप्त करते समय त्रुटि: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. IMAP निर्यात",

    "imap.tk.label_server": "IMAP सर्वर:",
    "imap.tk.label_email": "ईमेल पता:",
    "imap.tk.label_password": "पासवर्ड:",
    "imap.tk.label_date_start": "प्रारंभ तिथि (DD/MM/YYYY, वैकल्पिक):",
    "imap.tk.label_date_end": "समाप्ति तिथि (DD/MM/YYYY, वैकल्पिक):",
    "imap.tk.label_log": "लॉग:",
    "imap.tk.label_mailboxes": "निर्यात करने के लिए IMAP फ़ोल्डर:",
    "imap.tk.checkbox_select_all": "सभी चुनें / सभी हटाएँ",
    "imap.tk.label_progress": "प्रगति:",

    "imap.tk.msgbox_missing_fields_title": "गायब फ़ील्ड",
    "imap.tk.msgbox_missing_fields_text": "कृपया सर्वर, ईमेल और पासवर्ड भरें।",

    "imap.tk.log_fetch_mailboxes_start": "IMAP फ़ोल्डर प्राप्त किए जा रहे हैं...",
    "imap.tk.log_no_mailboxes_or_error": "कोई फ़ोल्डर नहीं मिला या कोई त्रुटि हुई।",
    "imap.tk.log_select_mailboxes_hint": "निर्यात के लिए फ़ोल्डर चुनें।",

    "imap.tk.button_list_mailboxes": "IMAP फ़ोल्डर सूचीबद्ध करें",

    "imap.tk.msgbox_date_start_invalid_title": "अमान्य प्रारंभ तिथि",
    "imap.tk.msgbox_date_start_invalid_text": "प्रारंभ तिथि DD/MM/YYYY प्रारूप में होनी चाहिए।",

    "imap.tk.msgbox_date_end_invalid_title": "अमान्य समाप्ति तिथि",
    "imap.tk.msgbox_date_end_invalid_text": "समाप्ति तिथि DD/MM/YYYY प्रारूप में होनी चाहिए।",

    "imap.tk.msgbox_date_range_invalid_title": "अमान्य तिथि सीमा",
    "imap.tk.msgbox_date_range_invalid_text": (
        "समाप्ति तिथि प्रारंभ तिथि से पहले नहीं हो सकती।"
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "कोई फ़ोल्डर चयनित नहीं",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "कृपया कम-से-कम एक IMAP फ़ोल्डर चुनें (\"IMAP फ़ोल्डर सूचीबद्ध करें\" के माध्यम से)।"
    ),

    "imap.tk.log_export_start": "निर्यात शुरू किया जा रहा है...",
    "imap.tk.button_run_export": "निर्यात चलाएँ (चयनित फ़ोल्डर)",

    "imap.tk.log_stop_requested": (
        "रोकने का अनुरोध किया गया, निर्यात प्रक्रिया सुरक्षित रूप से समाप्त होगी..."
    ),
    "imap.tk.button_stop_export": "निर्यात रोकें",

    "imap.tk.msgbox_export_done_title": "निर्यात पूरा हुआ",


    # ------------------------------------------------------------------
    # IMAP tab – logs
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "फ़ोल्डर सूची पाने के लिए IMAP सर्वर से कनेक्ट हो रहा है…"
    ),
    "imap.log.fetch_error": "❌ फ़ोल्डर प्राप्त करते समय त्रुटि:",
    "imap.log.no_mailboxes": "इस खाते पर कोई IMAP फ़ोल्डर नहीं मिला।",
    "imap.log.mailboxes_found": "सर्वर पर मिले फ़ोल्डर:",
    "imap.log.mailboxes_total": "कुल IMAP फ़ोल्डर: {count}",
    "imap.log.mailboxes_select_hint": (
        "केवल-पठन मोड में निकालने के लिए फ़ोल्डर चुनें।"
    ),
    "imap.log.start_export": (
        "IMAP एक्सट्रैक्शन शुरू हो रहा है (फोरेंसिक मोड, केवल-पठन)…"
    ),
    "imap.log.cancel_requested": (
        "IMAP वर्कर को रद्द करने का अनुरोध भेजा गया…"
    ),
    "imap.log.export_dir_saved": "एक्सपोर्ट डायरेक्टरी सहेजी गई: {path}",
    "imap.log.done": "IMAP प्रोसेसिंग समाप्त।",

    # ------------------------------------------------------------------
    # Dashboard v3 – sections / onglets
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "संदेह स्तर",
    "dashboard.tab_text": "EML इंडेक्स सारांश",
    "dashboard.tab_graphs": "ग्राफ़",
    "dashboard.section_charts": "ग्राफ़िकल विज़ुअलाइज़ेशन",

    "dashboard.chart_suspicion_title": "संदेह स्तर का वितरण",
    "dashboard.chart_folders_title": "IMAP फ़ोल्डर के अनुसार संदेश",
    "dashboard.chart_domains_title": "शीर्ष प्रेषक डोमेन",
    "dashboard.chart_attachments_title": "संलग्नक की उपस्थिति",
    "dashboard.chart_axis_count": "गिनती",
    "dashboard.chart_attachments_with": "संलग्नक के साथ",
    "dashboard.chart_attachments_without": "संलग्नक के बिना",

    # Légende / texte autour du scoring
    "dashboard.suspicion_distribution_line": (
        "संदेह स्तर के अनुसार ईमेल का वितरण:"
    ),
    "dashboard.suspicion_level.LOW": "कम",
    "dashboard.suspicion_level.MEDIUM": "मध्यम",
    "dashboard.suspicion_level.HIGH": "उच्च",
    "dashboard.suspicion_level.CRITICAL": "गंभीर",
    "dashboard.suspicion_level.UNKNOWN": "अज्ञात",

    # Graphes – titres (nouvelle nomenclature)
    "dashboard.chart.folders.title": "IMAP फ़ोल्डर के अनुसार ईमेल",
    "dashboard.chart.domains.title": "शीर्ष प्रेषक डोमेन",
    "dashboard.chart.attachments.title": "संलग्नक की उपस्थिति",
    "dashboard.chart.auth.title": "DKIM / SPF / DMARC परिणाम",
    "dashboard.chart.suspicion.title": "संदेह स्तर के अनुसार वितरण",

    # Graphes – libellés / états
    "dashboard.chart.no_data": (
        "इस ग्राफ़ को दिखाने के लिए पर्याप्त डेटा नहीं है।"
    ),
    "dashboard.chart.axis.emails": "ईमेल की संख्या",
    "dashboard.chart.axis.folders": "IMAP फ़ोल्डर",
    "dashboard.chart.axis.domains": "डोमेन",
    "dashboard.chart.axis.levels": "स्तर",

    # Petite aide visuelle sur les couleurs
    "dashboard.legend.safe": "मुख्यतः सुरक्षित मानी जाने वाली ज़ोन",
    "dashboard.legend.suspicious": "पहले जाँचने योग्य ज़ोन",

    # ------------------------------------------------------------------
    # Viewer – colonnes de scoring & suspicion
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "संदेह स्कोर",
    "viewer.col.suspicion_level": "स्तर",
    "viewer.col.suspicion_reasons": "कारण (सारांश)",

    # Tooltips scoring
    "viewer.score.tooltip.base": (
        "DKIM/SPF/DMARC, Received विसंगतियाँ, हेडर अखंडता "
        "और संलग्नकों के आधार पर गणना किया गया वैश्विक संदेह स्कोर।"
    ),
    "viewer.score.level.LOW": (
        "कम संदेह: वर्तमान नियमों के अनुसार कुछ भी असामान्य नहीं मिला।"
    ),
    "viewer.score.level.MEDIUM": (
        "मध्यम संदेह: कुछ तत्वों की जाँच करनी चाहिए "
        "(हेडर, प्रमाणीकरण या संलग्नक)।"
    ),
    "viewer.score.level.HIGH": (
        "उच्च संदेह: कई तकनीकी संकेतक असंगत या खतरनाक हैं।"
    ),
    "viewer.score.level.CRITICAL": (
        "गंभीर संदेह: ईमेल संभवतः दुर्भावनापूर्ण या जाली है।"
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth / providers restrictions
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "यह खाता ऐसे प्रोवाइडर द्वारा प्रबंधित प्रतीत होता है जो संदेशों तक पहुँच "
        "के लिए आधुनिक तंत्र (OAuth2, आधिकारिक एक्सपोर्ट) की आवश्यकता रखते हैं "
        "(जैसे Gmail, Outlook/Microsoft 365, Yahoo)।\n\n"
        "अनुपालन में रहने और इन नियमों को बायपास न करने के लिए, "
        "इस संस्करण का eml_forensic_suite इन सेवाओं के लिए प्रत्यक्ष IMAP एक्सट्रैक्शन "
        "नहीं करता।\n\n"
        "संदेशों को संगत तरीके से प्राप्त करने के लिए:\n"
        "  • Gmail: Google Takeout का उपयोग करके मेलबॉक्स (MBOX) एक्सपोर्ट करें,\n"
        "    या Thunderbird जैसे क्लाइंट से लोकल कॉपी बनाएँ।\n"
        "  • Outlook / Microsoft 365: अपने Outlook क्लाइंट एक्सपोर्ट (PST)\n"
        "    या अपनी संस्था के आर्काइविंग टूल्स का उपयोग करें।\n"
        "  • Yahoo आदि: प्रोवाइडर द्वारा दिए गए एक्सपोर्ट टूल्स का उपयोग करें।\n\n"
        "भविष्य के संस्करण इन एक्सपोर्ट्स (MBOX, PST आदि) को सीधे विश्लेषित करने "
        "का लक्ष्य रखेंगे ताकि इन प्लेटफॉर्म्स के साथ संगत बने रहें।"
    ),

    # ------------------------------------------------------------------
    # Viewer – mini langage de recherche
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "फोरेंसिक मिनी-लैंग्वेज:\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "ऑपरेटर्स: implicit AND, OR, NOT, कोष्ठक।"
    ),

    # ------------------------------------------------------------------
    # Viewer – CSV / index generic messages
    # ------------------------------------------------------------------
    "viewer.no_index_title": "कोई इंडेक्स उपलब्ध नहीं",
    "viewer.no_index_body": (
        "इस सत्र में कोई इंडेक्स उपलब्ध नहीं है।\n"
        "टैब 2 में इंडेक्स जनरेट करें या मैन्युअली CSV फ़ाइल खोलें।"
    ),
    "viewer.open_csv_title": "इंडेक्स CSV फ़ाइल खोलें",
    "viewer.error_csv_title": "CSV पढ़ने में त्रुटि",
    "viewer.error_csv_body": (
        "CSV फ़ाइल पढ़ने में असमर्थ: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – preview (version finale, lecture seule)
    # ------------------------------------------------------------------
    "viewer.attach.preview": "केवल-पठन पूर्वावलोकन",
    "viewer.attach.preview_failed_title": "पूर्वावलोकन असफल",
    "viewer.attach.preview_failed_body": (
        "इस संलग्नक का पूर्वावलोकन दिखाने में असमर्थ।"
    ),
    "viewer.attach.preview_unsupported_title": "असमर्थित प्रकार",
    "viewer.attach.preview_unsupported_body": (
        "इस MIME प्रकार के लिए कोई बिल्ट-इन पूर्वावलोकन उपलब्ध नहीं: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – extraction PJ (version finale)
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "कोई संदेश नहीं",
    "viewer.attach.no_msg_body": "अभी कोई संदेश चयनित नहीं है।",
    "viewer.attach.no_selection_title": "कोई संलग्नक चयनित नहीं",
    "viewer.attach.no_selection_body": (
        "कृपया सूची में से कोई संलग्नक चुनें।"
    ),
    "viewer.attach.no_root_title": "वर्किंग डायरेक्टरी नहीं मिली",
    "viewer.attach.no_root_body": (
        "एक्सट्रैक्शन के लिए कोई फोरेंसिक / इंडेक्स डायरेक्टरी कॉन्फ़िगर नहीं है।"
    ),
    "viewer.attach.extract_one_title": "संलग्नक निकाला गया",
    "viewer.attach.extract_one_body": (
        "संलग्नक यहाँ निकाला गया है:\n{path}"
    ),
    "viewer.attach.extract_all_title": "संलग्नक निकाले गए",
    "viewer.attach.extract_all_body": (
        "{count} संलग्नक यहाँ निकाले गए हैं:\n{paths}"
    ),

    # ------------------------------------------------------------------
    # Actions PJ (boutons – déjà couverts par les textes ci-dessus)
    # ------------------------------------------------------------------
    "viewer.attach.extract_one": "चयनित संलग्नक निकालें",
    "viewer.attach.extract_all": "सभी संलग्नक निकालें",

    # ------------------------------------------------------------------
    # About box
    # ------------------------------------------------------------------
    "about.version_label": "संस्करण:",
    "about.description": (
        "EML/IMAP ईमेल की फोरेंसिक विश्लेषण के लिए केवल-पठन टूल।"
    ),
}
