from __future__ import annotations

from enum import Enum
from typing import Dict, Tuple, List

# On importe maintenant depuis le sous-dossier "traductions"
from .traductions.i18n_fr import TRANSLATIONS_FR
from .traductions.i18n_en import TRANSLATIONS_EN
from .traductions.i18n_es import TRANSLATIONS_ES
from .traductions.i18n_de import TRANSLATIONS_DE
from .traductions.i18n_it import TRANSLATIONS_IT
from .traductions.i18n_nl import TRANSLATIONS_NL
from .traductions.i18n_pt import TRANSLATIONS_PT
from .traductions.i18n_ru import TRANSLATIONS_RU
from .traductions.i18n_zh import TRANSLATIONS_ZH
from .traductions.i18n_ja import TRANSLATIONS_JA
from .traductions.i18n_ko import TRANSLATIONS_KO
from .traductions.i18n_ar import TRANSLATIONS_AR
from .traductions.i18n_hi import TRANSLATIONS_HI
from .traductions.i18n_tr import TRANSLATIONS_TR
from .traductions.i18n_uk import TRANSLATIONS_UK


class Language(str, Enum):
    FR = "fr"
    EN = "en"
    ES = "es"
    PT = "pt"
    DE = "de"
    IT = "it"
    NL = "nl"
    RU = "ru"
    ZH = "zh"
    JA = "ja"
    KO = "ko"
    AR = "ar"
    HI = "hi"
    TR = "tr"
    UK = "uk"


# Tu peux choisir FR ou EN ici suivant ton choix par défaut
DEFAULT_LANGUAGE = Language.EN.value


LANG_CHOICES: List[Tuple[str, str]] = [
    (Language.FR.value, "Français"),
    (Language.EN.value, "English"),
    (Language.ES.value, "Español"),
    (Language.PT.value, "Português"),
    (Language.DE.value, "Deutsch"),
    (Language.IT.value, "Italiano"),
    (Language.NL.value, "Nederlands"),
    (Language.RU.value, "Русский"),
    (Language.ZH.value, "中文"),
    (Language.JA.value, "日本語"),
    (Language.KO.value, "한국어"),
    (Language.AR.value, "العربية"),
    (Language.HI.value, "हिन्दी"),
    (Language.TR.value, "Türkçe"),
    (Language.UK.value, "українською"),
]


# Dictionnaire des traductions par langue
LANG_MAPS: Dict[str, Dict[str, str]] = {
    Language.FR.value: TRANSLATIONS_FR,
    Language.EN.value: TRANSLATIONS_EN,
    Language.ES.value: TRANSLATIONS_ES,
    Language.DE.value: TRANSLATIONS_DE,
    Language.IT.value: TRANSLATIONS_IT,
    Language.NL.value: TRANSLATIONS_NL,
    Language.PT.value: TRANSLATIONS_PT,
    Language.RU.value: TRANSLATIONS_RU,
    Language.ZH.value: TRANSLATIONS_ZH,
    Language.JA.value: TRANSLATIONS_JA,
    Language.KO.value: TRANSLATIONS_KO,
    Language.AR.value: TRANSLATIONS_AR,
    Language.HI.value: TRANSLATIONS_HI,
    Language.TR.value: TRANSLATIONS_TR,
    Language.TR.value: TRANSLATIONS_UK,
    # Autres langues à ajouter ici si besoin plus tard
}


# ----------------------------------------------------------------------
# Compat : ancien dict TRANSLATIONS FR+EN (si d'autres modules l'utilisent)
# ----------------------------------------------------------------------
TRANSLATIONS: Dict[str, Dict[str, str]] = {}

for key, value in TRANSLATIONS_FR.items():
    TRANSLATIONS.setdefault(key, {})["fr"] = value

for key, value in TRANSLATIONS_EN.items():
    TRANSLATIONS.setdefault(key, {})["en"] = value

# Alias historique si tu l’utilises ailleurs
MESSAGES = TRANSLATIONS


# ----------------------------------------------------------------------
# Fonction utilitaire principale
# ----------------------------------------------------------------------
def t(key: str, lang: str = DEFAULT_LANGUAGE, **kwargs) -> str:
    """
    Retourne la traduction pour une clé donnée.

    Priorité :
    1. Langue demandée (si présente)
    2. Anglais (fallback universel)
    3. Langue par défaut (DEFAULT_LANGUAGE)
    4. À défaut : la clé elle-même
    """

    # Dico pour la langue demandée
    lang_dict = LANG_MAPS.get(lang) or {}

    # Fallback anglais
    en_dict = LANG_MAPS.get(Language.EN.value, {})

    # Fallback langue par défaut (peut être EN ou FR selon ton choix)
    default_dict = LANG_MAPS.get(DEFAULT_LANGUAGE, {})

    text = (
        lang_dict.get(key)
        or en_dict.get(key)
        or default_dict.get(key)
        or key
    )

    if kwargs:
        try:
            text = text.format(**kwargs)
        except Exception:
            # En cas de placeholder manquant
            pass

    return text
