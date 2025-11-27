from __future__ import annotations
from typing import Dict

TRANSLATIONS_JA: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "EML / IMAP フォレンジックスイート（読み取り専用）",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "ファイル",
    "menu.view": "表示",
    "menu.help": "ヘルプ",

    "menu.file.settings": "設定…",
    "menu.file.quit": "終了",

    "menu.view.theme.dark": "ダークテーマ",
    "menu.view.theme.light": "ライトテーマ",

    "menu.help.about": "バージョン情報…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. IMAP エクスポート",
    "tab.index": "2. EML インデックス作成",
    "tab.viewer": "3. フォレンジックビューア",
    "tab.dashboard": "4. フォレンジックダッシュボード",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "設定",
    "settings.reports_dir.label": "作業 / レポートディレクトリ:",
    "settings.reports_dir.browse": "参照…",
    "settings.language.label": "インターフェース言語:",
    "settings.reports_dir.dialog_title": "作業 / レポートディレクトリを選択",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "準備完了。",
    "status.settings.saved": "設定を保存しました。",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "EML エクスポートディレクトリ:",
    "index.browse": "参照…",
    "index.use_last_export": "前回の IMAP エクスポートを使用",
    "index.log_placeholder": "EML インデックス作成ログ（読み取り専用）…",
    "index.start_button": "EML インデックスを開始",
    "index.dialog_select_folder": "EML エクスポートフォルダを選択",
    "index.no_last_export": "まだ IMAP エクスポートがありません（タブ1）。",
    "index.error_already_running_title": "インデックス作成中",
    "index.error_already_running_body": "すでに EML インデックス作成が実行中です。",
    "index.error_no_folder_title": "フォルダが未選択",
    "index.error_no_folder_body": ".eml ファイルを含むフォルダを選択してください。",
    "index.error_invalid_folder_title": "無効なフォルダ",
    "index.error_invalid_folder_body": "指定されたフォルダが存在しません:\n{folder}",
    "index.status_selected_folder": "インデックス作成対象フォルダ: {folder}",
    "index.error_indexing_title": "インデックス作成中のエラー",
    "index.error_log": "❌ エラー: {error}",
    "index.done_log_success": "\nインデックス作成が正常に完了しました。",
    "index.done_log_path": "CSV パス: {csv_path}",
    "index.done_log_count": "インデックス登録件数: {count}",
    "index.done_msg_title": "インデックス完了",
    "index.done_msg_body": (
        "EML インデックス作成が完了しました。\n\nCSV ファイル: {csv_path}\n件数: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "前回のインデックスを使用",
    "dashboard.open_csv": "インデックス CSV を開く…",
    "dashboard.placeholder": "EML インデックスに基づくフォレンジック統計概要…",
    "dashboard.source_memory": "ソース：メモリ内インデックス（本セッション内の最新インデックス）。",
    "dashboard.source_csv": "ソース：{path}",
    "dashboard.no_index_title": "インデックスなし",
    "dashboard.no_index_body": (
        "このセッションにはインデックスがありません。\n"
        "タブ2でインデックスを生成するか、CSV を手動で開いてください。"
    ),
    "dashboard.dialog_open_csv": "インデックス CSV ファイルを開く",
    "dashboard.error_csv_missing_title": "ファイルが見つかりません",
    "dashboard.error_csv_missing_body": "指定されたファイルが存在しません:\n{path}",
    "dashboard.error_csv_read_title": "CSV 読み取りエラー",
    "dashboard.error_csv_read_body": "CSV ファイルを読み取れません: {path}",
    "dashboard.empty_csv_title": "空のインデックス",
    "dashboard.empty_csv_body": "CSV に使用可能なエントリが含まれていません。",
    "dashboard.no_data": "分析するデータがありません。",

    "dashboard.section_overview": "概要",
    "dashboard.overview_line": (
        "総メール数: {total} – 送信者数（ユニーク）: {senders}"
    ),
    "dashboard.dates_line": "対象期間: {date_min} → {date_max}",
    "dashboard.dates_unknown": "日付情報が無効または解析不能です。",

    "dashboard.section_folders": "IMAP フォルダ別分布",
    "dashboard.no_folders": "IMAP フォルダが検出されませんでした。",

    "dashboard.section_domains": "ドメイン別分布（送信者）",
    "dashboard.no_domains": "ドメインが検出されませんでした。",

    "dashboard.section_attachments": "添付ファイル",
    "dashboard.attachments_line": (
        "添付ありメール: {with_att}/{total} – 推定添付数: {total_att}"
    ),

    "dashboard.section_auth": "認証（DKIM / SPF / DMARC）",
    "dashboard.auth_header_dkim": "DKIM 結果:",
    "dashboard.auth_header_spf": "SPF 結果:",
    "dashboard.auth_header_dmarc": "DMARC 結果:",

    "dashboard.section_integrity": "整合性 / 欠落ヘッダー",
    "dashboard.integrity_flags_title": "検出された整合性フラグ:",
    "dashboard.no_integrity_flags": "特別な整合性フラグは検出されませんでした。",

    "dashboard.section_received": "Received チェーンの異常",
    "dashboard.no_received_anomalies": (
        "現在のルールでは異常は検出されていません。"
    ),

    # ------------------------------------------------------------------
    # Viewer tab – base columns
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "IMAP フォルダ",
    "viewer.col.sequence_number": "シーケンス",
    "viewer.col.date_header": "日付",
    "viewer.col.from_header": "差出人",
    "viewer.col.to_header": "宛先",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Bcc",
    "viewer.col.subject": "件名",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "添付あり？",
    "viewer.col.attachment_count": "添付数",
    "viewer.col.attachment_filenames": "添付ファイル名",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results（抜粋）",
    "viewer.col.received_count": "Received 数",
    "viewer.col.received_anomalies": "Received 異常",
    "viewer.col.integrity_flags": "整合性フラグ",
    "viewer.col.relative_path": "相対パス",
    "viewer.col.filename": "ファイル名",

    # ------------------------------------------------------------------
    # Viewer – search
    # ------------------------------------------------------------------
    "viewer.search_label": "検索:",
    "viewer.search_placeholder": "インデックスをフィルタ（全列）…",
    "viewer.search_clear": "クリア",

    "viewer.headers_label": "ヘッダー",
    "viewer.headers_placeholder": "選択したメッセージのヘッダー…",

    "viewer.body_label": "本文（テキスト）",
    "viewer.body_placeholder": (
        "text/plain 本文（または HTML 生データの代替）…"
    ),

    "viewer.btn_load_last": "前回の IMAP エクスポートを使用",
    "viewer.btn_open_csv": "インデックス CSV を開く...",
    "viewer.attachments_label": "添付ファイル",

    # ------------------------------------------------------------------
    # Viewer – EML errors
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "EML ファイルがありません",
    "viewer.error_missing_eml_body": "EML ファイルが見つかりません:\n{path}",
    "viewer.error_parse_eml_title": "EML 読み取りエラー",
    "viewer.error_parse_eml_body": "EML ファイルを解析できません:\n{path}",

    # ------------------------------------------------------------------
    # Viewer – attachment columns
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "名前",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "サイズ（バイト）",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "不審？",

    "viewer.attach.yes": "はい",
    "viewer.attach.no": "いいえ",

    # ------------------------------------------------------------------
    # IMAP tab – configuration fields
    # ------------------------------------------------------------------
    "imap.group.connection": "IMAP サーバ（証拠ソース）",
    "imap.label.host": "IMAP サーバアドレス",
    "imap.label.user": "解析対象メールアドレス",
    "imap.label.password": "パスワード（保存されません）",
    "imap.label.date_start": "開始日（フォレンジックフィルタ）",
    "imap.label.date_end": "終了日（フォレンジックフィルタ）",

    "imap.placeholder.host": "例: imap.example.com",
    "imap.placeholder.user": "例: incident@company.com",
    "imap.placeholder.password": "解析対象アカウントのパスワード",
    "imap.placeholder.date_start": "DD/MM/YYYY（任意）",
    "imap.placeholder.date_end": "DD/MM/YYYY（任意）",

    "imap.button.fetch_mailboxes": "IMAP フォルダを確認…",
    "imap.button.start_export": "フォレンジック抽出を開始",
    "imap.button.cancel_export": "抽出をキャンセル",

    "imap.label.mailboxes_title": "抽出する IMAP フォルダ（証拠ソース）:",
    "imap.checkbox.select_all": "すべて選択",

    "imap.log.placeholder": "IMAP 抽出ログ（読み取り専用、タイムスタンプ付）…",

    # ------------------------------------------------------------------
    # IMAP tab – errors
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "設定が不完全です",
    "imap.error.missing_fields.body": (
        "IMAP サーバ、ユーザ名、パスワードを入力してください。"
    ),

    "imap.info.export_running.title": "抽出実行中",
    "imap.info.export_running.body": "IMAP 抽出がすでに実行中です。",

    "imap.error.date_invalid.title": "無効な日付",
    "imap.error.date_invalid.body": "入力日付に誤りがあります: {error}",
    "imap.error.date_end_before_start.body": (
        "終了日は開始日より前にはできません。"
    ),

    "imap.error.no_mailbox_selected.title": "フォルダ未選択",
    "imap.error.no_mailbox_selected.body": (
        "少なくとも 1 つの IMAP フォルダを選択してください。"
    ),

    "imap.error.fetch_mailboxes.title": "IMAP エラー",
    "imap.error.fetch_mailboxes.body": (
        "IMAP フォルダを取得できません:\n{error}"
    ),

    "imap.info.generic.title": "情報",
    "imap.error.generic.title": "エラー",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "{host}:{port} に接続しています (SSL={use_ssl})...",
    "imap.log.connected": "IMAP サーバーに接続しました。",
    "imap.log.select_folder": "フォルダー \"{folder}\" を選択しています...",
    "imap.log.folder_selected": "フォルダー \"{folder}\" を選択しました。",
    "imap.log.message_count": "エクスポートするメッセージ数: {count}",
    "imap.log.fetching": "IMAP メッセージを取得しています...",
    "imap.log.export_done": "IMAP エクスポートが完了しました。",
    "imap.log.saving_to": "メッセージを \"{output_dir}\" に保存しています...",
    "imap.log.progress": "メッセージ {current}/{total} をエクスポートしています...",
    "imap.log.skip_existing": "ファイル \"{path}\" は既に存在するためスキップします。",

    "imap.error.connect_failed": "{host}:{port} に接続できません: {error}",
    "imap.error.login_failed": "IMAP 認証エラー: {error}",
    "imap.error.select_failed": "フォルダー \"{folder}\" を選択できません: {error}",
    "imap.error.fetch_failed": "メッセージ取得中にエラーが発生しました: {error}",
    "imap.error.generic": "IMAP エクスポート中にエラーが発生しました: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== IMAP エクスポートレポート (読み取り専用) ===",
    "imap.report.tool_line": "ツール      : eml_forensic_suite – IMAP エクスポート",
    "imap.report.version_line": "バージョン   : {version}",
    "imap.report.folder_line": "フォルダー   : {export_dir}",

    "imap.report.section_tool": "---- ツール情報 ----",
    "imap.report.tool_path": "ツールのパス           : {tool_path}",
    "imap.report.tool_hash": "ツール SHA-256         : {tool_hash}",

    "imap.report.section_env": "---- 実行環境 ----",
    "imap.report.env_os": "オペレーティングシステム : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Python バージョン      : {python_version}",

    "imap.report.section_context": "---- IMAP / アカウントのコンテキスト ----",
    "imap.report.context_host": "IMAP サーバー : {host}",
    "imap.report.context_user": "アカウント    : {user}",
    "imap.report.context_date_start": "要求された開始日 : {date_start}",
    "imap.report.context_date_end": "要求された終了日 : {date_end}",
    "imap.report.context_criteria": "IMAP 検索条件 : {search_criteria} (サーバーに送信された形式)",

    "imap.report.selected_folders_title": "選択されたフォルダー:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- IMAP サーバー情報 ----",
    "imap.report.server_greeting": "IMAP バナー  : {greeting}",
    "imap.report.server_capability": "CAPABILITY   : {capability}",

    "imap.report.section_timestamps": "---- 解析タイムスタンプ ----",
    "imap.report.timestamp_start_utc": "解析開始 (UTC)        : {dt}",
    "imap.report.timestamp_start_local": "解析開始 (ローカル)   : {dt}",
    "imap.report.timestamp_end_utc": "解析終了 (UTC)        : {dt}",
    "imap.report.timestamp_end_local": "解析終了 (ローカル)   : {dt}",
    "imap.report.duration": "総所要時間             : {duration}",

    "imap.report.section_folders": "---- 解析対象フォルダー ----",
    "imap.report.folders_count": "選択されたフォルダー数 : {count}",

    "imap.report.folder_header": "フォルダー : {name}",
    "imap.report.folder_messages": "  期間内に見つかったメッセージ数 : {count}",
    "imap.report.folder_exported": "  エクスポートされたメッセージ数 : {count}",
    "imap.report.folder_errors": "  取得エラー                  : {count}",
    "imap.report.folder_bytes": "  ダウンロード量              : {bytes} バイト",
    "imap.report.folder_size_stats": "  最小 / 最大 / 平均サイズ     : {min_size} / {max_size} / {avg_size} バイト",
    "imap.report.folder_period": "  対象期間 (INTERNALDATE)      : {first} → {last}",
    "imap.report.folder_error_uids": "  エラーになった UID (抜粋)    : {uids}",

    "imap.report.section_totals": "---- 全体集計 ----",
    "imap.report.total_messages": "見つかったメッセージ総数 (全フォルダー) : {count}",
    "imap.report.total_exported": "エクスポートされたメッセージ総数       : {count}",
    "imap.report.total_errors": "取得エラー総数                         : {count}",
    "imap.report.total_bytes": "総ダウンロード量                      : {bytes} バイト",

    "imap.report.section_forensic": "---- 手法およびフォレンジック上の保証 ----",
    "imap.report.forensic_item_readonly": "- 本ツールは読み取り専用の IMAP コマンド (SELECT readonly, SEARCH, FETCH) のみを使用しました。解析中にメッセージが変更・削除・既読化されることは一切ありません。",
    "imap.report.forensic_item_eml": "- メッセージは IMAP サーバーから提供されたとおりの内容でエクスポートされ、内容を変更することなく .eml ファイルとしてディスクに保存されました。",
    "imap.report.forensic_item_hashes": "- それぞれのエクスポート済みメッセージには SHA-256 ハッシュが割り当てられ、hashes.txt に一覧として記録されています。さらに、すべての個別ハッシュを連結して算出したグローバルハッシュも保持されます。",
    "imap.report.forensic_item_report_hash": "- 本解析レポート自体も SHA-256 でハッシュ化され、その値はレポートの完全性を保証するために hashes.txt に追加されています。",

    "imap.report.hashes_report_header": "解析レポート:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "フォルダーが選択されていません。",
    "imap.worker.log_export_dir": "エクスポート先フォルダー: {export_dir}",
    "imap.worker.tool_hash_error": "(ツールのハッシュ計算中にエラー)",

    "imap.worker.log_connecting": "IMAP サーバーに接続しています...",
    "imap.worker.greeting_not_available": "(IMAP バナーは利用できません)",
    "imap.worker.log_auth_classic": "通常の IMAP 認証を実行しています...",
    "imap.worker.error_auth_failed": "IMAP 認証エラー: {error}",
    "imap.worker.capability_error": "(CAPABILITY コマンド実行中にエラー)",

    "imap.worker.log_date_start_inclusive": "開始日 (含む): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "開始日は未指定 → 利用可能な最初のメッセージから抽出します。",
    "imap.worker.date_start_unset_label": "利用可能な最初のメッセージ (下限なし)",

    "imap.worker.log_date_end_inclusive": "終了日 (含む): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "終了日は未指定 → サーバー上で利用可能な最新日付まで抽出します。",
    "imap.worker.date_end_unset_label": "利用可能な最後のメッセージ (上限なし)",

    "imap.worker.log_criteria": "使用した IMAP 検索条件: {criteria}",
    "imap.worker.log_selected_folders_header": "選択されたフォルダー ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "カウントフェーズ中に停止要求が行われました。",
    "imap.worker.log_phase1_count": "[フェーズ 1] {folder} 内のメッセージ数をカウント中...",
    "imap.worker.log_select_folder_failed": "  ⚠️ このフォルダーを選択できないためスキップします。",
    "imap.worker.log_search_folder_failed": "  ⚠️ このフォルダーの検索中にエラーが発生したためスキップします。",
    "imap.worker.log_messages_to_process": "  → {folder} で処理するメッセージ数: {count}",

    "imap.worker.log_total_messages_to_download": "ダウンロード対象メッセージ総数 (全フォルダー): {count}",

    "imap.worker.log_stop_during_export": "停止要求が行われました: エクスポートを中断します。",
    "imap.worker.log_folder_header": "=== フォルダー: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  この期間内には {folder} にメッセージがありません。",
    "imap.worker.log_folder_message_count": "  {folder} で見つかったメッセージ数: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ このフォルダーを再選択できないためスキップします。",

    "imap.worker.log_first_message_download": "  最初のメッセージをダウンロード中 ({uid})...",
    "imap.worker.log_folder_progress": "  フォルダー {folder} の進行状況: {current}/{total} (最後: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ メッセージ {uid} の取得中にエラーが発生しましたが、処理を続行します。",
    "imap.worker.log_folder_end": "  フォルダー {folder} の処理終了",

    "imap.worker.hashes_header": "エクスポートされたファイルとその SHA-256 ハッシュの一覧",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "グローバルハッシュ (メッセージのみ):",

    "imap.worker.log_export_done_header": "=== エクスポート完了 ===",
    "imap.worker.log_export_done_count": "エクスポートされたメッセージ総数: {count}",
    "imap.worker.log_export_done_hashes_file": "ハッシュファイル: {path}",
    "imap.worker.log_export_done_hash": "グローバルハッシュ: {file_hash}",

    "imap.worker.summary": (
        "エクスポートが完了しました。\n\n"
        "エクスポートされたメッセージ数: {count}\n"
        "フォルダー: {export_dir}\n\n"
        "グローバルハッシュ (メッセージ):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "解析レポートが生成されハッシュ化されました (rapport_imap_export.txt および hashes.txt を参照)。",
    "imap.worker.log_report_failed": "⚠️ 解析レポートを生成できませんでした: {error}",

    "imap.worker.error_generic": "エラーが発生しました: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "IMAP サーバーに接続しています...",
    "imap.tk.log_auth_classic": "通常の IMAP 認証を実行しています...",
    "imap.tk.error_list_mailboxes_failed": "IMAP フォルダーを一覧表示できません。",

    "imap.tk.log_folders_found_header": "サーバー上で見つかったフォルダー:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "IMAP フォルダー総数: {count}",

    "imap.tk.msgbox_error_title": "エラー",
    "imap.tk.msgbox_error_fetch_mailboxes": "IMAP フォルダー取得中にエラーが発生しました: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ フォルダー取得中にエラーが発生しました: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. IMAP エクスポート",

    "imap.tk.label_server": "IMAP サーバー:",
    "imap.tk.label_email": "メールアドレス:",
    "imap.tk.label_password": "パスワード:",
    "imap.tk.label_date_start": "開始日 (DD/MM/YYYY、省略可):",
    "imap.tk.label_date_end": "終了日 (DD/MM/YYYY、省略可):",
    "imap.tk.label_log": "ログ:",
    "imap.tk.label_mailboxes": "エクスポートする IMAP フォルダー:",
    "imap.tk.checkbox_select_all": "すべて選択 / すべて解除",
    "imap.tk.label_progress": "進行状況:",

    "imap.tk.msgbox_missing_fields_title": "未入力フィールド",
    "imap.tk.msgbox_missing_fields_text": "サーバー、メールアドレス、パスワードを入力してください。",

    "imap.tk.log_fetch_mailboxes_start": "IMAP フォルダーを取得しています...",
    "imap.tk.log_no_mailboxes_or_error": "フォルダーが見つからないか、エラーが発生しました。",
    "imap.tk.log_select_mailboxes_hint": "エクスポートするフォルダーを選択してください。",

    "imap.tk.button_list_mailboxes": "IMAP フォルダーを一覧表示",

    "imap.tk.msgbox_date_start_invalid_title": "開始日が無効です",
    "imap.tk.msgbox_date_start_invalid_text": "開始日は DD/MM/YYYY 形式で指定する必要があります。",

    "imap.tk.msgbox_date_end_invalid_title": "終了日が無効です",
    "imap.tk.msgbox_date_end_invalid_text": "終了日は DD/MM/YYYY 形式で指定する必要があります。",

    "imap.tk.msgbox_date_range_invalid_title": "日付範囲が無効です",
    "imap.tk.msgbox_date_range_invalid_text": (
        "終了日は開始日より前にはできません。"
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "フォルダーが選択されていません",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "「IMAP フォルダーを一覧表示」から少なくとも 1 つの IMAP フォルダーを選択してください。"
    ),

    "imap.tk.log_export_start": "エクスポートを開始します...",
    "imap.tk.button_run_export": "エクスポートを実行 (選択したフォルダー)",

    "imap.tk.log_stop_requested": (
        "停止要求を受信しました。エクスポートは正常に終了します..."
    ),
    "imap.tk.button_stop_export": "エクスポートを停止",

    "imap.tk.msgbox_export_done_title": "エクスポート完了",


    # ------------------------------------------------------------------
    # IMAP tab – logs
    # ------------------------------------------------------------------
    "imap.log.connect_list": "IMAP サーバに接続してフォルダ一覧を取得中…",
    "imap.log.fetch_error": "❌ フォルダ取得エラー:",
    "imap.log.no_mailboxes": "このアカウントの IMAP フォルダはありません。",
    "imap.log.mailboxes_found": "サーバで検出されたフォルダ:",
    "imap.log.mailboxes_total": "IMAP フォルダ総数: {count}",
    "imap.log.mailboxes_select_hint": "読み取り専用で抽出するフォルダを選択してください。",
    "imap.log.start_export": "IMAP フォレンジック抽出を開始（読み取り専用）…",
    "imap.log.cancel_requested": "抽出キャンセル要求を送信…",
    "imap.log.export_dir_saved": "エクスポートディレクトリ保存: {path}",
    "imap.log.done": "IMAP 処理完了。",

    # ------------------------------------------------------------------
    # Dashboard v3
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "疑わしさレベル",
    "dashboard.tab_text": "EML インデックス概要",
    "dashboard.tab_graphs": "グラフ",
    "dashboard.section_charts": "可視化",

    "dashboard.chart_suspicion_title": "疑わしさレベルの分布",
    "dashboard.chart_folders_title": "IMAP フォルダ別メール数",
    "dashboard.chart_domains_title": "送信者ドメイントップ",
    "dashboard.chart_attachments_title": "添付ファイルの有無",
    "dashboard.chart_axis_count": "件数",
    "dashboard.chart_attachments_with": "添付あり",
    "dashboard.chart_attachments_without": "添付なし",

    "dashboard.suspicion_distribution_line": "疑わしさレベル別のメール分布:",
    "dashboard.suspicion_level.LOW": "低",
    "dashboard.suspicion_level.MEDIUM": "中",
    "dashboard.suspicion_level.HIGH": "高",
    "dashboard.suspicion_level.CRITICAL": "重大",
    "dashboard.suspicion_level.UNKNOWN": "不明",

    "dashboard.chart.folders.title": "IMAP フォルダ別メール数",
    "dashboard.chart.domains.title": "送信者ドメイントップ",
    "dashboard.chart.attachments.title": "添付ファイルの有無",
    "dashboard.chart.auth.title": "DKIM / SPF / DMARC 結果",
    "dashboard.chart.suspicion.title": "疑わしさレベル分布",

    "dashboard.chart.no_data": "このグラフを表示するためのデータが不足しています。",
    "dashboard.chart.axis.emails": "メール数",
    "dashboard.chart.axis.folders": "IMAP フォルダ",
    "dashboard.chart.axis.domains": "ドメイン",
    "dashboard.chart.axis.levels": "レベル",

    "dashboard.legend.safe": "比較的安全な領域",
    "dashboard.legend.suspicious": "優先調査領域",

    # ------------------------------------------------------------------
    # Viewer – scoring columns
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "疑わしさスコア",
    "viewer.col.suspicion_level": "レベル",
    "viewer.col.suspicion_reasons": "理由（要約）",

    "viewer.score.tooltip.base": (
        "DKIM/SPF/DMARC、Received 異常、ヘッダー整合性、添付ファイル"
        "などから総合疑わしさスコアを算出。"
    ),
    "viewer.score.level.LOW": (
        "低リスク: 現行ルールでは異常は検出されていません。"
    ),
    "viewer.score.level.MEDIUM": (
        "中リスク: 一部の要素を確認する必要があります（ヘッダー、認証、添付など）。"
    ),
    "viewer.score.level.HIGH": (
        "高リスク: 複数の技術的指標に不整合または危険性があります。"
    ),
    "viewer.score.level.CRITICAL": (
        "重大リスク: メールは悪意のある、または偽造された可能性が非常に高い。"
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "このアカウントは OAuth2 などの最新手法を必要とするプロバイダによって\n"
        "管理されている可能性があります（例: Gmail, Outlook/Microsoft 365, Yahoo）。\n\n"
        "規約順守のため、このバージョンの eml_forensic_suite はそれらのサービスへの\n"
        "直接 IMAP アクセスを実施しません。\n\n"
        "メッセージを取得する方法:\n"
        "  • Gmail: Google Takeout で MBOX をエクスポート、または Thunderbird を使用\n"
        "  • Outlook / Microsoft 365: Outlook クライアントで PST をエクスポート\n"
        "  • Yahoo など: プロバイダの提供するエクスポートツールを使用\n\n"
        "将来のバージョンでは MBOX や PST を直接解析できるようにする予定です。"
    ),

    # ------------------------------------------------------------------
    # Mini search language
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "フォレンジック検索ミニ言語:\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "演算子: 暗黙の AND, OR, NOT, ()"
    ),

    # ------------------------------------------------------------------
    # CSV / index errors
    # ------------------------------------------------------------------
    "viewer.no_index_title": "インデックスなし",
    "viewer.no_index_body": (
        "このセッションにはインデックスがありません。\n"
        "タブ2でインデックスを生成するか、CSV を手動で開いてください。"
    ),
    "viewer.open_csv_title": "インデックス CSV を開く",
    "viewer.error_csv_title": "CSV 読み取りエラー",
    "viewer.error_csv_body": (
        "CSV ファイルを読み取れません: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Attachment preview
    # ------------------------------------------------------------------
    "viewer.attach.preview": "読み取り専用プレビュー",
    "viewer.attach.preview_failed_title": "プレビュー失敗",
    "viewer.attach.preview_failed_body": (
        "この添付ファイルのプレビューを表示できません。"
    ),
    "viewer.attach.preview_unsupported_title": "非対応形式",
    "viewer.attach.preview_unsupported_body": (
        "この MIME タイプには内蔵プレビューがありません: {mime}"
    ),

    # ------------------------------------------------------------------
    # Attachment extraction
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "メッセージなし",
    "viewer.attach.no_msg_body": "選択されたメッセージがありません。",
    "viewer.attach.no_selection_title": "添付未選択",
    "viewer.attach.no_selection_body": "リストから添付ファイルを選択してください。",
    "viewer.attach.no_root_title": "作業ディレクトリがありません",
    "viewer.attach.no_root_body": (
        "抽出に必要なフォレンジック / インデックスディレクトリが設定されていません。"
    ),
    "viewer.attach.extract_one_title": "添付ファイルを抽出しました",
    "viewer.attach.extract_one_body": (
        "添付ファイルは次へ抽出されました:\n{path}"
    ),
    "viewer.attach.extract_all_title": "添付ファイルを抽出しました",
    "viewer.attach.extract_all_body": (
        "{count} 件の添付ファイルが抽出されました:\n{paths}"
    ),

    "viewer.attach.extract_one": "選択した添付を抽出",
    "viewer.attach.extract_all": "すべての添付を抽出",

    # ------------------------------------------------------------------
    # About box
    # ------------------------------------------------------------------
    "about.version_label": "バージョン:",
    "about.description": "EML / IMAP メールのフォレンジック解析ツール（読み取り専用）。",
}
