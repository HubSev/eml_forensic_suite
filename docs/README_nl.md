# 📂 EML / IMAP Forensic Suite – v1.0.1

### **IMAP-export alleen-lezen · CSV-indexering · Geavanceerde forensische viewer · Analyse van bijlagen · Statistisch dashboard · Booleaanse zoekfunctie**

[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 Over

**EML / IMAP Forensic Suite** is een professionele toolset voor  
**forensische e-mailanalyse**, ontworpen voor onderzoeken zoals:

- BEC (Business Email Compromise)
- Financiële fraude
- Compromittering van mailboxen
- Juridische onderzoeken en gerechtsdeskundigen

De applicatie maakt het mogelijk om:

- **IMAP-extractie in alleen-lezen modus** uit te voeren,
- een **EML-corpus te indexeren** in een gestructureerd CSV-bestand,
- **automatische forensische analyse** uit te voeren (headers, Received-keten, DKIM/SPF/DMARC, bijlagen…),
- **e-mails gedetailleerd te inspecteren**,
- een **volledig statistisch overzicht** te genereren.

Alle operaties zijn niet-destructief:  
🛡 **de originele EML-bestanden worden nooit gewijzigd.**

---

## 🧰 Belangrijkste functies (v1.0.1)

### ✔ IMAP-export alleen-lezen

- IMAP via SSL
- Export naar `.eml` zonder ooit naar de server te schrijven
- Selectie van IMAP-mappen
- Filteren op datum
- SHA-256-hash per bericht
- Globale exporthash
- Volledig forensisch rapport: mappen, groottes, periodes, fouten, hashing, server-greeting

### ✔ EML-indexering

- Volledige analyse van een map met `.eml`-bestanden
- Automatische extractie van:

  - Datum
  - From / To / CC / Bcc
  - Subject
  - Message-ID
  - Oorspronkelijke IMAP-map
  - Bijbehorende hash (`hashes.txt`)
  - Forensische indicatoren:
    - DKIM / SPF / DMARC
    - Received-keten (anomaliedetectie)
    - Integriteitsflags (ontbrekende datum, ontbrekende Message-ID, ...)
    - Bijlagen

- Generatie van een **CSV-index** + interne Python-index
- Multithread-indexering voor optimale prestaties

### ✔ Geavanceerde forensische viewer (nieuw)

- Volledige weergave:
  - Rauwe headers
  - Tekstbody + beveiligde HTML
  - Bijlagen (lijst + metadata)
- Forensische extractie van bijlagen:
  - SHA-256-hash
  - Individueel rapport per bijlage
- Voorbeeldweergave van afbeeldingen / PDF's / eenvoudige bestanden
- Krachtige zoekmotor (mini-taal):
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - Booleans: **AND / OR / NOT**
  - **Haakjes**: `(cond1 or cond2) and not cond3`
  - Impliciete AND
  - Volledige tekstzoekopdracht over headers + bijlagen + hash

### ✔ Forensisch dashboard (nieuw)

- Globale statistische weergave van een EML-corpus
- Analyse van:
  - Domeinen van afzenders
  - Verdeling per IMAP-map
  - Tijdperiode
  - DKIM/SPF/DMARC
  - Received-anomalieën
  - Integriteitsflags
  - Bijlagen
- Duidelijke, exporteerbare tekstsamenvatting

### ✔ Moderne grafische interface (PySide6)

- 4 tabbladen: IMAP • Indexering • Viewer • Dashboard
- Licht / donker thema
- Meertaligheid:
  - Frans, Engels
  - Arabisch, Duits, Spaans, Hindi, Italiaans, Japans, Koreaans, Nederlands, Portugees, Russisch, Turks, Oekraïens, Chinees
- Gedeeld statusbeheer (laatste index, laatste export…)

---

## 📦 Installatie (via broncode)

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
```
