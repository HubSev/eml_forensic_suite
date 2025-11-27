from __future__ import annotations

from typing import Dict

TRANSLATIONS_ES: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Aplicación
    # ------------------------------------------------------------------
    "app.title": "Suite forense EML / IMAP (solo lectura)",

    # ------------------------------------------------------------------
    # Menús
    # ------------------------------------------------------------------
    "menu.file": "Archivo",
    "menu.view": "Vista",
    "menu.help": "Ayuda",

    "menu.file.settings": "Opciones…",
    "menu.file.quit": "Salir",

    "menu.view.theme.dark": "Tema oscuro",
    "menu.view.theme.light": "Tema claro",

    "menu.help.about": "Acerca de…",

    # ------------------------------------------------------------------
    # Pestañas
    # ------------------------------------------------------------------
    "tab.imap": "1. Exportación IMAP",
    "tab.index": "2. Indexación EML",
    "tab.viewer": "3. Visor forense",
    "tab.dashboard": "4. Cuadro de mando forense",

    # ------------------------------------------------------------------
    # Diálogo de opciones
    # ------------------------------------------------------------------
    "settings.title": "Opciones",
    "settings.reports_dir.label": "Carpeta de trabajo / informes:",
    "settings.reports_dir.browse": "Examinar…",
    "settings.language.label": "Idioma de la interfaz:",
    "settings.reports_dir.dialog_title": "Elegir carpeta de trabajo / informes",

    # ------------------------------------------------------------------
    # Varios / Estado
    # ------------------------------------------------------------------
    "status.ready": "Listo.",
    "status.settings.saved": "Opciones guardadas.",

    # ------------------------------------------------------------------
    # Pestaña Index (indexación EML)
    # ------------------------------------------------------------------
    "index.folder_label": "Carpeta de exportación EML:",
    "index.browse": "Examinar…",
    "index.use_last_export": "Usar la última exportación IMAP",
    "index.log_placeholder": "Registro de indexación EML (solo lectura)…",
    "index.start_button": "Iniciar indexación EML",
    "index.dialog_select_folder": "Seleccionar carpeta de exportación EML",
    "index.no_last_export": (
        "Todavía no se conoce ninguna exportación IMAP (pestaña 1)."
    ),
    "index.error_already_running_title": "Indexación en curso",
    "index.error_already_running_body": (
        "Ya hay una operación de indexación EML en curso."
    ),
    "index.error_no_folder_title": "Carpeta ausente",
    "index.error_no_folder_body": (
        "Seleccione una carpeta que contenga archivos .eml."
    ),
    "index.error_invalid_folder_title": "Carpeta no válida",
    "index.error_invalid_folder_body": (
        "La carpeta especificada no existe:\n{folder}"
    ),
    "index.status_selected_folder": (
        "Carpeta seleccionada para la indexación: {folder}"
    ),
    "index.error_indexing_title": "Error durante la indexación",
    "index.error_log": "❌ Error: {error}",
    "index.done_log_success": "\nIndexación completada con éxito.",
    "index.done_log_path": "Ruta del CSV: {csv_path}",
    "index.done_log_count": "Número de entradas indexadas: {count}",
    "index.done_msg_title": "Indexación finalizada",
    "index.done_msg_body": (
        "Indexación EML finalizada.\n\nArchivo CSV: {csv_path}\nEntradas: {count}"
    ),

    # ------------------------------------------------------------------
    # Pestaña Dashboard (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "Usar el último índice",
    "dashboard.open_csv": "Abrir un índice CSV…",
    "dashboard.placeholder": (
        "Resumen estadístico forense basado en el índice EML…"
    ),
    "dashboard.source_memory": (
        "Origen: índice en memoria (última indexación de la sesión)."
    ),
    "dashboard.source_csv": "Origen: {path}",
    "dashboard.no_index_title": "Sin índice",
    "dashboard.no_index_body": (
        "No hay ningún índice disponible en esta sesión.\n"
        "Genere un índice en la pestaña 2 o abra un CSV manualmente."
    ),
    "dashboard.dialog_open_csv": "Abrir archivo de índice CSV",
    "dashboard.error_csv_missing_title": "Archivo no encontrado",
    "dashboard.error_csv_missing_body": (
        "El archivo especificado no existe:\n{path}"
    ),
    "dashboard.error_csv_read_title": "Error de lectura CSV",
    "dashboard.error_csv_read_body": (
        "No se puede leer el archivo CSV: {path}"
    ),
    "dashboard.empty_csv_title": "Índice vacío",
    "dashboard.empty_csv_body": (
        "El archivo CSV no contiene ninguna entrada utilizable."
    ),
    "dashboard.no_data": "No hay datos para analizar.",

    "dashboard.section_overview": "Vista general",
    "dashboard.overview_line": (
        "Total de correos: {total} – Remitentes distintos: {senders}"
    ),
    "dashboard.dates_line": "Periodo cubierto: {date_min} → {date_max}",
    "dashboard.dates_unknown": (
        "Fechas no disponibles o no interpretables."
    ),

    "dashboard.section_folders": "Distribución por carpeta IMAP",
    "dashboard.no_folders": "No se han detectado carpetas IMAP.",

    "dashboard.section_domains": "Distribución por dominio (remitente)",
    "dashboard.no_domains": "No se han detectado dominios.",

    "dashboard.section_attachments": "Archivos adjuntos",
    "dashboard.attachments_line": (
        "Correos con adjuntos: {with_att}/{total} – "
        "Total estimado de adjuntos: {total_att}"
    ),

    "dashboard.section_auth": "Autenticación (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "Resultados DKIM:",
    "dashboard.auth_header_spf": "Resultados SPF:",
    "dashboard.auth_header_dmarc": "Resultados DMARC:",

    "dashboard.section_integrity": "Integridad / cabeceras ausentes",
    "dashboard.integrity_flags_title": "Indicadores de integridad detectados:",
    "dashboard.no_integrity_flags": (
        "No se han detectado indicadores de integridad específicos."
    ),

    "dashboard.section_received": (
        "Anomalías en la cadena Received"
    ),
    "dashboard.no_received_anomalies": (
        "No se han detectado anomalías en Received (según las reglas actuales)."
    ),

    # ------------------------------------------------------------------
    # Pestaña Viewer – columnas básicas
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "Carpeta IMAP",
    "viewer.col.sequence_number": "Secuencia",
    "viewer.col.date_header": "Fecha",
    "viewer.col.from_header": "From",
    "viewer.col.to_header": "To",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Cci",
    "viewer.col.subject": "Asunto",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "¿Adjuntos?",
    "viewer.col.attachment_count": "Nº adjuntos",
    "viewer.col.attachment_filenames": "Nombres de adjuntos",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (extracto)",
    "viewer.col.received_count": "Nº Received",
    "viewer.col.received_anomalies": "Anomalías Received",
    "viewer.col.integrity_flags": "Indicadores de integridad",
    "viewer.col.relative_path": "Ruta relativa",
    "viewer.col.filename": "Nombre de archivo",

    # ------------------------------------------------------------------
    # Viewer – búsqueda + zonas
    # ------------------------------------------------------------------
    "viewer.search_label": "Búsqueda:",
    "viewer.search_placeholder": (
        "Filtrar en el índice (todas las columnas)…"
    ),
    "viewer.search_clear": "Limpiar",

    "viewer.headers_label": "Cabeceras",
    "viewer.headers_placeholder": (
        "Cabeceras del mensaje seleccionado…"
    ),

    "viewer.body_label": "Cuerpo (texto)",
    "viewer.body_placeholder": (
        "Cuerpo text/plain (o HTML bruto como alternativa) del mensaje seleccionado…"
    ),

    "viewer.btn_load_last": "Usar la última exportación IMAP",
    "viewer.btn_open_csv": "Abrir un índice CSV...",
    "viewer.attachments_label": "Archivos adjuntos",

    # ------------------------------------------------------------------
    # Viewer – errores EML
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "Archivo EML no encontrado",
    "viewer.error_missing_eml_body": (
        "No se puede encontrar el archivo EML en disco:\n{path}"
    ),
    "viewer.error_parse_eml_title": "Error de lectura EML",
    "viewer.error_parse_eml_body": (
        "No se puede analizar el archivo EML: {path}"
    ),

    # ------------------------------------------------------------------
    # Viewer – columnas adjuntos
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "Nombre",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "Tamaño (bytes)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "¿Sospechoso?",

    "viewer.attach.yes": "Sí",
    "viewer.attach.no": "No",

    # ------------------------------------------------------------------
    # IMAP – conexión y campos
    # ------------------------------------------------------------------
    "imap.group.connection": "Servidor IMAP (fuente de evidencia)",
    "imap.label.host": "Dirección del servidor IMAP",
    "imap.label.user": "Identificador del buzón analizado",
    "imap.label.password": "Contraseña (nunca almacenada)",
    "imap.label.date_start": "Fecha de inicio (filtro forense)",
    "imap.label.date_end": "Fecha de fin (filtro forense)",

    "imap.placeholder.host": "ej. imap.example.com",
    "imap.placeholder.user": "ej. incident@empresa.es",
    "imap.placeholder.password": "Contraseña de la cuenta analizada",
    "imap.placeholder.date_start": "DD/MM/AAAA (opcional)",
    "imap.placeholder.date_end": "DD/MM/AAAA (opcional)",

    "imap.button.fetch_mailboxes": "Inspeccionar carpetas IMAP…",
    "imap.button.start_export": "Iniciar extracción forense",
    "imap.button.cancel_export": "Cancelar extracción",

    "imap.label.mailboxes_title": (
        "Carpetas IMAP a extraer (fuente de evidencia):"
    ),
    "imap.checkbox.select_all": "Seleccionar todas las carpetas",

    "imap.log.placeholder": (
        "Registro de la extracción IMAP (solo lectura, con marcas de tiempo)…"
    ),

    # ------------------------------------------------------------------
    # IMAP – errores / información
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "Parámetros incompletos",
    "imap.error.missing_fields.body": (
        "Indique el servidor IMAP, el identificador y la contraseña."
    ),

    "imap.info.export_running.title": "Extracción en curso",
    "imap.info.export_running.body": (
        "Ya hay una extracción IMAP en curso."
    ),

    "imap.error.date_invalid.title": "Fecha no válida",
    "imap.error.date_invalid.body": "Error en las fechas proporcionadas: {error}",
    "imap.error.date_end_before_start.body": (
        "La fecha de fin no puede ser anterior a la fecha de inicio."
    ),

    "imap.error.no_mailbox_selected.title": "Ninguna carpeta seleccionada",
    "imap.error.no_mailbox_selected.body": (
        "Seleccione al menos una carpeta IMAP para extraer."
    ),

    "imap.error.fetch_mailboxes.title": "Error IMAP",
    "imap.error.fetch_mailboxes.body": (
        "No se puede recuperar la lista de carpetas IMAP:\n{error}"
    ),

    "imap.info.generic.title": "Información",
    "imap.error.generic.title": "Error",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "Conectando a {host}:{port} (SSL={use_ssl})...",
    "imap.log.connected": "Conectado al servidor IMAP.",
    "imap.log.select_folder": "Seleccionando la carpeta \"{folder}\"...",
    "imap.log.folder_selected": "Carpeta \"{folder}\" seleccionada.",
    "imap.log.message_count": "{count} mensajes para exportar.",
    "imap.log.fetching": "Recuperando mensajes IMAP...",
    "imap.log.export_done": "Exportación IMAP finalizada.",
    "imap.log.saving_to": "Guardando mensajes en \"{output_dir}\"...",
    "imap.log.progress": "Exportando mensaje {current}/{total}...",
    "imap.log.skip_existing": "El archivo \"{path}\" ya existe, se omite.",

    "imap.error.connect_failed": "No se puede conectar a {host}:{port}: {error}",
    "imap.error.login_failed": "Error de autenticación IMAP: {error}",
    "imap.error.select_failed": "No se puede seleccionar la carpeta \"{folder}\": {error}",
    "imap.error.fetch_failed": "Error al recuperar los mensajes: {error}",
    "imap.error.generic": "Error durante la exportación IMAP: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== Informe de exportación IMAP (solo lectura) ===",
    "imap.report.tool_line": "Herramienta : eml_forensic_suite – exportación IMAP",
    "imap.report.version_line": "Versión   : {version}",
    "imap.report.folder_line": "Carpeta  : {export_dir}",

    "imap.report.section_tool": "---- Información de la herramienta ----",
    "imap.report.tool_path": "Ruta de la herramienta    : {tool_path}",
    "imap.report.tool_hash": "SHA-256 de la herramienta : {tool_hash}",

    "imap.report.section_env": "---- Entorno de ejecución ----",
    "imap.report.env_os": "Sistema operativo   : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Versión de Python   : {python_version}",

    "imap.report.section_context": "---- Contexto IMAP / cuenta ----",
    "imap.report.context_host": "Servidor IMAP : {host}",
    "imap.report.context_user": "Cuenta        : {user}",
    "imap.report.context_date_start": "Fecha de inicio solicitada : {date_start}",
    "imap.report.context_date_end": "Fecha de fin solicitada    : {date_end}",
    "imap.report.context_criteria": "Criterios de búsqueda IMAP : {search_criteria} (tal como se enviaron al servidor)",

    "imap.report.selected_folders_title": "Carpetas seleccionadas:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- Información del servidor IMAP ----",
    "imap.report.server_greeting": "Banner IMAP : {greeting}",
    "imap.report.server_capability": "CAPABILITY  : {capability}",

    "imap.report.section_timestamps": "---- Marcas de tiempo del análisis ----",
    "imap.report.timestamp_start_utc": "Inicio del análisis (UTC)   : {dt}",
    "imap.report.timestamp_start_local": "Inicio del análisis (local) : {dt}",
    "imap.report.timestamp_end_utc": "Fin del análisis (UTC)      : {dt}",
    "imap.report.timestamp_end_local": "Fin del análisis (local)    : {dt}",
    "imap.report.duration": "Duración total              : {duration}",

    "imap.report.section_folders": "---- Carpetas analizadas ----",
    "imap.report.folders_count": "Número de carpetas seleccionadas : {count}",

    "imap.report.folder_header": "Carpeta : {name}",
    "imap.report.folder_messages": "  Mensajes encontrados (periodo) : {count}",
    "imap.report.folder_exported": "  Mensajes exportados            : {count}",
    "imap.report.folder_errors": "  Errores de descarga            : {count}",
    "imap.report.folder_bytes": "  Volumen descargado             : {bytes} bytes",
    "imap.report.folder_size_stats": "  Tamaño mín / máx / medio       : {min_size} / {max_size} / {avg_size} bytes",
    "imap.report.folder_period": "  Periodo cubierto (INTERNALDATE) : {first} → {last}",
    "imap.report.folder_error_uids": "  UIDs con error (lista no exhaustiva) : {uids}",

    "imap.report.section_totals": "---- Totales globales ----",
    "imap.report.total_messages": "Mensajes encontrados (todas las carpetas) : {count}",
    "imap.report.total_exported": "Mensajes exportados                       : {count}",
    "imap.report.total_errors": "Errores de descarga                       : {count}",
    "imap.report.total_bytes": "Volumen total descargado                  : {bytes} bytes",

    "imap.report.section_forensic": "---- Metodología y garantías forenses ----",
    "imap.report.forensic_item_readonly": "- La herramienta solo utilizó comandos IMAP de solo lectura (SELECT readonly, SEARCH, FETCH). Ningún mensaje fue modificado, eliminado ni marcado como leído durante el análisis.",
    "imap.report.forensic_item_eml": "- Los mensajes se exportaron exactamente como los proporcionó el servidor IMAP y se escribieron en disco como archivos .eml sin alterar su contenido.",
    "imap.report.forensic_item_hashes": "- Cada mensaje exportado está asociado a un hash SHA-256 listado en hashes.txt, así como a un hash global calculado a partir de la concatenación de todos los hashes individuales.",
    "imap.report.forensic_item_report_hash": "- Este propio informe de análisis se somete a un hash SHA-256 y dicho hash se añade a hashes.txt para garantizar la integridad del informe.",

    "imap.report.hashes_report_header": "INFORME DE ANÁLISIS:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "Ninguna carpeta seleccionada.",
    "imap.worker.log_export_dir": "Carpeta de exportación: {export_dir}",
    "imap.worker.tool_hash_error": "(error al calcular el hash de la herramienta)",

    "imap.worker.log_connecting": "Conectando al servidor IMAP...",
    "imap.worker.greeting_not_available": "(banner IMAP no disponible)",
    "imap.worker.log_auth_classic": "Autenticación IMAP clásica...",
    "imap.worker.error_auth_failed": "Error de autenticación IMAP: {error}",
    "imap.worker.capability_error": "(error durante el comando CAPABILITY)",

    "imap.worker.log_date_start_inclusive": "Fecha de inicio (incluida): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "Fecha de inicio: no definida → extracción desde el primer mensaje disponible.",
    "imap.worker.date_start_unset_label": "Primer mensaje disponible (sin límite inferior)",

    "imap.worker.log_date_end_inclusive": "Fecha de fin (incluida): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "Fecha de fin: no definida → hasta la última fecha disponible en el servidor.",
    "imap.worker.date_end_unset_label": "Último mensaje disponible (sin límite superior)",

    "imap.worker.log_criteria": "Criterios de búsqueda IMAP utilizados: {criteria}",
    "imap.worker.log_selected_folders_header": "Carpetas seleccionadas ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "Detención solicitada durante la fase de conteo.",
    "imap.worker.log_phase1_count": "[Fase 1] Contando mensajes en {folder}...",
    "imap.worker.log_select_folder_failed": "  ⚠️ No se puede seleccionar esta carpeta, se omite.",
    "imap.worker.log_search_folder_failed": "  ⚠️ Error al buscar en esta carpeta, se omite.",
    "imap.worker.log_messages_to_process": "  → {count} mensajes que procesar en {folder}",

    "imap.worker.log_total_messages_to_download": "Número total de mensajes a descargar (todas las carpetas): {count}",

    "imap.worker.log_stop_during_export": "Detención solicitada: interrumpiendo la exportación.",
    "imap.worker.log_folder_header": "=== Carpeta: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  No hay mensajes en {folder} para este periodo.",
    "imap.worker.log_folder_message_count": "  Número de mensajes encontrados en {folder}: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ No se puede volver a seleccionar esta carpeta, se omite.",

    "imap.worker.log_first_message_download": "  Descargando el primer mensaje ({uid})...",
    "imap.worker.log_folder_progress": "  Progreso de la carpeta {folder}: {current}/{total} (último: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ Error al recuperar el mensaje {uid}, se continúa.",
    "imap.worker.log_folder_end": "  Fin de la carpeta {folder}",

    "imap.worker.hashes_header": "Lista de archivos exportados y sus hashes SHA-256",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "HASH GLOBAL (solo mensajes):",

    "imap.worker.log_export_done_header": "=== Exportación completada ===",
    "imap.worker.log_export_done_count": "Número total de mensajes exportados: {count}",
    "imap.worker.log_export_done_hashes_file": "Archivo de hashes: {path}",
    "imap.worker.log_export_done_hash": "Hash global: {file_hash}",

    "imap.worker.summary": (
        "Exportación completada.\n\n"
        "Mensajes exportados: {count}\n"
        "Carpeta: {export_dir}\n\n"
        "Hash global (mensajes):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "Informe de análisis generado y con hash calculado (ver rapport_imap_export.txt y hashes.txt).",
    "imap.worker.log_report_failed": "⚠️ No se puede generar el informe de análisis: {error}",

    "imap.worker.error_generic": "Se ha producido un error: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "Conectando al servidor IMAP...",
    "imap.tk.log_auth_classic": "Autenticación IMAP clásica...",
    "imap.tk.error_list_mailboxes_failed": "No se pueden listar las carpetas IMAP.",

    "imap.tk.log_folders_found_header": "Carpetas encontradas en el servidor:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "Total de carpetas IMAP: {count}",

    "imap.tk.msgbox_error_title": "Error",
    "imap.tk.msgbox_error_fetch_mailboxes": "Error al recuperar las carpetas IMAP: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ Error al recuperar las carpetas: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. Exportación IMAP",

    "imap.tk.label_server": "Servidor IMAP:",
    "imap.tk.label_email": "Dirección de correo:",
    "imap.tk.label_password": "Contraseña:",
    "imap.tk.label_date_start": "Fecha de inicio (DD/MM/YYYY, opcional):",
    "imap.tk.label_date_end": "Fecha de fin (DD/MM/YYYY, opcional):",
    "imap.tk.label_log": "Registro:",
    "imap.tk.label_mailboxes": "Carpetas IMAP a exportar:",
    "imap.tk.checkbox_select_all": "Seleccionar todo / Deseleccionar todo",
    "imap.tk.label_progress": "Progreso:",

    "imap.tk.msgbox_missing_fields_title": "Campos faltantes",
    "imap.tk.msgbox_missing_fields_text": "Por favor, rellena el servidor, el correo y la contraseña.",

    "imap.tk.log_fetch_mailboxes_start": "Recuperando carpetas IMAP...",
    "imap.tk.log_no_mailboxes_or_error": "No se encontró ninguna carpeta o se produjo un error.",
    "imap.tk.log_select_mailboxes_hint": "Selecciona las carpetas a exportar.",

    "imap.tk.button_list_mailboxes": "Listar carpetas IMAP",

    "imap.tk.msgbox_date_start_invalid_title": "Fecha de inicio no válida",
    "imap.tk.msgbox_date_start_invalid_text": "La fecha de inicio debe estar en formato DD/MM/YYYY.",

    "imap.tk.msgbox_date_end_invalid_title": "Fecha de fin no válida",
    "imap.tk.msgbox_date_end_invalid_text": "La fecha de fin debe estar en formato DD/MM/YYYY.",

    "imap.tk.msgbox_date_range_invalid_title": "Rango de fechas no válido",
    "imap.tk.msgbox_date_range_invalid_text": (
        "La fecha de fin no puede ser anterior a la fecha de inicio."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "Ninguna carpeta seleccionada",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "Por favor, selecciona al menos una carpeta IMAP (mediante «Listar carpetas IMAP»)."
    ),

    "imap.tk.log_export_start": "Iniciando la exportación...",
    "imap.tk.button_run_export": "Ejecutar exportación (carpetas seleccionadas)",

    "imap.tk.log_stop_requested": (
        "Se ha solicitado detener, la exportación finalizará de forma limpia..."
    ),
    "imap.tk.button_stop_export": "Detener exportación",

    "imap.tk.msgbox_export_done_title": "Exportación completada",


    # ------------------------------------------------------------------
    # IMAP – registros
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "Conectando al servidor IMAP para enumerar las carpetas…"
    ),
    "imap.log.fetch_error": (
        "❌ Error al recuperar las carpetas:"
    ),
    "imap.log.no_mailboxes": (
        "No se ha encontrado ninguna carpeta IMAP en esta cuenta."
    ),
    "imap.log.mailboxes_found": "Carpetas encontradas en el servidor:",
    "imap.log.mailboxes_total": "Total de carpetas IMAP: {count}",
    "imap.log.mailboxes_select_hint": (
        "Seleccione las carpetas que desea extraer en modo solo lectura."
    ),
    "imap.log.start_export": (
        "Iniciando extracción IMAP (modo forense, solo lectura)…"
    ),
    "imap.log.cancel_requested": (
        "Solicitud de cancelación enviada al worker IMAP…"
    ),
    "imap.log.export_dir_saved": "Carpeta de exportación guardada: {path}",
    "imap.log.done": "Procesamiento IMAP finalizado.",

    # ------------------------------------------------------------------
    # Dashboard v3 – secciones / pestañas
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "Niveles de sospecha",
    "dashboard.tab_text": "Resumen del índice EML",
    "dashboard.tab_graphs": "Gráficos",
    "dashboard.section_charts": "Visualizaciones gráficas",

    "dashboard.chart_suspicion_title": (
        "Distribución de niveles de sospecha"
    ),
    "dashboard.chart_folders_title": "Mensajes por carpeta IMAP",
    "dashboard.chart_domains_title": (
        "Dominios de remitente más frecuentes"
    ),
    "dashboard.chart_attachments_title": "Presencia de adjuntos",
    "dashboard.chart_axis_count": "Cantidad",
    "dashboard.chart_attachments_with": "Con adjuntos",
    "dashboard.chart_attachments_without": "Sin adjuntos",

    # Leyenda / texto alrededor del scoring
    "dashboard.suspicion_distribution_line": (
        "Distribución de correos por nivel de sospecha:"
    ),
    "dashboard.suspicion_level.LOW": "Bajo",
    "dashboard.suspicion_level.MEDIUM": "Medio",
    "dashboard.suspicion_level.HIGH": "Alto",
    "dashboard.suspicion_level.CRITICAL": "Crítico",
    "dashboard.suspicion_level.UNKNOWN": "Desconocido",

    # Gráficos – títulos (nueva nomenclatura)
    "dashboard.chart.folders.title": "Correos por carpeta IMAP",
    "dashboard.chart.domains.title": "Principales dominios de remitente",
    "dashboard.chart.attachments.title": "Presencia de adjuntos",
    "dashboard.chart.auth.title": "Resultados DKIM / SPF / DMARC",
    "dashboard.chart.suspicion.title": "Distribución por nivel de sospecha",

    # Gráficos – etiquetas / estados
    "dashboard.chart.no_data": (
        "No hay datos suficientes para mostrar este gráfico."
    ),
    "dashboard.chart.axis.emails": "Número de correos",
    "dashboard.chart.axis.folders": "Carpetas IMAP",
    "dashboard.chart.axis.domains": "Dominios",
    "dashboard.chart.axis.levels": "Niveles",

    # Pequeña ayuda visual sobre los colores
    "dashboard.legend.safe": "Zona considerada más bien segura",
    "dashboard.legend.suspicious": "Zona a revisar con prioridad",

    # ------------------------------------------------------------------
    # Viewer – columnas de scoring y sospecha
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "Puntuación de sospecha",
    "viewer.col.suspicion_level": "Nivel",
    "viewer.col.suspicion_reasons": "Motivos (resumen)",

    # Tooltips de scoring
    "viewer.score.tooltip.base": (
        "Puntuación global de sospecha calculada a partir de DKIM/SPF/DMARC, "
        "anomalías en Received, integridad de cabeceras y adjuntos."
    ),
    "viewer.score.level.LOW": (
        "Sospecha baja: no se ha detectado nada anormal según las reglas actuales."
    ),
    "viewer.score.level.MEDIUM": (
        "Sospecha media: hay algunos elementos que conviene revisar "
        "(cabeceras, autenticación o adjuntos)."
    ),
    "viewer.score.level.HIGH": (
        "Sospecha alta: varios indicadores técnicos son incoherentes o peligrosos."
    ),
    "viewer.score.level.CRITICAL": (
        "Sospecha crítica: el correo es muy probablemente malicioso o falsificado."
    ),

    # ------------------------------------------------------------------
    # IMAP – texto sobre OAuth / restricciones
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "Esta cuenta parece estar gestionada por un proveedor que exige el uso de "
        "mecanismos modernos (OAuth2, exportaciones oficiales) para acceder a los mensajes "
        "(p. ej. Gmail, Outlook/Microsoft 365, Yahoo).\n\n"
        "Para mantener la conformidad y evitar eludir estas reglas, esta versión de "
        "eml_forensic_suite no realiza extracción IMAP directa para estos servicios.\n\n"
        "Para recuperar los mensajes de forma compatible:\n"
        "  • Gmail: utilice Google Takeout para exportar el buzón (MBOX)\n"
        "    o un cliente como Thunderbird para crear una copia local.\n"
        "  • Outlook / Microsoft 365: utilice la exportación de su cliente Outlook\n"
        "    (PST) o las herramientas de archivado de su organización.\n"
        "  • Yahoo, etc.: utilice las herramientas de exportación ofrecidas por el proveedor.\n\n"
        "Las futuras versiones de eml_forensic_suite apuntarán a analizar directamente "
        "estas exportaciones (MBOX, PST, etc.) para seguir siendo compatibles con estas plataformas."
    ),

    # ------------------------------------------------------------------
    # Viewer – mini lenguaje de búsqueda
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "Mini-lenguaje forense:\n"
        "  from:alice@example.com\n"
        "  domain:banco.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "Operadores: AND implícito, OR, NOT, paréntesis."
    ),

    # ------------------------------------------------------------------
    # Viewer – mensajes genéricos CSV / índice
    # ------------------------------------------------------------------
    "viewer.no_index_title": "Ningún índice disponible",
    "viewer.no_index_body": (
        "No hay ningún índice disponible en esta sesión.\n"
        "Genere un índice en la pestaña 2 o abra un archivo CSV manualmente."
    ),
    "viewer.open_csv_title": "Abrir archivo de índice CSV",
    "viewer.error_csv_title": "Error de lectura CSV",
    "viewer.error_csv_body": (
        "No se puede leer el archivo CSV: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – vista previa (solo lectura)
    # ------------------------------------------------------------------
    "viewer.attach.preview": "Vista previa solo lectura",
    "viewer.attach.preview_failed_title": "Vista previa imposible",
    "viewer.attach.preview_failed_body": (
        "No se puede mostrar una vista previa de este adjunto."
    ),
    "viewer.attach.preview_unsupported_title": "Tipo no soportado",
    "viewer.attach.preview_unsupported_body": (
        "No hay vista previa integrada disponible para este tipo MIME: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – extracción de adjuntos
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "Ningún mensaje",
    "viewer.attach.no_msg_body": (
        "Ningún mensaje está seleccionado actualmente."
    ),
    "viewer.attach.no_selection_title": "Ningún adjunto seleccionado",
    "viewer.attach.no_selection_body": (
        "Seleccione un adjunto en la lista."
    ),
    "viewer.attach.no_root_title": (
        "Carpeta de trabajo no encontrada"
    ),
    "viewer.attach.no_root_body": (
        "No se ha configurado ninguna carpeta forense / de índice para la extracción."
    ),
    "viewer.attach.extract_one_title": "Adjunto extraído",
    "viewer.attach.extract_one_body": (
        "El adjunto se ha extraído a:\n{path}"
    ),
    "viewer.attach.extract_all_title": "Adjuntos extraídos",
    "viewer.attach.extract_all_body": (
        "{count} adjuntos se han extraído a:\n{paths}"
    ),

    # ------------------------------------------------------------------
    # Acciones adjuntos (botones)
    # ------------------------------------------------------------------
    "viewer.attach.extract_one": "Extraer adjunto seleccionado",
    "viewer.attach.extract_all": "Extraer todos los adjuntos",

    # ------------------------------------------------------------------
    # About box
    # ------------------------------------------------------------------
    "about.version_label": "Versión:",
    "about.description": (
        "Herramienta de solo lectura para el análisis forense de correos EML/IMAP."
    ),
}
