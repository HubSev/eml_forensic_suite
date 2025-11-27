from __future__ import annotations

from typing import Dict

TRANSLATIONS_ZH: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "EML / IMAP 取证套件（只读）",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "文件",
    "menu.view": "视图",
    "menu.help": "帮助",

    "menu.file.settings": "设置…",
    "menu.file.quit": "退出",

    "menu.view.theme.dark": "深色主题",
    "menu.view.theme.light": "浅色主题",

    "menu.help.about": "关于…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. IMAP 导出",
    "tab.index": "2. EML 索引",
    "tab.viewer": "3. 取证查看器",
    "tab.dashboard": "4. 取证仪表盘",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "设置",
    "settings.reports_dir.label": "工作 / 报告目录：",
    "settings.reports_dir.browse": "浏览…",
    "settings.language.label": "界面语言：",
    "settings.reports_dir.dialog_title": "选择工作 / 报告目录",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "就绪。",
    "status.settings.saved": "设置已保存。",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "EML 导出目录：",
    "index.browse": "浏览…",
    "index.use_last_export": "使用上一次 IMAP 导出",
    "index.log_placeholder": "EML 索引日志（只读）…",
    "index.start_button": "开始 EML 索引",
    "index.dialog_select_folder": "选择 EML 导出文件夹",
    "index.no_last_export": "尚无 IMAP 导出记录（见选项卡 1）。",
    "index.error_already_running_title": "索引已在运行",
    "index.error_already_running_body": "已有 EML 索引操作正在运行。",
    "index.error_no_folder_title": "缺少文件夹",
    "index.error_no_folder_body": "请选择包含 .eml 文件的文件夹。",
    "index.error_invalid_folder_title": "无效文件夹",
    "index.error_invalid_folder_body": "指定的文件夹不存在：\n{folder}",
    "index.status_selected_folder": "已选择用于索引的文件夹：{folder}",
    "index.error_indexing_title": "索引过程中出错",
    "index.error_log": "❌ 错误：{error}",
    "index.done_log_success": "\n索引已成功完成。",
    "index.done_log_path": "CSV 路径：{csv_path}",
    "index.done_log_count": "索引条目数量：{count}",
    "index.done_msg_title": "索引完成",
    "index.done_msg_body": (
        "EML 索引已完成。\n\nCSV 文件：{csv_path}\n条目：{count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "使用上一次索引",
    "dashboard.open_csv": "打开索引 CSV…",
    "dashboard.placeholder": "基于 EML 索引的取证统计摘要…",
    "dashboard.source_memory": "来源：内存索引（本会话最近索引）。",
    "dashboard.source_csv": "来源：{path}",
    "dashboard.no_index_title": "无索引",
    "dashboard.no_index_body": (
        "本会话中没有可用索引。\n"
        "请在选项卡 2 生成索引或手动打开 CSV。"
    ),
    "dashboard.dialog_open_csv": "打开索引 CSV 文件",
    "dashboard.error_csv_missing_title": "文件未找到",
    "dashboard.error_csv_missing_body": "指定文件不存在：\n{path}",
    "dashboard.error_csv_read_title": "CSV 读取错误",
    "dashboard.error_csv_read_body": "无法读取 CSV 文件：{path}",
    "dashboard.empty_csv_title": "空索引",
    "dashboard.empty_csv_body": "CSV 文件不包含可用条目。",
    "dashboard.no_data": "没有可分析的数据。",

    "dashboard.section_overview": "概览",
    "dashboard.overview_line": (
        "邮件总数：{total} – 不同发件人：{senders}"
    ),
    "dashboard.dates_line": "覆盖时间段：{date_min} → {date_max}",
    "dashboard.dates_unknown": "日期不可用或无法解析。",

    "dashboard.section_folders": "按 IMAP 文件夹分布",
    "dashboard.no_folders": "未检测到 IMAP 文件夹。",

    "dashboard.section_domains": "按域名分布（发件人）",
    "dashboard.no_domains": "未检测到域名。",

    "dashboard.section_attachments": "附件",
    "dashboard.attachments_line": (
        "有附件的邮件：{with_att}/{total} – 估计附件总数：{total_att}"
    ),

    "dashboard.section_auth": "身份验证（DKIM / SPF / DMARC）",
    "dashboard.auth_header_dkim": "DKIM 结果：",
    "dashboard.auth_header_spf": "SPF 结果：",
    "dashboard.auth_header_dmarc": "DMARC 结果：",

    "dashboard.section_integrity": "完整性 / 缺失头部",
    "dashboard.integrity_flags_title": "检测到的完整性标记：",
    "dashboard.no_integrity_flags": "未检测到特定完整性标记。",

    "dashboard.section_received": "Received 链异常",
    "dashboard.no_received_anomalies": (
        "未检测到 Received 异常（当前规则下）。"
    ),

    # ------------------------------------------------------------------
    # Viewer tab – base columns
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "IMAP 文件夹",
    "viewer.col.sequence_number": "序号",
    "viewer.col.date_header": "日期",
    "viewer.col.from_header": "发件人",
    "viewer.col.to_header": "收件人",
    "viewer.col.cc_header": "抄送",
    "viewer.col.cci_header": "密送",
    "viewer.col.subject": "主题",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "有附件？",
    "viewer.col.attachment_count": "附件数量",
    "viewer.col.attachment_filenames": "附件名称",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results（摘录）",
    "viewer.col.received_count": "Received 数量",
    "viewer.col.received_anomalies": "Received 异常",
    "viewer.col.integrity_flags": "完整性标记",
    "viewer.col.relative_path": "相对路径",
    "viewer.col.filename": "文件名",

    # ------------------------------------------------------------------
    # Viewer – search + zones
    # ------------------------------------------------------------------
    "viewer.search_label": "搜索：",
    "viewer.search_placeholder": "在索引中筛选（所有列）…",
    "viewer.search_clear": "清除",

    "viewer.headers_label": "头部",
    "viewer.headers_placeholder": "所选邮件的头部…",

    "viewer.body_label": "正文（文本）",
    "viewer.body_placeholder": (
        "text/plain 正文（或原始 HTML 备选）…"
    ),

    "viewer.btn_load_last": "使用上一次 IMAP 导出",
    "viewer.btn_open_csv": "打开索引 CSV...",
    "viewer.attachments_label": "附件",

    # ------------------------------------------------------------------
    # Viewer – EML errors
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "未找到 EML 文件",
    "viewer.error_missing_eml_body": "无法在磁盘上找到 EML 文件：\n{path}",
    "viewer.error_parse_eml_title": "EML 读取错误",
    "viewer.error_parse_eml_body": "无法解析 EML 文件：{path}",

    # ------------------------------------------------------------------
    # Viewer – attachment columns
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "名称",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "大小（字节）",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "可疑？",

    "viewer.attach.yes": "是",
    "viewer.attach.no": "否",

    # ------------------------------------------------------------------
    # IMAP tab – connection & fields
    # ------------------------------------------------------------------
    "imap.group.connection": "IMAP 服务器（证据来源）",
    "imap.label.host": "IMAP 服务器地址",
    "imap.label.user": "被分析的邮箱标识",
    "imap.label.password": "密码（从不保存）",
    "imap.label.date_start": "开始日期（取证过滤）",
    "imap.label.date_end": "结束日期（取证过滤）",

    "imap.placeholder.host": "如 imap.example.com",
    "imap.placeholder.user": "如 incident@company.com",
    "imap.placeholder.password": "被分析账户的密码",
    "imap.placeholder.date_start": "DD/MM/YYYY（可选）",
    "imap.placeholder.date_end": "DD/MM/YYYY（可选）",

    "imap.button.fetch_mailboxes": "检查 IMAP 文件夹…",
    "imap.button.start_export": "开始取证提取",
    "imap.button.cancel_export": "取消提取",

    "imap.label.mailboxes_title": (
        "要提取的 IMAP 文件夹（证据来源）："
    ),
    "imap.checkbox.select_all": "选择所有文件夹",

    "imap.log.placeholder": (
        "IMAP 提取日志（只读，带时间戳）…"
    ),

    # ------------------------------------------------------------------
    # IMAP tab – errors / infos
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "设置不完整",
    "imap.error.missing_fields.body": (
        "请提供 IMAP 服务器、用户名和密码。"
    ),

    "imap.info.export_running.title": "提取已在运行",
    "imap.info.export_running.body": "已有 IMAP 提取正在运行。",

    "imap.error.date_invalid.title": "无效日期",
    "imap.error.date_invalid.body": "提供的日期有误：{error}",
    "imap.error.date_end_before_start.body": (
        "结束日期不能早于开始日期。"
    ),

    "imap.error.no_mailbox_selected.title": "未选择文件夹",
    "imap.error.no_mailbox_selected.body": (
        "请至少选择一个 IMAP 文件夹进行提取。"
    ),

    "imap.error.fetch_mailboxes.title": "IMAP 错误",
    "imap.error.fetch_mailboxes.body": (
        "无法检索 IMAP 文件夹：\n{error}"
    ),

    "imap.info.generic.title": "信息",
    "imap.error.generic.title": "错误",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "正在连接到 {host}:{port}（SSL={use_ssl}）...",
    "imap.log.connected": "已连接到 IMAP 服务器。",
    "imap.log.select_folder": "正在选择文件夹 \"{folder}\"...",
    "imap.log.folder_selected": "已选择文件夹 \"{folder}\"。",
    "imap.log.message_count": "共有 {count} 封邮件需要导出。",
    "imap.log.fetching": "正在获取 IMAP 邮件...",
    "imap.log.export_done": "IMAP 导出完成。",
    "imap.log.saving_to": "正在将邮件保存到 \"{output_dir}\"...",
    "imap.log.progress": "正在导出邮件 {current}/{total}...",
    "imap.log.skip_existing": "文件 \"{path}\" 已存在，跳过。",

    "imap.error.connect_failed": "无法连接到 {host}:{port}：{error}",
    "imap.error.login_failed": "IMAP 身份验证错误：{error}",
    "imap.error.select_failed": "无法选择文件夹 \"{folder}\"：{error}",
    "imap.error.fetch_failed": "获取邮件时发生错误：{error}",
    "imap.error.generic": "IMAP 导出过程中发生错误：{error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== IMAP 导出报告（只读）===",
    "imap.report.tool_line": "工具      : eml_forensic_suite – IMAP 导出",
    "imap.report.version_line": "版本      : {version}",
    "imap.report.folder_line": "文件夹    : {export_dir}",

    "imap.report.section_tool": "---- 工具信息 ----",
    "imap.report.tool_path": "工具路径           : {tool_path}",
    "imap.report.tool_hash": "工具 SHA-256       : {tool_hash}",

    "imap.report.section_env": "---- 运行环境 ----",
    "imap.report.env_os": "操作系统           : {os_system} {os_release}（{os_version}）/ {machine}",
    "imap.report.env_python": "Python 版本        : {python_version}",

    "imap.report.section_context": "---- IMAP / 账户上下文 ----",
    "imap.report.context_host": "IMAP 服务器 : {host}",
    "imap.report.context_user": "账户       : {user}",
    "imap.report.context_date_start": "请求的开始日期 : {date_start}",
    "imap.report.context_date_end": "请求的结束日期 : {date_end}",
    "imap.report.context_criteria": "IMAP 搜索条件 : {search_criteria}（按此发送至服务器）",

    "imap.report.selected_folders_title": "已选择的文件夹：",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- IMAP 服务器信息 ----",
    "imap.report.server_greeting": "IMAP 欢迎信息 : {greeting}",
    "imap.report.server_capability": "CAPABILITY   : {capability}",

    "imap.report.section_timestamps": "---- 分析时间戳 ----",
    "imap.report.timestamp_start_utc": "分析开始（UTC）     : {dt}",
    "imap.report.timestamp_start_local": "分析开始（本地）    : {dt}",
    "imap.report.timestamp_end_utc": "分析结束（UTC）     : {dt}",
    "imap.report.timestamp_end_local": "分析结束（本地）    : {dt}",
    "imap.report.duration": "总时长              : {duration}",

    "imap.report.section_folders": "---- 已分析的文件夹 ----",
    "imap.report.folders_count": "已选择的文件夹数量 : {count}",

    "imap.report.folder_header": "文件夹 : {name}",
    "imap.report.folder_messages": "  在该时间段内找到的邮件数 : {count}",
    "imap.report.folder_exported": "  已导出的邮件数           : {count}",
    "imap.report.folder_errors": "  获取错误数               : {count}",
    "imap.report.folder_bytes": "  下载的数据量             : {bytes} 字节",
    "imap.report.folder_size_stats": "  最小/最大/平均大小       : {min_size} / {max_size} / {avg_size} 字节",
    "imap.report.folder_period": "  覆盖的时间段（INTERNALDATE）: {first} → {last}",
    "imap.report.folder_error_uids": "  出错的 UID（非完整列表）    : {uids}",

    "imap.report.section_totals": "---- 全局汇总 ----",
    "imap.report.total_messages": "找到的邮件总数（所有文件夹）: {count}",
    "imap.report.total_exported": "已导出的邮件总数            : {count}",
    "imap.report.total_errors": "获取错误总数                : {count}",
    "imap.report.total_bytes": "总下载数据量                : {bytes} 字节",

    "imap.report.section_forensic": "---- 方法论与取证保证 ----",
    "imap.report.forensic_item_readonly": "- 本工具仅使用 IMAP 只读命令（SELECT readonly、SEARCH、FETCH）。在分析过程中，没有任何邮件被修改、删除或标记为已读。",
    "imap.report.forensic_item_eml": "- 邮件完全按照 IMAP 服务器提供的内容导出，并以 .eml 文件写入磁盘，其内容不会被修改。",
    "imap.report.forensic_item_hashes": "- 每封导出的邮件都关联一个列在 hashes.txt 中的 SHA-256 哈希，同时还计算了由所有单个哈希串联得到的全局哈希。",
    "imap.report.forensic_item_report_hash": "- 本分析报告本身也通过 SHA-256 进行哈希，该哈希同样被写入 hashes.txt，用于保证报告的完整性。",

    "imap.report.hashes_report_header": "分析报告：",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "未选择任何文件夹。",
    "imap.worker.log_export_dir": "导出文件夹: {export_dir}",
    "imap.worker.tool_hash_error": "（计算工具哈希时发生错误）",

    "imap.worker.log_connecting": "正在连接到 IMAP 服务器...",
    "imap.worker.greeting_not_available": "（IMAP 欢迎信息不可用）",
    "imap.worker.log_auth_classic": "经典 IMAP 身份验证...",
    "imap.worker.error_auth_failed": "IMAP 身份验证错误：{error}",
    "imap.worker.capability_error": "（执行 CAPABILITY 命令时发生错误）",

    "imap.worker.log_date_start_inclusive": "开始日期（包含）: {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "开始日期：未设置 → 从第一封可用邮件开始提取。",
    "imap.worker.date_start_unset_label": "第一封可用邮件（无下限）",

    "imap.worker.log_date_end_inclusive": "结束日期（包含）: {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "结束日期：未设置 → 一直到服务器上可用的最后日期。",
    "imap.worker.date_end_unset_label": "最后一封可用邮件（无上限）",

    "imap.worker.log_criteria": "使用的 IMAP 搜索条件: {criteria}",
    "imap.worker.log_selected_folders_header": "已选择的文件夹（{count} 个）：",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "在计数阶段收到停止请求。",
    "imap.worker.log_phase1_count": "[第 1 阶段] 正在统计 {folder} 中的邮件数...",
    "imap.worker.log_select_folder_failed": "  ⚠️ 无法选择此文件夹，跳过。",
    "imap.worker.log_search_folder_failed": "  ⚠️ 在此文件夹中搜索时发生错误，跳过。",
    "imap.worker.log_messages_to_process": "  → {folder} 中有 {count} 封邮件需要处理",

    "imap.worker.log_total_messages_to_download": "需下载的邮件总数（所有文件夹）: {count}",

    "imap.worker.log_stop_during_export": "收到停止请求：正在中止导出。",
    "imap.worker.log_folder_header": "=== 文件夹: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  在此时间段内，{folder} 中没有邮件。",
    "imap.worker.log_folder_message_count": "  在 {folder} 中找到的邮件数: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ 无法重新选择此文件夹，跳过。",

    "imap.worker.log_first_message_download": "  正在下载第一封邮件（{uid}）...",
    "imap.worker.log_folder_progress": "  文件夹 {folder} 进度: {current}/{total}（最后一封: {last_uid}）",
    "imap.worker.log_fetch_error_message": "    ⚠️ 获取邮件 {uid} 时发生错误，继续。",
    "imap.worker.log_folder_end": "  文件夹 {folder} 结束",

    "imap.worker.hashes_header": "已导出文件及其 SHA-256 哈希列表",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "全局哈希（仅邮件）：",

    "imap.worker.log_export_done_header": "=== 导出完成 ===",
    "imap.worker.log_export_done_count": "导出的邮件总数: {count}",
    "imap.worker.log_export_done_hashes_file": "哈希文件: {path}",
    "imap.worker.log_export_done_hash": "全局哈希: {file_hash}",

    "imap.worker.summary": (
        "导出完成。\n\n"
        "导出的邮件数: {count}\n"
        "文件夹: {export_dir}\n\n"
        "全局哈希（邮件）:\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "分析报告已生成并计算哈希（参见 rapport_imap_export.txt 和 hashes.txt）。",
    "imap.worker.log_report_failed": "⚠️ 无法生成分析报告: {error}",

    "imap.worker.error_generic": "发生错误: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "正在连接到 IMAP 服务器...",
    "imap.tk.log_auth_classic": "经典 IMAP 身份验证...",
    "imap.tk.error_list_mailboxes_failed": "无法列出 IMAP 文件夹。",

    "imap.tk.log_folders_found_header": "服务器上找到的文件夹：",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "IMAP 文件夹总数: {count}",

    "imap.tk.msgbox_error_title": "错误",
    "imap.tk.msgbox_error_fetch_mailboxes": "获取 IMAP 文件夹时发生错误: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ 获取文件夹时发生错误: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. IMAP 导出",

    "imap.tk.label_server": "IMAP 服务器：",
    "imap.tk.label_email": "电子邮件地址：",
    "imap.tk.label_password": "密码：",
    "imap.tk.label_date_start": "开始日期（DD/MM/YYYY，可选）：",
    "imap.tk.label_date_end": "结束日期（DD/MM/YYYY，可选）：",
    "imap.tk.label_log": "日志：",
    "imap.tk.label_mailboxes": "要导出的 IMAP 文件夹：",
    "imap.tk.checkbox_select_all": "全选 / 全不选",
    "imap.tk.label_progress": "进度：",

    "imap.tk.msgbox_missing_fields_title": "缺少字段",
    "imap.tk.msgbox_missing_fields_text": "请填写服务器、邮箱和密码。",

    "imap.tk.log_fetch_mailboxes_start": "正在获取 IMAP 文件夹...",
    "imap.tk.log_no_mailboxes_or_error": "未找到任何文件夹或发生错误。",
    "imap.tk.log_select_mailboxes_hint": "请选择要导出的文件夹。",

    "imap.tk.button_list_mailboxes": "列出 IMAP 文件夹",

    "imap.tk.msgbox_date_start_invalid_title": "无效的开始日期",
    "imap.tk.msgbox_date_start_invalid_text": "开始日期必须为 DD/MM/YYYY 格式。",

    "imap.tk.msgbox_date_end_invalid_title": "无效的结束日期",
    "imap.tk.msgbox_date_end_invalid_text": "结束日期必须为 DD/MM/YYYY 格式。",

    "imap.tk.msgbox_date_range_invalid_title": "无效的日期范围",
    "imap.tk.msgbox_date_range_invalid_text": (
        "结束日期不能早于开始日期。"
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "未选择任何文件夹",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "请至少选择一个 IMAP 文件夹（通过“列出 IMAP 文件夹”）。"
    ),

    "imap.tk.log_export_start": "正在开始导出...",
    "imap.tk.button_run_export": "运行导出（所选文件夹）",

    "imap.tk.log_stop_requested": (
        "已请求停止，导出将正常结束..."
    ),
    "imap.tk.button_stop_export": "停止导出",

    "imap.tk.msgbox_export_done_title": "导出完成",


    # ------------------------------------------------------------------
    # IMAP logs
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "正在连接 IMAP 服务器以列出文件夹…"
    ),
    "imap.log.fetch_error": "❌ 获取文件夹时出错：",
    "imap.log.no_mailboxes": "此账户未找到 IMAP 文件夹。",
    "imap.log.mailboxes_found": "服务器上找到的文件夹：",
    "imap.log.mailboxes_total": "IMAP 文件夹总数：{count}",
    "imap.log.mailboxes_select_hint": (
        "请选择要以只读模式提取的文件夹。"
    ),
    "imap.log.start_export": (
        "正在开始 IMAP 提取（取证模式，只读）…"
    ),
    "imap.log.cancel_requested": (
        "已向 IMAP 工作线程发送取消请求…"
    ),
    "imap.log.export_dir_saved": "导出目录已保存：{path}",
    "imap.log.done": "IMAP 处理已完成。",

    # ------------------------------------------------------------------
    # Dashboard v3
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "可疑级别",
    "dashboard.tab_text": "EML 索引摘要",
    "dashboard.tab_graphs": "图表",
    "dashboard.section_charts": "图形可视化",

    "dashboard.chart_suspicion_title": "可疑级别分布",
    "dashboard.chart_folders_title": "每个 IMAP 文件夹的邮件数量",
    "dashboard.chart_domains_title": "主要发件域名",
    "dashboard.chart_attachments_title": "附件情况",
    "dashboard.chart_axis_count": "数量",
    "dashboard.chart_attachments_with": "有附件",
    "dashboard.chart_attachments_without": "无附件",

    "dashboard.suspicion_distribution_line": (
        "按可疑级别分类的邮件分布："
    ),
    "dashboard.suspicion_level.LOW": "低",
    "dashboard.suspicion_level.MEDIUM": "中",
    "dashboard.suspicion_level.HIGH": "高",
    "dashboard.suspicion_level.CRITICAL": "严重",
    "dashboard.suspicion_level.UNKNOWN": "未知",

    "dashboard.chart.folders.title": "每个 IMAP 文件夹的邮件数量",
    "dashboard.chart.domains.title": "主要发件域名",
    "dashboard.chart.attachments.title": "附件情况",
    "dashboard.chart.auth.title": "DKIM / SPF / DMARC 结果",
    "dashboard.chart.suspicion.title": "按可疑级别分布",

    "dashboard.chart.no_data": "数据不足，无法显示此图表。",
    "dashboard.chart.axis.emails": "邮件数量",
    "dashboard.chart.axis.folders": "IMAP 文件夹",
    "dashboard.chart.axis.domains": "域名",
    "dashboard.chart.axis.levels": "级别",

    "dashboard.legend.safe": "主要被视为安全的区域",
    "dashboard.legend.suspicious": "优先调查区域",

    # ------------------------------------------------------------------
    # Viewer – scoring & suspicion columns
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "可疑评分",
    "viewer.col.suspicion_level": "级别",
    "viewer.col.suspicion_reasons": "原因（摘要）",

    "viewer.score.tooltip.base": (
        "全局可疑评分基于 DKIM/SPF/DMARC、Received 异常、头部完整性和附件。"
    ),
    "viewer.score.level.LOW": (
        "低可疑：在当前规则下未检测到异常。"
    ),
    "viewer.score.level.MEDIUM": (
        "中等可疑：某些元素需检查（头部、身份验证或附件）。"
    ),
    "viewer.score.level.HIGH": (
        "高可疑：多个技术指标不一致或具有风险。"
    ),
    "viewer.score.level.CRITICAL": (
        "严重可疑：邮件极有可能是恶意或伪造的。"
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth restrictions
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "此账户似乎属于需要现代机制（OAuth2、官方导出）的提供商\n"
        "（如 Gmail、Outlook/Microsoft 365、Yahoo）。\n\n"
        "为了保持合规并避免绕过这些规则，本版本的 eml_forensic_suite\n"
        "不会对这些服务执行直接 IMAP 提取。\n\n"
        "兼容的邮件获取方式：\n"
        "  • Gmail：使用 Google Takeout 导出邮箱（MBOX），\n"
        "    或使用 Thunderbird 创建本地副本。\n"
        "  • Outlook / Microsoft 365：使用 Outlook 客户端导出（PST）\n"
        "    或组织的归档工具。\n"
        "  • Yahoo 等：使用提供商提供的导出工具。\n\n"
        "未来版本将支持直接分析这些导出格式（MBOX、PST 等）。"
    ),

    # ------------------------------------------------------------------
    # Viewer – search mini-language
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "取证迷你查询语言：\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "运算符：隐式 AND、OR、NOT、括号。"
    ),

    # ------------------------------------------------------------------
    # Viewer – CSV / index messages
    # ------------------------------------------------------------------
    "viewer.no_index_title": "无可用索引",
    "viewer.no_index_body": (
        "本会话中无可用索引。\n"
        "请在选项卡 2 生成索引或手动打开 CSV 文件。"
    ),
    "viewer.open_csv_title": "打开索引 CSV 文件",
    "viewer.error_csv_title": "CSV 读取错误",
    "viewer.error_csv_body": (
        "无法读取 CSV 文件：{path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – preview
    # ------------------------------------------------------------------
    "viewer.attach.preview": "只读预览",
    "viewer.attach.preview_failed_title": "预览失败",
    "viewer.attach.preview_failed_body": (
        "无法显示该附件的预览。"
    ),
    "viewer.attach.preview_unsupported_title": "不支持的类型",
    "viewer.attach.preview_unsupported_body": (
        "无内置预览可显示此 MIME 类型：{mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – extraction
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "无邮件",
    "viewer.attach.no_msg_body": "当前未选择任何邮件。",
    "viewer.attach.no_selection_title": "未选择附件",
    "viewer.attach.no_selection_body": (
        "请在列表中选择一个附件。"
    ),
    "viewer.attach.no_root_title": "找不到工作目录",
    "viewer.attach.no_root_body": (
        "未配置用于附件提取的取证/索引目录。"
    ),
    "viewer.attach.extract_one_title": "附件已提取",
    "viewer.attach.extract_one_body": (
        "附件已提取到：\n{path}"
    ),
    "viewer.attach.extract_all_title": "附件已提取",
    "viewer.attach.extract_all_body": (
        "已提取 {count} 个附件：\n{paths}"
    ),

    "viewer.attach.extract_one": "提取所选附件",
    "viewer.attach.extract_all": "提取全部附件",

    # ------------------------------------------------------------------
    # About
    # ------------------------------------------------------------------
    "about.version_label": "版本：",
    "about.description": (
        "用于对 EML/IMAP 邮件进行取证分析的只读工具。"
    ),
}
