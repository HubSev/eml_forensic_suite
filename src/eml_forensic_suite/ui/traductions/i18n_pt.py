from __future__ import annotations

from typing import Dict

TRANSLATIONS_PT: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "Suite Forense EML / IMAP (somente leitura)",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "Arquivo",
    "menu.view": "Exibir",
    "menu.help": "Ajuda",

    "menu.file.settings": "Configurações…",
    "menu.file.quit": "Sair",

    "menu.view.theme.dark": "Tema escuro",
    "menu.view.theme.light": "Tema claro",

    "menu.help.about": "Sobre…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. Exportação IMAP",
    "tab.index": "2. Indexação de EML",
    "tab.viewer": "3. Visualizador forense",
    "tab.dashboard": "4. Painel forense",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "Configurações",
    "settings.reports_dir.label": "Diretório de trabalho / relatórios:",
    "settings.reports_dir.browse": "Procurar…",
    "settings.language.label": "Idioma da interface:",
    "settings.reports_dir.dialog_title": "Escolher diretório de trabalho / relatórios",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "Pronto.",
    "status.settings.saved": "Configurações salvas.",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "Diretório de exportação EML:",
    "index.browse": "Procurar…",
    "index.use_last_export": "Usar última exportação IMAP",
    "index.log_placeholder": "Log de indexação EML (somente leitura)…",
    "index.start_button": "Iniciar indexação EML",
    "index.dialog_select_folder": "Selecionar pasta de exportação EML",
    "index.no_last_export": "Nenhuma exportação IMAP conhecida ainda (aba 1).",
    "index.error_already_running_title": "Indexação já em execução",
    "index.error_already_running_body": "Uma operação de indexação EML já está em andamento.",
    "index.error_no_folder_title": "Pasta ausente",
    "index.error_no_folder_body": "Por favor selecione uma pasta contendo arquivos .eml.",
    "index.error_invalid_folder_title": "Pasta inválida",
    "index.error_invalid_folder_body": "A pasta especificada não existe:\n{folder}",
    "index.status_selected_folder": "Pasta selecionada para indexação: {folder}",
    "index.error_indexing_title": "Erro durante a indexação",
    "index.error_log": "❌ Erro: {error}",
    "index.done_log_success": "\nIndexação concluída com sucesso.",
    "index.done_log_path": "Caminho do CSV: {csv_path}",
    "index.done_log_count": "Número de entradas indexadas: {count}",
    "index.done_msg_title": "Indexação concluída",
    "index.done_msg_body": (
        "Indexação EML concluída.\n\nArquivo CSV: {csv_path}\nEntradas: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "Usar último índice",
    "dashboard.open_csv": "Abrir arquivo CSV…",
    "dashboard.placeholder": "Resumo estatístico forense baseado no índice EML…",
    "dashboard.source_memory": "Fonte: índice em memória (última indexação nesta sessão).",
    "dashboard.source_csv": "Fonte: {path}",
    "dashboard.no_index_title": "Nenhum índice",
    "dashboard.no_index_body": (
        "Nenhum índice está disponível nesta sessão.\n"
        "Gere um índice na aba 2 ou abra um CSV manualmente."
    ),
    "dashboard.dialog_open_csv": "Abrir arquivo CSV de índice",
    "dashboard.error_csv_missing_title": "Arquivo não encontrado",
    "dashboard.error_csv_missing_body": "O arquivo especificado não existe:\n{path}",
    "dashboard.error_csv_read_title": "Erro ao ler CSV",
    "dashboard.error_csv_read_body": "Não foi possível ler o arquivo CSV: {path}",
    "dashboard.empty_csv_title": "Índice vazio",
    "dashboard.empty_csv_body": "O arquivo CSV não contém entradas utilizáveis.",
    "dashboard.no_data": "Nenhum dado para analisar.",

    "dashboard.section_overview": "Visão geral",
    "dashboard.overview_line": (
        "Total de emails: {total} – Remetentes distintos: {senders}"
    ),
    "dashboard.dates_line": "Período coberto: {date_min} → {date_max}",
    "dashboard.dates_unknown": "Datas indisponíveis ou não analisáveis.",

    "dashboard.section_folders": "Distribuição por pasta IMAP",
    "dashboard.no_folders": "Nenhuma pasta IMAP detectada.",

    "dashboard.section_domains": "Distribuição por domínio (remetente)",
    "dashboard.no_domains": "Nenhum domínio detectado.",

    "dashboard.section_attachments": "Anexos",
    "dashboard.attachments_line": (
        "Emails com anexos: {with_att}/{total} – Total estimado de anexos: {total_att}"
    ),

    "dashboard.section_auth": "Autenticação (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "Resultados DKIM:",
    "dashboard.auth_header_spf": "Resultados SPF:",
    "dashboard.auth_header_dmarc": "Resultados DMARC:",

    "dashboard.section_integrity": "Integridade / cabeçalhos ausentes",
    "dashboard.integrity_flags_title": "Flags de integridade detectadas:",
    "dashboard.no_integrity_flags": "Nenhum flag de integridade detectado.",

    "dashboard.section_received": "Anomalias na cadeia Received",
    "dashboard.no_received_anomalies": (
        "Nenhuma anomalia em Received detectada (segundo as regras atuais)."
    ),

    # ------------------------------------------------------------------
    # Viewer tab – base columns
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "Pasta IMAP",
    "viewer.col.sequence_number": "Sequência",
    "viewer.col.date_header": "Data",
    "viewer.col.from_header": "De",
    "viewer.col.to_header": "Para",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Bcc",
    "viewer.col.subject": "Assunto",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "Anexos?",
    "viewer.col.attachment_count": "Quantidade de anexos",
    "viewer.col.attachment_filenames": "Nomes dos anexos",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (trecho)",
    "viewer.col.received_count": "Count Received",
    "viewer.col.received_anomalies": "Anomalias em Received",
    "viewer.col.integrity_flags": "Flags de integridade",
    "viewer.col.relative_path": "Caminho relativo",
    "viewer.col.filename": "Nome do arquivo",

    # ------------------------------------------------------------------
    # Viewer – search + zones
    # ------------------------------------------------------------------
    "viewer.search_label": "Pesquisar:",
    "viewer.search_placeholder": "Filtro no índice (todas as colunas)…",
    "viewer.search_clear": "Limpar",

    "viewer.headers_label": "Cabeçalhos",
    "viewer.headers_placeholder": "Cabeçalhos da mensagem selecionada…",

    "viewer.body_label": "Corpo (texto)",
    "viewer.body_placeholder": (
        "corpo text/plain (ou fallback HTML bruto) da mensagem selecionada…"
    ),

    "viewer.btn_load_last": "Usar última exportação IMAP",
    "viewer.btn_open_csv": "Abrir CSV de índice...",
    "viewer.attachments_label": "Anexos",

    # ------------------------------------------------------------------
    # Viewer – EML errors
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "Arquivo EML não encontrado",
    "viewer.error_missing_eml_body": "Não foi possível encontrar o arquivo EML:\n{path}",
    "viewer.error_parse_eml_title": "Erro ao ler EML",
    "viewer.error_parse_eml_body": "Não foi possível analisar o arquivo EML: {path}",

    # ------------------------------------------------------------------
    # Viewer – attachment columns
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "Nome",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "Tamanho (bytes)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "Suspeito?",

    "viewer.attach.yes": "Sim",
    "viewer.attach.no": "Não",

    # ------------------------------------------------------------------
    # IMAP tab – connection & fields
    # ------------------------------------------------------------------
    "imap.group.connection": "Servidor IMAP (fonte de evidências)",
    "imap.label.host": "Endereço do servidor IMAP",
    "imap.label.user": "Identificador da caixa analisada",
    "imap.label.password": "Senha (nunca armazenada)",
    "imap.label.date_start": "Data inicial (filtro forense)",
    "imap.label.date_end": "Data final (filtro forense)",

    "imap.placeholder.host": "ex.: imap.exemplo.com",
    "imap.placeholder.user": "ex.: incidente@empresa.com",
    "imap.placeholder.password": "Senha da conta analisada",
    "imap.placeholder.date_start": "DD/MM/AAAA (opcional)",
    "imap.placeholder.date_end": "DD/MM/AAAA (opcional)",

    "imap.button.fetch_mailboxes": "Inspecionar pastas IMAP…",
    "imap.button.start_export": "Iniciar extração forense",
    "imap.button.cancel_export": "Cancelar extração",

    "imap.label.mailboxes_title": (
        "Pastas IMAP a extrair (fonte de evidências):"
    ),
    "imap.checkbox.select_all": "Selecionar todas as pastas",

    "imap.log.placeholder": (
        "Log da extração IMAP (somente leitura, com timestamps)…"
    ),

    # ------------------------------------------------------------------
    # IMAP errors
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "Configurações incompletas",
    "imap.error.missing_fields.body": (
        "Por favor informe servidor IMAP, usuário e senha."
    ),

    "imap.info.export_running.title": "Extração já em execução",
    "imap.info.export_running.body": "Uma extração IMAP já está em andamento.",

    "imap.error.date_invalid.title": "Data inválida",
    "imap.error.date_invalid.body": "Erro nas datas fornecidas: {error}",
    "imap.error.date_end_before_start.body": (
        "A data final não pode ser anterior à data inicial."
    ),

    "imap.error.no_mailbox_selected.title": "Nenhuma pasta selecionada",
    "imap.error.no_mailbox_selected.body": (
        "Por favor selecione ao menos uma pasta IMAP."
    ),

    "imap.error.fetch_mailboxes.title": "Erro IMAP",
    "imap.error.fetch_mailboxes.body": (
        "Não foi possível obter as pastas IMAP:\n{error}"
    ),

    "imap.info.generic.title": "Informação",
    "imap.error.generic.title": "Erro",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "A ligar a {host}:{port} (SSL={use_ssl})...",
    "imap.log.connected": "Ligação estabelecida com o servidor IMAP.",
    "imap.log.select_folder": "A selecionar a pasta \"{folder}\"...",
    "imap.log.folder_selected": "Pasta \"{folder}\" selecionada.",
    "imap.log.message_count": "{count} mensagens a exportar.",
    "imap.log.fetching": "A recuperar mensagens IMAP...",
    "imap.log.export_done": "Exportação IMAP concluída.",
    "imap.log.saving_to": "A guardar mensagens em \"{output_dir}\"...",
    "imap.log.progress": "A exportar mensagem {current}/{total}...",
    "imap.log.skip_existing": "O ficheiro \"{path}\" já existe, a ignorar.",

    "imap.error.connect_failed": "Não é possível ligar a {host}:{port}: {error}",
    "imap.error.login_failed": "Erro de autenticação IMAP: {error}",
    "imap.error.select_failed": "Não é possível selecionar a pasta \"{folder}\": {error}",
    "imap.error.fetch_failed": "Erro ao recuperar mensagens: {error}",
    "imap.error.generic": "Erro durante a exportação IMAP: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== Relatório de exportação IMAP (apenas leitura) ===",
    "imap.report.tool_line": "Ferramenta : eml_forensic_suite – exportação IMAP",
    "imap.report.version_line": "Versão    : {version}",
    "imap.report.folder_line": "Pasta     : {export_dir}",

    "imap.report.section_tool": "---- Informações da ferramenta ----",
    "imap.report.tool_path": "Caminho da ferramenta   : {tool_path}",
    "imap.report.tool_hash": "SHA-256 da ferramenta   : {tool_hash}",

    "imap.report.section_env": "---- Ambiente de execução ----",
    "imap.report.env_os": "Sistema operativo       : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Versão do Python        : {python_version}",

    "imap.report.section_context": "---- Contexto IMAP / conta ----",
    "imap.report.context_host": "Servidor IMAP : {host}",
    "imap.report.context_user": "Conta        : {user}",
    "imap.report.context_date_start": "Data de início solicitada : {date_start}",
    "imap.report.context_date_end": "Data de fim solicitada    : {date_end}",
    "imap.report.context_criteria": "Critérios de pesquisa IMAP : {search_criteria} (tal como enviados ao servidor)",

    "imap.report.selected_folders_title": "Pastas selecionadas:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- Informações do servidor IMAP ----",
    "imap.report.server_greeting": "Banner IMAP : {greeting}",
    "imap.report.server_capability": "CAPABILITY  : {capability}",

    "imap.report.section_timestamps": "---- Marcas temporais da análise ----",
    "imap.report.timestamp_start_utc": "Início da análise (UTC)   : {dt}",
    "imap.report.timestamp_start_local": "Início da análise (local) : {dt}",
    "imap.report.timestamp_end_utc": "Fim da análise (UTC)      : {dt}",
    "imap.report.timestamp_end_local": "Fim da análise (local)    : {dt}",
    "imap.report.duration": "Duração total             : {duration}",

    "imap.report.section_folders": "---- Pastas analisadas ----",
    "imap.report.folders_count": "Número de pastas selecionadas : {count}",

    "imap.report.folder_header": "Pasta : {name}",
    "imap.report.folder_messages": "  Mensagens encontradas (período) : {count}",
    "imap.report.folder_exported": "  Mensagens exportadas            : {count}",
    "imap.report.folder_errors": "  Erros de recuperação            : {count}",
    "imap.report.folder_bytes": "  Volume transferido              : {bytes} bytes",
    "imap.report.folder_size_stats": "  Tamanho mín / máx / méd         : {min_size} / {max_size} / {avg_size} bytes",
    "imap.report.folder_period": "  Período coberto (INTERNALDATE)  : {first} → {last}",
    "imap.report.folder_error_uids": "  UIDs com erro (lista não exaustiva) : {uids}",

    "imap.report.section_totals": "---- Totais globais ----",
    "imap.report.total_messages": "Mensagens encontradas (todas as pastas) : {count}",
    "imap.report.total_exported": "Mensagens exportadas                    : {count}",
    "imap.report.total_errors": "Erros de recuperação                    : {count}",
    "imap.report.total_bytes": "Volume total transferido                : {bytes} bytes",

    "imap.report.section_forensic": "---- Metodologia e garantias forenses ----",
    "imap.report.forensic_item_readonly": "- A ferramenta utilizou apenas comandos IMAP de leitura (SELECT readonly, SEARCH, FETCH). Nenhuma mensagem foi modificada, apagada ou marcada como lida durante a análise.",
    "imap.report.forensic_item_eml": "- As mensagens foram exportadas exatamente como fornecidas pelo servidor IMAP e gravadas em disco como ficheiros .eml sem alteração do seu conteúdo.",
    "imap.report.forensic_item_hashes": "- Cada mensagem exportada está associada a um hash SHA-256 listado em hashes.txt, bem como a um hash global calculado a partir da concatenação de todos os hashes individuais.",
    "imap.report.forensic_item_report_hash": "- O próprio relatório de análise é alvo de um hash SHA-256, e esse hash é adicionado a hashes.txt para garantir a integridade do relatório.",

    "imap.report.hashes_report_header": "RELATÓRIO DE ANÁLISE:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "Nenhuma pasta selecionada.",
    "imap.worker.log_export_dir": "Pasta de exportação: {export_dir}",
    "imap.worker.tool_hash_error": "(erro ao calcular o hash da ferramenta)",

    "imap.worker.log_connecting": "A ligar ao servidor IMAP...",
    "imap.worker.greeting_not_available": "(banner IMAP não disponível)",
    "imap.worker.log_auth_classic": "Autenticação IMAP clássica...",
    "imap.worker.error_auth_failed": "Erro de autenticação IMAP: {error}",
    "imap.worker.capability_error": "(erro durante o comando CAPABILITY)",

    "imap.worker.log_date_start_inclusive": "Data de início (inclusiva): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "Data de início: não definida → extração a partir da primeira mensagem disponível.",
    "imap.worker.date_start_unset_label": "Primeira mensagem disponível (sem limite inferior)",

    "imap.worker.log_date_end_inclusive": "Data de fim (inclusiva): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "Data de fim: não definida → até à última data disponível no servidor.",
    "imap.worker.date_end_unset_label": "Última mensagem disponível (sem limite superior)",

    "imap.worker.log_criteria": "Critérios de pesquisa IMAP utilizados: {criteria}",
    "imap.worker.log_selected_folders_header": "Pastas selecionadas ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "Paragem solicitada durante a fase de contagem.",
    "imap.worker.log_phase1_count": "[Fase 1] A contar mensagens em {folder}...",
    "imap.worker.log_select_folder_failed": "  ⚠️ Não foi possível selecionar esta pasta, a ignorar.",
    "imap.worker.log_search_folder_failed": "  ⚠️ Erro ao pesquisar nesta pasta, a ignorar.",
    "imap.worker.log_messages_to_process": "  → {count} mensagens a processar em {folder}",

    "imap.worker.log_total_messages_to_download": "Número total de mensagens a transferir (todas as pastas): {count}",

    "imap.worker.log_stop_during_export": "Paragem solicitada: a exportação será interrompida.",
    "imap.worker.log_folder_header": "=== Pasta: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  Nenhuma mensagem em {folder} para este período.",
    "imap.worker.log_folder_message_count": "  Número de mensagens encontradas em {folder}: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ Não foi possível voltar a selecionar esta pasta, a ignorar.",

    "imap.worker.log_first_message_download": "  A transferir a primeira mensagem ({uid})...",
    "imap.worker.log_folder_progress": "  Progresso da pasta {folder}: {current}/{total} (última: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ Erro ao recuperar a mensagem {uid}, a continuar.",
    "imap.worker.log_folder_end": "  Fim da pasta {folder}",

    "imap.worker.hashes_header": "Lista de ficheiros exportados e respetivos hashes SHA-256",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "HASH GLOBAL (apenas mensagens):",

    "imap.worker.log_export_done_header": "=== Exportação concluída ===",
    "imap.worker.log_export_done_count": "Número total de mensagens exportadas: {count}",
    "imap.worker.log_export_done_hashes_file": "Ficheiro de hashes: {path}",
    "imap.worker.log_export_done_hash": "Hash global: {file_hash}",

    "imap.worker.summary": (
        "Exportação concluída.\n\n"
        "Mensagens exportadas: {count}\n"
        "Pasta: {export_dir}\n\n"
        "Hash global (mensagens):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "Relatório de análise gerado e hasheado (ver rapport_imap_export.txt e hashes.txt).",
    "imap.worker.log_report_failed": "⚠️ Não foi possível gerar o relatório de análise: {error}",

    "imap.worker.error_generic": "Ocorreu um erro: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "A ligar ao servidor IMAP...",
    "imap.tk.log_auth_classic": "Autenticação IMAP clássica...",
    "imap.tk.error_list_mailboxes_failed": "Não foi possível listar as pastas IMAP.",

    "imap.tk.log_folders_found_header": "Pastas encontradas no servidor:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "Total de pastas IMAP: {count}",

    "imap.tk.msgbox_error_title": "Erro",
    "imap.tk.msgbox_error_fetch_mailboxes": "Erro ao obter as pastas IMAP: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ Erro ao obter as pastas: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. Exportação IMAP",

    "imap.tk.label_server": "Servidor IMAP:",
    "imap.tk.label_email": "Endereço de email:",
    "imap.tk.label_password": "Palavra-passe:",
    "imap.tk.label_date_start": "Data de início (DD/MM/YYYY, opcional):",
    "imap.tk.label_date_end": "Data de fim (DD/MM/YYYY, opcional):",
    "imap.tk.label_log": "Log:",
    "imap.tk.label_mailboxes": "Pastas IMAP a exportar:",
    "imap.tk.checkbox_select_all": "Selecionar tudo / Desselecionar tudo",
    "imap.tk.label_progress": "Progresso:",

    "imap.tk.msgbox_missing_fields_title": "Campos em falta",
    "imap.tk.msgbox_missing_fields_text": "Preencha o servidor, o email e a palavra-passe.",

    "imap.tk.log_fetch_mailboxes_start": "A obter pastas IMAP...",
    "imap.tk.log_no_mailboxes_or_error": "Nenhuma pasta encontrada ou ocorreu um erro.",
    "imap.tk.log_select_mailboxes_hint": "Selecione as pastas a exportar.",

    "imap.tk.button_list_mailboxes": "Listar pastas IMAP",

    "imap.tk.msgbox_date_start_invalid_title": "Data de início inválida",
    "imap.tk.msgbox_date_start_invalid_text": "A data de início deve estar no formato DD/MM/YYYY.",

    "imap.tk.msgbox_date_end_invalid_title": "Data de fim inválida",
    "imap.tk.msgbox_date_end_invalid_text": "A data de fim deve estar no formato DD/MM/YYYY.",

    "imap.tk.msgbox_date_range_invalid_title": "Intervalo de datas inválido",
    "imap.tk.msgbox_date_range_invalid_text": (
        "A data de fim não pode ser anterior à data de início."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "Nenhuma pasta selecionada",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "Selecione pelo menos uma pasta IMAP (através de 'Listar pastas IMAP')."
    ),

    "imap.tk.log_export_start": "A iniciar a exportação...",
    "imap.tk.button_run_export": "Executar exportação (pastas selecionadas)",

    "imap.tk.log_stop_requested": (
        "Paragem solicitada, a exportação será terminada de forma limpa..."
    ),
    "imap.tk.button_stop_export": "Parar exportação",

    "imap.tk.msgbox_export_done_title": "Exportação concluída",


    # ------------------------------------------------------------------
    # IMAP logs
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "Conectando ao servidor IMAP para listar pastas…"
    ),
    "imap.log.fetch_error": "❌ Erro ao obter pastas:",
    "imap.log.no_mailboxes": "Nenhuma pasta IMAP encontrada nesta conta.",
    "imap.log.mailboxes_found": "Pastas encontradas no servidor:",
    "imap.log.mailboxes_total": "Total de pastas IMAP: {count}",
    "imap.log.mailboxes_select_hint": (
        "Selecione as pastas para extrair em modo somente leitura."
    ),
    "imap.log.start_export": (
        "Iniciando extração IMAP (modo forense, somente leitura)…"
    ),
    "imap.log.cancel_requested": (
        "Pedido de cancelamento enviado ao worker IMAP…"
    ),
    "imap.log.export_dir_saved": "Diretório de exportação salvo: {path}",
    "imap.log.done": "Processamento IMAP concluído.",

    # ------------------------------------------------------------------
    # Dashboard v3 – new sections
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "Níveis de suspeição",
    "dashboard.tab_text": "Resumo do índice EML",
    "dashboard.tab_graphs": "Gráficos",
    "dashboard.section_charts": "Visualizações gráficas",

    "dashboard.chart_suspicion_title": "Distribuição dos níveis de suspeição",
    "dashboard.chart_folders_title": "Emails por pasta IMAP",
    "dashboard.chart_domains_title": "Principais domínios remetentes",
    "dashboard.chart_attachments_title": "Presença de anexos",
    "dashboard.chart_axis_count": "Quantidade",
    "dashboard.chart_attachments_with": "Com anexos",
    "dashboard.chart_attachments_without": "Sem anexos",

    "dashboard.suspicion_distribution_line": (
        "Distribuição de emails por nível de suspeição:"
    ),
    "dashboard.suspicion_level.LOW": "Baixo",
    "dashboard.suspicion_level.MEDIUM": "Médio",
    "dashboard.suspicion_level.HIGH": "Alto",
    "dashboard.suspicion_level.CRITICAL": "Crítico",
    "dashboard.suspicion_level.UNKNOWN": "Desconhecido",

    "dashboard.chart.folders.title": "Emails por pasta IMAP",
    "dashboard.chart.domains.title": "Principais domínios remetentes",
    "dashboard.chart.attachments.title": "Presença de anexos",
    "dashboard.chart.auth.title": "Resultados DKIM / SPF / DMARC",
    "dashboard.chart.suspicion.title": "Distribuição por nível de suspeição",

    "dashboard.chart.no_data": (
        "Não há dados suficientes para exibir este gráfico."
    ),
    "dashboard.chart.axis.emails": "Número de emails",
    "dashboard.chart.axis.folders": "Pastas IMAP",
    "dashboard.chart.axis.domains": "Domínios",
    "dashboard.chart.axis.levels": "Níveis",

    "dashboard.legend.safe": "Área considerada majoritariamente segura",
    "dashboard.legend.suspicious": "Área a investigar primeiro",

    # ------------------------------------------------------------------
    # Viewer – scoring columns
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "Pontuação de suspeição",
    "viewer.col.suspicion_level": "Nível",
    "viewer.col.suspicion_reasons": "Motivos (resumo)",

    "viewer.score.tooltip.base": (
        "Pontuação global de suspeição baseada em DKIM/SPF/DMARC, "
        "anomalias Received, integridade de cabeçalhos e anexos."
    ),
    "viewer.score.level.LOW": (
        "Baixa suspeição: nada anormal detectado segundo as regras atuais."
    ),
    "viewer.score.level.MEDIUM": (
        "Suspeição média: alguns elementos devem ser verificados "
        "(cabeçalhos, autenticação ou anexos)."
    ),
    "viewer.score.level.HIGH": (
        "Alta suspeição: múltiplos indicadores técnicos inconsistentes ou perigosos."
    ),
    "viewer.score.level.CRITICAL": (
        "Suspeição crítica: email provavelmente malicioso ou forjado."
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth restrictions
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "Esta conta parece ser gerenciada por um provedor que requer "
        "mecanismos modernos (OAuth2, exportações oficiais) para acessar mensagens "
        "(ex.: Gmail, Outlook/Microsoft 365, Yahoo).\n\n"
        "Para permanecer em conformidade e evitar contornar estas regras, esta versão "
        "do eml_forensic_suite não realiza extração IMAP direta para esses serviços.\n\n"
        "Para recuperar mensagens de forma compatível:\n"
        "  • Gmail: use Google Takeout para exportar a caixa (MBOX),\n"
        "    ou um cliente como Thunderbird para criar uma cópia local.\n"
        "  • Outlook / Microsoft 365: use a exportação do cliente Outlook (PST)\n"
        "    ou ferramentas de arquivamento da organização.\n"
        "  • Yahoo, etc.: use as ferramentas de exportação do provedor.\n\n"
        "Versões futuras do eml_forensic_suite buscarão analisar esses formatos "
        "(MBOX, PST, etc.) diretamente."
    ),

    # ------------------------------------------------------------------
    # Viewer – search mini-language
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "Mini-linguagem forense:\n"
        "  from:alice@example.com\n"
        "  domain:banco.com\n"
        "  folder:\"INBOX/Importante\"\n"
        "  attachment:true\n"
        "Operadores: AND implícito, OR, NOT, parênteses."
    ),

    # ------------------------------------------------------------------
    # Viewer – CSV/index generic
    # ------------------------------------------------------------------
    "viewer.no_index_title": "Nenhum índice disponível",
    "viewer.no_index_body": (
        "Nenhum índice está disponível nesta sessão.\n"
        "Gere um índice na aba 2 ou abra um CSV manualmente."
    ),
    "viewer.open_csv_title": "Abrir arquivo CSV de índice",
    "viewer.error_csv_title": "Erro ao ler CSV",
    "viewer.error_csv_body": (
        "Não foi possível ler o arquivo CSV: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – preview
    # ------------------------------------------------------------------
    "viewer.attach.preview": "Pré-visualização (somente leitura)",
    "viewer.attach.preview_failed_title": "Falha na pré-visualização",
    "viewer.attach.preview_failed_body": (
        "Não foi possível exibir uma pré-visualização deste anexo."
    ),
    "viewer.attach.preview_unsupported_title": "Tipo não suportado",
    "viewer.attach.preview_unsupported_body": (
        "Não há pré-visualização disponível para este tipo MIME: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – attachments extraction
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "Nenhuma mensagem",
    "viewer.attach.no_msg_body": "Nenhuma mensagem está selecionada.",
    "viewer.attach.no_selection_title": "Nenhum anexo selecionado",
    "viewer.attach.no_selection_body": (
        "Por favor selecione um anexo na lista."
    ),
    "viewer.attach.no_root_title": "Diretório de trabalho não encontrado",
    "viewer.attach.no_root_body": (
        "Nenhum diretório forense / índice configurado para extração."
    ),
    "viewer.attach.extract_one_title": "Anexo extraído",
    "viewer.attach.extract_one_body": (
        "O anexo foi extraído para:\n{path}"
    ),
    "viewer.attach.extract_all_title": "Anexos extraídos",
    "viewer.attach.extract_all_body": (
        "{count} anexos foram extraídos:\n{paths}"
    ),

    # ------------------------------------------------------------------
    # Viewer – extraction buttons
    # ------------------------------------------------------------------
    "viewer.attach.extract_one": "Extrair anexo selecionado",
    "viewer.attach.extract_all": "Extrair todos os anexos",

    # ------------------------------------------------------------------
    # About box
    # ------------------------------------------------------------------
    "about.version_label": "Versão:",
    "about.description": (
        "Ferramenta somente leitura para análise forense de emails EML/IMAP."
    ),
}
