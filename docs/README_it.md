# 📂 EML / IMAP Forensic Suite – v1.0.1

[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 Informazioni

**EML / IMAP Forensic Suite** è una suite professionale dedicata  
all’**analisi forense delle e-mail**, progettata per indagini come:

- BEC (Business Email Compromise)
- Frodi finanziarie
- Compromissione della casella e-mail
- Indagini legali e perizie giudiziarie

L’applicazione consente di:

- effettuare **estrazione IMAP in sola lettura**
- **indicizzare un corpus EML** in un file CSV strutturato
- eseguire **analisi forense automatica** (headers, catena Received, DKIM/SPF/DMARC, allegati…)
- **analizzare in profondità** singole e-mail
- generare un **riassunto statistico completo**

Tutte le operazioni sono non distruttive:  
🛡 **i file EML originali non vengono mai modificati.**

---

## 🧰 Funzionalità principali (v1.0.1)

### ✔ Esportazione IMAP in sola lettura

- IMAP su SSL
- Esportazione in `.eml` senza mai scrivere sul server
- Selezione delle cartelle IMAP
- Filtro per data
- Hash SHA-256 per ogni messaggio
- Hash globale dell’esportazione
- Report forense completo: cartelle, dimensioni, periodi, errori, hashing, greeting del server

### ✔ Indicizzazione EML

- Analisi completa di una cartella contenente file `.eml`
- Estrazione automatica di:

  - Data
  - From / To / CC / Bcc
  - Subject
  - Message-ID
  - Cartella IMAP originale
  - Hash corrispondente (`hashes.txt`)
  - Indicatori forensi:
    - DKIM / SPF / DMARC (da Authentication-Results)
    - Catena Received (rilevamento anomalie)
    - Flag di integrità (data mancante, Message-ID mancante, ecc.)
    - Allegati

- Generazione di un **indice CSV** + indice interno Python
- Indicizzazione multi-thread per prestazioni fluide

### ✔ Viewer forense avanzato (nuovo)

- Visualizzazione completa:
  - Headers grezzi
  - Corpo testo + HTML sanificato
  - Allegati (lista + metadati)
- Estrazione forense degli allegati:
  - Hash SHA-256
  - Report individuale per allegato
- Anteprima immagini / PDF / file semplici
- Sistema di ricerca forense avanzato (mini-linguaggio):
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - Booleani: **AND / OR / NOT**
  - **Parentesi**: `(cond1 or cond2) and not cond3`
  - AND implicito
  - Ricerca full-text globale

### ✔ Dashboard forense (nuovo)

- Vista statistica globale di un corpus EML
- Analisi:
  - Domini dei mittenti
  - Distribuzione per cartella IMAP
  - Periodo temporale
  - DKIM/SPF/DMARC
  - Anomalie Received
  - Flag di integrità
  - Allegati
- Riassunto testuale chiaro ed esportabile

### ✔ Interfaccia grafica moderna (PySide6)

- 4 schede: IMAP • Indexing • Viewer • Dashboard
- Tema chiaro / scuro
- Multilingue:
  - Francese, Inglese
  - Arabo, Tedesco, Spagnolo, Hindi, Italiano, Giapponese, Coreano, Olandese, Portoghese, Russo, Turco, Ucraino, Cinese
- Gestione dello stato condiviso (ultimo indice, ultima esportazione…)

---

## 📦 Installazione (da sorgente)

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
```
