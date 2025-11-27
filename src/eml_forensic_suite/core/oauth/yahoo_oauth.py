from __future__ import annotations
from typing import Optional, Dict
import json
import os

from authlib.integrations.requests_client import OAuth2Session

from eml_forensic_suite.core.oauth.oauth_server import OAuthCallbackServer
from eml_forensic_suite.core.oauth.config import (
    YAHOO_CLIENT_ID,
    YAHOO_CLIENT_SECRET,
    TOKEN_DIR,
)

AUTH_URL = "https://api.login.yahoo.com/oauth2/request_auth"
TOKEN_URL = "https://api.login.yahoo.com/oauth2/get_token"
REDIRECT_PORT = 8767
REDIRECT_URI = f"http://localhost:{REDIRECT_PORT}/callback"

SCOPES = ["mail-r"]  # lecture mail (à confirmer dans la doc Yahoo)


class YahooOAuthClient:
    def __init__(self) -> None:
        self.client_id = YAHOO_CLIENT_ID
        self.client_secret = YAHOO_CLIENT_SECRET
        self.token_path = os.path.join(TOKEN_DIR, "yahoo_token.json")
        self.session: Optional[OAuth2Session] = None

    def load_token(self) -> Optional[Dict]:
        if os.path.isfile(self.token_path):
            with open(self.token_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

    def save_token(self, token: Dict) -> None:
        with open(self.token_path, "w", encoding="utf-8") as f:
            json.dump(token, f, indent=2)

    def login_interactive(self) -> Dict:
        if not self.client_id or not self.client_secret:
            raise RuntimeError("Client ID/secret Yahoo manquants dans config.py")

        server = OAuthCallbackServer(port=REDIRECT_PORT)
        server.start()

        self.session = OAuth2Session(
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope=SCOPES,
            redirect_uri=REDIRECT_URI,
        )

        url, state = self.session.create_authorization_url(AUTH_URL)

        import webbrowser
        webbrowser.open(url)

        import time
        while server.code is None:
            time.sleep(0.2)

        code = server.code
        server.stop()

        token = self.session.fetch_token(
            TOKEN_URL,
            code=code,
            client_secret=self.client_secret,
        )

        self.save_token(token)
        return token

    def get_valid_access_token(self) -> str:
        token = self.load_token()
        if not token:
            raise RuntimeError(
                "Aucun token OAuth2 Yahoo n'est enregistré. Lance d'abord login_interactive()."
            )

        self.session = OAuth2Session(
            client_id=self.client_id,
            client_secret=self.client_secret,
            token=token,
        )

        if self.session.token.is_expired():
            new_token = self.session.refresh_token(
                TOKEN_URL,
                refresh_token=token.get("refresh_token"),
            )
            self.save_token(new_token)
            return new_token["access_token"]

        return token["access_token"]
