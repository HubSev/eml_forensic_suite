from __future__ import annotations

from typing import Dict, List

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

from eml_forensic_suite.ui.i18n import t


class IndexTableModel(QAbstractTableModel):

    COLUMNS = [
        "folder_imap",
        "sequence_number",
        "date_header",
        "from_header",
        "to_header",
        "cc_header",
        "cci_header",
        "subject",
        "message_id",
        "sha256",
        "has_attachments",
        "attachment_count",
        "attachment_filenames",
        "dkim_result",
        "spf_result",
        "dmarc_result",
        "auth_comment",
        "received_count",
        "received_anomalies",
        "integrity_flags",
        "suspicion_score",
        "suspicion_level",
        "suspicion_reasons",
        "relative_path",
        "filename",
    ]

    HEADERS_KEYS = {
        "folder_imap": "viewer.col.folder_imap",
        "sequence_number": "viewer.col.sequence_number",
        "date_header": "viewer.col.date_header",
        "from_header": "viewer.col.from_header",
        "to_header": "viewer.col.to_header",
        "cc_header": "viewer.col.cc_header",
        "cci_header": "viewer.col.cci_header",
        "subject": "viewer.col.subject",
        "message_id": "viewer.col.message_id",
        "sha256": "viewer.col.sha256",
        "has_attachments": "viewer.col.has_attachments",
        "attachment_count": "viewer.col.attachment_count",
        "attachment_filenames": "viewer.col.attachment_filenames",
        "dkim_result": "viewer.col.dkim_result",
        "spf_result": "viewer.col.spf_result",
        "dmarc_result": "viewer.col.dmarc_result",
        "auth_comment": "viewer.col.auth_comment",
        "received_count": "viewer.col.received_count",
        "received_anomalies": "viewer.col.received_anomalies",
        "integrity_flags": "viewer.col.integrity_flags",
        "suspicion_score": "viewer.col.suspicion_score",
        "suspicion_level": "viewer.col.suspicion_level",
        "suspicion_reasons": "viewer.col.suspicion_reasons",
        "relative_path": "viewer.col.relative_path",
        "filename": "viewer.col.filename",
    }

    def __init__(
        self,
        rows: List[Dict[str, str]] | None = None,
        lang: str = "fr",
        parent=None,
    ) -> None:
        super().__init__(parent)
        self._rows: List[Dict[str, str]] = rows or []
        self.lang = lang


    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self._rows)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self.COLUMNS)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid():
            return None

        row = self._rows[index.row()]
        col_name = self.COLUMNS[index.column()]

        if role in (Qt.DisplayRole, Qt.EditRole):
            if col_name == "suspicion_score":
                score_str = row.get("suspicion_score", "") or ""
                return score_str

            if col_name == "suspicion_level":
                level = (row.get("suspicion_level") or "").upper()
                icon = self._level_to_icon(level, row.get("suspicion_score"))
                if level:
                    return f"{icon} {level}"
                score_str = row.get("suspicion_score", "") or ""
                if score_str:
                    return f"{icon} {score_str}"
                return ""

            return row.get(col_name, "")

        if role == Qt.ToolTipRole and col_name == "suspicion_level":
            reasons = row.get("suspicion_reasons", "") or ""
            if reasons:
                return reasons

        return None

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.DisplayRole,
    ):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            col_name = self.COLUMNS[section]
            key = self.HEADERS_KEYS.get(col_name, col_name)
            return t(key, self.lang)
        else:
            return section + 1


    def _level_to_icon(self, level: str, score_str: str | None) -> str:
        level = (level or "").upper()
        score = 0
        try:
            if score_str:
                score = int(score_str)
        except Exception:
            score = 0

        if level == "HIGH":
            return "🔴"
        if level == "MEDIUM":
            return "🟠"
        if level == "LOW":
            return "🟢"

        if score > 0:
            return "🟢"
        return "⚪"

    def set_rows(self, rows: List[Dict[str, str]]) -> None:
        self.beginResetModel()
        self._rows = rows
        self.endResetModel()

    def row_at(self, row: int) -> Dict[str, str] | None:
        if 0 <= row < len(self._rows):
            return self._rows[row]
        return None

    def all_rows(self) -> List[Dict[str, str]]:
        return list(self._rows)

    def set_language(self, lang: str) -> None:
        self.lang = lang
        self.headerDataChanged.emit(Qt.Horizontal, 0, len(self.COLUMNS) - 1)
