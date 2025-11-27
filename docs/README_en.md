# 📂 EML / IMAP Forensic Suite – v1.0.1

### **Read-only IMAP export · CSV indexing · Advanced forensic viewer · Attachment analysis · Statistical dashboard · Boolean search**

[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 About

**EML / IMAP Forensic Suite** is a professional suite dedicated to  
**forensic email analysis**, designed for investigations such as:

- BEC (Business Email Compromise)
- Financial fraud
- Mailbox compromise
- Legal investigations and court-appointed expert work

The application allows you to:

- perform **read-only IMAP extraction**,
- **index an EML corpus** into a structured CSV file,
- run **automatic forensic analysis** (headers, Received chain, DKIM/SPF/DMARC, attachments…),
- **deeply inspect** individual emails,
- and produce a **complete statistical summary**.

All operations are non-destructive:  
🛡 **the original EML files are never modified.**

---

## 🧰 Main features (v1.0.1)

### ✔ Read-only IMAP export

- IMAP over SSL
- Export to `.eml` without ever writing back to the server
- IMAP folder selection
- Date filtering
- Per-message SHA-256 hash
- Global export hash
- Full forensic report: folders, sizes, periods, errors, hashing, server greeting

### ✔ EML indexing

- Full analysis of a folder of `.eml` files
- Automatic extraction of:

  - Date
  - From / To / CC / Bcc (via CC + Bcc)
  - Subject
  - Message-ID
  - Original IMAP folder
  - Corresponding hash (via `hashes.txt`)
  - Forensic indicators:
    - DKIM / SPF / DMARC (from Authentication-Results)
    - Received chain (anomaly detection)
    - Integrity flags (missing date, missing Message-ID, etc.)
    - Attachments

- Generation of a **CSV index** + internal Python index
- Multi-threaded indexing for smooth performance

### ✔ Advanced forensic viewer (new)

- Full display of:
  - Raw headers
  - Text body + sanitized HTML
  - Attachments (list + metadata)
- Forensic attachment extraction:
  - SHA-256 hash
  - Per-attachment individual report
- Preview of images / PDFs / simple files
- Powerful forensic search system (mini-language):
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - Booleans: **AND / OR / NOT**
  - **Parentheses**: `(cond1 or cond2) and not cond3`
  - Implicit AND
  - Global full-text search (headers + attachments + hash)

### ✔ Forensic dashboard (new)

- Global statistical view of an EML corpus
- Analysis of:
  - Sender domains
  - Distribution by IMAP folder
  - Time period
  - DKIM/SPF/DMARC
  - Received anomalies
  - Integrity flags
  - Attachments
- Clear, exportable textual summary

### ✔ Modern graphical interface (PySide6)

- 4 tabs: IMAP • Indexing • Viewer • Dashboard
- Light / dark theme
- Multi-language:
  - French, English
  - - Arabic, German, Spanish, Hindi, Italian, Japanese, Korean, Dutch, Portuguese, Russian, Turkish, Ukrainian, Chinese
- Shared state management (last index, last export, etc.)

---

## 📦 Installation (from source)

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
```
