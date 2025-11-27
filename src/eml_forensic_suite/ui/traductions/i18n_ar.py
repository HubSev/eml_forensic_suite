from __future__ import annotations

from typing import Dict

TRANSLATIONS_AR: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "مجموعة أدوات التحليل الجنائي EML / IMAP (وضع القراءة فقط)",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "ملف",
    "menu.view": "عرض",
    "menu.help": "مساعدة",

    "menu.file.settings": "الإعدادات…",
    "menu.file.quit": "خروج",

    "menu.view.theme.dark": "الوضع الداكن",
    "menu.view.theme.light": "الوضع الفاتح",

    "menu.help.about": "حول…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. تصدير IMAP",
    "tab.index": "2. فهرسة EML",
    "tab.viewer": "3. عارض جنائي",
    "tab.dashboard": "4. لوحة التحليل الجنائي",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "الإعدادات",
    "settings.reports_dir.label": "مجلد العمل / التقارير:",
    "settings.reports_dir.browse": "تصفح…",
    "settings.language.label": "لغة الواجهة:",
    "settings.reports_dir.dialog_title": "اختر مجلد العمل / التقارير",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "جاهز.",
    "status.settings.saved": "تم حفظ الإعدادات.",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "مجلد تصدير ملفات EML:",
    "index.browse": "تصفح…",
    "index.use_last_export": "استخدام آخر تصدير IMAP",
    "index.log_placeholder": "سجل فهرسة EML (للقراءة فقط)…",
    "index.start_button": "بدء فهرسة EML",
    "index.dialog_select_folder": "اختر مجلد تصدير EML",
    "index.no_last_export": "لا يوجد تصدير IMAP معروف بعد (علامة التبويب 1).",
    "index.error_already_running_title": "الفهرسة قيد التشغيل",
    "index.error_already_running_body": "عملية فهرسة EML قيد التشغيل بالفعل.",
    "index.error_no_folder_title": "المجلد مفقود",
    "index.error_no_folder_body": "يرجى اختيار مجلد يحتوي على ملفات .eml.",
    "index.error_invalid_folder_title": "مجلد غير صالح",
    "index.error_invalid_folder_body": "المجلد المحدد غير موجود:\n{folder}",
    "index.status_selected_folder": "المجلد المحدد للفهرسة: {folder}",
    "index.error_indexing_title": "خطأ أثناء الفهرسة",
    "index.error_log": "❌ خطأ: {error}",
    "index.done_log_success": "\nتم إكمال الفهرسة بنجاح.",
    "index.done_log_path": "مسار CSV: {csv_path}",
    "index.done_log_count": "عدد العناصر المفهرسة: {count}",
    "index.done_msg_title": "اكتملت الفهرسة",
    "index.done_msg_body": (
        "تم إكمال فهرسة EML.\n\nملف CSV: {csv_path}\nالعناصر: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "استخدام آخر فهرس",
    "dashboard.open_csv": "فتح ملف CSV…",
    "dashboard.placeholder": "ملخص إحصائي جنائي استناداً إلى فهرس EML…",
    "dashboard.source_memory": "المصدر: الفهرس في الذاكرة (آخر فهرسة في هذه الجلسة).",
    "dashboard.source_csv": "المصدر: {path}",
    "dashboard.no_index_title": "لا يوجد فهرس",
    "dashboard.no_index_body": (
        "لا يوجد فهرس متاح في هذه الجلسة.\n"
        "قم بإنشاء فهرس في علامة التبويب 2 أو افتح ملف CSV يدوياً."
    ),
    "dashboard.dialog_open_csv": "فتح ملف الفهرس CSV",
    "dashboard.error_csv_missing_title": "الملف غير موجود",
    "dashboard.error_csv_missing_body": "الملف المحدد غير موجود:\n{path}",
    "dashboard.error_csv_read_title": "خطأ في قراءة CSV",
    "dashboard.error_csv_read_body": "غير قادر على قراءة ملف CSV: {path}",
    "dashboard.empty_csv_title": "فهرس فارغ",
    "dashboard.empty_csv_body": "ملف CSV لا يحتوي على أي عناصر قابلة للاستخدام.",
    "dashboard.no_data": "لا توجد بيانات للتحليل.",

    "dashboard.section_overview": "نظرة عامة",
    "dashboard.overview_line": (
        "إجمالي الرسائل: {total} – المرسلون المميزون: {senders}"
    ),
    "dashboard.dates_line": "الفترة المغطاة: {date_min} → {date_max}",
    "dashboard.dates_unknown": "التواريخ غير متوفرة أو غير قابلة للتحليل.",

    "dashboard.section_folders": "التوزيع حسب مجلد IMAP",
    "dashboard.no_folders": "لا توجد مجلدات IMAP.",

    "dashboard.section_domains": "التوزيع حسب النطاق (المرسل)",
    "dashboard.no_domains": "لا توجد نطاقات.",

    "dashboard.section_attachments": "المرفقات",
    "dashboard.attachments_line": (
        "الرسائل مع مرفقات: {with_att}/{total} – إجمالي المرفقات المقدر: {total_att}"
    ),

    "dashboard.section_auth": "المصادقة (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "نتائج DKIM:",
    "dashboard.auth_header_spf": "نتائج SPF:",
    "dashboard.auth_header_dmarc": "نتائج DMARC:",

    "dashboard.section_integrity": "السلامة / الرؤوس المفقودة",
    "dashboard.integrity_flags_title": "علامات السلامة المكتشفة:",
    "dashboard.no_integrity_flags": "لا توجد علامات سلامة محددة.",

    "dashboard.section_received": "التحقق من سلسلة Received",
    "dashboard.no_received_anomalies": (
        "لا توجد شذوذات في رؤوس Received (ضمن القواعد الحالية)."
    ),

    # ------------------------------------------------------------------
    # Viewer tab – base columns
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "مجلد IMAP",
    "viewer.col.sequence_number": "التسلسل",
    "viewer.col.date_header": "التاريخ",
    "viewer.col.from_header": "من",
    "viewer.col.to_header": "إلى",
    "viewer.col.cc_header": "نسخة",
    "viewer.col.cci_header": "نسخة مخفية",
    "viewer.col.subject": "الموضوع",
    "viewer.col.message_id": "معرّف الرسالة",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "مرفقات؟",
    "viewer.col.attachment_count": "عدد المرفقات",
    "viewer.col.attachment_filenames": "أسماء المرفقات",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "نتائج Authentication-Results (مقتطف)",
    "viewer.col.received_count": "عدد Received",
    "viewer.col.received_anomalies": "شذوذات Received",
    "viewer.col.integrity_flags": "علامات السلامة",
    "viewer.col.relative_path": "المسار النسبي",
    "viewer.col.filename": "اسم الملف",

    # ------------------------------------------------------------------
    # Viewer search
    # ------------------------------------------------------------------
    "viewer.search_label": "بحث:",
    "viewer.search_placeholder": "تصفية الفهرس (جميع الأعمدة)…",
    "viewer.search_clear": "مسح",

    "viewer.headers_label": "الرؤوس",
    "viewer.headers_placeholder": "رؤوس الرسالة المحددة…",

    "viewer.body_label": "المحتوى (نصي)",
    "viewer.body_placeholder": (
        "نص text/plain (أو HTML خام في حال عدم توفره)…"
    ),

    "viewer.btn_load_last": "استخدام آخر تصدير IMAP",
    "viewer.btn_open_csv": "فتح ملف CSV...",
    "viewer.attachments_label": "المرفقات",

    # ------------------------------------------------------------------
    # Viewer – EML errors
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "ملف EML غير موجود",
    "viewer.error_missing_eml_body": "غير قادر على العثور على ملف EML:\n{path}",
    "viewer.error_parse_eml_title": "خطأ في قراءة EML",
    "viewer.error_parse_eml_body": "غير قادر على تحليل ملف EML: {path}",

    # ------------------------------------------------------------------
    # Viewer – attachments table
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "الاسم",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "الحجم (بايت)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "مشبوه؟",

    "viewer.attach.yes": "نعم",
    "viewer.attach.no": "لا",

    # ------------------------------------------------------------------
    # IMAP tab
    # ------------------------------------------------------------------
    "imap.group.connection": "خادم IMAP (مصدر الأدلة)",
    "imap.label.host": "عنوان خادم IMAP",
    "imap.label.user": "معرّف علبة البريد المحللة",
    "imap.label.password": "كلمة المرور (غير مخزنة)",
    "imap.label.date_start": "تاريخ البداية (تصفية جنائية)",
    "imap.label.date_end": "تاريخ النهاية (تصفية جنائية)",

    "imap.placeholder.host": "مثال: imap.example.com",
    "imap.placeholder.user": "مثال: incident@company.com",
    "imap.placeholder.password": "كلمة مرور الحساب المحلل",
    "imap.placeholder.date_start": "يوم/شهر/سنة (اختياري)",
    "imap.placeholder.date_end": "يوم/شهر/سنة (اختياري)",

    "imap.button.fetch_mailboxes": "تفقد مجلدات IMAP…",
    "imap.button.start_export": "بدء الاستخراج الجنائي",
    "imap.button.cancel_export": "إلغاء الاستخراج",

    "imap.label.mailboxes_title": "مجلدات IMAP المراد استخراجها (مصدر الأدلة):",
    "imap.checkbox.select_all": "تحديد الكل",

    "imap.log.placeholder": "سجل استخراج IMAP (للقراءة فقط، مع طوابع زمنية)…",

    # ------------------------------------------------------------------
    # IMAP – errors
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "إعدادات غير مكتملة",
    "imap.error.missing_fields.body": (
        "يرجى إدخال خادم IMAP واسم المستخدم وكلمة المرور."
    ),

    "imap.info.export_running.title": "الاستخراج قيد التشغيل",
    "imap.info.export_running.body": "عملية استخراج IMAP قيد التشغيل بالفعل.",

    "imap.error.date_invalid.title": "تاريخ غير صالح",
    "imap.error.date_invalid.body": "خطأ في التواريخ المقدمة: {error}",
    "imap.error.date_end_before_start.body": (
        "لا يمكن أن يكون تاريخ النهاية أسبق من تاريخ البداية."
    ),

    "imap.error.no_mailbox_selected.title": "لا يوجد مجلد محدد",
    "imap.error.no_mailbox_selected.body": (
        "يرجى اختيار مجلد IMAP واحد على الأقل."
    ),

    "imap.error.fetch_mailboxes.title": "خطأ IMAP",
    "imap.error.fetch_mailboxes.body": "غير قادر على استرجاع مجلدات IMAP:\n{error}",

    "imap.info.generic.title": "معلومة",
    "imap.error.generic.title": "خطأ",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "جارٍ الاتصال بـ {host}:{port} ‏(SSL={use_ssl})...",
    "imap.log.connected": "تم الاتصال بخادم IMAP.",
    "imap.log.select_folder": "جارٍ اختيار المجلد \"{folder}\"...",
    "imap.log.folder_selected": "تم اختيار المجلد \"{folder}\".",
    "imap.log.message_count": "عدد الرسائل المطلوب تصديرها: {count}.",
    "imap.log.fetching": "جارٍ جلب رسائل IMAP...",
    "imap.log.export_done": "اكتمل تصدير IMAP.",
    "imap.log.saving_to": "جارٍ حفظ الرسائل في \"{output_dir}\"...",
    "imap.log.progress": "تصدير الرسالة {current}/{total}...",
    "imap.log.skip_existing": "الملف \"{path}\" موجود مسبقًا، يتم تجاوزه.",

    "imap.error.connect_failed": "تعذر الاتصال بـ {host}:{port}: {error}",
    "imap.error.login_failed": "خطأ في مصادقة IMAP: {error}",
    "imap.error.select_failed": "تعذر اختيار المجلد \"{folder}\": {error}",
    "imap.error.fetch_failed": "حدث خطأ أثناء جلب الرسائل: {error}",
    "imap.error.generic": "حدث خطأ أثناء تصدير IMAP: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== تقرير تصدير IMAP (وضع القراءة فقط) ===",
    "imap.report.tool_line": "الأداة     : eml_forensic_suite – تصدير IMAP",
    "imap.report.version_line": "الإصدار    : {version}",
    "imap.report.folder_line": "المجلد     : {export_dir}",

    "imap.report.section_tool": "---- معلومات الأداة ----",
    "imap.report.tool_path": "مسار الأداة           : {tool_path}",
    "imap.report.tool_hash": "قيمة SHA-256 للأداة   : {tool_hash}",

    "imap.report.section_env": "---- بيئة التشغيل ----",
    "imap.report.env_os": "نظام التشغيل          : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "إصدار Python          : {python_version}",

    "imap.report.section_context": "---- سياق IMAP / الحساب ----",
    "imap.report.context_host": "خادم IMAP : {host}",
    "imap.report.context_user": "الحساب    : {user}",
    "imap.report.context_date_start": "تاريخ البدء المطلوب : {date_start}",
    "imap.report.context_date_end": "تاريخ الانتهاء المطلوب : {date_end}",
    "imap.report.context_criteria": "معايير بحث IMAP : {search_criteria} (كما أُرسلت إلى الخادم)",

    "imap.report.selected_folders_title": "المجلدات المحددة:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- معلومات خادم IMAP ----",
    "imap.report.server_greeting": "راية IMAP  : {greeting}",
    "imap.report.server_capability": "CAPABILITY : {capability}",

    "imap.report.section_timestamps": "---- الطوابع الزمنية للتحليل ----",
    "imap.report.timestamp_start_utc": "بداية التحليل (UTC)     : {dt}",
    "imap.report.timestamp_start_local": "بداية التحليل (المحلي)  : {dt}",
    "imap.report.timestamp_end_utc": "نهاية التحليل (UTC)     : {dt}",
    "imap.report.timestamp_end_local": "نهاية التحليل (المحلي)  : {dt}",
    "imap.report.duration": "المدة الإجمالية          : {duration}",

    "imap.report.section_folders": "---- المجلدات المُحلَّلة ----",
    "imap.report.folders_count": "عدد المجلدات المحددة : {count}",

    "imap.report.folder_header": "المجلد : {name}",
    "imap.report.folder_messages": "  الرسائل الموجودة (ضمن الفترة) : {count}",
    "imap.report.folder_exported": "  الرسائل المصدَّرة              : {count}",
    "imap.report.folder_errors": "  أخطاء الجلب                    : {count}",
    "imap.report.folder_bytes": "  الحجم الذي تم تنزيله           : {bytes} بايت",
    "imap.report.folder_size_stats": "  أصغر / أكبر / متوسط حجم       : {min_size} / {max_size} / {avg_size} بايت",
    "imap.report.folder_period": "  الفترة المغطاة (INTERNALDATE) : {first} → {last}",
    "imap.report.folder_error_uids": "  UIDs التي حدثت بها أخطاء (قائمة غير شاملة) : {uids}",

    "imap.report.section_totals": "---- الإجماليات العامة ----",
    "imap.report.total_messages": "الرسائل الموجودة (كل المجلدات) : {count}",
    "imap.report.total_exported": "الرسائل المصدَّرة               : {count}",
    "imap.report.total_errors": "أخطاء الجلب                     : {count}",
    "imap.report.total_bytes": "الحجم الإجمالي الذي تم تنزيله   : {bytes} بايت",

    "imap.report.section_forensic": "---- المنهجية والضمانات الجنائية ----",
    "imap.report.forensic_item_readonly": "- استخدمت الأداة فقط أوامر IMAP بالوضع للقراءة فقط (SELECT readonly، SEARCH، FETCH). لم يتم تعديل أو حذف أي رسالة أو وضع علامة \"مقروء\" عليها أثناء التحليل.",
    "imap.report.forensic_item_eml": "- تم تصدير الرسائل تمامًا كما قدّمها خادم IMAP، وحُفظت على القرص كملفات ‎.eml دون أي تعديل في محتواها.",
    "imap.report.forensic_item_hashes": "- تم ربط كل رسالة مُصدَّرة بقيمة تجزئة SHA-256 مدرجة في hashes.txt، إضافة إلى تجزئة شاملة محسوبة من تجميع جميع القيم الفردية.",
    "imap.report.forensic_item_report_hash": "- تم حساب تجزئة SHA-256 لهذا التقرير التحليلي نفسه، وأُضيفت هذه التجزئة إلى hashes.txt لضمان سلامة التقرير.",

    "imap.report.hashes_report_header": "تقرير التحليل:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "لم يتم اختيار أي مجلد.",
    "imap.worker.log_export_dir": "مجلد التصدير: {export_dir}",
    "imap.worker.tool_hash_error": "(خطأ أثناء حساب تجزئة الأداة)",

    "imap.worker.log_connecting": "جارٍ الاتصال بخادم IMAP...",
    "imap.worker.greeting_not_available": "(راية IMAP غير متوفرة)",
    "imap.worker.log_auth_classic": "مصادقة IMAP الكلاسيكية...",
    "imap.worker.error_auth_failed": "خطأ في مصادقة IMAP: {error}",
    "imap.worker.capability_error": "(خطأ أثناء أمر CAPABILITY)",

    "imap.worker.log_date_start_inclusive": "تاريخ البدء (شامل): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "تاريخ البدء: غير مُحدَّد → الاستخراج من أول رسالة متاحة.",
    "imap.worker.date_start_unset_label": "أول رسالة متاحة (بدون حد أدنى)",

    "imap.worker.log_date_end_inclusive": "تاريخ الانتهاء (شامل): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "تاريخ الانتهاء: غير مُحدَّد → حتى آخر تاريخ متاح على الخادم.",
    "imap.worker.date_end_unset_label": "آخر رسالة متاحة (بدون حد أقصى)",

    "imap.worker.log_criteria": "معايير بحث IMAP المستخدمة: {criteria}",
    "imap.worker.log_selected_folders_header": "المجلدات المحددة ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "طُلِب الإيقاف أثناء مرحلة العد.",
    "imap.worker.log_phase1_count": "[المرحلة 1] عدّ الرسائل في {folder}...",
    "imap.worker.log_select_folder_failed": "  ⚠️ تعذر اختيار هذا المجلد، يتم تجاوزه.",
    "imap.worker.log_search_folder_failed": "  ⚠️ حدث خطأ أثناء البحث في هذا المجلد، يتم تجاوزه.",
    "imap.worker.log_messages_to_process": "  → {count} رسالة للمعالجة في {folder}",

    "imap.worker.log_total_messages_to_download": "العدد الإجمالي للرسائل المطلوب تنزيلها (كل المجلدات): {count}",

    "imap.worker.log_stop_during_export": "طُلِب الإيقاف: يتم إيقاف التصدير بشكل منظّم.",
    "imap.worker.log_folder_header": "=== المجلد: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  لا توجد رسائل في {folder} لهذه الفترة.",
    "imap.worker.log_folder_message_count": "  عدد الرسائل الموجودة في {folder}: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ تعذر إعادة اختيار هذا المجلد، يتم تجاوزه.",

    "imap.worker.log_first_message_download": "  تنزيل أول رسالة ({uid})...",
    "imap.worker.log_folder_progress": "  تقدم المجلد {folder}: ‏{current}/{total} (آخر UID: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ حدث خطأ أثناء جلب الرسالة {uid}، المتابعة...",
    "imap.worker.log_folder_end": "  نهاية المجلد {folder}",

    "imap.worker.hashes_header": "قائمة الملفات المصدَّرة وقيم تجزئة SHA-256 الخاصة بها",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "التجزئة الشاملة (الرسائل فقط):",

    "imap.worker.log_export_done_header": "=== اكتمل التصدير ===",
    "imap.worker.log_export_done_count": "إجمالي عدد الرسائل المصدَّرة: {count}",
    "imap.worker.log_export_done_hashes_file": "ملف التجزئات: {path}",
    "imap.worker.log_export_done_hash": "التجزئة الشاملة: {file_hash}",

    "imap.worker.summary": (
        "اكتمل التصدير.\n\n"
        "عدد الرسائل المصدَّرة: {count}\n"
        "المجلد: {export_dir}\n\n"
        "التجزئة الشاملة (الرسائل):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "تم إنشاء تقرير التحليل وحسابه تجزئة (راجع rapport_imap_export.txt و hashes.txt).",
    "imap.worker.log_report_failed": "⚠️ تعذر إنشاء تقرير التحليل: {error}",

    "imap.worker.error_generic": "حدث خطأ: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "جارٍ الاتصال بخادم IMAP...",
    "imap.tk.log_auth_classic": "مصادقة IMAP الكلاسيكية...",
    "imap.tk.error_list_mailboxes_failed": "تعذر سرد مجلدات IMAP.",

    "imap.tk.log_folders_found_header": "المجلدات الموجودة على الخادم:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "إجمالي مجلدات IMAP: {count}",

    "imap.tk.msgbox_error_title": "خطأ",
    "imap.tk.msgbox_error_fetch_mailboxes": "حدث خطأ أثناء جلب مجلدات IMAP: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ خطأ أثناء جلب المجلدات: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. تصدير IMAP",

    "imap.tk.label_server": "خادم IMAP:",
    "imap.tk.label_email": "عنوان البريد الإلكتروني:",
    "imap.tk.label_password": "كلمة المرور:",
    "imap.tk.label_date_start": "تاريخ البدء (DD/MM/YYYY، اختياري):",
    "imap.tk.label_date_end": "تاريخ الانتهاء (DD/MM/YYYY، اختياري):",
    "imap.tk.label_log": "السجل:",
    "imap.tk.label_mailboxes": "مجلدات IMAP المطلوب تصديرها:",
    "imap.tk.checkbox_select_all": "تحديد الكل / إلغاء التحديد",
    "imap.tk.label_progress": "التقدم:",

    "imap.tk.msgbox_missing_fields_title": "حقول ناقصة",
    "imap.tk.msgbox_missing_fields_text": "يرجى ملء الخادم والبريد الإلكتروني وكلمة المرور.",

    "imap.tk.log_fetch_mailboxes_start": "جارٍ جلب مجلدات IMAP...",
    "imap.tk.log_no_mailboxes_or_error": "لم يُعثر على أي مجلد أو حدث خطأ.",
    "imap.tk.log_select_mailboxes_hint": "اختر المجلدات المطلوب تصديرها.",

    "imap.tk.button_list_mailboxes": "سرد مجلدات IMAP",

    "imap.tk.msgbox_date_start_invalid_title": "تاريخ بدء غير صالح",
    "imap.tk.msgbox_date_start_invalid_text": "يجب أن يكون تاريخ البدء بصيغة DD/MM/YYYY.",

    "imap.tk.msgbox_date_end_invalid_title": "تاريخ انتهاء غير صالح",
    "imap.tk.msgbox_date_end_invalid_text": "يجب أن يكون تاريخ الانتهاء بصيغة DD/MM/YYYY.",

    "imap.tk.msgbox_date_range_invalid_title": "نطاق تواريخ غير صالح",
    "imap.tk.msgbox_date_range_invalid_text": (
        "لا يمكن أن يكون تاريخ الانتهاء أسبق من تاريخ البدء."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "لم يتم اختيار أي مجلد",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "يرجى اختيار مجلد IMAP واحد على الأقل (عبر \"سرد مجلدات IMAP\")."
    ),

    "imap.tk.log_export_start": "جارٍ بدء التصدير...",
    "imap.tk.button_run_export": "تشغيل التصدير (المجلدات المحددة)",

    "imap.tk.log_stop_requested": (
        "طُلِب الإيقاف، سيتم إنهاء التصدير بشكل منظّم..."
    ),
    "imap.tk.button_stop_export": "إيقاف التصدير",

    "imap.tk.msgbox_export_done_title": "اكتمل التصدير",


    # ------------------------------------------------------------------
    # IMAP – logs
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "الاتصال بخادم IMAP لاستعراض المجلدات…"
    ),
    "imap.log.fetch_error": "❌ خطأ أثناء استرجاع المجلدات:",
    "imap.log.no_mailboxes": "لا توجد مجلدات IMAP في هذا الحساب.",
    "imap.log.mailboxes_found": "المجلدات الموجودة على الخادم:",
    "imap.log.mailboxes_total": "إجمالي المجلدات: {count}",
    "imap.log.mailboxes_select_hint": (
        "اختر المجلدات التي تريد استخراجها في وضع القراءة فقط."
    ),
    "imap.log.start_export": (
        "بدء استخراج IMAP (وضع جنائي، قراءة فقط)…"
    ),
    "imap.log.cancel_requested": (
        "تم إرسال طلب الإلغاء إلى عامل IMAP…"
    ),
    "imap.log.export_dir_saved": "تم حفظ مجلد التصدير: {path}",
    "imap.log.done": "اكتمل تجهيز IMAP.",

    # ------------------------------------------------------------------
    # Dashboard v3
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "مستويات الاشتباه",
    "dashboard.tab_text": "ملخص فهرس EML",
    "dashboard.tab_graphs": "الرسوم البيانية",
    "dashboard.section_charts": "المرئيات البيانية",

    "dashboard.chart_suspicion_title": "توزيع مستويات الاشتباه",
    "dashboard.chart_folders_title": "عدد الرسائل حسب مجلد IMAP",
    "dashboard.chart_domains_title": "أعلى نطاقات المرسلين",
    "dashboard.chart_attachments_title": "وجود المرفقات",
    "dashboard.chart_axis_count": "العدد",
    "dashboard.chart_attachments_with": "مع مرفقات",
    "dashboard.chart_attachments_without": "بدون مرفقات",

    "dashboard.suspicion_distribution_line": (
        "توزيع الرسائل حسب مستوى الاشتباه:"
    ),
    "dashboard.suspicion_level.LOW": "منخفض",
    "dashboard.suspicion_level.MEDIUM": "متوسط",
    "dashboard.suspicion_level.HIGH": "عالٍ",
    "dashboard.suspicion_level.CRITICAL": "حرج",
    "dashboard.suspicion_level.UNKNOWN": "غير معروف",

    "dashboard.chart.folders.title": "الرسائل حسب مجلد IMAP",
    "dashboard.chart.domains.title": "أعلى نطاقات المرسلين",
    "dashboard.chart.attachments.title": "وجود المرفقات",
    "dashboard.chart.auth.title": "نتائج DKIM / SPF / DMARC",
    "dashboard.chart.suspicion.title": "التوزيع حسب مستوى الاشتباه",

    "dashboard.chart.no_data": "لا توجد بيانات كافية لعرض هذا الرسم.",
    "dashboard.chart.axis.emails": "عدد الرسائل",
    "dashboard.chart.axis.folders": "مجلدات IMAP",
    "dashboard.chart.axis.domains": "النطاقات",
    "dashboard.chart.axis.levels": "المستويات",

    "dashboard.legend.safe": "منطقة تعتبر آمنة بشكل عام",
    "dashboard.legend.suspicious": "منطقة يجب التحقيق فيها أولاً",

    # ------------------------------------------------------------------
    # Viewer – scoring
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "درجة الاشتباه",
    "viewer.col.suspicion_level": "المستوى",
    "viewer.col.suspicion_reasons": "الأسباب (ملخص)",

    "viewer.score.tooltip.base": (
        "يتم حساب درجة الاشتباه بناءً على DKIM/SPF/DMARC، "
        "وشذوذات Received، وسلامة الرؤوس، والمرفقات."
    ),
    "viewer.score.level.LOW": "اشتباه منخفض: لا شيء غير طبيعي.",
    "viewer.score.level.MEDIUM": (
        "اشتباه متوسط: يوجد بعض العناصر التي يجب التحقق منها."
    ),
    "viewer.score.level.HIGH": (
        "اشتباه عالٍ: عدة مؤشرات تقنية غير متسقة أو خطيرة."
    ),
    "viewer.score.level.CRITICAL": (
        "اشتباه حرج: الرسالة على الأرجح خبيثة أو مزورة."
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "يبدو أن هذا الحساب مُدار بواسطة مزود يتطلب آليات حديثة "
        "(OAuth2، صادرات رسمية) للوصول إلى الرسائل "
        "(مثل Gmail، Outlook/M365، Yahoo).\n\n"
        "للبقاء متوافقين مع القواعد، لا يقوم هذا الإصدار من الأداة "
        "بالوصول المباشر عبر IMAP لهذه الخدمات.\n\n"
        "طرق استخراج الرسائل:\n"
        " • Gmail: استخدم Google Takeout (MBOX)\n"
        "   أو عميل Thunderbird.\n"
        " • Outlook / Microsoft 365: استخدم التصدير من Outlook (PST)\n"
        "   أو أدوات الأرشفة.\n"
        " • Yahoo: استخدم أدوات التصدير الخاصة بالمزود.\n\n"
        "ستدعم الإصدارات المستقبلية تحليل ملفات MBOX / PST مباشرة."
    ),

    # ------------------------------------------------------------------
    # Viewer – search language
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "لغة بحث جنائية:\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "العوامل: AND و OR و NOT، والأقواس."
    ),

    # ------------------------------------------------------------------
    # Viewer – CSV load
    # ------------------------------------------------------------------
    "viewer.no_index_title": "لا يوجد فهرس متاح",
    "viewer.no_index_body": (
        "لا يوجد فهرس في هذه الجلسة.\n"
        "قم بإنشاء واحد في علامة التبويب 2 أو افتح ملف CSV يدوياً."
    ),
    "viewer.open_csv_title": "فتح ملف CSV",
    "viewer.error_csv_title": "خطأ في قراءة CSV",
    "viewer.error_csv_body": "غير قادر على قراءة ملف CSV: {path}\n\n{error}",

    # ------------------------------------------------------------------
    # Viewer – attachment preview
    # ------------------------------------------------------------------
    "viewer.attach.preview": "معاينة (قراءة فقط)",
    "viewer.attach.preview_failed_title": "فشل المعاينة",
    "viewer.attach.preview_failed_body": "غير قادر على عرض معاينة لهذا المرفق.",
    "viewer.attach.preview_unsupported_title": "نوع غير مدعوم",
    "viewer.attach.preview_unsupported_body": (
        "لا توجد معاينة مضمنة لنوع MIME هذا: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – extraction
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "لا توجد رسالة",
    "viewer.attach.no_msg_body": "لا توجد رسالة محددة حالياً.",
    "viewer.attach.no_selection_title": "لا يوجد مرفق محدد",
    "viewer.attach.no_selection_body": "يرجى اختيار مرفق من القائمة.",
    "viewer.attach.no_root_title": "مجلد العمل غير موجود",
    "viewer.attach.no_root_body": (
        "لا يوجد مجلد فهرس / أدلة مهيأ للاستخراج."
    ),
    "viewer.attach.extract_one_title": "تم استخراج المرفق",
    "viewer.attach.extract_one_body": (
        "تم استخراج المرفق إلى:\n{path}"
    ),
    "viewer.attach.extract_all_title": "تم استخراج المرفقات",
    "viewer.attach.extract_all_body": (
        "تم استخراج {count} مرفقاً:\n{paths}"
    ),

    "viewer.attach.extract_one": "استخراج المرفق المحدد",
    "viewer.attach.extract_all": "استخراج كل المرفقات",

    # ------------------------------------------------------------------
    # About box
    # ------------------------------------------------------------------
    "about.version_label": "الإصدار:",
    "about.description": "أداة قراءة فقط للتحليل الجنائي لرسائل EML/IMAP.",
}
