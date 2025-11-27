📘 CHANGELOG — EML Forensic Suite  
All major changes since the earliest versions are listed here.

---

## [1.0.1] — 2025-XX-XX

### Added

- Full new PySide6 interface (replaces Tkinter)
- Light & dark themes
- 14 integrated languages (FR, EN, ES, DE, NL, IT, PT, TR, AR, HI, JA, KO, ZH, RU, UK)
- New **Forensic Dashboard** tab
- New forensic mini-language: `AND / OR / NOT / ( )`
- New filters: `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:`, `hash:`, `folder:`, `date:`
- Global full-text search
- Attachment preview (images, PDFs)
- Forensic attachment extraction + per-attachment report
- DKIM / SPF / DMARC analysis via _Authentication-Results_
- Advanced Received analysis: `NO_RECEIVED`, `MANY_HOPS`
- Integrity flags: `MISSING_DATE`, `MISSING_MESSAGE_ID`, `MISSING_FROM`
- New enriched indexing engine (20+ fields)
- Completely rewritten forensic Viewer
- Improved threading support
- New persistent settings system
- Integrated app + window icon
- Fully reorganized project structure (`core/` and `ui/`)

### Improved

- IMAP export: colored logs, better stability, enriched report
- Indexing: more robust SHA-256 mapping
- Viewer: faster performance (instant selection)
- Dashboard: clearer and multilingual summary
- PyInstaller packaging: stronger compatibility
- Secure HTML rendering (no active execution)
- Centralized shared_state management

### Fixed

- Tkinter threading freezes (replaced by Qt)
- Attachment extraction bugs
- Encoding issues in headers
- Crashes when opening certain EML files
- More reliable Authentication-Results parsing
- Stronger IMAP folder validation

---

## [1.0.0] — 2024-XX-XX

### Initial version

- Read-only IMAP export
- Per-message SHA-256 hash + global hash
- IMAP forensic report
- Basic CSV indexing
- Raw EML Viewer
- Tkinter interface (3 tabs)
- Basic multi-threading
