"""
Application principale : suite forensic EML/IMAP

Composants :
  - Onglet 1 : Export IMAP (lecture seule)
  - Onglet 2 : Indexation EML (lecture seule)
  - Onglet 3 : Viewer CSV / EML (lecture seule)
"""

import sys
import tkinter as tk
from tkinter import ttk, messagebox

from imap_exporter import build_imap_tab
from indexer import build_indexer_tab
from viewer import build_viewer_tab
from common_utils import VERSION, resource_path

APP_TITLE = "Suite forensic EML / IMAP (lecture seule)"
APP_VERSION = VERSION  # 1.0.0, défini dans common_utils.py


def configure_style(root: tk.Tk) -> None:
    """
    Configuration basique du style ttk pour harmoniser un peu l'UI.
    (Reste volontairement sobre pour rester compatible partout.)
    """
    style = ttk.Style(root)

    try:
        if sys.platform.startswith("win"):
            style.theme_use("vista")
        else:
            style.theme_use("clam")
    except Exception:
        # Si le thème n'existe pas, on laisse le thème par défaut
        pass

    style.configure("TNotebook", tabposition="n")
    style.configure("TNotebook.Tab", padding=(12, 6, 12, 6))


def build_menu(root: tk.Tk) -> None:
    """
    Crée un menu minimal Fichier / Aide.
    """
    menubar = tk.Menu(root)

    # Menu Fichier
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(
        label="Quitter",
        command=root.quit,
    )
    menubar.add_cascade(label="Fichier", menu=file_menu)

    # Menu Aide
    def show_about():
        messagebox.showinfo(
            "À propos",
            f"{APP_TITLE}\nVersion : {APP_VERSION}\n\n"
            "Outil de collecte et d'analyse forensic de boîtes mail IMAP "
            "(lecture seule, export .eml + indexation CSV + viewer EML).",
        )

    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="À propos…", command=show_about)
    menubar.add_cascade(label="Aide", menu=help_menu)

    root.config(menu=menubar)


def main() -> None:
    root = tk.Tk()
    root.title(f"{APP_TITLE} – v{APP_VERSION}")
    root.geometry("1200x800")

    # Icône de la fenêtre (essaie, mais ne plante pas si introuvable)
    try:
        root.iconbitmap(resource_path("icone.ico"))
    except Exception:
        pass

    configure_style(root)
    build_menu(root)

    # État partagé entre les onglets :
    shared_state: dict = {
        "version": APP_VERSION,
        # Tu peux ajouter d’autres clés si tu veux partager des infos :
        # "last_export_dir": None,
        # "last_index_dir": None,
        # "last_index_csv": None,
        # "last_index_entries": [],
    }

    main_frame = ttk.Frame(root, padding=10)
    main_frame.pack(fill=tk.BOTH, expand=True)

    notebook = ttk.Notebook(main_frame)
    notebook.pack(fill=tk.BOTH, expand=True)

    # Onglet 1 : Export IMAP
    build_imap_tab(notebook, shared_state)

    # Onglet 2 : Indexation EML
    build_indexer_tab(notebook, shared_state)

    # Onglet 3 : Viewer CSV / EML
    build_viewer_tab(notebook, shared_state)

    notebook.select(0)

    root.mainloop()


if __name__ == "__main__":
    main()
