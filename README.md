# 📂 EML / IMAP Forensic Suite

### **Export IMAP (lecture seule) · Indexation CSV · Analyse d’en-têtes · Viewer brut EML**

[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 À propos

**EML / IMAP Forensic Suite** est une suite d’outils professionnels orientés
**analyse forensic d’emails**, conçue pour :

- Exporter une boîte mail IMAP **en lecture seule**
- Télécharger tous les messages au format `.eml` sans jamais les modifier
- Générer les **hashes SHA-256 uniques** des messages + un **hash global**
- Indexer tout un export `.eml` en un **fichier CSV exploitable**
- Lire les en-têtes bruts et métadonnées **sans altération**
- Fournir un **rapport d’audit complet** (dossiers, tailles, périodes, erreurs, hashing)

Développé pour des **investigations BEC (Business Email Compromise)**,  
et utilisé dans des cas réels de compromission de boîtes mail.

---

## 🧰 Fonctionnalités principales

### ✔ Export IMAP (lecture seule)

- Connexion IMAP SSL
- Pas de modification des messages (READONLY)
- Hash SHA-256 pour chaque `.eml`
- Hash global des messages exportés
- Rapport forensic horodaté (UTC + local)
- Aucune écriture sur le serveur

### ✔ Indexation EML

- Scan d’un dossier contenant des `.eml`
- Extraction automatique :
  - Date
  - From / To / CC / BCC
  - Subject
  - Message-ID
  - Dossier IMAP d’origine
- Création d’un **CSV compatible Excel et LibreOffice**
- Correspondance automatique avec `hashes.txt`

### ✔ Viewer EML

- Recherche par numéro de séquence
- Consultation des en-têtes bruts
- Visualisation sans altération du fichier

### ✔ Interface graphique complète (Tkinter)

- 3 onglets : Export / Indexation / Viewer
- Multi-threading pour éviter les blocages
- Journal en temps réel
- Barre de progression

---

## 📦 Installation (sources)

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml-forensic-suite
pip install -r requirements.txt
python main_app.py
```

