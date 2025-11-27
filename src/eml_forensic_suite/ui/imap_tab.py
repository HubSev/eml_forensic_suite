from __future__ import annotations

from typing import Dict, Any, List, Tuple

import imaplib
import threading
import queue

from PySide6.QtCore import Qt, QTimer, QSignalBlocker
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QPlainTextEdit,
    QProgressBar,
    QCheckBox,
    QScrollArea,
    QFrame,
    QMessageBox,
)

from eml_forensic_suite.core.imap_exporter import export_imap_worker
from eml_forensic_suite.core.common_utils import (
    parse_french_date,
    decode_imap_mailbox,
)
from eml_forensic_suite.ui.i18n import t


class ImapTab(QWidget):

    def __init__(self, shared_state: Dict[str, Any], parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.shared_state = shared_state

        self.lang: str = str(shared_state.get("language", "fr"))

        self.mailbox_checkboxes: List[QCheckBox] = []
        self.worker_thread: threading.Thread | None = None
        self.stop_event: threading.Event | None = None
        self.queue: "queue.Queue[Tuple[str, object]]" | None = None
        self.progress_total_msgs: int = 0
        self.progress_current: int = 0

        self.queue_timer = QTimer(self)
        self.queue_timer.setInterval(100)
        self.queue_timer.timeout.connect(self._poll_queue)

        self.group_conn: QGroupBox | None = None
        self.label_host: QLabel | None = None
        self.label_user: QLabel | None = None
        self.label_password: QLabel | None = None
        self.label_date_start: QLabel | None = None
        self.label_date_end: QLabel | None = None

        self.edit_host: QLineEdit | None = None
        self.edit_user: QLineEdit | None = None
        self.edit_password: QLineEdit | None = None
        self.edit_date_start: QLineEdit | None = None
        self.edit_date_end: QLineEdit | None = None

        self.btn_fetch: QPushButton | None = None
        self.btn_export: QPushButton | None = None
        self.btn_cancel: QPushButton | None = None

        self.label_mailboxes_title: QLabel | None = None
        self.chk_select_all: QCheckBox | None = None

        self.scroll_area: QScrollArea | None = None
        self.mailbox_layout: QVBoxLayout | None = None

        self.progress_bar: QProgressBar | None = None
        self.log_widget: QPlainTextEdit | None = None

        self._build_ui()
        self.retranslate(self.lang)

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        self.group_conn = QGroupBox(self)
        form = QFormLayout(self.group_conn)

        self.label_host = QLabel(self.group_conn)
        self.label_user = QLabel(self.group_conn)
        self.label_password = QLabel(self.group_conn)
        self.label_date_start = QLabel(self.group_conn)
        self.label_date_end = QLabel(self.group_conn)

        self.edit_host = QLineEdit(self.group_conn)
        self.edit_user = QLineEdit(self.group_conn)
        self.edit_password = QLineEdit(self.group_conn)
        self.edit_password.setEchoMode(QLineEdit.Password)

        self.edit_date_start = QLineEdit(self.group_conn)
        self.edit_date_end = QLineEdit(self.group_conn)

        form.addRow(self.label_host, self.edit_host)
        form.addRow(self.label_user, self.edit_user)
        form.addRow(self.label_password, self.edit_password)
        form.addRow(self.label_date_start, self.edit_date_start)
        form.addRow(self.label_date_end, self.edit_date_end)

        layout.addWidget(self.group_conn)

        btn_row = QHBoxLayout()

        self.btn_fetch = QPushButton(self)
        self.btn_fetch.clicked.connect(self._on_fetch_mailboxes)

        self.btn_export = QPushButton(self)
        self.btn_export.setEnabled(False)
        self.btn_export.setProperty("primary", True)
        self.btn_export.clicked.connect(self._on_start_export)

        self.btn_cancel = QPushButton(self)
        self.btn_cancel.setEnabled(False)
        self.btn_cancel.clicked.connect(self._on_cancel_export)

        btn_row.addWidget(self.btn_fetch)
        btn_row.addWidget(self.btn_export)
        btn_row.addWidget(self.btn_cancel)
        btn_row.addStretch(1)

        layout.addLayout(btn_row)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.log_widget = QPlainTextEdit(self)
        self.log_widget.setReadOnly(True)
        layout.addWidget(self.log_widget)

        self.label_mailboxes_title = QLabel(self)
        layout.addWidget(self.label_mailboxes_title)

        self.chk_select_all = QCheckBox(self)
        self.chk_select_all.stateChanged.connect(self._on_select_all_toggled)
        layout.addWidget(self.chk_select_all)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        container = QFrame(self.scroll_area)
        self.mailbox_layout = QVBoxLayout(container)
        self.mailbox_layout.setAlignment(Qt.AlignTop)

        self.scroll_area.setWidget(container)
        layout.addWidget(self.scroll_area, 1)

    def retranslate(self, lang: str) -> None:
        self.lang = lang

        if self.group_conn is not None:
            self.group_conn.setTitle(t("imap.group.connection", lang))

        if self.label_host is not None:
            self.label_host.setText(t("imap.label.host", lang))
        if self.label_user is not None:
            self.label_user.setText(t("imap.label.user", lang))
        if self.label_password is not None:
            self.label_password.setText(t("imap.label.password", lang))
        if self.label_date_start is not None:
            self.label_date_start.setText(t("imap.label.date_start", lang))
        if self.label_date_end is not None:
            self.label_date_end.setText(t("imap.label.date_end", lang))

        if self.edit_host is not None:
            self.edit_host.setPlaceholderText(t("imap.placeholder.host", lang))
        if self.edit_user is not None:
            self.edit_user.setPlaceholderText(t("imap.placeholder.user", lang))
        if self.edit_password is not None:
            self.edit_password.setPlaceholderText(t("imap.placeholder.password", lang))
        if self.edit_date_start is not None:
            self.edit_date_start.setPlaceholderText(t("imap.placeholder.date_start", lang))
        if self.edit_date_end is not None:
            self.edit_date_end.setPlaceholderText(t("imap.placeholder.date_end", lang))

        if self.btn_fetch is not None:
            self.btn_fetch.setText(t("imap.button.fetch_mailboxes", lang))
        if self.btn_export is not None:
            self.btn_export.setText(t("imap.button.start_export", lang))
        if self.btn_cancel is not None:
            self.btn_cancel.setText(t("imap.button.cancel_export", lang))

        if self.label_mailboxes_title is not None:
            self.label_mailboxes_title.setText(t("imap.label.mailboxes_title", lang))

        if self.chk_select_all is not None:
            self.chk_select_all.setText(t("imap.checkbox.select_all", lang))

        if self.log_widget is not None:
            self.log_widget.setPlaceholderText(t("imap.log.placeholder", lang))

    def log(self, message: str) -> None:
        if self.log_widget is None:
            return
        self.log_widget.appendPlainText(message)
        sb = self.log_widget.verticalScrollBar()
        sb.setValue(sb.maximum())

    def _is_oauth_restricted_provider(self, host: str, user: str) -> bool:
        host_l = host.lower()
        domain = ""
        if "@" in user:
            domain = user.split("@", 1)[1].lower()

        if (
            "gmail.com" in host_l
            or "googlemail.com" in host_l
            or domain in {"gmail.com", "googlemail.com"}
        ):
            return True

        if (
            "outlook.office365.com" in host_l
            or "outlook.office.com" in host_l
            or "imap-mail.outlook.com" in host_l
            or "imap.outlook.com" in host_l
            or domain in {
                "outlook.com",
                "hotmail.com",
                "live.com",
                "msn.com",
                "outlook.fr",
                "office365.com",
            }
        ):
            return True

        if "yahoo" in host_l or domain.endswith("yahoo.com"):
            return True

        return False

    def _show_oauth_help_dialog(self, host: str, user: str) -> None:
        QMessageBox.information(
            self,
            t("imap.info.generic.title", self.lang),
            t("imap.info.oauth_restricted_body", self.lang),
        )

    def _on_fetch_mailboxes(self) -> None:
        if self.edit_host is None or self.edit_user is None or self.edit_password is None:
            return

        host = self.edit_host.text().strip()
        user = self.edit_user.text().strip()
        password = self.edit_password.text()

        if not host or not user or not password:
            QMessageBox.warning(
                self,
                t("imap.error.missing_fields.title", self.lang),
                t("imap.error.missing_fields.body", self.lang),
            )
            return

        if self._is_oauth_restricted_provider(host, user):
            self._show_oauth_help_dialog(host, user)
            return

        self._clear_mailboxes()
        if self.log_widget is not None:
            self.log_widget.clear()
        self.log(t("imap.log.connect_list", self.lang))

        try:
            mailboxes = self._fetch_mailboxes_core(host, user, password)
        except Exception as e:
            self.log(t("imap.log.fetch_error", self.lang) + f" {e}")
            QMessageBox.critical(
                self,
                t("imap.error.fetch_mailboxes.title", self.lang),
                t("imap.error.fetch_mailboxes.body", self.lang, error=str(e)),
            )
            if self.btn_export is not None:
                self.btn_export.setEnabled(False)
            return

        if not mailboxes:
            self.log(t("imap.log.no_mailboxes", self.lang))
            if self.btn_export is not None:
                self.btn_export.setEnabled(False)
            return

        self.log(t("imap.log.mailboxes_found", self.lang))
        for mb in mailboxes:
            self.log(f"  - {mb}")
            cb = QCheckBox(mb, self)
            if self.mailbox_layout is not None:
                self.mailbox_layout.addWidget(cb)
            self.mailbox_checkboxes.append(cb)

        self.log("")
        self.log(
            t(
                "imap.log.mailboxes_total",
                self.lang,
                count=len(mailboxes),
            )
        )
        self.log(t("imap.log.mailboxes_select_hint", self.lang))

        if self.btn_export is not None:
            self.btn_export.setEnabled(True)

    def _fetch_mailboxes_core(self, host: str, user: str, password: str) -> List[str]:
        M: imaplib.IMAP4_SSL | None = None
        mailboxes: List[str] = []

        try:
            self.log("Connexion au serveur IMAP...")

            M = imaplib.IMAP4_SSL(host)
            self.log("Authentification IMAP (mot de passe)...")
            M.login(user, password)

            typ, data = M.list()
            if typ != "OK":
                raise RuntimeError("Unable to list IMAP folders.")

            for raw in data:
                if raw is None:
                    continue
                name = decode_imap_mailbox(raw)
                mailboxes.append(name)

            return mailboxes
        finally:
            if M is not None:
                try:
                    M.logout()
                except Exception:
                    pass

    def _clear_mailboxes(self) -> None:
        for cb in self.mailbox_checkboxes:
            cb.setParent(None)
        self.mailbox_checkboxes.clear()
        if self.chk_select_all is not None:
            self.chk_select_all.setChecked(False)

    def _on_select_all_toggled(self, _state: int) -> None:
        if not self.mailbox_checkboxes or self.chk_select_all is None:
            return

        all_checked = all(cb.isChecked() for cb in self.mailbox_checkboxes)
        new_value = not all_checked

        for cb in self.mailbox_checkboxes:
            cb.setChecked(new_value)

        blocker = QSignalBlocker(self.chk_select_all)
        self.chk_select_all.setCheckState(Qt.Checked if new_value else Qt.Unchecked)
        del blocker

    def _on_start_export(self) -> None:
        if self.worker_thread is not None:
            QMessageBox.information(
                self,
                t("imap.info.export_running.title", self.lang),
                t("imap.info.export_running.body", self.lang),
            )
            return

        if (
            self.edit_host is None
            or self.edit_user is None
            or self.edit_password is None
        ):
            return

        host = self.edit_host.text().strip()
        user = self.edit_user.text().strip()
        password = self.edit_password.text()

        if not host or not user or not password:
            QMessageBox.warning(
                self,
                t("imap.error.missing_fields.title", self.lang),
                t("imap.error.missing_fields.body", self.lang),
            )
            return

        if self._is_oauth_restricted_provider(host, user):
            self._show_oauth_help_dialog(host, user)
            return

        date_debut = None
        date_fin = None

        txt_start = (self.edit_date_start.text().strip()
                     if self.edit_date_start is not None
                     else "")
        txt_end = (self.edit_date_end.text().strip()
                   if self.edit_date_end is not None
                   else "")

        try:
            if txt_start:
                date_debut = parse_french_date(txt_start)
            if txt_end:
                date_fin = parse_french_date(txt_end)
                if date_debut and date_fin < date_debut:
                    raise ValueError("end-before-start")
        except Exception as e:
            msg = str(e)
            if "end-before-start" in msg:
                err_text = t("imap.error.date_end_before_start.body", self.lang)
            else:
                err_text = t("imap.error.date_invalid.body", self.lang, error=msg)

            QMessageBox.warning(
                self,
                t("imap.error.date_invalid.title", self.lang),
                err_text,
            )
            return

        selected_mailboxes = [cb.text() for cb in self.mailbox_checkboxes if cb.isChecked()]

        if not selected_mailboxes:
            QMessageBox.warning(
                self,
                t("imap.error.no_mailbox_selected.title", self.lang),
                t("imap.error.no_mailbox_selected.body", self.lang),
            )
            return

        if self.btn_export is not None:
            self.btn_export.setEnabled(False)
        if self.btn_fetch is not None:
            self.btn_fetch.setEnabled(False)
        if self.btn_cancel is not None:
            self.btn_cancel.setEnabled(True)
        if self.progress_bar is not None:
            self.progress_bar.setValue(0)

        self.progress_total_msgs = 0
        self.progress_current = 0
        if self.log_widget is not None:
            self.log_widget.clear()
        self.log(t("imap.log.start_export", self.lang))

        self.queue = queue.Queue()
        self.stop_event = threading.Event()

        export_root_dir = self.shared_state.get("reports_root_dir")

        def worker() -> None:
            export_imap_worker(
                host,
                user,
                password,
                date_debut,
                date_fin,
                selected_mailboxes,
                self.queue,
                self.stop_event,
                export_root_dir=export_root_dir,
            )

        self.worker_thread = threading.Thread(target=worker, daemon=True)
        self.worker_thread.start()

        self.queue_timer.start()

    def _on_cancel_export(self) -> None:
        if self.stop_event is not None:
            self.stop_event.set()
            self.log(t("imap.log.cancel_requested", self.lang))

    def _poll_queue(self) -> None:
        if self.queue is None:
            return

        try:
            while True:
                kind, payload = self.queue.get_nowait()
                self._handle_worker_message(kind, payload)
        except queue.Empty:
            pass

    def _handle_worker_message(self, kind: str, payload: object) -> None:
        if kind == "log":
            self.log(str(payload))

        elif kind == "progress_total":
            try:
                self.progress_total_msgs = int(payload)
            except Exception:
                self.progress_total_msgs = 0
            self._update_progress_bar()

        elif kind == "progress":
            try:
                self.progress_current = int(payload)
            except Exception:
                self.progress_current += 1
            self._update_progress_bar()

        elif kind == "info":
            QMessageBox.information(
                self,
                t("imap.info.generic.title", self.lang),
                str(payload),
            )

        elif kind == "error":
            QMessageBox.critical(
                self,
                t("imap.error.generic.title", self.lang),
                str(payload),
            )

        elif kind == "export_dir":
            self.shared_state["last_export_dir"] = str(payload)
            self.log(
                t(
                    "imap.log.export_dir_saved",
                    self.lang,
                    path=str(payload),
                )
            )

        elif kind == "done":
            self.queue_timer.stop()
            self.worker_thread = None
            self.stop_event = None
            if self.btn_fetch is not None:
                self.btn_fetch.setEnabled(True)
            if self.btn_export is not None:
                self.btn_export.setEnabled(True)
            if self.btn_cancel is not None:
                self.btn_cancel.setEnabled(False)
            self.log(t("imap.log.done", self.lang))

    def _update_progress_bar(self) -> None:
        if self.progress_bar is None:
            return

        if self.progress_total_msgs <= 0:
            self.progress_bar.setRange(0, 0)
            return

        self.progress_bar.setRange(0, 100)
        pct = int((self.progress_current / max(1, self.progress_total_msgs)) * 100)
        if pct < 0:
            pct = 0
        if pct > 100:
            pct = 100
        self.progress_bar.setValue(pct)
