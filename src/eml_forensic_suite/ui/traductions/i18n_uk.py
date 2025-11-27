from __future__ import annotations

from typing import Dict

TRANSLATIONS_UK: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "Forensic-набір EML / IMAP (лише для читання)",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "Файл",
    "menu.view": "Вигляд",
    "menu.help": "Довідка",

    "menu.file.settings": "Параметри…",
    "menu.file.quit": "Вийти",

    "menu.view.theme.dark": "Темна тема",
    "menu.view.theme.light": "Світла тема",

    "menu.help.about": "Про програму…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. Експорт IMAP",
    "tab.index": "2. Індексування EML",
    "tab.viewer": "3. Forensic-переглядач",
    "tab.dashboard": "4. Forensic-дашборд",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "Параметри",
    "settings.reports_dir.label": "Робочий / звітний каталог:",
    "settings.reports_dir.browse": "Огляд…",
    "settings.language.label": "Мова інтерфейсу:",
    "settings.reports_dir.dialog_title": "Виберіть робочий / звітний каталог",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "Готово.",
    "status.settings.saved": "Параметри збережено.",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "Каталог експорту EML:",
    "index.browse": "Огляд…",
    "index.use_last_export": "Використати останній експорт IMAP",
    "index.log_placeholder": "Журнал індексування EML (лише для читання)…",
    "index.start_button": "Запустити індексування EML",
    "index.dialog_select_folder": "Виберіть каталог експорту EML",
    "index.no_last_export": "Поки що немає відомого експорту IMAP (вкладка 1).",
    "index.error_already_running_title": "Індексування вже виконується",
    "index.error_already_running_body": "Індексування EML вже виконується.",
    "index.error_no_folder_title": "Каталог не вказано",
    "index.error_no_folder_body": (
        "Будь ласка, виберіть каталог, що містить файли .eml."
    ),
    "index.error_invalid_folder_title": "Некоректний каталог",
    "index.error_invalid_folder_body": "Вказаний каталог не існує:\n{folder}",
    "index.status_selected_folder": "Вибраний каталог для індексування: {folder}",
    "index.error_indexing_title": "Помилка під час індексування",
    "index.error_log": "❌ Помилка: {error}",
    "index.done_log_success": "\nІндексування успішно завершено.",
    "index.done_log_path": "Шлях до CSV: {csv_path}",
    "index.done_log_count": "Кількість проіндексованих записів: {count}",
    "index.done_msg_title": "Індексування завершено",
    "index.done_msg_body": (
        "Індексування EML завершено.\n\nФайл CSV: {csv_path}\nЗаписів: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "Використати останній індекс",
    "dashboard.open_csv": "Відкрити індекс CSV…",
    "dashboard.placeholder": (
        "Forensic-статистичний підсумок на основі індексу EML…"
    ),
    "dashboard.source_memory": (
        "Джерело: індекс у пам’яті (останнє індексування в цій сесії)."
    ),
    "dashboard.source_csv": "Джерело: {path}",
    "dashboard.no_index_title": "Немає індексу",
    "dashboard.no_index_body": (
        "У цій сесії індекс недоступний.\n"
        "Згенеруйте індекс у вкладці 2 або відкрийте CSV вручну."
    ),
    "dashboard.dialog_open_csv": "Відкрити файл індексу CSV",
    "dashboard.error_csv_missing_title": "Файл не знайдено",
    "dashboard.error_csv_missing_body": "Вказаний файл не існує:\n{path}",
    "dashboard.error_csv_read_title": "Помилка читання CSV",
    "dashboard.error_csv_read_body": "Неможливо прочитати файл CSV: {path}",
    "dashboard.empty_csv_title": "Порожній індекс",
    "dashboard.empty_csv_body": "Файл CSV не містить корисних записів.",
    "dashboard.no_data": "Немає даних для аналізу.",

    "dashboard.section_overview": "Загальний огляд",
    "dashboard.overview_line": (
        "Усього листів: {total} – Унікальних відправників: {senders}"
    ),
    "dashboard.dates_line": "Період, що охоплюється: {date_min} → {date_max}",
    "dashboard.dates_unknown": "Дати відсутні або не підлягають обробці.",

    "dashboard.section_folders": "Розподіл за папками IMAP",
    "dashboard.no_folders": "Папки IMAP не виявлені.",

    "dashboard.section_domains": "Розподіл за доменом (відправник)",
    "dashboard.no_domains": "Жодного домену не виявлено.",

    "dashboard.section_attachments": "Вкладення",
    "dashboard.attachments_line": (
        "Листи з вкладеннями: {with_att}/{total} – "
        "Орієнтовна загальна кількість вкладень: {total_att}"
    ),

    "dashboard.section_auth": "Автентифікація (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "Результати DKIM:",
    "dashboard.auth_header_spf": "Результати SPF:",
    "dashboard.auth_header_dmarc": "Результати DMARC:",

    "dashboard.section_integrity": "Цілісність / відсутні заголовки",
    "dashboard.integrity_flags_title": "Виявлені прапорці цілісності:",
    "dashboard.no_integrity_flags": "Специфічних прапорців цілісності не виявлено.",

    "dashboard.section_received": "Аномалії в ланцюжку Received",
    "dashboard.no_received_anomalies": (
        "Аномалій Received не виявлено (за поточними правилами)."
    ),

    # ------------------------------------------------------------------
    # Viewer tab – базові колонки
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "Папка IMAP",
    "viewer.col.sequence_number": "Секвенція",
    "viewer.col.date_header": "Дата",
    "viewer.col.from_header": "From",
    "viewer.col.to_header": "To",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Cci",
    "viewer.col.subject": "Тема",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "Вкладення?",
    "viewer.col.attachment_count": "К-ть вкладень",
    "viewer.col.attachment_filenames": "Імена вкладень",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (фрагмент)",
    "viewer.col.received_count": "К-ть Received",
    "viewer.col.received_anomalies": "Аномалії Received",
    "viewer.col.integrity_flags": "Прапорці цілісності",
    "viewer.col.relative_path": "Відносний шлях",
    "viewer.col.filename": "Ім’я файлу",

    # ------------------------------------------------------------------
    # Viewer tab – пошук + зони
    # ------------------------------------------------------------------
    "viewer.search_label": "Пошук:",
    "viewer.search_placeholder": "Фільтр по індексу (усі колонки)…",
    "viewer.search_clear": "Очистити",

    "viewer.headers_label": "Заголовки",
    "viewer.headers_placeholder": "Заголовки вибраного повідомлення…",

    "viewer.body_label": "Тіло (текст)",
    "viewer.body_placeholder": (
        "Тіло text/plain (або сирий HTML як запасний варіант) вибраного повідомлення…"
    ),

    "viewer.btn_load_last": "Використати останній експорт IMAP",
    "viewer.btn_open_csv": "Відкрити індекс CSV...",
    "viewer.attachments_label": "Вкладення",

    # ------------------------------------------------------------------
    # Viewer – помилки EML
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "Файл EML не знайдено",
    "viewer.error_missing_eml_body": (
        "Неможливо знайти файл EML на диску:\n{path}"
    ),
    "viewer.error_parse_eml_title": "Помилка читання EML",
    "viewer.error_parse_eml_body": (
        "Неможливо розібрати файл EML: {path}"
    ),

    # ------------------------------------------------------------------
    # Viewer – колонки вкладень
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "Назва",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "Розмір (байт)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "Підозріле?",

    "viewer.attach.yes": "Так",
    "viewer.attach.no": "Ні",

    # ------------------------------------------------------------------
    # IMAP tab – підключення та поля
    # ------------------------------------------------------------------
    "imap.group.connection": "Сервер IMAP (джерело доказів)",
    "imap.label.host": "Адреса сервера IMAP",
    "imap.label.user": "Ідентифікатор аналізованої скриньки",
    "imap.label.password": "Пароль (ніколи не зберігається)",
    "imap.label.date_start": "Дата початку (forensic-фільтр)",
    "imap.label.date_end": "Дата завершення (forensic-фільтр)",

    "imap.placeholder.host": "напр. imap.example.com",
    "imap.placeholder.user": "напр. incident@entreprise.be",
    "imap.placeholder.password": "Пароль аналізованого облікового запису",
    "imap.placeholder.date_start": "ДД/ММ/РРРР (необов’язково)",
    "imap.placeholder.date_end": "ДД/ММ/РРРР (необов’язково)",

    "imap.button.fetch_mailboxes": "Переглянути папки IMAP…",
    "imap.button.start_export": "Запустити forensic-екстракцію",
    "imap.button.cancel_export": "Скасувати екстракцію",

    "imap.label.mailboxes_title": (
        "Папки IMAP для екстракції (джерело доказів):"
    ),
    "imap.checkbox.select_all": "Вибрати всі папки",

    "imap.log.placeholder": (
        "Журнал екстракції IMAP (лише читання, з мітками часу)…"
    ),

    # ------------------------------------------------------------------
    # IMAP tab – загальні помилки / повідомлення
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "Неповні параметри",
    "imap.error.missing_fields.body": (
        "Будь ласка, вкажіть сервер IMAP, ідентифікатор та пароль."
    ),

    "imap.info.export_running.title": "Екстракція вже виконується",
    "imap.info.export_running.body": "Екстракція IMAP вже триває.",

    "imap.error.date_invalid.title": "Невірна дата",
    "imap.error.date_invalid.body": "Помилка у введених датах: {error}",
    "imap.error.date_end_before_start.body": (
        "Дата завершення не може бути раніше за дату початку."
    ),

    "imap.error.no_mailbox_selected.title": "Папки не вибрано",
    "imap.error.no_mailbox_selected.body": (
        "Будь ласка, виберіть принаймні одну папку IMAP для екстракції."
    ),

    "imap.error.fetch_mailboxes.title": "Помилка IMAP",
    "imap.error.fetch_mailboxes.body": (
        "Неможливо отримати список папок IMAP:\n{error}"
    ),

    "imap.info.generic.title": "Інформація",
    "imap.error.generic.title": "Помилка",

    # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "Підключення до {host}:{port} (SSL={use_ssl})...",
    "imap.log.connected": "Підключено до сервера IMAP.",
    "imap.log.select_folder": "Вибір папки «{folder}»...",
    "imap.log.folder_selected": "Папку «{folder}» вибрано.",
    "imap.log.message_count": "{count} повідомлень для експорту.",
    "imap.log.fetching": "Отримання повідомлень IMAP...",
    "imap.log.export_done": "Експорт IMAP завершено.",
    "imap.log.saving_to": "Збереження повідомлень до «{output_dir}»...",
    "imap.log.progress": "Експорт повідомлення {current}/{total}...",
    "imap.log.skip_existing": "Файл «{path}» уже існує, пропуск.",

    "imap.error.connect_failed": (
        "Неможливо підключитися до {host}:{port}: {error}"
    ),
    "imap.error.login_failed": "Помилка автентифікації IMAP: {error}",
    "imap.error.select_failed": (
        "Неможливо вибрати папку «{folder}»: {error}"
    ),
    "imap.error.fetch_failed": (
        "Помилка під час отримання повідомлень: {error}"
    ),
    "imap.error.generic": "Помилка під час експорту IMAP: {error}",

    # ------------------------------------------------------------------
    # IMAP - Звіт про експорт
    # ------------------------------------------------------------------
    "imap.report.title": "=== Звіт про експорт IMAP (лише читання) ===",
    "imap.report.tool_line": "Інструмент : eml_forensic_suite – експорт IMAP",
    "imap.report.version_line": "Версія      : {version}",
    "imap.report.folder_line": "Каталог     : {export_dir}",

    "imap.report.section_tool": "---- Інформація про інструмент ----",
    "imap.report.tool_path": "Шлях до інструмента    : {tool_path}",
    "imap.report.tool_hash": "SHA-256 інструмента    : {tool_hash}",

    "imap.report.section_env": "---- Середовище виконання ----",
    "imap.report.env_os": (
        "Операційна система     : {os_system} {os_release} "
        "({os_version}) / {machine}"
    ),
    "imap.report.env_python": "Версія Python          : {python_version}",

    "imap.report.section_context": "---- Контекст IMAP / облікового запису ----",
    "imap.report.context_host": "Сервер IMAP : {host}",
    "imap.report.context_user": "Обліковий запис : {user}",
    "imap.report.context_date_start": "Запитувана дата початку : {date_start}",
    "imap.report.context_date_end": "Запитувана дата завершення : {date_end}",
    "imap.report.context_criteria": (
        "Пошукові критерії IMAP : {search_criteria} (як надіслано на сервер)"
    ),

    "imap.report.selected_folders_title": "Вибрані папки:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- Інформація про сервер IMAP ----",
    "imap.report.server_greeting": "Банер IMAP  : {greeting}",
    "imap.report.server_capability": "CAPABILITY : {capability}",

    "imap.report.section_timestamps": "---- Часові мітки аналізу ----",
    "imap.report.timestamp_start_utc": "Початок аналізу (UTC)   : {dt}",
    "imap.report.timestamp_start_local": "Початок аналізу (локальний час) : {dt}",
    "imap.report.timestamp_end_utc": "Кінець аналізу (UTC)     : {dt}",
    "imap.report.timestamp_end_local": "Кінець аналізу (локальний час)  : {dt}",
    "imap.report.duration": "Загальна тривалість      : {duration}",

    "imap.report.section_folders": "---- Проаналізовані папки ----",
    "imap.report.folders_count": "Кількість вибраних папок : {count}",

    "imap.report.folder_header": "Папка : {name}",
    "imap.report.folder_messages": (
        "  Повідомлень, знайдених у періоді : {count}"
    ),
    "imap.report.folder_exported": "  Експортовано повідомлень       : {count}",
    "imap.report.folder_errors": "  Помилок отримання (fetch)      : {count}",
    "imap.report.folder_bytes": (
        "  Обсяг завантажених даних      : {bytes} байт"
    ),
    "imap.report.folder_size_stats": (
        "  Мін / макс / середній розмір  : {min_size} / {max_size} / {avg_size} байт"
    ),
    "imap.report.folder_period": (
        "  Період (INTERNALDATE)         : {first} → {last}"
    ),
    "imap.report.folder_error_uids": (
        "  UIDs з помилкою (неповний список) : {uids}"
    ),

    "imap.report.section_totals": "---- Загальні підсумки ----",
    "imap.report.total_messages": (
        "Повідомлень знайдено (усі папки) : {count}"
    ),
    "imap.report.total_exported": "Повідомлень експортовано          : {count}",
    "imap.report.total_errors": "Помилок отримання (fetch)         : {count}",
    "imap.report.total_bytes": "Загальний обсяг завантаження      : {bytes} байт",

    "imap.report.section_forensic": "---- Методологія та forensic-гарантії ----",
    "imap.report.forensic_item_readonly": (
        "- Інструмент використовував лише IMAP-команди в режимі читання "
        "(SELECT readonly, SEARCH, FETCH). Жодне повідомлення не було "
        "змінено, видалено чи позначено як прочитане під час аналізу."
    ),
    "imap.report.forensic_item_eml": (
        "- Повідомлення експортувалися в точності так, як надавав сервер IMAP, "
        "і записувалися на диск як файли .eml без зміни вмісту."
    ),
    "imap.report.forensic_item_hashes": (
        "- Кожне експортоване повідомлення має власний SHA-256-хеш "
        "у файлі hashes.txt, а також глобальний хеш, обчислений на основі "
        "конкатенації всіх індивідуальних хешів."
    ),
    "imap.report.forensic_item_report_hash": (
        "- Цей звіт аналізу також хешується за допомогою SHA-256, і цей хеш "
        "додається до hashes.txt для гарантії цілісності звіту."
    ),

    "imap.report.hashes_report_header": "ЗВІТ ПРО АНАЛІЗ:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Worker експортера (журнали, помилки, підсумок)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "Папки не вибрано.",
    "imap.worker.log_export_dir": "Каталог експорту: {export_dir}",
    "imap.worker.tool_hash_error": "(помилка під час обчислення хеша інструмента)",

    "imap.worker.log_connecting": "Підключення до сервера IMAP...",
    "imap.worker.greeting_not_available": "(банер IMAP недоступний)",
    "imap.worker.log_auth_classic": "Класична автентифікація IMAP...",
    "imap.worker.error_auth_failed": "Помилка автентифікації IMAP: {error}",
    "imap.worker.capability_error": (
        "(помилка під час виконання команди CAPABILITY)"
    ),

    "imap.worker.log_date_start_inclusive": (
        "Дата початку (включно): {date} → IMAP SINCE {imap_since}"
    ),
    "imap.worker.log_date_start_unset": (
        "Дата початку: не вказана → екстракція з першого доступного повідомлення."
    ),
    "imap.worker.date_start_unset_label": (
        "Перше доступне повідомлення (немає нижньої межі)"
    ),

    "imap.worker.log_date_end_inclusive": (
        "Дата завершення (включно): {date} → IMAP BEFORE {imap_before}"
    ),
    "imap.worker.log_date_end_unset": (
        "Дата завершення: не вказана → до останньої доступної дати на сервері."
    ),
    "imap.worker.date_end_unset_label": (
        "Останнє доступне повідомлення (немає верхньої межі)"
    ),

    "imap.worker.log_criteria": "Критерії IMAP, що використовуються: {criteria}",
    "imap.worker.log_selected_folders_header": "Вибрані папки ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": (
        "Зупинку запитано під час фази підрахунку."
    ),
    "imap.worker.log_phase1_count": (
        "[Фаза 1] Підрахунок повідомлень у {folder}..."
    ),
    "imap.worker.log_select_folder_failed": (
        "  ⚠️ Неможливо вибрати цю папку, перехід до наступної."
    ),
    "imap.worker.log_search_folder_failed": (
        "  ⚠️ Помилка під час пошуку в цій папці, перехід до наступної."
    ),
    "imap.worker.log_messages_to_process": (
        "  → {count} повідомлень до обробки в {folder}"
    ),

    "imap.worker.log_total_messages_to_download": (
        "Загальна кількість повідомлень для завантаження (усі папки): {count}"
    ),

    "imap.worker.log_stop_during_export": (
        "Запитано зупинку: екстракцію буде перервано."
    ),
    "imap.worker.log_folder_header": "=== Папка: {folder} ===",
    "imap.worker.log_no_messages_in_period": (
        "  У {folder} немає повідомлень за цей період."
    ),
    "imap.worker.log_folder_message_count": (
        "  Кількість повідомлень, знайдених у {folder}: {count}"
    ),
    "imap.worker.log_reselect_folder_failed": (
        "  ⚠️ Неможливо повторно вибрати цю папку, перехід до наступної."
    ),

    "imap.worker.log_first_message_download": (
        "  Завантаження першого повідомлення ({uid})..."
    ),
    "imap.worker.log_folder_progress": (
        "  Прогрес папки {folder}: {current}/{total} (останнє: {last_uid})"
    ),
    "imap.worker.log_fetch_error_message": (
        "    ⚠️ Помилка під час отримання повідомлення {uid}, продовжуємо."
    ),
    "imap.worker.log_folder_end": "  Кінець папки {folder}",

    "imap.worker.hashes_header": (
        "Список експортованих файлів та їх SHA-256-хешів"
    ),
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "ГЛОБАЛЬНИЙ ХЕШ (лише повідомлення):",

    "imap.worker.log_export_done_header": "=== Експорт завершено ===",
    "imap.worker.log_export_done_count": (
        "Загальна кількість експортованих повідомлень: {count}"
    ),
    "imap.worker.log_export_done_hashes_file": "Файл хешів: {path}",
    "imap.worker.log_export_done_hash": "Глобальний хеш: {file_hash}",

    "imap.worker.summary": (
        "Екстракцію завершено.\n\n"
        "Експортовані повідомлення: {count}\n"
        "Каталог: {export_dir}\n\n"
        "Глобальний хеш (повідомлення):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": (
        "Звіт аналізу згенеровано та захешовано "
        "(див. rapport_imap_export.txt та hashes.txt)."
    ),
    "imap.worker.log_report_failed": (
        "⚠️ Неможливо згенерувати звіт аналізу: {error}"
    ),

    "imap.worker.error_generic": "Сталася помилка: {error}",

    # ------------------------------------------------------------------
    # IMAP - Інтерфейс Tk (список папок)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "Підключення до сервера IMAP...",
    "imap.tk.log_auth_classic": "Класична автентифікація IMAP...",
    "imap.tk.error_list_mailboxes_failed": (
        "Неможливо отримати список папок IMAP."
    ),

    "imap.tk.log_folders_found_header": "Папки, знайдені на сервері:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "Усього папок IMAP: {count}",

    "imap.tk.msgbox_error_title": "Помилка",
    "imap.tk.msgbox_error_fetch_mailboxes": (
        "Помилка під час отримання папок IMAP: {error}"
    ),
    "imap.tk.log_error_fetch_mailboxes": (
        "❌ Помилка під час отримання папок: {error}"
    ),

    # ------------------------------------------------------------------
    # IMAP - Інтерфейс Tk (повна вкладка)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. Експорт IMAP",

    "imap.tk.label_server": "Сервер IMAP:",
    "imap.tk.label_email": "Адреса e-mail:",
    "imap.tk.label_password": "Пароль:",
    "imap.tk.label_date_start": "Дата початку (ДД/ММ/РРРР, необов’язкова):",
    "imap.tk.label_date_end": "Дата завершення (ДД/ММ/РРРР, необов’язкова):",
    "imap.tk.label_log": "Журнал:",
    "imap.tk.label_mailboxes": "Папки IMAP для експорту:",
    "imap.tk.checkbox.select_all": "Вибрати всі / зняти вибір",
    "imap.tk.label_progress": "Прогрес:",

    "imap.tk.msgbox_missing_fields_title": "Не всі поля заповнено",
    "imap.tk.msgbox_missing_fields_text": (
        "Будь ласка, заповніть сервер, електронну адресу та пароль."
    ),

    "imap.tk.log_fetch_mailboxes_start": "Отримання папок IMAP...",
    "imap.tk.log_no_mailboxes_or_error": (
        "Папок не знайдено або сталася помилка."
    ),
    "imap.tk.log_select_mailboxes_hint": (
        "Виберіть папки, які потрібно експортувати."
    ),

    "imap.tk.button_list_mailboxes": "Список папок IMAP",

    "imap.tk.msgbox_date_start_invalid_title": "Невірна дата початку",
    "imap.tk.msgbox_date_start_invalid_text": (
        "Дата початку має бути у форматі ДД/ММ/РРРР."
    ),

    "imap.tk.msgbox_date_end_invalid_title": "Невірна дата завершення",
    "imap.tk.msgbox_date_end_invalid_text": (
        "Дата завершення має бути у форматі ДД/ММ/РРРР."
    ),

    "imap.tk.msgbox_date_range_invalid_title": "Невірний діапазон дат",
    "imap.tk.msgbox_date_range_invalid_text": (
        "Дата завершення не може бути раніше за дату початку."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "Папки не вибрано",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "Будь ласка, виберіть принаймні одну папку IMAP "
        "(через «Список папок IMAP»)."
    ),

    "imap.tk.log_export_start": "Запуск експортy...",
    "imap.tk.button_run_export": "Запустити експорт (вибрані папки)",

    "imap.tk.log_stop_requested": (
        "Запитано зупинку, експорт буде коректно завершено..."
    ),
    "imap.tk.button_stop_export": "Зупинити експорт",

    "imap.tk.msgbox_export_done_title": "Експорт завершено",

    # ------------------------------------------------------------------
    # IMAP tab – журнали
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "Підключення до сервера IMAP для переліку папок…"
    ),
    "imap.log.fetch_error": "❌ Помилка під час отримання папок:",
    "imap.log.no_mailboxes": (
        "На цьому обліковому записі не знайдено жодної папки IMAP."
    ),
    "imap.log.mailboxes_found": "Папки, знайдені на сервері:",
    "imap.log.mailboxes_total": "Усього папок IMAP: {count}",
    "imap.log.mailboxes_select_hint": (
        "Виберіть папки для екстракції в режимі лише читання."
    ),
    "imap.log.start_export": (
        "Запуск екстракції IMAP (forensic-режим, лише для читання)…"
    ),
    "imap.log.cancel_requested": (
        "Запит на скасування надіслано worker-процесу IMAP…"
    ),
    "imap.log.export_dir_saved": "Каталог експорту збережено: {path}",
    "imap.log.done": "Обробку IMAP завершено.",

    # ------------------------------------------------------------------
    # Dashboard v3 – розділи / вкладки
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "Рівні підозрілості",
    "dashboard.tab_text": "Підсумок індексу EML",
    "dashboard.tab_graphs": "Графіки",
    "dashboard.section_charts": "Графічні візуалізації",

    "dashboard.chart_suspicion_title": "Розподіл за рівнями підозрілості",
    "dashboard.chart_folders_title": "Повідомлення за папками IMAP",
    "dashboard.chart_domains_title": "Найчастіші домени відправників",
    "dashboard.chart_attachments_title": "Наявність вкладень",
    "dashboard.chart_axis_count": "Кількість",
    "dashboard.chart_attachments_with": "З вкладеннями",
    "dashboard.chart_attachments_without": "Без вкладень",

    # Легенда / текст навколо scoring
    "dashboard.suspicion_distribution_line": (
        "Розподіл листів за рівнем підозрілості:"
    ),
    "dashboard.suspicion_level.LOW": "Низький",
    "dashboard.suspicion_level.MEDIUM": "Середній",
    "dashboard.suspicion_level.HIGH": "Високий",
    "dashboard.suspicion_level.CRITICAL": "Критичний",
    "dashboard.suspicion_level.UNKNOWN": "Невідомий",

    # Графіки – заголовки (нова номенклатура)
    "dashboard.chart.folders.title": "Листи за папками IMAP",
    "dashboard.chart.domains.title": "ТОП доменів відправників",
    "dashboard.chart.attachments.title": "Наявність вкладень",
    "dashboard.chart.auth.title": "Результати DKIM / SPF / DMARC",
    "dashboard.chart.suspicion.title": (
        "Розподіл за рівнем підозрілості"
    ),

    # Графіки – підписи / стани
    "dashboard.chart.no_data": (
        "Недостатньо даних для побудови цього графіка."
    ),
    "dashboard.chart.axis.emails": "Кількість листів",
    "dashboard.chart.axis.folders": "Папки IMAP",
    "dashboard.chart.axis.domains": "Домени",
    "dashboard.chart.axis.levels": "Рівні",
    "dashboard.section_suspicion": "Бали підозрілості",
    "dashboard.suspicion_scores_line": (
        "Глобальний бал підозрілості: мін {score_min}, "
        "макс {score_max}, середній {score_avg:.1f}"
    ),
    "dashboard.suspicion_levels_title": (
        "Розподіл за рівнями підозрілості"
    ),
    "dashboard.no_suspicion_data": (
        "Немає доступних даних про підозрілість."
    ),
    "dashboard.no_suspicion_levels": (
        "Не виявлено окремих рівнів підозрілості."
    ),
    "dashboard.suspicion_unknown": "Невідомий / не обчислено",
    "dashboard.chart_folders_serie": "Листи за папкою",
    "dashboard.chart_domains_serie": "Листи за доменом",

    # Візуальна підказка щодо кольорів
    "dashboard.legend.safe": "Зона, що вважається переважно безпечною",
    "dashboard.legend.suspicious": "Зона для пріоритетної перевірки",

    # ------------------------------------------------------------------
    # Viewer – колонки scoring та підозрілості
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "Бал підозрілості",
    "viewer.col.suspicion_level": "Рівень",
    "viewer.col.suspicion_reasons": "Причини (коротко)",

    # Підказки scoring
    "viewer.score.tooltip.base": (
        "Глобальний бал підозрілості обчислюється за DKIM/SPF/DMARC, "
        "аномаліями Received, цілісністю заголовків та вкладеннями."
    ),
    "viewer.score.level.LOW": (
        "Низька підозрілість: за поточними правилами нічого "
        "аномального не виявлено."
    ),
    "viewer.score.level.MEDIUM": (
        "Середня підозрілість: є певні елементи для перевірки "
        "(заголовки, автентифікація або вкладення)."
    ),
    "viewer.score.level.HIGH": (
        "Висока підозрілість: кілька технічних індикаторів "
        "є несумісними або небезпечними."
    ),
    "viewer.score.level.CRITICAL": (
        "Критична підозрілість: імовірно, лист є зловмисним або підробленим."
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth / обмеження постачальників
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "Схоже, що цей обліковий запис керується постачальником, який "
        "вимагає використання сучасних механізмів (OAuth2, офіційні "
        "засоби експорту) для доступу до повідомлень "
        "(наприклад, Gmail, Outlook/Microsoft 365, Yahoo).\n\n"
        "З міркувань відповідності та щоб не обходити ці правила, "
        "ця версія eml_forensic_suite не виконує прямий експорт IMAP "
        "для таких сервісів.\n\n"
        "Щоб отримати повідомлення сумісним способом:\n"
        "  • Gmail: використовуйте Google Takeout для експорту скриньки (MBOX)\n"
        "    або клієнт на кшталт Thunderbird для створення локальної копії.\n"
        "  • Outlook / Microsoft 365: використовуйте експорт вашого клієнта Outlook\n"
        "    (PST) або засоби архівації вашої організації.\n"
        "  • Yahoo тощо: використовуйте засоби експорту, що надає постачальник.\n\n"
        "Майбутні версії eml_forensic_suite будуть здатні аналізувати ці експорти "
        "(MBOX, PST тощо) безпосередньо, щоб залишатися сумісними з цими платформами."
    ),

    # ------------------------------------------------------------------
    # Viewer – міні-мова пошуку
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "Forensic-міні-мова:\n"
        "  from:alice@example.com\n"
        "  domain:banque.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "Оператори: неявний AND, OR, NOT, дужки."
    ),

    # ------------------------------------------------------------------
    # Viewer – CSV / загальні повідомлення індексу
    # ------------------------------------------------------------------
    "viewer.no_index_title": "Індекс недоступний",
    "viewer.no_index_body": (
        "У цій сесії індекс недоступний.\n"
        "Згенеруйте індекс у вкладці 2 або відкрийте CSV вручну."
    ),
    "viewer.open_csv_title": "Відкрити файл індексу CSV",
    "viewer.error_csv_title": "Помилка читання CSV",
    "viewer.error_csv_body": (
        "Неможливо прочитати файл CSV: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – попередній перегляд (фінальна версія, лише читання)
    # ------------------------------------------------------------------
    "viewer.attach.preview": "Попередній перегляд (тільки читання)",
    "viewer.attach.preview_failed_title": "Не вдалося відобразити попередній перегляд",
    "viewer.attach.preview_failed_body": (
        "Неможливо показати попередній перегляд цього вкладення."
    ),
    "viewer.attach.preview_unsupported_title": "Непідтримуваний тип",
    "viewer.attach.preview_unsupported_body": (
        "Немає вбудованого перегляду для цього типу MIME: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – екстракція вкладень (фінальна версія)
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "Немає повідомлення",
    "viewer.attach.no_msg_body": (
        "Наразі жодне повідомлення не вибрано."
    ),
    "viewer.attach.no_selection_title": "Вкладення не вибрано",
    "viewer.attach.no_selection_body": (
        "Будь ласка, виберіть вкладення у списку."
    ),
    "viewer.attach.no_root_title": "Робочий каталог не знайдено",
    "viewer.attach.no_root_body": (
        "Каталог forensic / індексу не налаштовано для екстракції."
    ),
    "viewer.attach.extract_one_title": "Вкладення експортовано",
    "viewer.attach.extract_one_body": (
        "Вкладення експортовано до:\n{path}"
    ),
    "viewer.attach.extract_all_title": "Вкладення експортовано",
    "viewer.attach.extract_all_body": (
        "{count} вкладень було експортовано:\n{paths}"
    ),

    # ------------------------------------------------------------------
    # Дії з вкладеннями (кнопки)
    # ------------------------------------------------------------------
    "viewer.attach.extract_one": "Експортувати вибране вкладення",
    "viewer.attach.extract_all": "Експортувати всі вкладення",

    # ------------------------------------------------------------------
    # OAuth діалог
    # ------------------------------------------------------------------
    "oauth.title": "Підключення OAuth2",
    "oauth.choose_provider": (
        "Виберіть провайдера для автентифікації OAuth2:"
    ),
    "oauth.btn_google": "Google (Gmail / Workspace)",
    "oauth.btn_microsoft": "Microsoft 365 / Outlook",
    "oauth.btn_yahoo": "Yahoo Mail",
    "common.cancel": "Скасувати",

    "oauth.generic_title": "OAuth2",
    "oauth.google.success": "Успішне підключення через Google OAuth2.",
    "oauth.microsoft.success": "Успішне підключення через Microsoft OAuth2.",
    "oauth.yahoo.success": "Успішне підключення через Yahoo OAuth2.",
    "oauth.google.error_title": "Помилка Google OAuth2",
    "oauth.microsoft.error_title": "Помилка Microsoft OAuth2",
    "oauth.yahoo.error_title": "Помилка Yahoo OAuth2",

    # ------------------------------------------------------------------
    # Вікно «Про програму»
    # ------------------------------------------------------------------
    "about.version_label": "Версія:",
    "about.description": (
        "Інструмент лише для читання для forensic-аналізу листів EML/IMAP."
    ),
}
