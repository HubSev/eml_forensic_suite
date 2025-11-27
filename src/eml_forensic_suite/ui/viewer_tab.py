from __future__ import annotations

from typing import Dict, List, Any, Optional

import os
import csv

from email import policy
from email.parser import BytesParser
from email.message import EmailMessage

from PySide6.QtCore import (
    Qt,
    QModelIndex,
    QUrl,
)
from PySide6.QtGui import QFont, QPixmap, QDesktopServices
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QPlainTextEdit,
    QTableView,
    QHeaderView,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QSplitter,
    QFileDialog,
    QDialog,
    QCompleter,
)

from eml_forensic_suite.ui.i18n import t
from eml_forensic_suite.core.attachments import (
    extract_attachments,
    save_attachment,
    AttachmentInfo,
)
from eml_forensic_suite.ui.index_model import IndexTableModel
from eml_forensic_suite.ui.forensic_query import ForensicFilterProxyModel


class ViewerTab(QWidget):

    def __init__(self, shared_state: Dict[str, Any], parent: QWidget | None = None):
        super().__init__(parent)
        self.shared_state = shared_state
        self.lang = str(shared_state.get("language", "fr"))

        self.index_model = IndexTableModel(
            rows=shared_state.get("last_index_entries") or [],
            lang=self.lang,
        )
        self.proxy_model = ForensicFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.index_model)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_model.setFilterKeyColumn(-1)

        self.current_msg: EmailMessage | None = None
        self.current_attachments: List[tuple[AttachmentInfo, bytes]] = []
        self.current_entry: Dict[str, str] | None = None

        self.completer: QCompleter | None = None

        self._build_ui()
        self._load_initial_state()

    def _build_ui(self) -> None:
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(6)

        top_row = QHBoxLayout()

        self.btn_load_last = QPushButton(t("viewer.btn_load_last", self.lang), self)
        self.btn_load_last.clicked.connect(self._load_last_index_from_state)
        top_row.addWidget(self.btn_load_last)

        self.btn_open_csv = QPushButton(t("viewer.btn_open_csv", self.lang), self)
        self.btn_open_csv.clicked.connect(self._open_csv_dialog)
        top_row.addWidget(self.btn_open_csv)

        top_row.addStretch(1)
        main_layout.addLayout(top_row)

        search_row = QHBoxLayout()
        self.lbl_search = QLabel(t("viewer.search_label", self.lang), self)
        self.edit_search = QLineEdit(self)
        self.edit_search.setPlaceholderText(t("viewer.search_placeholder", self.lang))
        self.edit_search.setToolTip(
            t("viewer.search_tooltip", self.lang)
        )

        self.btn_clear = QPushButton(t("viewer.search_clear", self.lang), self)
        self.btn_clear.clicked.connect(self._clear_search)

        self.edit_search.textChanged.connect(self._on_search_changed)

        search_row.addWidget(self.lbl_search)
        search_row.addWidget(self.edit_search, 1)
        search_row.addWidget(self.btn_clear)

        main_layout.addLayout(search_row)

        splitter = QSplitter(Qt.Vertical, self)

        self.table_index = QTableView(self)
        self.table_index.setModel(self.proxy_model)
        self.table_index.setSelectionBehavior(QTableView.SelectRows)
        self.table_index.setSelectionMode(QTableView.SingleSelection)
        self.table_index.setAlternatingRowColors(True)
        self.table_index.horizontalHeader().setStretchLastSection(True)
        self.table_index.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.table_index.verticalHeader().setVisible(False)

        self.table_index.selectionModel().selectionChanged.connect(
            self._on_selection_changed,
        )

        splitter.addWidget(self.table_index)

        detail_widget = QWidget(self)
        detail_layout = QVBoxLayout(detail_widget)
        detail_layout.setSpacing(4)

        self.lbl_headers = QLabel(t("viewer.headers_label", self.lang), detail_widget)
        self.lbl_headers.setFont(self._bold_font())
        detail_layout.addWidget(self.lbl_headers)

        self.text_headers = QPlainTextEdit(detail_widget)
        self.text_headers.setReadOnly(True)
        self.text_headers.setPlaceholderText(t("viewer.headers_placeholder", self.lang))
        detail_layout.addWidget(self.text_headers, 1)

        self.lbl_body = QLabel(t("viewer.body_label", self.lang), detail_widget)
        self.lbl_body.setFont(self._bold_font())
        detail_layout.addWidget(self.lbl_body)

        self.text_body = QPlainTextEdit(detail_widget)
        self.text_body.setReadOnly(True)
        self.text_body.setPlaceholderText(t("viewer.body_placeholder", self.lang))
        detail_layout.addWidget(self.text_body, 2)

        self.lbl_attachments = QLabel(
            t("viewer.attachments_label", self.lang),
            detail_widget,
        )
        self.lbl_attachments.setFont(self._bold_font())
        detail_layout.addWidget(self.lbl_attachments)

        self.table_attachments = QTableWidget(detail_widget)
        self.table_attachments.setColumnCount(5)
        self.table_attachments.setHorizontalHeaderLabels(
            [
                t("viewer.attach.col.name", self.lang),
                t("viewer.attach.col.mime", self.lang),
                t("viewer.attach.col.size", self.lang),
                t("viewer.attach.col.sha256", self.lang),
                t("viewer.attach.col.suspicious", self.lang),
            ]
        )
        self.table_attachments.horizontalHeader().setStretchLastSection(True)
        self.table_attachments.horizontalHeader().setSectionResizeMode(
            QHeaderView.Interactive,
        )
        self.table_attachments.verticalHeader().setVisible(False)
        self.table_attachments.setSelectionBehavior(QTableWidget.SelectRows)
        self.table_attachments.setSelectionMode(QTableWidget.SingleSelection)

        detail_layout.addWidget(self.table_attachments, 1)

        attach_btn_row = QHBoxLayout()
        self.btn_extract_one = QPushButton(
            t("viewer.attach.extract_one", self.lang),
            detail_widget,
        )
        self.btn_extract_all = QPushButton(
            t("viewer.attach.extract_all", self.lang),
            detail_widget,
        )
        self.btn_preview = QPushButton(
            t("viewer.attach.preview", self.lang),
            detail_widget,
        )

        self.btn_extract_one.clicked.connect(self._extract_selected_attachment)
        self.btn_extract_all.clicked.connect(self._extract_all_attachments)
        self.btn_preview.clicked.connect(self._preview_selected_attachment)

        attach_btn_row.addWidget(self.btn_extract_one)
        attach_btn_row.addWidget(self.btn_extract_all)
        attach_btn_row.addWidget(self.btn_preview)
        attach_btn_row.addStretch(1)

        detail_layout.addLayout(attach_btn_row)

        splitter.addWidget(detail_widget)
        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 3)

        main_layout.addWidget(splitter)


    def _bold_font(self) -> QFont:
        f = QFont()
        f.setBold(True)
        return f

    def _load_initial_state(self) -> None:
        entries = self.shared_state.get("last_index_entries") or []
        if entries:
            self._set_rows(entries)

    def _set_rows(self, rows: List[Dict[str, str]]) -> None:
        self.index_model.set_rows(rows)
        self.table_index.resizeColumnsToContents()
        self.text_headers.clear()
        self.text_body.clear()
        self.table_attachments.setRowCount(0)
        self.current_msg = None
        self.current_attachments = []
        self.current_entry = None

        self._rebuild_autocomplete_from_rows(rows)

    def _rebuild_autocomplete_from_rows(self, rows: List[Dict[str, str]]) -> None:
        senders: set[str] = set()
        domains: set[str] = set()
        folders: set[str] = set()
        exts: set[str] = set()
        levels: set[str] = set()

        for row in rows:
            from_h = (row.get("from_header") or "").strip()
            if from_h:
                senders.add(from_h)

                lower = from_h.lower()
                if "@" in lower:
                    dom = lower.split("@", 1)[1]
                    for sep in [">", ")", " ", ","]:
                        if sep in dom:
                            dom = dom.split(sep, 1)[0]
                    dom = dom.strip()
                    if dom:
                        domains.add(dom)

            folder = (row.get("folder_imap") or "").strip()
            if folder:
                folders.add(folder)

            att_names = row.get("attachment_filenames") or ""
            if att_names:
                raw_parts = []
                for part in att_names.split(";"):
                    raw_parts.extend(part.split(","))
                for name in raw_parts:
                    name = name.strip()
                    if not name:
                        continue
                    _, ext = os.path.splitext(name)
                    ext = ext.lower().lstrip(".")
                    if ext:
                        exts.add(ext)

            level = (row.get("suspicion_level") or "").upper().strip()
            if level:
                levels.add(level)

        base_tokens = {
            "from:",
            "to:",
            "cc:",
            "subject:",
            "hash:",
            "folder:",
            "domain:",
            "date:",
            "attachment:true",
            "attachment:false",
            "NOT ",
            "suspicion_score:",
            "suspicion_level:",
        }

        tokens: set[str] = set(base_tokens)

        for s in senders:
            tokens.add(f'from:"{s}"')
        for d in domains:
            tokens.add(f"domain:{d}")
        for f in folders:
            tokens.add(f'folder:"{f}"')
        for e in exts:
            tokens.add(e)
            tokens.add(f".{e}")
            tokens.add(f'"{e}"')
        for lvl in levels:
            tokens.add(f"suspicion_level:{lvl.lower()}")
            tokens.add(f"suspicion_level:{lvl}")

        tokens_list = sorted(tokens)

        completer = QCompleter(tokens_list, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        completer.setCompletionMode(QCompleter.PopupCompletion)

        self.completer = completer
        self.edit_search.setCompleter(completer)

    def _load_last_index_from_state(self) -> None:
        entries = self.shared_state.get("last_index_entries")
        csv_path = self.shared_state.get("last_index_csv")

        if entries:
            self._set_rows(entries)
            if csv_path:
                self._log_info(f"Dernier index chargé depuis : {csv_path}")
            else:
                self._log_info("Dernier index chargé depuis la mémoire.")
            return

        if not csv_path:
            QMessageBox.information(
                self,
                t("viewer.no_index_title", self.lang),
                t("viewer.no_index_body", self.lang),
            )
            return

        try:
            rows = self._load_entries_from_csv(csv_path)
        except Exception as e:
            QMessageBox.critical(
                self,
                t("viewer.error_csv_title", self.lang),
                t("viewer.error_csv_body", self.lang, path=csv_path, error=str(e)),
            )
            return

        self.shared_state["last_index_entries"] = rows
        self._set_rows(rows)
        self._log_info(f"Index rechargé depuis le CSV : {csv_path}")

    def _open_csv_dialog(self) -> None:
        csv_path, _ = QFileDialog.getOpenFileName(
            self,
            t("viewer.open_csv_title", self.lang),
            "",
            "Fichiers CSV (*.csv);;Tous les fichiers (*.*)",
        )
        if not csv_path:
            return

        try:
            rows = self._load_entries_from_csv(csv_path)
        except Exception as e:
            QMessageBox.critical(
                self,
                t("viewer.error_csv_title", self.lang),
                t("viewer.error_csv_body", self.lang, path=csv_path, error=str(e)),
            )
            return

        self.shared_state["last_index_dir"] = os.path.dirname(csv_path)
        self.shared_state["last_index_csv"] = csv_path
        self.shared_state["last_index_entries"] = rows

        self._set_rows(rows)
        self._log_info(f"Index chargé depuis : {csv_path}")

    def _load_entries_from_csv(self, csv_path: str) -> List[Dict[str, str]]:
        base_dir = os.path.dirname(csv_path)
        rows: List[Dict[str, str]] = []

        with open(csv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rel = row.get("relative_path", "") or ""
                full_path = os.path.join(base_dir, rel) if rel else ""
                row["full_path"] = full_path
                rows.append(row)

        return rows

    def _clear_search(self) -> None:
        self.edit_search.clear()
        self.proxy_model.set_query_text("")

    def _on_search_changed(self, text: str) -> None:
        pattern = text.strip()
        self.proxy_model.set_query_text(pattern)

    def _on_selection_changed(self, selected, _deselected) -> None:
        if not selected.indexes():
            return

        index: QModelIndex = selected.indexes()[0]
        source_index = self.proxy_model.mapToSource(index)
        row_data = self.index_model.row_at(source_index.row())
        if not row_data:
            return

        self._load_email(row_data)

    def _load_email(self, entry: Dict[str, str]) -> None:
        self.current_entry = entry

        full_path = entry.get("full_path")
        if not full_path:
            base_dir = self.shared_state.get("last_index_dir") or ""
            rel = entry.get("relative_path", "")
            full_path = os.path.join(str(base_dir), rel)

        if not os.path.isfile(full_path):
            QMessageBox.warning(
                self,
                t("viewer.error_missing_eml_title", self.lang),
                t("viewer.error_missing_eml_body", self.lang, path=full_path),
            )
            return

        try:
            with open(full_path, "rb") as f:
                msg = BytesParser(policy=policy.default).parse(f)
        except Exception as e:
            QMessageBox.critical(
                self,
                t("viewer.error_parse_eml_title", self.lang),
                f"{t('viewer.error_parse_eml_body', self.lang, path=full_path)}\n\n{e}",
            )
            return

        self.current_msg = msg

        headers_lines: List[str] = [f"{k}: {v}" for k, v in msg.items()]
        self.text_headers.setPlainText("\n".join(headers_lines))

        body_text = self._extract_body_text(msg)
        self.text_body.setPlainText(body_text)

        self.current_attachments = extract_attachments(msg)
        self._refresh_attachments_table()

    def _extract_body_text(self, msg: EmailMessage) -> str:
        if msg.is_multipart():
            parts_text: List[str] = []
            parts_html: List[str] = []

            for part in msg.walk():
                if part.is_multipart():
                    continue

                ctype = part.get_content_type()
                try:
                    payload = part.get_payload(decode=True) or b""
                    text = payload.decode(
                        part.get_content_charset() or "utf-8",
                        errors="replace",
                    )
                except Exception:
                    text = ""

                if ctype == "text/plain":
                    parts_text.append(text)
                elif ctype == "text/html":
                    parts_html.append(text)

            if parts_text:
                return "\n\n".join(parts_text)
            if parts_html:
                return "\n\n---- [HTML Fallback] ----\n\n" + "\n\n".join(parts_html)

            return ""
        else:
            try:
                payload = msg.get_payload(decode=True) or b""
                return payload.decode(
                    msg.get_content_charset() or "utf-8",
                    errors="replace",
                )
            except Exception:
                return ""

    def _build_attachment_subfolder(self, msg_id: str) -> str:
        entry = self.current_entry or {}
        folder = entry.get("folder_imap", "UNKNOWN")
        seq = entry.get("sequence_number", "")
        subject = (entry.get("subject") or "").strip()

        if len(subject) > 40:
            subject = subject[:40] + "…"

        def _clean(s: str) -> str:
            s = s.replace(os.sep, "_").replace(":", "_")
            allowed = (
                "abcdefghijklmnopqrstuvwxyz"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "0123456789-_ ."
            )
            return "".join(ch if ch in allowed else "_" for ch in s)

        folder_clean = _clean(folder)
        seq_clean = _clean(seq)
        subj_clean = _clean(subject) or "no-subject"

        msg_id_clean = (
            msg_id.replace("<", "")
            .replace(">", "")
            .replace(":", "")
            .replace("/", "_")
        )
        if len(msg_id_clean) > 20:
            msg_id_clean = msg_id_clean[:20]

        parts = [
            folder_clean,
            f"seq{seq_clean}" if seq_clean else "",
            subj_clean,
            msg_id_clean,
        ]
        parts = [p for p in parts if p]

        subfolder = "__".join(parts)
        if not subfolder:
            subfolder = "UNKNOWN"

        return subfolder

    def _refresh_attachments_table(self) -> None:
        self.table_attachments.setRowCount(0)

        for info, _data in self.current_attachments:
            row = self.table_attachments.rowCount()
            self.table_attachments.insertRow(row)

            self.table_attachments.setItem(row, 0, QTableWidgetItem(info.filename))
            self.table_attachments.setItem(row, 1, QTableWidgetItem(info.mime_type))
            self.table_attachments.setItem(row, 2, QTableWidgetItem(str(info.size)))
            self.table_attachments.setItem(row, 3, QTableWidgetItem(info.sha256))

            label = t("viewer.attach.no", self.lang)
            if info.is_suspicious:
                label = t("viewer.attach.yes", self.lang) + f" ({info.suspicion_flags})"
            self.table_attachments.setItem(row, 4, QTableWidgetItem(label))

        self.table_attachments.resizeColumnsToContents()

    def _get_root_extract_dir(self) -> Optional[str]:
        reports_dir = self.shared_state.get("reports_root_dir")
        if reports_dir:
            return str(reports_dir)

        last_index_dir = self.shared_state.get("last_index_dir")
        if last_index_dir:
            return str(last_index_dir)

        return None

    def _extract_selected_attachment(self) -> None:
        if self.current_msg is None or not self.current_attachments:
            QMessageBox.information(
                self,
                t("viewer.attach.no_msg_title", self.lang),
                t("viewer.attach.no_msg_body", self.lang),
            )
            return

        row = self.table_attachments.currentRow()
        if row < 0 or row >= len(self.current_attachments):
            QMessageBox.information(
                self,
                t("viewer.attach.no_selection_title", self.lang),
                t("viewer.attach.no_selection_body", self.lang),
            )
            return

        root_dir = self._get_root_extract_dir()
        if not root_dir:
            QMessageBox.warning(
                self,
                t("viewer.attach.no_root_title", self.lang),
                t("viewer.attach.no_root_body", self.lang),
            )
            return

        info, data = self.current_attachments[row]

        msg_id = str(
            self.current_msg.get("Message-ID")
            or self.current_msg.get("Message-Id")
            or "NO_MESSAGE_ID"
        )
        subfolder = self._build_attachment_subfolder(msg_id)

        out_path = save_attachment(
            root_dir,
            subfolder,
            info,
            data,
            email_entry=self.current_entry,
            msg_id=msg_id,
        )

        QMessageBox.information(
            self,
            t("viewer.attach.extract_one_title", self.lang),
            t("viewer.attach.extract_one_body", self.lang, path=out_path),
        )

    def _extract_all_attachments(self) -> None:
        if self.current_msg is None or not self.current_attachments:
            QMessageBox.information(
                self,
                t("viewer.attach.no_msg_title", self.lang),
                t("viewer.attach.no_msg_body", self.lang),
            )
            return

        root_dir = self._get_root_extract_dir()
        if not root_dir:
            QMessageBox.warning(
                self,
                t("viewer.attach.no_root_title", self.lang),
                t("viewer.attach.no_root_body", self.lang),
            )
            return

        msg_id = str(
            self.current_msg.get("Message-ID")
            or self.current_msg.get("Message-Id")
            or "NO_MESSAGE_ID"
        )
        subfolder = self._build_attachment_subfolder(msg_id)

        paths: List[str] = []
        for info, data in self.current_attachments:
            out_path = save_attachment(
                root_dir,
                subfolder,
                info,
                data,
                email_entry=self.current_entry,
                msg_id=msg_id,
            )
            paths.append(out_path)

        text_paths = "\n".join(paths)

        QMessageBox.information(
            self,
            t("viewer.attach.extract_all_title", self.lang),
            t(
                "viewer.attach.extract_all_body",
                self.lang,
                count=len(paths),
                paths=text_paths,
            ),
        )

    def _preview_selected_attachment(self) -> None:
        if self.current_msg is None or not self.current_attachments:
            QMessageBox.information(
                self,
                t("viewer.attach.no_msg_title", self.lang),
                t("viewer.attach.no_msg_body", self.lang),
            )
            return

        row = self.table_attachments.currentRow()
        if row < 0 or row >= len(self.current_attachments):
            QMessageBox.information(
                self,
                t("viewer.attach.no_selection_title", self.lang),
                t("viewer.attach.no_selection_body", self.lang),
            )
            return

        info, data = self.current_attachments[row]

        if info.mime_type.startswith("image/"):
            pixmap = QPixmap()
            if not pixmap.loadFromData(data):
                QMessageBox.warning(
                    self,
                    t("viewer.attach.preview_failed_title", self.lang),
                    t("viewer.attach.preview_failed_body", self.lang),
                )
                return

            dlg = QDialog(self)
            dlg.setWindowTitle(info.filename)
            vbox = QVBoxLayout(dlg)

            lbl = QLabel(dlg)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setPixmap(pixmap)
            vbox.addWidget(lbl)

            dlg.resize(800, 600)
            dlg.exec()
            return

        if info.mime_type == "application/pdf" or info.filename.lower().endswith(".pdf"):
            root_dir = self._get_root_extract_dir()
            if not root_dir:
                QMessageBox.warning(
                    self,
                    t("viewer.attach.no_root_title", self.lang),
                    t("viewer.attach.no_root_body", self.lang),
                )
                return

            msg_id = str(
                self.current_msg.get("Message-ID")
                or self.current_msg.get("Message-Id")
                or "NO_MESSAGE_ID"
            )
            subfolder = self._build_attachment_subfolder(msg_id)

            out_path = save_attachment(
                root_dir,
                subfolder,
                info,
                data,
                email_entry=self.current_entry,
                msg_id=msg_id,
            )

            url = QUrl.fromLocalFile(out_path)
            if not QDesktopServices.openUrl(url):
                QMessageBox.warning(
                    self,
                    t("viewer.attach.preview_failed_title", self.lang),
                    t("viewer.attach.preview_failed_body", self.lang),
                )
            return

        QMessageBox.information(
            self,
            t("viewer.attach.preview_unsupported_title", self.lang),
            t("viewer.attach.preview_unsupported_body", self.lang, mime=info.mime_type),
        )

    def retranslate(self, lang: str) -> None:
        self.lang = lang


        self.lbl_search.setText(t("viewer.search_label", self.lang))
        self.edit_search.setPlaceholderText(t("viewer.search_placeholder", self.lang))
        self.edit_search.setToolTip(t("viewer.search_tooltip", self.lang))
        self.btn_clear.setText(t("viewer.search_clear", self.lang))

        self.lbl_headers.setText(t("viewer.headers_label", self.lang))
        self.text_headers.setPlaceholderText(t("viewer.headers_placeholder", self.lang))

        self.lbl_body.setText(t("viewer.body_label", self.lang))
        self.text_body.setPlaceholderText(t("viewer.body_placeholder", self.lang))

        self.lbl_attachments.setText(t("viewer.attachments_label", self.lang))

        self.table_attachments.setHorizontalHeaderLabels(
            [
                t("viewer.attach.col.name", self.lang),
                t("viewer.attach.col.mime", self.lang),
                t("viewer.attach.col.size", self.lang),
                t("viewer.attach.col.sha256", self.lang),
                t("viewer.attach.col.suspicious", self.lang),
            ]
        )

        self.btn_extract_one.setText(t("viewer.attach.extract_one", self.lang))
        self.btn_extract_all.setText(t("viewer.attach.extract_all", self.lang))
        self.btn_preview.setText(t("viewer.attach.preview", self.lang))


    def _log_info(self, message: str) -> None:
        print(f"[ViewerTab] {message}")
