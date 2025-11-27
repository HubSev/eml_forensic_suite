from __future__ import annotations

from typing import Dict, Any, Tuple, List
import os
import threading
import queue

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QPlainTextEdit,
    QProgressBar,
    QMessageBox,
)

from eml_forensic_suite.core.indexer import build_index_csv
from eml_forensic_suite.ui.i18n import t


class IndexTab(QWidget):

    def __init__(self, shared_state: Dict[str, Any], parent: QWidget | None = None):
        super().__init__(parent)
        self.shared_state = shared_state
        self.lang = str(shared_state.get("language", "fr"))

        self.worker_thread: threading.Thread | None = None
        self.queue: "queue.Queue[Tuple[str, object]] | None" = None

        self.index_entries: List[Dict[str, str]] = []

        self.queue_timer = QTimer(self)
        self.queue_timer.setInterval(100)
        self.queue_timer.timeout.connect(self._poll_queue)

        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        row = QHBoxLayout()

        self.label_folder = QLabel(t("index.folder_label", self.lang), self)
        row.addWidget(self.label_folder)

        self.edit_folder = QLineEdit(self)
        row.addWidget(self.edit_folder, 1)

        self.btn_browse = QPushButton(t("index.browse", self.lang), self)
        self.btn_browse.clicked.connect(self._browse_folder)
        row.addWidget(self.btn_browse)

        self.btn_last = QPushButton(t("index.use_last_export", self.lang), self)
        self.btn_last.clicked.connect(self._use_last_export)
        row.addWidget(self.btn_last)

        layout.addLayout(row)

        self.progress = QProgressBar(self)
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        self.log_widget = QPlainTextEdit(self)
        self.log_widget.setReadOnly(True)
        self.log_widget.setPlaceholderText(
            t("index.log_placeholder", self.lang)
        )
        layout.addWidget(self.log_widget)

        self.btn_index = QPushButton(t("index.start_button", self.lang), self)
        self.btn_index.setProperty("primary", True)
        self.btn_index.clicked.connect(self._start_indexing)
        layout.addWidget(self.btn_index)

    def retranslate(self, lang: str) -> None:
        self.lang = lang

        self.label_folder.setText(t("index.folder_label", self.lang))
        self.btn_browse.setText(t("index.browse", self.lang))
        self.btn_last.setText(t("index.use_last_export", self.lang))
        self.log_widget.setPlaceholderText(t("index.log_placeholder", self.lang))
        self.btn_index.setText(t("index.start_button", self.lang))



    def _browse_folder(self) -> None:
        folder = QFileDialog.getExistingDirectory(
            self, t("index.dialog_select_folder", self.lang)
        )
        if folder:
            self.edit_folder.setText(folder)

    def _use_last_export(self) -> None:
        last_export = self.shared_state.get("last_export_dir")
        if last_export:
            self.edit_folder.setText(str(last_export))
        else:
            self.log(t("index.no_last_export", self.lang))

    def _start_indexing(self) -> None:
        if self.worker_thread is not None:
            QMessageBox.information(
                self,
                t("index.error_already_running_title", self.lang),
                t("index.error_already_running_body", self.lang),
            )
            return

        folder = self.edit_folder.text().strip()
        if not folder:
            QMessageBox.warning(
                self,
                t("index.error_no_folder_title", self.lang),
                t("index.error_no_folder_body", self.lang),
            )
            return

        if not os.path.isdir(folder):
            QMessageBox.warning(
                self,
                t("index.error_invalid_folder_title", self.lang),
                t("index.error_invalid_folder_body", self.lang, folder=folder),
            )
            return

        self.btn_index.setEnabled(False)
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.log_widget.clear()
        self.log(t("index.status_selected_folder", self.lang, folder=folder))

        self.queue = queue.Queue()

        def log_cb(msg: str) -> None:
            assert self.queue is not None
            self.queue.put(("log", msg))

        def progress_cb(pct: float) -> None:
            assert self.queue is not None
            self.queue.put(("progress", pct))

        def worker() -> None:
            try:
                csv_path, entries = build_index_csv(folder, log_cb, progress_cb)
                assert self.queue is not None
                self.queue.put(("done", (csv_path, entries)))
            except Exception as e:
                assert self.queue is not None
                self.queue.put(("error", str(e)))

        self.worker_thread = threading.Thread(target=worker, daemon=True)
        self.worker_thread.start()

        self.queue_timer.start()

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

        elif kind == "progress":
            try:
                pct = float(payload)
            except Exception:
                pct = 0.0
            pct = max(0.0, min(100.0, pct))
            self.progress.setRange(0, 100)
            self.progress.setValue(int(pct))

        elif kind == "error":
            self.queue_timer.stop()
            self.worker_thread = None
            self.btn_index.setEnabled(True)
            QMessageBox.critical(
                self,
                t("index.error_indexing_title", self.lang),
                str(payload),
            )
            self.log(t("index.error_log", self.lang, error=str(payload)))

        elif kind == "done":
            self.queue_timer.stop()
            self.worker_thread = None
            self.btn_index.setEnabled(True)

            csv_path, entries = payload
            self.index_entries = entries

            self.shared_state["last_index_dir"] = os.path.dirname(csv_path)
            self.shared_state["last_index_csv"] = csv_path
            self.shared_state["last_index_entries"] = self.index_entries

            self.log(t("index.done_log_success", self.lang))
            self.log(t("index.done_log_path", self.lang, csv_path=csv_path))
            self.log(
                t(
                    "index.done_log_count",
                    self.lang,
                    count=len(self.index_entries),
                )
            )

            QMessageBox.information(
                self,
                t("index.done_msg_title", self.lang),
                t(
                    "index.done_msg_body",
                    self.lang,
                    csv_path=csv_path,
                    count=len(self.index_entries),
                ),
            )

    def log(self, message: str) -> None:
        self.log_widget.appendPlainText(message)
        sb = self.log_widget.verticalScrollBar()
        sb.setValue(sb.maximum())
