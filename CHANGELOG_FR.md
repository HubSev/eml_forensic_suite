# 📘 CHANGELOG — EML Forensic Suite

Toutes les modifications majeures depuis les premières versions sont listées ici.

---

## [1.0.1] — 2025-XX-XX

### Ajouté

- Nouvelle interface complète **PySide6** (remplace Tkinter)
- Thèmes **clair & sombre**
- **14 langues** intégrées (FR, EN, ES, DE, NL, IT, PT, TR, AR, HI, JA, KO, ZH, RU, UK)
- Onglet **Dashboard Forensic** (nouveau)
- Mini-langage de recherche forensic : AND / OR / NOT / parenthèses
- Filtres : from:, to:, cc:, subject:, domain:, attachment:, hash:, folder:, date:
- Recherche plein texte globale
- Prévisualisation des pièces jointes (images, PDF)
- Extraction forensic des PJ + rapport individuel
- Analyse DKIM / SPF / DMARC via Authentication-Results
- Analyse Received avancée : NO_RECEIVED, MANY_HOPS
- Flags d’intégrité : MISSING_DATE, MISSING_MESSAGE_ID, MISSING_FROM
- Nouveau moteur d’indexation enrichi (plus de 20 champs)
- Nouveau Viewer forensic (complètement réécrit)
- Support threading amélioré
- Nouveau système de paramètres persistants
- Icône intégrée pour l’exécutable et la fenêtre
- Réorganisation totale de l’arborescence (`core/` et `ui/`)

### Amélioré

- Export IMAP : logs colorisés, stabilité, rapport enrichi
- Indexation : mapping SHA256 plus robuste
- Viewer : performance renforcée (sélection instantanée)
- Dashboard : résumé clair, multilingue
- Packaging PyInstaller : compatibilité renforcée
- Lecture HTML sécurisée (pas d’exécution active)
- Gestion du shared_state centralisée

### Corrigé

- Blocages liés au threading Tkinter (remplacé par Qt)
- Bugs dans l’extraction PJ
- Problèmes d’encodage dans les headers
- Correction de crashs lors de l’ouverture de certains EML
- Fiabilisation du parsing Authentication-Results
- Validation robuste des dossiers IMAP

---

## [1.0.0] — 2024-XX-XX

### Version initiale

- Export IMAP lecture seule
- Hash SHA-256 par message + hash global
- Rapport forensic IMAP
- Indexation simple en CSV
- Viewer brut EML
- Interface Tkinter (3 onglets)
- Multi-threading basique

---
