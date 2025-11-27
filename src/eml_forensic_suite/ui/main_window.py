from __future__ import annotations

from typing import Any, Dict

from PySide6.QtCore import QSettings
from PySide6.QtGui import QAction
from PySide6.QtGui import QIcon
import os
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QStatusBar,
    QMessageBox,
)

from eml_forensic_suite.core.common_utils import VERSION
from eml_forensic_suite.core.settings import AppSettings, load_settings, save_settings
from eml_forensic_suite.ui.imap_tab import ImapTab
from eml_forensic_suite.ui.index_tab import IndexTab
from eml_forensic_suite.ui.viewer_tab import ViewerTab
from eml_forensic_suite.ui.dashboard_tab import DashboardTab
from eml_forensic_suite.ui.settings_dialog import SettingsDialog
from eml_forensic_suite.ui.themes import Theme, get_stylesheet
from eml_forensic_suite.ui.i18n import t


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        icon_path = os.path.join(os.path.dirname(__file__), "icone.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.app_settings: AppSettings = load_settings()
        self.lang: str = self.app_settings.language or "fr"

        self.resize(1280, 800)

        self.shared_state: Dict[str, Any] = {
            "version": VERSION,
            "last_export_dir": None,
            "last_index_dir": None,
            "last_index_csv": None,
            "last_index_entries": [],
            "reports_root_dir": self.app_settings.reports_root_dir,
            "language": self.lang,
            "lang": self.lang,
            "auth_mode": "password",
            "oauth_provider": None,
            "oauth_email": None,    
        }

        self.qsettings = QSettings()
        self.current_theme: Theme | None = None

        self.file_menu = None
        self.view_menu = None
        self.help_menu = None

        self.act_settings: QAction | None = None
        self.act_quit: QAction | None = None
        self.act_theme_dark: QAction | None = None
        self.act_theme_light: QAction | None = None
        self.act_about: QAction | None = None

        self._init_ui()
        self._init_menu()
        self._init_status_bar()
        self._init_theme()
        self._retranslate_ui()

    def _init_ui(self) -> None:
        central = QWidget(self)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)

        self.tabs = QTabWidget(central)
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(False)

        self.imap_tab = ImapTab(shared_state=self.shared_state, parent=self)
        self.tabs.addTab(self.imap_tab, "")

        self.index_tab = IndexTab(shared_state=self.shared_state, parent=self)
        self.tabs.addTab(self.index_tab, "")

        self.viewer_tab = ViewerTab(shared_state=self.shared_state, parent=self)
        self.tabs.addTab(self.viewer_tab, "")

        self.dashboard_tab = DashboardTab(shared_state=self.shared_state, parent=self)
        self.tabs.addTab(self.dashboard_tab, "")

        layout.addWidget(self.tabs)
        self.setCentralWidget(central)

    def _init_menu(self) -> None:
        menubar = self.menuBar()

        self.file_menu = menubar.addMenu("")

        self.act_settings = QAction(self)
        self.act_settings.triggered.connect(self._open_settings_dialog)
        self.file_menu.addAction(self.act_settings)

        self.file_menu.addSeparator()

        self.act_quit = QAction(self)
        self.act_quit.setShortcut("Ctrl+Q")
        self.act_quit.triggered.connect(self.close)
        self.file_menu.addAction(self.act_quit)

        self.view_menu = menubar.addMenu("")

        self.act_theme_dark = QAction(self, checkable=True)
        self.act_theme_light = QAction(self, checkable=True)

        self.act_theme_dark.triggered.connect(
            lambda: self._change_theme(Theme.DARK)
        )
        self.act_theme_light.triggered.connect(
            lambda: self._change_theme(Theme.LIGHT)
        )

        self.view_menu.addAction(self.act_theme_dark)
        self.view_menu.addAction(self.act_theme_light)

        self.help_menu = menubar.addMenu("")

        self.act_about = QAction(self)
        self.act_about.triggered.connect(self._show_about)
        self.help_menu.addAction(self.act_about)

    def _open_settings_dialog(self) -> None:
        dialog = SettingsDialog(self.app_settings, self)
        if not dialog.exec():
            return

        if dialog.result_settings is None:
            return


        self.app_settings = dialog.result_settings
        save_settings(self.app_settings)

        self.shared_state["reports_root_dir"] = self.app_settings.reports_root_dir
        self.shared_state["language"] = self.app_settings.language
        self.lang = self.app_settings.language or "fr"

        self._retranslate_ui()

        self.set_status(t("status.settings.saved", self.lang), 5000)


    def _show_about(self) -> None:
        QMessageBox.information(
            self,
            t("menu.help.about", self.lang),
            (
                f"{t('app.title', self.lang)}\n"
                f"{t('about.version_label', self.lang)} {VERSION}\n\n"
                f"{t('about.description', self.lang)}\n\n"
                "HubSev / HubMyWeb Cyberlab."
            ),
        )

    def _init_status_bar(self) -> None:
        status = QStatusBar(self)
        self.setStatusBar(status)

    def set_status(self, message: str, timeout_ms: int = 0) -> None:
        if self.statusBar():
            self.statusBar().showMessage(message, timeout_ms)

    def _init_theme(self) -> None:
        stored = self.qsettings.value("ui/theme", Theme.DARK.value)
        try:
            theme = Theme(stored)
        except Exception:
            theme = Theme.DARK
        self._apply_theme(theme)

    def _change_theme(self, theme: Theme) -> None:
        if theme == self.current_theme:
            return
        self._apply_theme(theme)
        self.qsettings.setValue("ui/theme", theme.value)

    def _apply_theme(self, theme: Theme) -> None:
        self.current_theme = theme
        self.setStyleSheet(get_stylesheet(theme))

        if self.act_theme_dark and self.act_theme_light:
            if theme == Theme.DARK:
                self.act_theme_dark.setChecked(True)
                self.act_theme_light.setChecked(False)
            else:
                self.act_theme_dark.setChecked(False)
                self.act_theme_light.setChecked(True)

    def _retranslate_ui(self) -> None:
        self.file_menu.setTitle(t("menu.file", self.lang))
        self.view_menu.setTitle(t("menu.view", self.lang))
        self.help_menu.setTitle(t("menu.help", self.lang))

        self.act_settings.setText(t("menu.file.settings", self.lang))
        self.act_quit.setText(t("menu.file.quit", self.lang))
        self.act_theme_dark.setText(t("menu.view.theme.dark", self.lang))
        self.act_theme_light.setText(t("menu.view.theme.light", self.lang))
        self.act_about.setText(t("menu.help.about", self.lang))

        self.setWindowTitle(t("app.title", self.lang))

        self.tabs.setTabText(0, t("tab.imap", self.lang))
        self.tabs.setTabText(1, t("tab.index", self.lang))
        self.tabs.setTabText(2, t("tab.viewer", self.lang))
        self.tabs.setTabText(3, t("tab.dashboard", self.lang))

        self.imap_tab.retranslate(self.lang)
        self.index_tab.retranslate(self.lang)
        self.viewer_tab.retranslate(self.lang)
        self.dashboard_tab.retranslate(self.lang)


        if hasattr(self.imap_tab, "retranslate"):
            self.imap_tab.retranslate(self.lang)
        if hasattr(self.index_tab, "retranslate"):
            self.index_tab.retranslate(self.lang)
        if hasattr(self.viewer_tab, "retranslate"):
            self.viewer_tab.retranslate(self.lang)
        if hasattr(self.dashboard_tab, "retranslate"):
            self.dashboard_tab.retranslate(self.lang)

        if self.statusBar() and not self.statusBar().currentMessage():
            self.statusBar().showMessage(t("status.ready", self.lang))
