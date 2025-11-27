from __future__ import annotations

from typing import Dict

TRANSLATIONS_RU: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "EML / IMAP Forensic Suite (только чтение)",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "Файл",
    "menu.view": "Вид",
    "menu.help": "Справка",

    "menu.file.settings": "Настройки…",
    "menu.file.quit": "Выход",

    "menu.view.theme.dark": "Тёмная тема",
    "menu.view.theme.light": "Светлая тема",

    "menu.help.about": "О программе…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. Экспорт IMAP",
    "tab.index": "2. Индексация EML",
    "tab.viewer": "3. Forensic-просмотр",
    "tab.dashboard": "4. Forensic-панель",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "Настройки",
    "settings.reports_dir.label": "Рабочий / отчётный каталог:",
    "settings.reports_dir.browse": "Обзор…",
    "settings.language.label": "Язык интерфейса:",
    "settings.reports_dir.dialog_title": "Выберите рабочий / отчётный каталог",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "Готово.",
    "status.settings.saved": "Настройки сохранены.",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "Каталог экспорта EML:",
    "index.browse": "Обзор…",
    "index.use_last_export": "Использовать последний IMAP-экспорт",
    "index.log_placeholder": "Журнал индексации EML (только чтение)…",
    "index.start_button": "Начать индексацию EML",
    "index.dialog_select_folder": "Выберите каталог экспорта EML",
    "index.no_last_export": "Ещё нет IMAP-экспорта (вкладка 1).",
    "index.error_already_running_title": "Индексация уже выполняется",
    "index.error_already_running_body": "Операция индексации EML уже запущена.",
    "index.error_no_folder_title": "Каталог не указан",
    "index.error_no_folder_body": "Пожалуйста, выберите каталог, содержащий файлы .eml.",
    "index.error_invalid_folder_title": "Недействительный каталог",
    "index.error_invalid_folder_body": "Указанный каталог не существует:\n{folder}",
    "index.status_selected_folder": "Выбранный каталог для индексации: {folder}",
    "index.error_indexing_title": "Ошибка при индексации",
    "index.error_log": "❌ Ошибка: {error}",
    "index.done_log_success": "\nИндексация успешно завершена.",
    "index.done_log_path": "Путь к CSV: {csv_path}",
    "index.done_log_count": "Количество проиндексированных записей: {count}",
    "index.done_msg_title": "Индексация завершена",
    "index.done_msg_body": (
        "Индексация EML завершена.\n\nCSV-файл: {csv_path}\nЗаписей: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "Использовать последний индекс",
    "dashboard.open_csv": "Открыть CSV-индекса…",
    "dashboard.placeholder": "Forensic-сводка на основе индекса EML…",
    "dashboard.source_memory": "Источник: индекс в памяти (последняя индексация в этой сессии).",
    "dashboard.source_csv": "Источник: {path}",
    "dashboard.no_index_title": "Нет индекса",
    "dashboard.no_index_body": (
        "В этой сессии индекс отсутствует.\n"
        "Создайте индекс на вкладке 2 или откройте CSV вручную."
    ),
    "dashboard.dialog_open_csv": "Открыть CSV-файл индекса",
    "dashboard.error_csv_missing_title": "Файл не найден",
    "dashboard.error_csv_missing_body": "Указанный файл не существует:\n{path}",
    "dashboard.error_csv_read_title": "Ошибка чтения CSV",
    "dashboard.error_csv_read_body": "Невозможно прочитать CSV-файл: {path}",
    "dashboard.empty_csv_title": "Пустой индекс",
    "dashboard.empty_csv_body": "CSV-файл не содержит полезных записей.",
    "dashboard.no_data": "Нет данных для анализа.",

    "dashboard.section_overview": "Обзор",
    "dashboard.overview_line": (
        "Всего писем: {total} – Уникальных отправителей: {senders}"
    ),
    "dashboard.dates_line": "Период охвата: {date_min} → {date_max}",
    "dashboard.dates_unknown": "Даты недоступны или не распознаны.",

    "dashboard.section_folders": "Распределение по папкам IMAP",
    "dashboard.no_folders": "Папки IMAP не обнаружены.",

    "dashboard.section_domains": "Распределение по доменам отправителей",
    "dashboard.no_domains": "Домены не обнаружены.",

    "dashboard.section_attachments": "Вложения",
    "dashboard.attachments_line": (
        "Писем с вложениями: {with_att}/{total} – Оценочное количество вложений: {total_att}"
    ),

    "dashboard.section_auth": "Аутентификация (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "Результаты DKIM:",
    "dashboard.auth_header_spf": "Результаты SPF:",
    "dashboard.auth_header_dmarc": "Результаты DMARC:",

    "dashboard.section_integrity": "Целостность / отсутствующие заголовки",
    "dashboard.integrity_flags_title": "Обнаруженные признаки нарушения целостности:",
    "dashboard.no_integrity_flags": "Нарушений целостности не обнаружено.",

    "dashboard.section_received": "Аномалии в цепочке Received",
    "dashboard.no_received_anomalies": (
        "Аномалии в Received не обнаружены (по текущим правилам)."
    ),

    # ------------------------------------------------------------------
    # Viewer tab – base columns
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "Папка IMAP",
    "viewer.col.sequence_number": "№",
    "viewer.col.date_header": "Дата",
    "viewer.col.from_header": "От",
    "viewer.col.to_header": "Кому",
    "viewer.col.cc_header": "Копия",
    "viewer.col.cci_header": "Скрытая копия",
    "viewer.col.subject": "Тема",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "Вложения?",
    "viewer.col.attachment_count": "Кол-во вложений",
    "viewer.col.attachment_filenames": "Имена вложений",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (фрагмент)",
    "viewer.col.received_count": "Кол-во Received",
    "viewer.col.received_anomalies": "Аномалии Received",
    "viewer.col.integrity_flags": "Флаги целостности",
    "viewer.col.relative_path": "Относительный путь",
    "viewer.col.filename": "Имя файла",

    # ------------------------------------------------------------------
    # Viewer – search + zones
    # ------------------------------------------------------------------
    "viewer.search_label": "Поиск:",
    "viewer.search_placeholder": "Фильтр по индексу (все колонки)…",
    "viewer.search_clear": "Очистить",

    "viewer.headers_label": "Заголовки",
    "viewer.headers_placeholder": "Заголовки выбранного сообщения…",

    "viewer.body_label": "Тело сообщения (текст)",
    "viewer.body_placeholder": (
        "text/plain тело (или HTML как резервный вариант)…"
    ),

    "viewer.btn_load_last": "Использовать последний IMAP-экспорт",
    "viewer.btn_open_csv": "Открыть CSV-индекса…",
    "viewer.attachments_label": "Вложения",

    # ------------------------------------------------------------------
    # Viewer – EML errors
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "Файл EML не найден",
    "viewer.error_missing_eml_body": "Невозможно найти файл EML по пути:\n{path}",
    "viewer.error_parse_eml_title": "Ошибка чтения EML",
    "viewer.error_parse_eml_body": "Невозможно разобрать файл EML: {path}",

    # ------------------------------------------------------------------
    # Viewer – attachment columns
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "Имя",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "Размер (байт)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "Подозрительно?",

    "viewer.attach.yes": "Да",
    "viewer.attach.no": "Нет",

    # ------------------------------------------------------------------
    # IMAP tab – connection fields
    # ------------------------------------------------------------------
    "imap.group.connection": "IMAP-сервер (источник доказательств)",
    "imap.label.host": "Адрес IMAP-сервера",
    "imap.label.user": "Идентификатор анализируемого ящика",
    "imap.label.password": "Пароль (не сохраняется)",
    "imap.label.date_start": "Дата начала (forensic-фильтр)",
    "imap.label.date_end": "Дата конца (forensic-фильтр)",

    "imap.placeholder.host": "например imap.example.com",
    "imap.placeholder.user": "например incident@company.com",
    "imap.placeholder.password": "Пароль анализируемого аккаунта",
    "imap.placeholder.date_start": "ДД/ММ/ГГГГ (необязательно)",
    "imap.placeholder.date_end": "ДД/ММ/ГГГГ (необязательно)",

    "imap.button.fetch_mailboxes": "Просмотреть папки IMAP…",
    "imap.button.start_export": "Начать forensic-экстракцию",
    "imap.button.cancel_export": "Отменить экстракцию",

    "imap.label.mailboxes_title": (
        "Папки IMAP для извлечения (источник доказательств):"
    ),
    "imap.checkbox.select_all": "Выбрать все папки",

    "imap.log.placeholder": (
        "Журнал IMAP-экстракции (только чтение, с метками времени)…"
    ),

    # ------------------------------------------------------------------
    # IMAP – generic errors
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "Настройки неполные",
    "imap.error.missing_fields.body": (
        "Укажите сервер IMAP, имя пользователя и пароль."
    ),

    "imap.info.export_running.title": "Экстракция уже выполняется",
    "imap.info.export_running.body": "Экстракция IMAP уже запущена.",

    "imap.error.date_invalid.title": "Неверная дата",
    "imap.error.date_invalid.body": "Ошибка в указанных датах: {error}",
    "imap.error.date_end_before_start.body": (
        "Дата окончания не может быть раньше даты начала."
    ),

    "imap.error.no_mailbox_selected.title": "Папки не выбраны",
    "imap.error.no_mailbox_selected.body": (
        "Выберите хотя бы одну папку IMAP для извлечения."
    ),

    "imap.error.fetch_mailboxes.title": "Ошибка IMAP",
    "imap.error.fetch_mailboxes.body": (
        "Невозможно получить список папок IMAP:\n{error}"
    ),

    "imap.info.generic.title": "Информация",
    "imap.error.generic.title": "Ошибка",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "Подключение к {host}:{port} (SSL={use_ssl})...",
    "imap.log.connected": "Подключено к серверу IMAP.",
    "imap.log.select_folder": "Выбор папки \"{folder}\"...",
    "imap.log.folder_selected": "Папка \"{folder}\" выбрана.",
    "imap.log.message_count": "{count} сообщений для экспорта.",
    "imap.log.fetching": "Получение сообщений IMAP...",
    "imap.log.export_done": "Экспорт IMAP завершён.",
    "imap.log.saving_to": "Сохранение сообщений в \"{output_dir}\"...",
    "imap.log.progress": "Экспорт сообщения {current}/{total}...",
    "imap.log.skip_existing": "Файл \"{path}\" уже существует, пропуск.",

    "imap.error.connect_failed": "Не удалось подключиться к {host}:{port}: {error}",
    "imap.error.login_failed": "Ошибка аутентификации IMAP: {error}",
    "imap.error.select_failed": "Не удалось выбрать папку \"{folder}\": {error}",
    "imap.error.fetch_failed": "Ошибка при получении сообщений: {error}",
    "imap.error.generic": "Ошибка во время экспорта IMAP: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== Отчёт об экспорте IMAP (только чтение) ===",
    "imap.report.tool_line": "Инструмент : eml_forensic_suite – экспорт IMAP",
    "imap.report.version_line": "Версия    : {version}",
    "imap.report.folder_line": "Каталог   : {export_dir}",

    "imap.report.section_tool": "---- Сведения об инструменте ----",
    "imap.report.tool_path": "Путь к инструменту    : {tool_path}",
    "imap.report.tool_hash": "SHA-256 инструмента   : {tool_hash}",

    "imap.report.section_env": "---- Исполняемая среда ----",
    "imap.report.env_os": "Операционная система  : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Версия Python         : {python_version}",

    "imap.report.section_context": "---- Контекст IMAP / учётной записи ----",
    "imap.report.context_host": "Сервер IMAP : {host}",
    "imap.report.context_user": "Учётная запись : {user}",
    "imap.report.context_date_start": "Запрошенная дата начала : {date_start}",
    "imap.report.context_date_end": "Запрошенная дата окончания : {date_end}",
    "imap.report.context_criteria": "Критерии поиска IMAP : {search_criteria} (как отправлено серверу)",

    "imap.report.selected_folders_title": "Выбранные папки:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- Сведения о сервере IMAP ----",
    "imap.report.server_greeting": "Баннер IMAP   : {greeting}",
    "imap.report.server_capability": "CAPABILITY    : {capability}",

    "imap.report.section_timestamps": "---- Временные метки анализа ----",
    "imap.report.timestamp_start_utc": "Начало анализа (UTC)       : {dt}",
    "imap.report.timestamp_start_local": "Начало анализа (местное)   : {dt}",
    "imap.report.timestamp_end_utc": "Окончание анализа (UTC)    : {dt}",
    "imap.report.timestamp_end_local": "Окончание анализа (местное): {dt}",
    "imap.report.duration": "Общая продолжительность     : {duration}",

    "imap.report.section_folders": "---- Проанализированные папки ----",
    "imap.report.folders_count": "Количество выбранных папок : {count}",

    "imap.report.folder_header": "Папка : {name}",
    "imap.report.folder_messages": "  Найдено сообщений (за период) : {count}",
    "imap.report.folder_exported": "  Экспортировано сообщений      : {count}",
    "imap.report.folder_errors": "  Ошибок при получении          : {count}",
    "imap.report.folder_bytes": "  Загруженный объём             : {bytes} байт",
    "imap.report.folder_size_stats": "  Мин/макс/средний размер       : {min_size} / {max_size} / {avg_size} байт",
    "imap.report.folder_period": "  Охватываемый период (INTERNALDATE) : {first} → {last}",
    "imap.report.folder_error_uids": "  UID с ошибками (неисчерпывающий список) : {uids}",

    "imap.report.section_totals": "---- Общие итоги ----",
    "imap.report.total_messages": "Найдено сообщений (все папки) : {count}",
    "imap.report.total_exported": "Экспортировано сообщений      : {count}",
    "imap.report.total_errors": "Ошибок получения              : {count}",
    "imap.report.total_bytes": "Общий объём загруженных данных: {bytes} байт",

    "imap.report.section_forensic": "---- Методология и гарантии судебной экспертизы ----",
    "imap.report.forensic_item_readonly": "- Инструмент использовал только команды IMAP в режиме только чтения (SELECT readonly, SEARCH, FETCH). Во время анализа ни одно сообщение не было изменено, удалено или помечено как прочитанное.",
    "imap.report.forensic_item_eml": "- Сообщения экспортировались в точности в том виде, как их предоставил сервер IMAP, и записывались на диск как файлы .eml без изменения содержимого.",
    "imap.report.forensic_item_hashes": "- С каждым экспортированным сообщением связан хэш SHA-256, указанный в hashes.txt, а также глобальный хэш, вычисленный по конкатенации всех отдельных хэшей.",
    "imap.report.forensic_item_report_hash": "- Сам настоящий отчёт об анализе также хэшируется с помощью SHA-256, и этот хэш добавляется в hashes.txt для гарантии целостности отчёта.",

    "imap.report.hashes_report_header": "ОТЧЁТ ОБ АНАЛИЗЕ:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "Папка не выбрана.",
    "imap.worker.log_export_dir": "Каталог экспорта: {export_dir}",
    "imap.worker.tool_hash_error": "(ошибка при вычислении хэша инструмента)",

    "imap.worker.log_connecting": "Подключение к серверу IMAP...",
    "imap.worker.greeting_not_available": "(баннер IMAP недоступен)",
    "imap.worker.log_auth_classic": "Классическая аутентификация IMAP...",
    "imap.worker.error_auth_failed": "Ошибка аутентификации IMAP: {error}",
    "imap.worker.capability_error": "(ошибка при выполнении команды CAPABILITY)",

    "imap.worker.log_date_start_inclusive": "Дата начала (включительно): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "Дата начала: не задана → извлечение с самого первого доступного сообщения.",
    "imap.worker.date_start_unset_label": "Первое доступное сообщение (нет нижней границы)",

    "imap.worker.log_date_end_inclusive": "Дата окончания (включительно): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "Дата окончания: не задана → до самой последней даты, доступной на сервере.",
    "imap.worker.date_end_unset_label": "Последнее доступное сообщение (нет верхней границы)",

    "imap.worker.log_criteria": "Используемые критерии поиска IMAP: {criteria}",
    "imap.worker.log_selected_folders_header": "Выбранные папки ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "Во время фазы подсчёта запрошена остановка.",
    "imap.worker.log_phase1_count": "[Фаза 1] Подсчёт сообщений в {folder}...",
    "imap.worker.log_select_folder_failed": "  ⚠️ Не удалось выбрать эту папку, пропуск.",
    "imap.worker.log_search_folder_failed": "  ⚠️ Ошибка при поиске в этой папке, пропуск.",
    "imap.worker.log_messages_to_process": "  → {count} сообщений для обработки в {folder}",

    "imap.worker.log_total_messages_to_download": "Общее количество сообщений для загрузки (все папки): {count}",

    "imap.worker.log_stop_during_export": "Запрошена остановка: экспорт прерывается.",
    "imap.worker.log_folder_header": "=== Папка: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  В {folder} нет сообщений за указанный период.",
    "imap.worker.log_folder_message_count": "  Количество найденных сообщений в {folder}: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ Не удалось повторно выбрать эту папку, пропуск.",

    "imap.worker.log_first_message_download": "  Загрузка первого сообщения ({uid})...",
    "imap.worker.log_folder_progress": "  Ход обработки папки {folder}: {current}/{total} (последнее: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ Ошибка при получении сообщения {uid}, продолжаем.",
    "imap.worker.log_folder_end": "  Конец обработки папки {folder}",

    "imap.worker.hashes_header": "Список экспортированных файлов и их хэшей SHA-256",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "ГЛОБАЛЬНЫЙ ХЭШ (только сообщения):",

    "imap.worker.log_export_done_header": "=== Экспорт завершён ===",
    "imap.worker.log_export_done_count": "Общее количество экспортированных сообщений: {count}",
    "imap.worker.log_export_done_hashes_file": "Файл с хэшами: {path}",
    "imap.worker.log_export_done_hash": "Глобальный хэш: {file_hash}",

    "imap.worker.summary": (
        "Экспорт завершён.\n\n"
        "Экспортировано сообщений: {count}\n"
        "Каталог: {export_dir}\n\n"
        "Глобальный хэш (сообщения):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "Отчёт анализа создан и захэширован (см. rapport_imap_export.txt и hashes.txt).",
    "imap.worker.log_report_failed": "⚠️ Не удалось создать отчёт анализа: {error}",

    "imap.worker.error_generic": "Произошла ошибка: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "Подключение к серверу IMAP...",
    "imap.tk.log_auth_classic": "Классическая аутентификация IMAP...",
    "imap.tk.error_list_mailboxes_failed": "Не удалось получить список папок IMAP.",

    "imap.tk.log_folders_found_header": "Найденные на сервере папки:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "Всего папок IMAP: {count}",

    "imap.tk.msgbox_error_title": "Ошибка",
    "imap.tk.msgbox_error_fetch_mailboxes": "Ошибка при получении папок IMAP: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ Ошибка при получении папок: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. Экспорт IMAP",

    "imap.tk.label_server": "Сервер IMAP:",
    "imap.tk.label_email": "Адрес электронной почты:",
    "imap.tk.label_password": "Пароль:",
    "imap.tk.label_date_start": "Дата начала (ДД/ММ/ГГГГ, необязательно):",
    "imap.tk.label_date_end": "Дата окончания (ДД/ММ/ГГГГ, необязательно):",
    "imap.tk.label_log": "Журнал:",
    "imap.tk.label_mailboxes": "Папки IMAP для экспорта:",
    "imap.tk.checkbox_select_all": "Выбрать всё / Снять выбор",
    "imap.tk.label_progress": "Прогресс:",

    "imap.tk.msgbox_missing_fields_title": "Отсутствующие поля",
    "imap.tk.msgbox_missing_fields_text": "Пожалуйста, укажите сервер, адрес электронной почты и пароль.",

    "imap.tk.log_fetch_mailboxes_start": "Получение папок IMAP...",
    "imap.tk.log_no_mailboxes_or_error": "Папки не найдены или произошла ошибка.",
    "imap.tk.log_select_mailboxes_hint": "Выберите папки для экспорта.",

    "imap.tk.button_list_mailboxes": "Показать папки IMAP",

    "imap.tk.msgbox_date_start_invalid_title": "Неверная дата начала",
    "imap.tk.msgbox_date_start_invalid_text": "Дата начала должна быть в формате ДД/ММ/ГГГГ.",

    "imap.tk.msgbox_date_end_invalid_title": "Неверная дата окончания",
    "imap.tk.msgbox_date_end_invalid_text": "Дата окончания должна быть в формате ДД/ММ/ГГГГ.",

    "imap.tk.msgbox_date_range_invalid_title": "Неверный диапазон дат",
    "imap.tk.msgbox_date_range_invalid_text": (
        "Конечная дата не может быть раньше начальной."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "Папка не выбрана",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "Пожалуйста, выберите как минимум одну папку IMAP (через «Показать папки IMAP»)."
    ),

    "imap.tk.log_export_start": "Запуск экспорта...",
    "imap.tk.button_run_export": "Запустить экспорт (выбранные папки)",

    "imap.tk.log_stop_requested": (
        "Получен запрос на остановку, экспорт будет корректно завершён..."
    ),
    "imap.tk.button_stop_export": "Остановить экспорт",

    "imap.tk.msgbox_export_done_title": "Экспорт завершён",


    # ------------------------------------------------------------------
    # IMAP – logs
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "Подключение к IMAP-серверу для перечисления папок…"
    ),
    "imap.log.fetch_error": "❌ Ошибка при получении папок:",
    "imap.log.no_mailboxes": "На этом аккаунте папок IMAP не найдено.",
    "imap.log.mailboxes_found": "Папки, найденные на сервере:",
    "imap.log.mailboxes_total": "Всего папок IMAP: {count}",
    "imap.log.mailboxes_select_hint": (
        "Выберите папки для извлечения в режиме только чтение."
    ),
    "imap.log.start_export": (
        "Начинается forensic-экстракция IMAP (режим только чтение)…"
    ),
    "imap.log.cancel_requested": (
        "Запрос на отмену отправлен рабочему IMAP…"
    ),
    "imap.log.export_dir_saved": "Каталог экспорта сохранён: {path}",
    "imap.log.done": "Обработка IMAP завершена.",

    # ------------------------------------------------------------------
    # Dashboard v3 – charts & scoring
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "Уровни подозрительности",
    "dashboard.tab_text": "Сводка индекса EML",
    "dashboard.tab_graphs": "Графики",
    "dashboard.section_charts": "Графические представления",

    "dashboard.chart_suspicion_title": "Распределение уровней подозрительности",
    "dashboard.chart_folders_title": "Письма по папкам IMAP",
    "dashboard.chart_domains_title": "Топ доменов отправителей",
    "dashboard.chart_attachments_title": "Наличие вложений",
    "dashboard.chart_axis_count": "Количество",
    "dashboard.chart_attachments_with": "С вложениями",
    "dashboard.chart_attachments_without": "Без вложений",

    "dashboard.suspicion_distribution_line": (
        "Распределение писем по уровням подозрительности:"
    ),
    "dashboard.suspicion_level.LOW": "Низкий",
    "dashboard.suspicion_level.MEDIUM": "Средний",
    "dashboard.suspicion_level.HIGH": "Высокий",
    "dashboard.suspicion_level.CRITICAL": "Критический",
    "dashboard.suspicion_level.UNKNOWN": "Неизвестно",

    "dashboard.chart.folders.title": "Письма по папкам IMAP",
    "dashboard.chart.domains.title": "Топ доменов отправителей",
    "dashboard.chart.attachments.title": "Наличие вложений",
    "dashboard.chart.auth.title": "Результаты DKIM / SPF / DMARC",
    "dashboard.chart.suspicion.title": "Распределение уровней подозрительности",

    "dashboard.chart.no_data": (
        "Недостаточно данных для отображения диаграммы."
    ),
    "dashboard.chart.axis.emails": "Количество писем",
    "dashboard.chart.axis.folders": "Папки IMAP",
    "dashboard.chart.axis.domains": "Домены",
    "dashboard.chart.axis.levels": "Уровни",

    "dashboard.legend.safe": "Область, считающаяся относительно безопасной",
    "dashboard.legend.suspicious": "Зона первоочередного анализа",

    # ------------------------------------------------------------------
    # Viewer – scoring columns
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "Счёт подозрительности",
    "viewer.col.suspicion_level": "Уровень",
    "viewer.col.suspicion_reasons": "Причины (кратко)",

    "viewer.score.tooltip.base": (
        "Глобальный счёт подозрительности, рассчитанный по DKIM/SPF/DMARC, "
        "аномалиям Received, целостности заголовков и вложениям."
    ),
    "viewer.score.level.LOW": (
        "Низкий уровень подозрительности: ничего необычного не обнаружено."
    ),
    "viewer.score.level.MEDIUM": (
        "Средний уровень: некоторые элементы требуют проверки "
        "(заголовки, аутентификация или вложения)."
    ),
    "viewer.score.level.HIGH": (
        "Высокий уровень: несколько технических индикаторов несогласованы или опасны."
    ),
    "viewer.score.level.CRITICAL": (
        "Критический уровень: письмо, вероятно, вредоносное или поддельное."
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth restrictions
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "Похоже, что этот аккаунт управляется провайдером, "
        "требующим современных механизмов доступа (OAuth2, официальные экспорты), "
        "например Gmail, Outlook/Microsoft 365, Yahoo.\n\n"
        "Чтобы соблюдать требования, эта версия eml_forensic_suite "
        "не выполняет прямую IMAP-экстракцию для таких сервисов.\n\n"
        "Чтобы получить сообщения корректным способом:\n"
        "  • Gmail: используйте Google Takeout (MBOX) или Thunderbird.\n"
        "  • Outlook / Microsoft 365: экспорт через Outlook (PST)\n"
        "    или инструменты архивирования вашей организации.\n"
        "  • Yahoo и др.: используйте инструменты экспорта провайдера.\n\n"
        "В будущих версиях будет предусмотрен анализ MBOX, PST и других форматов."
    ),

    # ------------------------------------------------------------------
    # Viewer – search mini language
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "Forensic мини-язык:\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "Операторы: неявный AND, OR, NOT, скобки."
    ),

    # ------------------------------------------------------------------
    # Viewer – index generic messages
    # ------------------------------------------------------------------
    "viewer.no_index_title": "Индекс недоступен",
    "viewer.no_index_body": (
        "В этой сессии индекс отсутствует.\n"
        "Создайте индекс на вкладке 2 или откройте CSV вручную."
    ),
    "viewer.open_csv_title": "Открыть CSV-файл индекса",
    "viewer.error_csv_title": "Ошибка чтения CSV",
    "viewer.error_csv_body": (
        "Невозможно прочитать CSV-файл: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – preview
    # ------------------------------------------------------------------
    "viewer.attach.preview": "Предпросмотр (только чтение)",
    "viewer.attach.preview_failed_title": "Ошибка предпросмотра",
    "viewer.attach.preview_failed_body": (
        "Невозможно отобразить предпросмотр вложения."
    ),
    "viewer.attach.preview_unsupported_title": "Неподдерживаемый тип",
    "viewer.attach.preview_unsupported_body": (
        "Предпросмотр для этого MIME-типа не поддерживается: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – extraction
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "Нет сообщения",
    "viewer.attach.no_msg_body": "Сообщение не выбрано.",
    "viewer.attach.no_selection_title": "Нет выбранного вложения",
    "viewer.attach.no_selection_body": (
        "Выберите вложение из списка."
    ),
    "viewer.attach.no_root_title": "Рабочий каталог не найден",
    "viewer.attach.no_root_body": (
        "Каталог forensic / индексирования не настроен."
    ),
    "viewer.attach.extract_one_title": "Вложение извлечено",
    "viewer.attach.extract_one_body": (
        "Вложение было извлечено в:\n{path}"
    ),
    "viewer.attach.extract_all_title": "Вложения извлечены",
    "viewer.attach.extract_all_body": (
        "{count} вложений были извлечены:\n{paths}"
    ),

    "viewer.attach.extract_one": "Извлечь выбранное вложение",
    "viewer.attach.extract_all": "Извлечь все вложения",

    # ------------------------------------------------------------------
    # About box
    # ------------------------------------------------------------------
    "about.version_label": "Версия:",
    "about.description": (
        "Инструмент для forensic-анализа писем EML/IMAP (только чтение)."
    ),
}
