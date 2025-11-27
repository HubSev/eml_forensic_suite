from __future__ import annotations
from typing import Optional
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import urllib.parse


class OAuthCallbackServer:

    def __init__(self, port: int = 8765):
        self.port = port
        self._code: Optional[str] = None
        self._server: Optional[HTTPServer] = None
        self._thread: Optional[threading.Thread] = None

    @property
    def code(self) -> Optional[str]:
        return self._code

    def start(self) -> None:
        handler = self._make_handler()
        self._server = HTTPServer(("127.0.0.1", self.port), handler)
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        if self._server:
            self._server.shutdown()

    def _make_handler(self):
        parent = self

        class CallbackHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                parsed = urllib.parse.urlparse(self.path)
                params = urllib.parse.parse_qs(parsed.query)

                if "code" in params:
                    parent._code = params["code"][0]
                    self.send_response(200)
                    self.send_header("Content-type", "text/html; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(
                        b"<h2>Authentification r\xc3\xa9ussie</h2><p>Vous pouvez fermer cette fenetre.</p>"
                    )
                else:
                    self.send_response(400)
                    self.end_headers()

        return CallbackHandler
