from __future__ import annotations

import sys
from PySide6.QtWidgets import QApplication

from eml_forensic_suite.ui.main_window import MainWindow


def main() -> None:
    app = QApplication(sys.argv)

    app.setApplicationName("EML / IMAP Forensic Suite")
    app.setOrganizationName("HubMyWeb Cyberlab")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
