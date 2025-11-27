from __future__ import annotations

from typing import Optional

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QComboBox,
    QDialogButtonBox,
    QWidget,
    QHBoxLayout,
)

from eml_forensic_suite.core.settings import AppSettings
from eml_forensic_suite.ui.i18n import t, LANG_CHOICES


class SettingsDialog(QDialog):
    def __init__(self, app_settings: AppSettings, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self._initial_settings = app_settings
        self.result_settings: Optional[AppSettings] = None

        self.lang = app_settings.language or "fr"

        self._build_ui()
        self._load_from_settings(app_settings)

    def _build_ui(self) -> None:
        self.setWindowTitle(t("settings.title", self.lang))

        main_layout = QVBoxLayout(self)

        form = QFormLayout()
        main_layout.addLayout(form)

        self.edit_reports_dir = QLineEdit(self)
        btn_browse = QPushButton(t("settings.reports_dir.browse", self.lang), self)
        btn_browse.clicked.connect(self._browse_reports_dir)

        row_reports = QHBoxLayout()
        row_reports.addWidget(self.edit_reports_dir, 1)
        row_reports.addWidget(btn_browse)

        form.addRow(t("settings.reports_dir.label", self.lang), row_reports)

        self.combo_language = QComboBox(self)
        for code, label in LANG_CHOICES:
            self.combo_language.addItem(label, code)
        form.addRow(t("settings.language.label", self.lang), self.combo_language)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            parent=self,
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        main_layout.addWidget(buttons)

    def _load_from_settings(self, settings: AppSettings) -> None:
        if settings.reports_root_dir:
            self.edit_reports_dir.setText(settings.reports_root_dir)
        else:
            self.edit_reports_dir.clear()

        code = settings.language or "fr"
        index = self.combo_language.findData(code)
        if index == -1:
            index = self.combo_language.findData("fr")
        if index >= 0:
            self.combo_language.setCurrentIndex(index)

    def _browse_reports_dir(self) -> None:
        current = self.edit_reports_dir.text().strip()
        start_dir = current or ""

        folder = QFileDialog.getExistingDirectory(
            self,
            t("settings.reports_dir.dialog_title", self.lang),
            start_dir,
        )
        if folder:
            self.edit_reports_dir.setText(folder)

    def accept(self) -> None:
        reports_root_dir = self.edit_reports_dir.text().strip() or None
        lang_code = self.combo_language.currentData() or "fr"

        self.result_settings = AppSettings(
            reports_root_dir=reports_root_dir,
            language=str(lang_code),
        )

        super().accept()
