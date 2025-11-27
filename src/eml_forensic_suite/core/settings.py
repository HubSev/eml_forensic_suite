from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional
import json


CONFIG_DIR_NAME = ".eml_forensic_suite"
CONFIG_FILE_NAME = "settings.json"


@dataclass
class AppSettings:

    reports_root_dir: Optional[str] = None
    language: str = "fr"


def _get_config_dir() -> Path:
    home = Path.home()
    config_dir = home / CONFIG_DIR_NAME
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


def _get_config_path() -> Path:
    return _get_config_dir() / CONFIG_FILE_NAME


def load_settings() -> AppSettings:
    path = _get_config_path()
    if not path.is_file():
        return AppSettings()

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return AppSettings()

    reports_root_dir = data.get("reports_root_dir")
    if reports_root_dir is not None and not isinstance(reports_root_dir, str):
        reports_root_dir = None

    language = data.get("language", "fr")
    if not isinstance(language, str):
        language = "fr"

    return AppSettings(
        reports_root_dir=reports_root_dir,
        language=language,
    )


def save_settings(settings: AppSettings) -> None:
    path = _get_config_path()
    data = asdict(settings)

    try:
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        return
