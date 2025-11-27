# 📂 EML / IMAP Forensic Suite – v1.0.1

### **Export IMAP (lecture seule) · Indexation CSV · Viewer forensic avancé · Analyse pièces jointes · Dashboard statistique · Recherche booléenne**

[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 À propos

**EML / IMAP Forensic Suite** est une suite professionnelle dédiée à  
l’**analyse forensic d’e-mails**, pensée pour les enquêtes :

- BEC (Business Email Compromise)
- Fraudes financières
- Compromissions de boîtes mail
- Investigations juridiques et expertises judiciaires

L’application permet :

- l’**extraction IMAP en lecture seule**,  
- l’**indexation d’un corpus EML** en un fichier CSV structuré,
- l’**analyse forensic automatique** (headers, Received, DKIM/SPF/DMARC, pièces jointes…),
- la **visualisation approfondie** des emails,
- et la **production d’un résumé statistique complet**.

Toutes les opérations sont non-destructives :  
🛡 **aucune modification n’est jamais apportée aux fichiers EML originaux.**

---

## 🧰 Fonctionnalités principales (v1.0.1)

### ✔ Export IMAP (lecture seule)
- Connexion IMAP SSL
- Export en `.eml` sans jamais écrire sur le serveur
- Sélection de dossiers IMAP
- Filtrage par date
- Hash SHA-256 pour chaque message
- Hash global de l'export
- Rapport forensic complet : dossiers, tailles, périodes, erreurs, hashing, greeting serveur

### ✔ Indexation EML
- Analyse complète d’un dossier de fichiers `.eml`
- Extraction automatique :
  - Date
  - From / To / CC / Bcc (via CC + CCI)
  - Subject
  - Message-ID
  - Dossier IMAP d’origine
  - Hash correspondant (via `hashes.txt`)
  - Indicateurs forensic :
    - DKIM / SPF / DMARC (lecture Authentication-Results)
    - Received (détection d’anomalies)
    - Flags d’intégrité (date manquante, Message-ID manquant…)
    - Pièces jointes

- Génération d’un **index CSV** + index interne Python
- Multi-threading pour un indexage fluide

### ✔ Viewer forensic avancé (nouveau)
- Affichage complet :
  - Headers bruts
  - Corps texte + HTML sécurisé
  - Pièces jointes (liste + métadonnées)
- Extraction de pièces jointes (forensic)
  - Hash SHA-256
  - Rapport individuel par PJ
- Prévisualisation d’images / PDF / fichiers simples
- Système de recherche forensic puissant (mini-langage) :
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - Booléens : **AND / OR / NOT**
  - **Parenthèses** : `(cond1 or cond2) and not cond3`
  - ET implicite
  - Recherche plein texte globale (headers + PJ + hash)

### ✔ Dashboard forensic (nouveau)
- Vue statistique globale d’un corpus EML
- Analyse :
  - Domaines expéditeurs
  - Répartition par dossiers IMAP
  - Période temporelle
  - DKIM/SPF/DMARC
  - Anomalies Received
  - Flags d’intégrité
  - Pièces jointes
- Résumé textuel clair et exportable

### ✔ Interface graphique moderne (PySide6)
- 4 onglets : IMAP • Indexation • Viewer • Dashboard
- Thème clair / sombre
- Multi-langues :
  - Français, Anglais
  - + arabe, allemand, espagnol, hindi, italien, japonais, coréen, néerlandais, portugais, russe, turc, ukrainien, chinois
- Gestion d’état partagé (last index, last export…)

---

## 📦 Installation (sources)

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
