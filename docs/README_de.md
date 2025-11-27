# 📂 EML / IMAP Forensic Suite – v1.0.1

### **Schreibgeschützter IMAP-Export · CSV-Indexierung · Erweiterter Forensik-Viewer · Analyse von Anhängen · Statistisches Dashboard · Boolesche Suche**

[![Lizenz](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)  
![Status](https://img.shields.io/badge/Status-Aktiv-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![Plattform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 Überblick

Die **EML / IMAP Forensic Suite** ist eine professionelle Suite für  
**forensische E-Mail-Analyse**, entwickelt für Untersuchungen wie:

- BEC (Business Email Compromise)
- Finanzbetrug
- Kompromittierte Postfächer
- Juristische Untersuchungen und Gerichtsgutachten

Die Anwendung ermöglicht:

- **schreibgeschützte IMAP-Extraktion**
- **Indexierung eines EML-Korpus** in eine strukturierte CSV-Datei
- **automatische forensische Analyse** (Header, Received-Kette, DKIM/SPF/DMARC, Anhänge …)
- **detaillierte Untersuchung** einzelner E-Mails
- Erstellung einer **kompletten statistischen Zusammenfassung**

Alle Vorgänge sind nicht-destruktiv:  
🛡 **Die ursprünglichen EML-Dateien werden niemals verändert.**

---

## 🧰 Hauptfunktionen (v1.0.1)

### ✔ Schreibgeschützter IMAP-Export

- IMAP über SSL
- Export in `.eml` ohne jegliches Schreiben auf dem Server
- Auswahl der IMAP-Ordner
- Datumsfilterung
- SHA-256-Hash pro Nachricht
- Globaler Export-Hash
- Vollständiger forensischer Bericht: Ordner, Größen, Zeiträume, Fehler, Hashing, Server-Gruß

### ✔ EML-Indexierung

- Vollständige Analyse eines Ordners mit `.eml`-Dateien
- Automatische Extraktion von:

  - Datum
  - From / To / CC / Bcc
  - Betreff
  - Message-ID
  - Ursprünglicher IMAP-Ordner
  - Zugehöriger Hash (via `hashes.txt`)
  - Forensische Indikatoren:
    - DKIM / SPF / DMARC (aus Authentication-Results)
    - Received-Kette (Anomalieerkennung)
    - Integritätsflags (fehlendes Datum, fehlende Message-ID usw.)
    - Anhänge

- Erstellung eines **CSV-Indexes** + interner Python-Index
- Multithread-Indexierung für flüssige Leistung

### ✔ Erweiterter Forensik-Viewer (neu)

- Vollständige Anzeige:
  - Rohe Header
  - Textkörper + bereinigtes HTML
  - Anhänge (Liste + Metadaten)
- Forensische Extraktion von Anhängen:
  - SHA-256-Hash
  - Individueller Bericht pro Anhang
- Vorschau für Bilder / PDFs / einfache Dateien
- Leistungsstarkes forensisches Suchsystem (Mini-Sprache):
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - Boolesche Operatoren: **AND / OR / NOT**
  - **Klammern**: `(bed1 or bed2) and not bed3`
  - Implizites AND
  - Volltextsuche (Header + Anhänge + Hash)

### ✔ Forensisches Dashboard (neu)

- Statistische Gesamtansicht eines EML-Korpus
- Analyse von:
  - Absenderdomänen
  - Verteilung nach IMAP-Ordnern
  - Zeitraum
  - DKIM/SPF/DMARC
  - Received-Anomalien
  - Integritätsflags
  - Anhängen
- Klarer, exportierbarer Textbericht

### ✔ Moderne grafische Oberfläche (PySide6)

- 4 Tabs: IMAP • Indexierung • Viewer • Dashboard
- Hell- / Dunkelmodus
- Mehrsprachigkeit:
  - Französisch, Englisch
  - - Arabisch, Deutsch, Spanisch, Hindi, Italienisch, Japanisch, Koreanisch, Niederländisch, Portugiesisch, Russisch, Türkisch, Ukrainisch, Chinesisch
- Gemeinsame Statusverwaltung (letzter Index, letzter Export …)

---

## 📦 Installation (aus dem Quellcode)

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
```
