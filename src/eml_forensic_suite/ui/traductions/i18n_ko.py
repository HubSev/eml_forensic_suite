from __future__ import annotations

from typing import Dict

TRANSLATIONS_KO: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "EML / IMAP 포렌식 도구 (읽기 전용)",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "파일",
    "menu.view": "보기",
    "menu.help": "도움말",

    "menu.file.settings": "설정…",
    "menu.file.quit": "종료",

    "menu.view.theme.dark": "다크 테마",
    "menu.view.theme.light": "라이트 테마",

    "menu.help.about": "정보…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. IMAP 내보내기",
    "tab.index": "2. EML 인덱싱",
    "tab.viewer": "3. 포렌식 뷰어",
    "tab.dashboard": "4. 포렌식 대시보드",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "설정",
    "settings.reports_dir.label": "작업 / 보고서 디렉터리:",
    "settings.reports_dir.browse": "탐색…",
    "settings.language.label": "인터페이스 언어:",
    "settings.reports_dir.dialog_title": "작업 / 보고서 디렉터리 선택",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "준비 완료.",
    "status.settings.saved": "설정이 저장되었습니다.",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "EML 내보내기 디렉터리:",
    "index.browse": "탐색…",
    "index.use_last_export": "마지막 IMAP 내보내기 사용",
    "index.log_placeholder": "EML 인덱싱 로그 (읽기 전용)…",
    "index.start_button": "EML 인덱싱 시작",
    "index.dialog_select_folder": "EML 내보내기 폴더 선택",
    "index.no_last_export": "아직 알려진 IMAP 내보내기가 없습니다 (탭 1).",
    "index.error_already_running_title": "이미 인덱싱 실행 중",
    "index.error_already_running_body": "이미 EML 인덱싱 작업이 실행 중입니다.",
    "index.error_no_folder_title": "폴더 누락",
    "index.error_no_folder_body": "EML 파일이 들어 있는 폴더를 선택해 주세요.",
    "index.error_invalid_folder_title": "잘못된 폴더",
    "index.error_invalid_folder_body": "지정한 폴더가 존재하지 않습니다:\n{folder}",
    "index.status_selected_folder": "인덱싱에 선택된 폴더: {folder}",
    "index.error_indexing_title": "인덱싱 중 오류",
    "index.error_log": "❌ 오류: {error}",
    "index.done_log_success": "\n인덱싱이 성공적으로 완료되었습니다.",
    "index.done_log_path": "CSV 경로: {csv_path}",
    "index.done_log_count": "인덱싱된 항목 수: {count}",
    "index.done_msg_title": "인덱싱 완료",
    "index.done_msg_body": (
        "EML 인덱싱이 완료되었습니다.\n\nCSV 파일: {csv_path}\n항목 수: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "마지막 인덱스 사용",
    "dashboard.open_csv": "인덱스 CSV 열기…",
    "dashboard.placeholder": "EML 인덱스를 기반으로 한 포렌식 통계 요약…",
    "dashboard.source_memory": "소스: 메모리 내 인덱스 (이 세션에서 마지막 인덱싱).",
    "dashboard.source_csv": "소스: {path}",
    "dashboard.no_index_title": "인덱스 없음",
    "dashboard.no_index_body": (
        "이 세션에서 사용 가능한 인덱스가 없습니다.\n"
        "탭 2에서 인덱스를 생성하거나 CSV를 수동으로 여세요."
    ),
    "dashboard.dialog_open_csv": "인덱스 CSV 파일 열기",
    "dashboard.error_csv_missing_title": "파일을 찾을 수 없음",
    "dashboard.error_csv_missing_body": "지정한 파일이 존재하지 않습니다:\n{path}",
    "dashboard.error_csv_read_title": "CSV 읽기 오류",
    "dashboard.error_csv_read_body": "CSV 파일을 읽을 수 없습니다: {path}",
    "dashboard.empty_csv_title": "빈 인덱스",
    "dashboard.empty_csv_body": "CSV 파일에 사용 가능한 항목이 없습니다.",
    "dashboard.no_data": "분석할 데이터가 없습니다.",

    "dashboard.section_overview": "개요",
    "dashboard.overview_line": (
        "총 이메일: {total} – 고유 발신자 수: {senders}"
    ),
    "dashboard.dates_line": "포함 기간: {date_min} → {date_max}",
    "dashboard.dates_unknown": "날짜를 사용할 수 없거나 해석할 수 없습니다.",

    "dashboard.section_folders": "IMAP 폴더별 분포",
    "dashboard.no_folders": "IMAP 폴더가 감지되지 않았습니다.",

    "dashboard.section_domains": "도메인별 분포 (발신자)",
    "dashboard.no_domains": "감지된 도메인이 없습니다.",

    "dashboard.section_attachments": "첨부 파일",
    "dashboard.attachments_line": (
        "첨부 파일이 있는 이메일: {with_att}/{total} – 추정 총 첨부 파일 수: {total_att}"
    ),

    "dashboard.section_auth": "인증 (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "DKIM 결과:",
    "dashboard.auth_header_spf": "SPF 결과:",
    "dashboard.auth_header_dmarc": "DMARC 결과:",

    "dashboard.section_integrity": "무결성 / 누락된 헤더",
    "dashboard.integrity_flags_title": "감지된 무결성 플래그:",
    "dashboard.no_integrity_flags": "특정 무결성 플래그가 감지되지 않았습니다.",

    "dashboard.section_received": "Received 체인의 이상 현상",
    "dashboard.no_received_anomalies": (
        "현재 규칙 하에서 Received 이상 현상이 감지되지 않았습니다."
    ),

    # ------------------------------------------------------------------
    # Viewer tab – columns de base
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "IMAP 폴더",
    "viewer.col.sequence_number": "시퀀스",
    "viewer.col.date_header": "날짜",
    "viewer.col.from_header": "발신자",
    "viewer.col.to_header": "수신자",
    "viewer.col.cc_header": "참조",
    "viewer.col.cci_header": "숨은 참조",
    "viewer.col.subject": "제목",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "첨부 파일 있음?",
    "viewer.col.attachment_count": "첨부 파일 개수",
    "viewer.col.attachment_filenames": "첨부 파일 이름",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (발췌)",
    "viewer.col.received_count": "Received 개수",
    "viewer.col.received_anomalies": "Received 이상",
    "viewer.col.integrity_flags": "무결성 플래그",
    "viewer.col.relative_path": "상대 경로",
    "viewer.col.filename": "파일 이름",

    # ------------------------------------------------------------------
    # Viewer tab – search + zones
    # ------------------------------------------------------------------
    "viewer.search_label": "검색:",
    "viewer.search_placeholder": "인덱스에서 필터링 (모든 열)…",
    "viewer.search_clear": "지우기",

    "viewer.headers_label": "헤더",
    "viewer.headers_placeholder": "선택된 메시지의 헤더…",

    "viewer.body_label": "본문 (텍스트)",
    "viewer.body_placeholder": (
        "선택된 메시지의 text/plain 본문 (또는 원시 HTML 대체)…"
    ),

    "viewer.btn_load_last": "마지막 IMAP 내보내기 사용",
    "viewer.btn_open_csv": "인덱스 CSV 열기...",
    "viewer.attachments_label": "첨부 파일",

    # ------------------------------------------------------------------
    # Viewer – erreurs EML
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "EML 파일을 찾을 수 없음",
    "viewer.error_missing_eml_body": "디스크에서 EML 파일을 찾을 수 없습니다:\n{path}",
    "viewer.error_parse_eml_title": "EML 읽기 오류",
    "viewer.error_parse_eml_body": "EML 파일을 파싱할 수 없습니다: {path}",

    # ------------------------------------------------------------------
    # Viewer – colonnes PJ
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "이름",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "크기 (바이트)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "의심스러움?",

    "viewer.attach.yes": "예",
    "viewer.attach.no": "아니오",

    # ------------------------------------------------------------------
    # IMAP tab – connexion & champs
    # ------------------------------------------------------------------
    "imap.group.connection": "IMAP 서버 (증거 소스)",
    "imap.label.host": "IMAP 서버 주소",
    "imap.label.user": "분석 대상 사서함 식별자",
    "imap.label.password": "비밀번호 (저장되지 않음)",
    "imap.label.date_start": "시작 날짜 (포렌식 필터)",
    "imap.label.date_end": "종료 날짜 (포렌식 필터)",

    "imap.placeholder.host": "예: imap.example.com",
    "imap.placeholder.user": "예: incident@company.com",
    "imap.placeholder.password": "분석 대상 계정의 비밀번호",
    "imap.placeholder.date_start": "DD/MM/YYYY (선택 사항)",
    "imap.placeholder.date_end": "DD/MM/YYYY (선택 사항)",

    "imap.button.fetch_mailboxes": "IMAP 폴더 검사…",
    "imap.button.start_export": "포렌식 추출 시작",
    "imap.button.cancel_export": "추출 취소",

    "imap.label.mailboxes_title": (
        "추출할 IMAP 폴더 (증거 소스):"
    ),
    "imap.checkbox.select_all": "모든 폴더 선택",

    "imap.log.placeholder": (
        "IMAP 추출 로그 (읽기 전용, 타임스탬프 포함)…"
    ),

    # ------------------------------------------------------------------
    # IMAP tab – erreurs / infos génériques
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "설정 불완전",
    "imap.error.missing_fields.body": (
        "IMAP 서버, 사용자 이름 및 비밀번호를 입력해 주세요."
    ),

    "imap.info.export_running.title": "이미 추출 실행 중",
    "imap.info.export_running.body": "이미 IMAP 추출 작업이 실행 중입니다.",

    "imap.error.date_invalid.title": "잘못된 날짜",
    "imap.error.date_invalid.body": "제공된 날짜에 오류가 있습니다: {error}",
    "imap.error.date_end_before_start.body": (
        "종료 날짜는 시작 날짜보다 이전일 수 없습니다."
    ),

    "imap.error.no_mailbox_selected.title": "폴더 미선택",
    "imap.error.no_mailbox_selected.body": (
        "추출할 IMAP 폴더를 하나 이상 선택해 주세요."
    ),

    "imap.error.fetch_mailboxes.title": "IMAP 오류",
    "imap.error.fetch_mailboxes.body": (
        "IMAP 폴더를 가져올 수 없습니다:\n{error}"
    ),

    "imap.info.generic.title": "정보",
    "imap.error.generic.title": "오류",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "{host}:{port}에 연결 중입니다 (SSL={use_ssl})...",
    "imap.log.connected": "IMAP 서버에 연결되었습니다.",
    "imap.log.select_folder": "\"{folder}\" 폴더를 선택하는 중입니다...",
    "imap.log.folder_selected": "\"{folder}\" 폴더가 선택되었습니다.",
    "imap.log.message_count": "내보낼 메시지: {count}개.",
    "imap.log.fetching": "IMAP 메시지를 가져오는 중입니다...",
    "imap.log.export_done": "IMAP 내보내기가 완료되었습니다.",
    "imap.log.saving_to": "메시지를 \"{output_dir}\"에 저장하는 중입니다...",
    "imap.log.progress": "{current}/{total}번째 메시지를 내보내는 중입니다...",
    "imap.log.skip_existing": "\"{path}\" 파일이 이미 존재합니다. 건너뜁니다.",

    "imap.error.connect_failed": "{host}:{port}에 연결할 수 없습니다: {error}",
    "imap.error.login_failed": "IMAP 인증 오류: {error}",
    "imap.error.select_failed": "\"{folder}\" 폴더를 선택할 수 없습니다: {error}",
    "imap.error.fetch_failed": "메시지를 가져오는 동안 오류가 발생했습니다: {error}",
    "imap.error.generic": "IMAP 내보내기 중 오류가 발생했습니다: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== IMAP 내보내기 보고서 (읽기 전용) ===",
    "imap.report.tool_line": "도구       : eml_forensic_suite – IMAP 내보내기",
    "imap.report.version_line": "버전       : {version}",
    "imap.report.folder_line": "폴더       : {export_dir}",

    "imap.report.section_tool": "---- 도구 정보 ----",
    "imap.report.tool_path": "도구 경로            : {tool_path}",
    "imap.report.tool_hash": "도구 SHA-256         : {tool_hash}",

    "imap.report.section_env": "---- 실행 환경 ----",
    "imap.report.env_os": "운영 체제            : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Python 버전          : {python_version}",

    "imap.report.section_context": "---- IMAP / 계정 컨텍스트 ----",
    "imap.report.context_host": "IMAP 서버   : {host}",
    "imap.report.context_user": "계정        : {user}",
    "imap.report.context_date_start": "요청된 시작 날짜      : {date_start}",
    "imap.report.context_date_end": "요청된 종료 날짜      : {date_end}",
    "imap.report.context_criteria": "IMAP 검색 기준        : {search_criteria} (서버로 전송된 그대로)",

    "imap.report.selected_folders_title": "선택된 폴더:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- IMAP 서버 정보 ----",
    "imap.report.server_greeting": "IMAP 배너    : {greeting}",
    "imap.report.server_capability": "CAPABILITY   : {capability}",

    "imap.report.section_timestamps": "---- 분석 타임스탬프 ----",
    "imap.report.timestamp_start_utc": "분석 시작 (UTC)        : {dt}",
    "imap.report.timestamp_start_local": "분석 시작 (로컬)       : {dt}",
    "imap.report.timestamp_end_utc": "분석 종료 (UTC)        : {dt}",
    "imap.report.timestamp_end_local": "분석 종료 (로컬)       : {dt}",
    "imap.report.duration": "총 소요 시간           : {duration}",

    "imap.report.section_folders": "---- 분석된 폴더 ----",
    "imap.report.folders_count": "선택된 폴더 수         : {count}",

    "imap.report.folder_header": "폴더 : {name}",
    "imap.report.folder_messages": "  해당 기간에서 발견된 메시지 수 : {count}",
    "imap.report.folder_exported": "  내보낸 메시지 수              : {count}",
    "imap.report.folder_errors": "  가져오기 오류                  : {count}",
    "imap.report.folder_bytes": "  다운로드된 데이터 양           : {bytes} 바이트",
    "imap.report.folder_size_stats": "  최소 / 최대 / 평균 크기        : {min_size} / {max_size} / {avg_size} 바이트",
    "imap.report.folder_period": "  적용 기간 (INTERNALDATE)       : {first} → {last}",
    "imap.report.folder_error_uids": "  오류가 발생한 UID(완전한 목록 아님) : {uids}",

    "imap.report.section_totals": "---- 전체 합계 ----",
    "imap.report.total_messages": "발견된 메시지 수 (전체 폴더) : {count}",
    "imap.report.total_exported": "내보낸 메시지 수             : {count}",
    "imap.report.total_errors": "가져오기 오류                : {count}",
    "imap.report.total_bytes": "총 다운로드 데이터 양        : {bytes} 바이트",

    "imap.report.section_forensic": "---- 방법론 및 포렌식 보장 ----",
    "imap.report.forensic_item_readonly": "- 이 도구는 SELECT readonly, SEARCH, FETCH와 같이 읽기 전용 IMAP 명령만 사용했으며, 분석 동안 어떤 메시지도 수정·삭제되거나 읽음으로 표시되지 않았습니다.",
    "imap.report.forensic_item_eml": "- 메시지는 IMAP 서버가 제공한 그대로 .eml 파일로 디스크에 기록되었으며, 내용은 전혀 변경되지 않았습니다.",
    "imap.report.forensic_item_hashes": "- 내보낸 각 메시지는 hashes.txt에 나열된 SHA-256 해시와, 모든 개별 해시를 연결하여 계산한 전역 해시와 연관되어 있습니다.",
    "imap.report.forensic_item_report_hash": "- 이 분석 보고서 자체도 SHA-256으로 해시되며, 보고서의 무결성을 보장하기 위해 해당 해시는 hashes.txt에 추가됩니다.",

    "imap.report.hashes_report_header": "ANALYSIS REPORT (분석 보고서):",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "선택된 폴더가 없습니다.",
    "imap.worker.log_export_dir": "내보내기 폴더: {export_dir}",
    "imap.worker.tool_hash_error": "(도구 해시를 계산하는 동안 오류 발생)",

    "imap.worker.log_connecting": "IMAP 서버에 연결하는 중입니다...",
    "imap.worker.greeting_not_available": "(IMAP 배너를 가져올 수 없음)",
    "imap.worker.log_auth_classic": "기본 IMAP 인증 중...",
    "imap.worker.error_auth_failed": "IMAP 인증 오류: {error}",
    "imap.worker.capability_error": "(CAPABILITY 명령 실행 중 오류)",

    "imap.worker.log_date_start_inclusive": "시작 날짜(포함): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "시작 날짜: 설정되지 않음 → 사용 가능한 첫 번째 메시지부터 추출합니다.",
    "imap.worker.date_start_unset_label": "사용 가능한 첫 번째 메시지(하한 없음)",

    "imap.worker.log_date_end_inclusive": "종료 날짜(포함): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "종료 날짜: 설정되지 않음 → 서버에서 사용 가능한 마지막 날짜까지.",
    "imap.worker.date_end_unset_label": "사용 가능한 마지막 메시지(상한 없음)",

    "imap.worker.log_criteria": "사용된 IMAP 검색 기준: {criteria}",
    "imap.worker.log_selected_folders_header": "선택된 폴더 ({count}개):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "카운트 단계에서 중지 요청이 수신되었습니다.",
    "imap.worker.log_phase1_count": "[1단계] {folder} 폴더의 메시지 수를 계산하는 중입니다...",
    "imap.worker.log_select_folder_failed": "  ⚠️ 이 폴더를 선택할 수 없습니다. 건너뜁니다.",
    "imap.worker.log_search_folder_failed": "  ⚠️ 이 폴더에서 검색하는 동안 오류가 발생했습니다. 건너뜁니다.",
    "imap.worker.log_messages_to_process": "  → {folder} 폴더에서 처리할 메시지: {count}개",

    "imap.worker.log_total_messages_to_download": "다운로드할 전체 메시지 수(모든 폴더): {count}개",

    "imap.worker.log_stop_during_export": "중지 요청 수신: 내보내기를 중단합니다.",
    "imap.worker.log_folder_header": "=== 폴더: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  이 기간 동안 {folder} 폴더에 메시지가 없습니다.",
    "imap.worker.log_folder_message_count": "  {folder} 폴더에서 발견된 메시지 수: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ 이 폴더를 다시 선택할 수 없습니다. 건너뜁니다.",

    "imap.worker.log_first_message_download": "  첫 번째 메시지({uid})를 다운로드하는 중입니다...",
    "imap.worker.log_folder_progress": "  {folder} 폴더 진행 상황: {current}/{total} (마지막: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ 메시지 {uid}를 가져오는 동안 오류가 발생했습니다. 계속 진행합니다.",
    "imap.worker.log_folder_end": "  {folder} 폴더 끝",

    "imap.worker.hashes_header": "내보낸 파일과 해당 SHA-256 해시 목록",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "GLOBAL HASH (메시지만):",

    "imap.worker.log_export_done_header": "=== 내보내기 완료 ===",
    "imap.worker.log_export_done_count": "내보낸 총 메시지 수: {count}",
    "imap.worker.log_export_done_hashes_file": "해시 파일: {path}",
    "imap.worker.log_export_done_hash": "글로벌 해시: {file_hash}",

    "imap.worker.summary": (
        "내보내기가 완료되었습니다.\n\n"
        "내보낸 메시지 수: {count}\n"
        "폴더: {export_dir}\n\n"
        "글로벌 해시(메시지):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "분석 보고서가 생성되어 해시되었습니다 (rapport_imap_export.txt 및 hashes.txt 참조).",
    "imap.worker.log_report_failed": "⚠️ 분석 보고서를 생성할 수 없습니다: {error}",

    "imap.worker.error_generic": "오류가 발생했습니다: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "IMAP 서버에 연결하는 중입니다...",
    "imap.tk.log_auth_classic": "기본 IMAP 인증 중...",
    "imap.tk.error_list_mailboxes_failed": "IMAP 폴더 목록을 가져올 수 없습니다.",

    "imap.tk.log_folders_found_header": "서버에서 발견된 폴더:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "총 IMAP 폴더 수: {count}",

    "imap.tk.msgbox_error_title": "오류",
    "imap.tk.msgbox_error_fetch_mailboxes": "IMAP 폴더를 가져오는 동안 오류가 발생했습니다: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ 폴더를 가져오는 동안 오류가 발생했습니다: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. IMAP 내보내기",

    "imap.tk.label_server": "IMAP 서버:",
    "imap.tk.label_email": "이메일 주소:",
    "imap.tk.label_password": "비밀번호:",
    "imap.tk.label_date_start": "시작 날짜 (DD/MM/YYYY, 선택 사항):",
    "imap.tk.label_date_end": "종료 날짜 (DD/MM/YYYY, 선택 사항):",
    "imap.tk.label_log": "로그:",
    "imap.tk.label_mailboxes": "내보낼 IMAP 폴더:",
    "imap.tk.checkbox_select_all": "모두 선택 / 모두 해제",
    "imap.tk.label_progress": "진행 상황:",

    "imap.tk.msgbox_missing_fields_title": "필수 항목 누락",
    "imap.tk.msgbox_missing_fields_text": "서버, 이메일, 비밀번호를 모두 입력해 주세요.",

    "imap.tk.log_fetch_mailboxes_start": "IMAP 폴더를 가져오는 중입니다...",
    "imap.tk.log_no_mailboxes_or_error": "폴더를 찾을 수 없거나 오류가 발생했습니다.",
    "imap.tk.log_select_mailboxes_hint": "내보낼 폴더를 선택하세요.",

    "imap.tk.button_list_mailboxes": "IMAP 폴더 나열",

    "imap.tk.msgbox_date_start_invalid_title": "시작 날짜가 올바르지 않습니다",
    "imap.tk.msgbox_date_start_invalid_text": "시작 날짜는 DD/MM/YYYY 형식이어야 합니다.",

    "imap.tk.msgbox_date_end_invalid_title": "종료 날짜가 올바르지 않습니다",
    "imap.tk.msgbox_date_end_invalid_text": "종료 날짜는 DD/MM/YYYY 형식이어야 합니다.",

    "imap.tk.msgbox_date_range_invalid_title": "날짜 범위가 올바르지 않습니다",
    "imap.tk.msgbox_date_range_invalid_text": (
        "종료 날짜는 시작 날짜보다 빠를 수 없습니다."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "폴더가 선택되지 않았습니다",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "‘IMAP 폴더 나열’을 통해 최소 한 개의 IMAP 폴더를 선택해 주세요."
    ),

    "imap.tk.log_export_start": "내보내기를 시작합니다...",
    "imap.tk.button_run_export": "내보내기 실행 (선택된 폴더)",

    "imap.tk.log_stop_requested": (
        "중지 요청 수신: 내보내기가 정상적으로 종료됩니다..."
    ),
    "imap.tk.button_stop_export": "내보내기 중지",

    "imap.tk.msgbox_export_done_title": "내보내기 완료",


    # ------------------------------------------------------------------
    # IMAP tab – logs
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "폴더를 나열하기 위해 IMAP 서버에 연결 중…"
    ),
    "imap.log.fetch_error": "❌ 폴더를 가져오는 중 오류:",
    "imap.log.no_mailboxes": "이 계정에서 IMAP 폴더를 찾을 수 없습니다.",
    "imap.log.mailboxes_found": "서버에서 찾은 폴더:",
    "imap.log.mailboxes_total": "총 IMAP 폴더 수: {count}",
    "imap.log.mailboxes_select_hint": (
        "읽기 전용 모드로 추출할 폴더를 선택하세요."
    ),
    "imap.log.start_export": (
        "IMAP 추출 시작 (포렌식 모드, 읽기 전용)…"
    ),
    "imap.log.cancel_requested": (
        "IMAP 작업자에게 취소 요청을 전송했습니다…"
    ),
    "imap.log.export_dir_saved": "내보내기 디렉터리가 저장되었습니다: {path}",
    "imap.log.done": "IMAP 처리가 완료되었습니다.",

    # ------------------------------------------------------------------
    # Dashboard v3 – sections / onglets
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "의심 수준",
    "dashboard.tab_text": "EML 인덱스 요약",
    "dashboard.tab_graphs": "그래프",
    "dashboard.section_charts": "그래픽 시각화",

    "dashboard.chart_suspicion_title": "의심 수준 분포",
    "dashboard.chart_folders_title": "IMAP 폴더별 메시지 수",
    "dashboard.chart_domains_title": "상위 발신 도메인",
    "dashboard.chart_attachments_title": "첨부 파일 존재 여부",
    "dashboard.chart_axis_count": "개수",
    "dashboard.chart_attachments_with": "첨부 파일 있음",
    "dashboard.chart_attachments_without": "첨부 파일 없음",

    # Légende / texte autour du scoring
    "dashboard.suspicion_distribution_line": (
        "의심 수준별 이메일 분포:"
    ),
    "dashboard.suspicion_level.LOW": "낮음",
    "dashboard.suspicion_level.MEDIUM": "중간",
    "dashboard.suspicion_level.HIGH": "높음",
    "dashboard.suspicion_level.CRITICAL": "심각",
    "dashboard.suspicion_level.UNKNOWN": "알 수 없음",

    # Graphes – titres (nouvelle nomenclature)
    "dashboard.chart.folders.title": "IMAP 폴더별 이메일 수",
    "dashboard.chart.domains.title": "상위 발신 도메인",
    "dashboard.chart.attachments.title": "첨부 파일 존재 여부",
    "dashboard.chart.auth.title": "DKIM / SPF / DMARC 결과",
    "dashboard.chart.suspicion.title": "의심 수준별 분포",

    # Graphes – libellés / états
    "dashboard.chart.no_data": (
        "이 그래프를 표시할 만큼 충분한 데이터가 없습니다."
    ),
    "dashboard.chart.axis.emails": "이메일 수",
    "dashboard.chart.axis.folders": "IMAP 폴더",
    "dashboard.chart.axis.domains": "도메인",
    "dashboard.chart.axis.levels": "수준",

    # Petite aide visuelle sur les couleurs
    "dashboard.legend.safe": "대체로 안전하다고 간주되는 영역",
    "dashboard.legend.suspicious": "먼저 조사해야 할 영역",

    # ------------------------------------------------------------------
    # Viewer – colonnes de scoring & suspicion
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "의심 점수",
    "viewer.col.suspicion_level": "수준",
    "viewer.col.suspicion_reasons": "사유 (요약)",

    # Tooltips scoring
    "viewer.score.tooltip.base": (
        "DKIM/SPF/DMARC, Received 이상, 헤더 무결성 및 첨부 파일 정보를 "
        "기반으로 계산된 전체 의심 점수입니다."
    ),
    "viewer.score.level.LOW": (
        "의심 수준 낮음: 현재 규칙 하에서 비정상적인 요소가 감지되지 않았습니다."
    ),
    "viewer.score.level.MEDIUM": (
        "의심 수준 중간: 일부 요소를 확인해야 합니다 "
        "(헤더, 인증 또는 첨부 파일)."
    ),
    "viewer.score.level.HIGH": (
        "의심 수준 높음: 여러 기술적 지표가 불일치하거나 위험합니다."
    ),
    "viewer.score.level.CRITICAL": (
        "의심 수준 심각: 이메일이 악의적이거나 위조되었을 가능성이 매우 높습니다."
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth / providers restrictions
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "이 계정은 메시지에 접근하기 위해 최신 메커니즘 "
        "(OAuth2, 공식 내보내기 등)을 요구하는 제공업체에 의해 관리되는 것으로 보입니다 "
        "(예: Gmail, Outlook/Microsoft 365, Yahoo).\n\n"
        "규정을 준수하고 이러한 규칙을 우회하지 않기 위해, 이 버전의 "
        "eml_forensic_suite는 이러한 서비스에 대해 직접적인 IMAP 추출을 수행하지 않습니다.\n\n"
        "호환 가능한 방식으로 메시지를 가져오려면:\n"
        "  • Gmail: Google Takeout을 사용하여 사서함(MBOX)을 내보내거나,\n"
        "    Thunderbird와 같은 클라이언트로 로컬 복사본을 만듭니다.\n"
        "  • Outlook / Microsoft 365: Outlook 클라이언트 내보내기(PST)\n"
        "    또는 조직의 보관 도구를 사용합니다.\n"
        "  • Yahoo 등: 제공업체가 제공하는 내보내기 도구를 사용합니다.\n\n"
        "향후 버전의 eml_forensic_suite는 이러한 내보내기 "
        "(MBOX, PST 등)를 직접 분석하여 이러한 플랫폼과의 호환성을 유지하는 것을 목표로 합니다."
    ),

    # ------------------------------------------------------------------
    # Viewer – mini langage de recherche
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "포렌식 미니 언어:\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "연산자: 암시적 AND, OR, NOT, 괄호."
    ),

    # ------------------------------------------------------------------
    # Viewer – CSV / index generic messages
    # ------------------------------------------------------------------
    "viewer.no_index_title": "사용 가능한 인덱스 없음",
    "viewer.no_index_body": (
        "이 세션에서 사용 가능한 인덱스가 없습니다.\n"
        "탭 2에서 인덱스를 생성하거나 CSV 파일을 수동으로 여세요."
    ),
    "viewer.open_csv_title": "인덱스 CSV 파일 열기",
    "viewer.error_csv_title": "CSV 읽기 오류",
    "viewer.error_csv_body": (
        "CSV 파일을 읽을 수 없습니다: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – preview (version finale, lecture seule)
    # ------------------------------------------------------------------
    "viewer.attach.preview": "읽기 전용 미리 보기",
    "viewer.attach.preview_failed_title": "미리 보기 실패",
    "viewer.attach.preview_failed_body": (
        "이 첨부 파일의 미리 보기를 표시할 수 없습니다."
    ),
    "viewer.attach.preview_unsupported_title": "지원되지 않는 유형",
    "viewer.attach.preview_unsupported_body": (
        "이 MIME 유형에 대해 내장 미리 보기가 제공되지 않습니다: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – extraction PJ (version finale)
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "메시지 없음",
    "viewer.attach.no_msg_body": "현재 선택된 메시지가 없습니다.",
    "viewer.attach.no_selection_title": "첨부 파일 미선택",
    "viewer.attach.no_selection_body": (
        "목록에서 첨부 파일을 선택해 주세요."
    ),
    "viewer.attach.no_root_title": "작업 디렉터리를 찾을 수 없음",
    "viewer.attach.no_root_body": (
        "추출에 사용할 포렌식 / 인덱스 디렉터리가 설정되어 있지 않습니다."
    ),
    "viewer.attach.extract_one_title": "첨부 파일 추출됨",
    "viewer.attach.extract_one_body": (
        "첨부 파일이 다음 위치로 추출되었습니다:\n{path}"
    ),
    "viewer.attach.extract_all_title": "첨부 파일 추출됨",
    "viewer.attach.extract_all_body": (
        "{count}개의 첨부 파일이 다음 위치로 추출되었습니다:\n{paths}"
    ),

    # ------------------------------------------------------------------
    # Actions PJ (boutons – déjà couverts par les textes ci-dessus)
    # ------------------------------------------------------------------
    "viewer.attach.extract_one": "선택한 첨부 파일 추출",
    "viewer.attach.extract_all": "모든 첨부 파일 추출",

    # ------------------------------------------------------------------
    # About box
    # ------------------------------------------------------------------
    "about.version_label": "버전:",
    "about.description": (
        "EML/IMAP 이메일의 포렌식 분석을 위한 읽기 전용 도구입니다."
    ),
}
