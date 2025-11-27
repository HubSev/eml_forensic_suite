from __future__ import annotations
from typing import Dict, Any

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox,
)

from eml_forensic_suite.ui.i18n import t
from eml_forensic_suite.core.oauth.google_oauth import GoogleOAuthClient
from eml_forensic_suite.core.oauth.microsoft_oauth import MicrosoftOAuthClient
from eml_forensic_suite.core.oauth.yahoo_oauth import YahooOAuthClient


class OAuthDialog(QDialog):

    def __init__(self, shared_state: Dict[str, Any], parent=None) -> None:
        super().__init__(parent)
        self.shared_state = shared_state
        self.lang = str(shared_state.get("language", "fr"))

        self._build_ui()

    def _build_ui(self) -> None:
        # Texte entièrement géré par le système de traduction (voir i18n_*).
        self.setWindowTitle(t("oauth.title", self.lang))

        layout = QVBoxLayout(self)

        lbl = QLabel(t("oauth.choose_provider", self.lang), self)
        layout.addWidget(lbl)

        btn_google = QPushButton(t("oauth.btn_google", self.lang), self)
        btn_google.clicked.connect(self._login_google)
        layout.addWidget(btn_google)

        btn_ms = QPushButton(t("oauth.btn_microsoft", self.lang), self)
        btn_ms.clicked.connect(self._login_microsoft)
        layout.addWidget(btn_ms)

        btn_yahoo = QPushButton(t("oauth.btn_yahoo", self.lang), self)
        btn_yahoo.clicked.connect(self._login_yahoo)
        layout.addWidget(btn_yahoo)

        btn_cancel = QPushButton(t("common.cancel", self.lang), self)
        btn_cancel.clicked.connect(self.reject)
        layout.addWidget(btn_cancel)



    def _login_google(self) -> None:
        try:
            client = GoogleOAuthClient()
            client.login_interactive()

            self.shared_state["auth_mode"] = "oauth"
            self.shared_state["oauth_provider"] = "google"
            self.shared_state["oauth_email"] = None

            QMessageBox.information(
                self,
                t("oauth.generic_title", self.lang),
                t("oauth.google.success", self.lang),
            )
            self.accept()
        except Exception as e:
            QMessageBox.critical(
                self,
                t("oauth.google.error_title", self.lang),
                str(e),
            )


    def _login_microsoft(self) -> None:
        try:
            client = MicrosoftOAuthClient()
            client.login_interactive()

            self.shared_state["auth_mode"] = "oauth"
            self.shared_state["oauth_provider"] = "microsoft"
            self.shared_state["oauth_email"] = None

            QMessageBox.information(
                self,
                t("oauth.generic_title", self.lang),
                t("oauth.microsoft.success", self.lang),
            )
            self.accept()
        except Exception as e:
            QMessageBox.critical(
                self,
                t("oauth.microsoft.error_title", self.lang),
                str(e),
            )


    def _login_yahoo(self) -> None:
        try:
            client = YahooOAuthClient()
            client.login_interactive()

            self.shared_state["auth_mode"] = "oauth"
            self.shared_state["oauth_provider"] = "yahoo"
            self.shared_state["oauth_email"] = None

            QMessageBox.information(
                self,
                t("oauth.generic_title", self.lang),
                t("oauth.yahoo.success", self.lang),
            )
            self.accept()
        except Exception as e:
            QMessageBox.critical(
                self,
                t("oauth.yahoo.error_title", self.lang),
                str(e),
            )

