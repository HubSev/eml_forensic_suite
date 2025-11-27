from __future__ import annotations

from enum import Enum


class Theme(str, Enum):
    DARK = "dark"
    LIGHT = "light"


DARK_QSS = """
QMainWindow {
    background-color: #1f2430;
}

QWidget {
    font-family: Segoe UI, -apple-system, Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 10pt;
    color: #f0f0f0;
    background-color: #1f2430;
}

/* Tabs */
QTabWidget::pane {
    border: 1px solid #444;
    border-radius: 4px;
    background: #252b39;
}

QTabBar::tab {
    padding: 8px 18px;
    background: #2b3142;
    border: 1px solid #444;
    border-bottom: none;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    margin-right: 2px;
}

QTabBar::tab:selected {
    background: #3c4459;
}

QTabBar::tab:hover {
    background: #343b4e;
}

/* Menu */
QMenuBar {
    background-color: #252b39;
    color: #f0f0f0;
}

QMenuBar::item:selected {
    background: #3c4459;
}

QMenu {
    background-color: #252b39;
    color: #f0f0f0;
}

QMenu::item:selected {
    background-color: #3c4459;
}

/* Status bar */
QStatusBar {
    background: #252b39;
    color: #cccccc;
}

/* GroupBox */
QGroupBox {
    border: 1px solid #3a4153;
    border-radius: 4px;
    margin-top: 8px;
    padding: 8px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 4px;
    color: #cfd4e3;
}

/* Boutons */
QPushButton {
    background-color: #2b3142;
    color: #f5f5f5;
    border: 1px solid #4b5265;
    border-radius: 4px;
    padding: 6px 12px;
}

QPushButton:hover {
    background-color: #3c4459;
}

QPushButton:pressed {
    background-color: #31384a;
}

QPushButton:disabled {
    background-color: #2b3142;
    color: #777777;
    border-color: #3b4150;
}

/* Boutons primaires (actions importantes) */
QPushButton[primary="true"] {
    background-color: #3b82f6;
    border: 1px solid #1d4ed8;
    color: #ffffff;
}

QPushButton[primary="true"]:hover {
    background-color: #2563eb;
}

QPushButton[primary="true"]:pressed {
    background-color: #1d4ed8;
}

/* Champs de texte */
QLineEdit,
QPlainTextEdit {
    background-color: #252b39;
    color: #f0f0f0;
    border: 1px solid #3a4153;
    border-radius: 3px;
}

QLineEdit:focus,
QPlainTextEdit:focus {
    border: 1px solid #3b82f6;
}

/* ProgressBar */
QProgressBar {
    border: 1px solid #3a4153;
    border-radius: 3px;
    text-align: center;
    background-color: #252b39;
}

QProgressBar::chunk {
    background-color: #3b82f6;
}

/* TableView */
QTableView {
    background-color: #252b39;
    alternate-background-color: #2b3142;
    gridline-color: #3a4153;
    color: #f0f0f0;
    selection-background-color: #3b82f6;
    selection-color: #ffffff;
}

QHeaderView::section {
    background-color: #2b3142;
    color: #e5e7eb;
    padding: 4px;
    border: 1px solid #3a4153;
}
"""


LIGHT_QSS = """
QMainWindow {
    background-color: #f4f5f7;
}

QWidget {
    font-family: Segoe UI, -apple-system, Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 10pt;
    color: #222222;
    background-color: #f4f5f7;
}

/* Tabs */
QTabWidget::pane {
    border: 1px solid #d0d4dd;
    border-radius: 4px;
    background: #ffffff;
}

QTabBar::tab {
    padding: 8px 18px;
    background: #e5e7eb;
    border: 1px solid #cbd5e1;
    border-bottom: none;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    margin-right: 2px;
}

QTabBar::tab:selected {
    background: #ffffff;
}

QTabBar::tab:hover {
    background: #e2e8f0;
}

/* Menu */
QMenuBar {
    background-color: #e5e7eb;
    color: #111827;
}

QMenuBar::item:selected {
    background: #d1d5db;
}

QMenu {
    background-color: #ffffff;
    color: #111827;
}

QMenu::item:selected {
    background-color: #e5e7eb;
}

/* Status bar */
QStatusBar {
    background: #e5e7eb;
    color: #374151;
}

/* GroupBox */
QGroupBox {
    border: 1px solid #d1d5db;
    border-radius: 4px;
    margin-top: 8px;
    padding: 8px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 4px;
    color: #4b5563;
}

/* Boutons */
QPushButton {
    background-color: #ffffff;
    color: #111827;
    border: 1px solid #d1d5db;
    border-radius: 4px;
    padding: 6px 12px;
}

QPushButton:hover {
    background-color: #f3f4f6;
}

QPushButton:pressed {
    background-color: #e5e7eb;
}

QPushButton:disabled {
    background-color: #f9fafb;
    color: #9ca3af;
    border-color: #e5e7eb;
}

/* Boutons primaires */
QPushButton[primary="true"] {
    background-color: #2563eb;
    border: 1px solid #1d4ed8;
    color: #ffffff;
}

QPushButton[primary="true"]:hover {
    background-color: #1d4ed8;
}

QPushButton[primary="true"]:pressed {
    background-color: #1e40af;
}

/* Champs de texte */
QLineEdit,
QPlainTextEdit {
    background-color: #ffffff;
    color: #111827;
    border: 1px solid #d1d5db;
    border-radius: 3px;
}

QLineEdit:focus,
QPlainTextEdit:focus {
    border: 1px solid #2563eb;
}

/* ProgressBar */
QProgressBar {
    border: 1px solid #d1d5db;
    border-radius: 3px;
    text-align: center;
    background-color: #ffffff;
}

QProgressBar::chunk {
    background-color: #2563eb;
}

/* TableView */
QTableView {
    background-color: #ffffff;
    alternate-background-color: #f3f4f6;
    gridline-color: #e5e7eb;
    color: #111827;
    selection-background-color: #2563eb;
    selection-color: #ffffff;
}

QHeaderView::section {
    background-color: #e5e7eb;
    color: #111827;
    padding: 4px;
    border: 1px solid #d1d5db;
}
"""


def get_stylesheet(theme: Theme) -> str:
    if theme == Theme.LIGHT:
        return LIGHT_QSS
    return DARK_QSS
