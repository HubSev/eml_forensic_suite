from __future__ import annotations

from typing import Dict

TRANSLATIONS_TR: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "EML / IMAP Adli Suite (salt okunur)",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "Dosya",
    "menu.view": "Görünüm",
    "menu.help": "Yardım",

    "menu.file.settings": "Ayarlar…",
    "menu.file.quit": "Çıkış",

    "menu.view.theme.dark": "Koyu tema",
    "menu.view.theme.light": "Açık tema",

    "menu.help.about": "Hakkında…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. IMAP dışa aktarma",
    "tab.index": "2. EML indeksleme",
    "tab.viewer": "3. Adli görüntüleyici",
    "tab.dashboard": "4. Adli gösterge paneli",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "Ayarlar",
    "settings.reports_dir.label": "Çalışma / rapor dizini:",
    "settings.reports_dir.browse": "Gözat…",
    "settings.language.label": "Arayüz dili:",
    "settings.reports_dir.dialog_title": "Çalışma / rapor dizini seçin",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "Hazır.",
    "status.settings.saved": "Ayarlar kaydedildi.",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "EML dışa aktarma dizini:",
    "index.browse": "Gözat…",
    "index.use_last_export": "Son IMAP dışa aktarmayı kullan",
    "index.log_placeholder": "EML indeksleme günlüğü (salt okunur)…",
    "index.start_button": "EML indekslemeyi başlat",
    "index.dialog_select_folder": "EML dışa aktarma klasörünü seçin",
    "index.no_last_export": "Henüz bilinen IMAP dışa aktarması yok (sekme 1).",
    "index.error_already_running_title": "İndeksleme zaten çalışıyor",
    "index.error_already_running_body": "Bir EML indeksleme işlemi zaten çalışıyor.",
    "index.error_no_folder_title": "Klasör eksik",
    "index.error_no_folder_body": "Lütfen .eml dosyaları içeren bir klasör seçin.",
    "index.error_invalid_folder_title": "Geçersiz klasör",
    "index.error_invalid_folder_body": "Belirtilen klasör mevcut değil:\n{folder}",
    "index.status_selected_folder": "İndeksleme için seçilen klasör: {folder}",
    "index.error_indexing_title": "İndeksleme sırasında hata",
    "index.error_log": "❌ Hata: {error}",
    "index.done_log_success": "\nİndeksleme başarıyla tamamlandı.",
    "index.done_log_path": "CSV yolu: {csv_path}",
    "index.done_log_count": "İndekslenen giriş sayısı: {count}",
    "index.done_msg_title": "İndeksleme tamamlandı",
    "index.done_msg_body": (
        "EML indeksleme tamamlandı.\n\nCSV dosyası: {csv_path}\nGirişler: {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "Son indeksi kullan",
    "dashboard.open_csv": "İndeks CSV aç…",
    "dashboard.placeholder": "EML indeksi temelinde adli istatistiksel özet…",
    "dashboard.source_memory": "Kaynak: Bellekteki indeks (bu oturumdaki son indeksleme).",
    "dashboard.source_csv": "Kaynak: {path}",
    "dashboard.no_index_title": "İndeks yok",
    "dashboard.no_index_body": (
        "Bu oturumda kullanılabilir bir indeks yok.\n"
        "Sekme 2’de bir indeks oluşturun veya bir CSV dosyası açın."
    ),
    "dashboard.dialog_open_csv": "İndeks CSV dosyasını aç",
    "dashboard.error_csv_missing_title": "Dosya bulunamadı",
    "dashboard.error_csv_missing_body": "Belirtilen dosya mevcut değil:\n{path}",
    "dashboard.error_csv_read_title": "CSV okuma hatası",
    "dashboard.error_csv_read_body": "CSV dosyası okunamıyor: {path}",
    "dashboard.empty_csv_title": "Boş indeks",
    "dashboard.empty_csv_body": "CSV dosyası kullanılabilir giriş içermiyor.",
    "dashboard.no_data": "Analiz edilecek veri yok.",

    "dashboard.section_overview": "Genel bakış",
    "dashboard.overview_line": (
        "Toplam e-posta: {total} – Farklı gönderen sayısı: {senders}"
    ),
    "dashboard.dates_line": "Kapsanan dönem: {date_min} → {date_max}",
    "dashboard.dates_unknown": "Tarihler mevcut değil veya işlenemiyor.",

    "dashboard.section_folders": "IMAP klasör dağılımı",
    "dashboard.no_folders": "IMAP klasörü tespit edilmedi.",

    "dashboard.section_domains": "Alan adlarına göre dağılım (gönderen)",
    "dashboard.no_domains": "Alan adı tespit edilmedi.",

    "dashboard.section_attachments": "Ekler",
    "dashboard.attachments_line": (
        "Ek içeren e-postalar: {with_att}/{total} – Tahmini toplam ek: {total_att}"
    ),

    "dashboard.section_auth": "Kimlik doğrulama (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "DKIM sonuçları:",
    "dashboard.auth_header_spf": "SPF sonuçları:",
    "dashboard.auth_header_dmarc": "DMARC sonuçları:",

    "dashboard.section_integrity": "Bütünlük / eksik başlıklar",
    "dashboard.integrity_flags_title": "Tespit edilen bütünlük işaretleri:",
    "dashboard.no_integrity_flags": "Belirli bir bütünlük işareti tespit edilmedi.",

    "dashboard.section_received": "Received zincirindeki anormallikler",
    "dashboard.no_received_anomalies": (
        "Received zincirinde anormallik tespit edilmedi (mevcut kurallara göre)."
    ),

    # ------------------------------------------------------------------
    # Viewer — columns
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "IMAP klasörü",
    "viewer.col.sequence_number": "Sıra",
    "viewer.col.date_header": "Tarih",
    "viewer.col.from_header": "Kimden",
    "viewer.col.to_header": "Kime",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Bcc",
    "viewer.col.subject": "Konu",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "Ek var mı?",
    "viewer.col.attachment_count": "Ek sayısı",
    "viewer.col.attachment_filenames": "Ek adları",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (özet)",
    "viewer.col.received_count": "Received sayısı",
    "viewer.col.received_anomalies": "Received anomalileri",
    "viewer.col.integrity_flags": "Bütünlük işaretleri",
    "viewer.col.relative_path": "Göreli yol",
    "viewer.col.filename": "Dosya adı",

    # ------------------------------------------------------------------
    # Viewer – search
    # ------------------------------------------------------------------
    "viewer.search_label": "Ara:",
    "viewer.search_placeholder": "Indekste filtrele (tüm sütunlar)…",
    "viewer.search_clear": "Temizle",

    "viewer.headers_label": "Başlıklar",
    "viewer.headers_placeholder": "Seçili mesajın başlıkları…",

    "viewer.body_label": "Gövde (metin)",
    "viewer.body_placeholder": (
        "text/plain gövde (veya ham HTML yedek) – seçili mesaj…"
    ),

    "viewer.btn_load_last": "Son IMAP dışa aktarmayı kullan",
    "viewer.btn_open_csv": "İndeks CSV aç...",
    "viewer.attachments_label": "Ekler",

    # ------------------------------------------------------------------
    # Viewer – EML errors
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "EML dosyası bulunamadı",
    "viewer.error_missing_eml_body": "EML dosyası diskte bulunamadı:\n{path}",
    "viewer.error_parse_eml_title": "EML okuma hatası",
    "viewer.error_parse_eml_body": "EML dosyası işlenemiyor: {path}",

    # ------------------------------------------------------------------
    # Viewer – attachments list
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "Ad",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "Boyut (bayt)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "Şüpheli?",

    "viewer.attach.yes": "Evet",
    "viewer.attach.no": "Hayır",

    # ------------------------------------------------------------------
    # IMAP tab
    # ------------------------------------------------------------------
    "imap.group.connection": "IMAP sunucusu (delil kaynağı)",
    "imap.label.host": "IMAP sunucusu adresi",
    "imap.label.user": "Analiz edilen posta kutusu kimliği",
    "imap.label.password": "Şifre (asla kaydedilmez)",
    "imap.label.date_start": "Başlangıç tarihi (adli filtre)",
    "imap.label.date_end": "Bitiş tarihi (adli filtre)",

    "imap.placeholder.host": "örn. imap.example.com",
    "imap.placeholder.user": "örn. incident@company.com",
    "imap.placeholder.password": "Analiz edilen hesabın şifresi",
    "imap.placeholder.date_start": "GG/AA/YYYY (isteğe bağlı)",
    "imap.placeholder.date_end": "GG/AA/YYYY (isteğe bağlı)",

    "imap.button.fetch_mailboxes": "IMAP klasörlerini incele…",
    "imap.button.start_export": "Adli çıkarımı başlat",
    "imap.button.cancel_export": "Çıkarımı iptal et",

    "imap.label.mailboxes_title": (
        "Çıkarılacak IMAP klasörleri (delil kaynağı):"
    ),
    "imap.checkbox.select_all": "Tüm klasörleri seç",

    "imap.log.placeholder": (
        "IMAP çıkarım günlüğü (salt okunur, zaman damgalı)…"
    ),

    # ------------------------------------------------------------------
    # IMAP — errors/info
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "Eksik ayarlar",
    "imap.error.missing_fields.body": (
        "Lütfen IMAP sunucusu, kullanıcı adı ve şifreyi belirtin."
    ),

    "imap.info.export_running.title": "Çıkarım zaten çalışıyor",
    "imap.info.export_running.body": "Bir IMAP çıkarım işlemi zaten çalışıyor.",

    "imap.error.date_invalid.title": "Geçersiz tarih",
    "imap.error.date_invalid.body": "Sağlanan tarihlerde hata: {error}",
    "imap.error.date_end_before_start.body": (
        "Bitiş tarihi başlangıç tarihinden önce olamaz."
    ),

    "imap.error.no_mailbox_selected.title": "Klasör seçilmedi",
    "imap.error.no_mailbox_selected.body": (
        "Lütfen çıkarılacak en az bir IMAP klasörü seçin."
    ),

    "imap.error.fetch_mailboxes.title": "IMAP hatası",
    "imap.error.fetch_mailboxes.body": (
        "IMAP klasörleri alınamadı:\n{error}"
    ),

    "imap.info.generic.title": "Bilgi",
    "imap.error.generic.title": "Hata",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "{host}:{port} adresine bağlanılıyor (SSL={use_ssl})...",
    "imap.log.connected": "IMAP sunucusuna bağlanıldı.",
    "imap.log.select_folder": "\"{folder}\" klasörü seçiliyor...",
    "imap.log.folder_selected": "\"{folder}\" klasörü seçildi.",
    "imap.log.message_count": "Dışa aktarılacak {count} mesaj.",
    "imap.log.fetching": "IMAP mesajları alınıyor...",
    "imap.log.export_done": "IMAP dışa aktarma tamamlandı.",
    "imap.log.saving_to": "Mesajlar \"{output_dir}\" konumuna kaydediliyor...",
    "imap.log.progress": "{current}/{total} mesaj dışa aktarılıyor...",
    "imap.log.skip_existing": "\"{path}\" dosyası zaten mevcut, atlanıyor.",

    "imap.error.connect_failed": "{host}:{port} adresine bağlanılamıyor: {error}",
    "imap.error.login_failed": "IMAP kimlik doğrulama hatası: {error}",
    "imap.error.select_failed": "\"{folder}\" klasörü seçilemedi: {error}",
    "imap.error.fetch_failed": "Mesajlar alınırken hata oluştu: {error}",
    "imap.error.generic": "IMAP dışa aktarma sırasında hata: {error}",

    # ------------------------------------------------------------------
    # IMAP - Export report
    # ------------------------------------------------------------------
    "imap.report.title": "=== IMAP dışa aktarma raporu (salt okunur) ===",
    "imap.report.tool_line": "Araç      : eml_forensic_suite – IMAP dışa aktarma",
    "imap.report.version_line": "Sürüm     : {version}",
    "imap.report.folder_line": "Klasör    : {export_dir}",

    "imap.report.section_tool": "---- Araç bilgileri ----",
    "imap.report.tool_path": "Araç yolu            : {tool_path}",
    "imap.report.tool_hash": "Araç SHA-256         : {tool_hash}",

    "imap.report.section_env": "---- Çalışma ortamı ----",
    "imap.report.env_os": "İşletim sistemi      : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Python sürümü        : {python_version}",

    "imap.report.section_context": "---- IMAP / hesap bağlamı ----",
    "imap.report.context_host": "IMAP sunucusu : {host}",
    "imap.report.context_user": "Hesap        : {user}",
    "imap.report.context_date_start": "Talep edilen başlangıç tarihi : {date_start}",
    "imap.report.context_date_end": "Talep edilen bitiş tarihi     : {date_end}",
    "imap.report.context_criteria": "IMAP arama ölçütleri          : {search_criteria} (sunucuya gönderildiği şekliyle)",

    "imap.report.selected_folders_title": "Seçilen klasörler:",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- IMAP sunucu bilgileri ----",
    "imap.report.server_greeting": "IMAP banner   : {greeting}",
    "imap.report.server_capability": "CAPABILITY    : {capability}",

    "imap.report.section_timestamps": "---- Analiz zaman damgaları ----",
    "imap.report.timestamp_start_utc": "Analiz başlangıcı (UTC)   : {dt}",
    "imap.report.timestamp_start_local": "Analiz başlangıcı (yerel) : {dt}",
    "imap.report.timestamp_end_utc": "Analiz bitişi (UTC)       : {dt}",
    "imap.report.timestamp_end_local": "Analiz bitişi (yerel)     : {dt}",
    "imap.report.duration": "Toplam süre               : {duration}",

    "imap.report.section_folders": "---- Analiz edilen klasörler ----",
    "imap.report.folders_count": "Seçilen klasör sayısı : {count}",

    "imap.report.folder_header": "Klasör : {name}",
    "imap.report.folder_messages": "  Bulunan mesajlar (dönem) : {count}",
    "imap.report.folder_exported": "  Dışa aktarılan mesajlar  : {count}",
    "imap.report.folder_errors": "  Alma hataları            : {count}",
    "imap.report.folder_bytes": "  İndirilen veri           : {bytes} bayt",
    "imap.report.folder_size_stats": "  Min / maks / ort. boyut  : {min_size} / {max_size} / {avg_size} bayt",
    "imap.report.folder_period": "  Kapsanan dönem (INTERNALDATE) : {first} → {last}",
    "imap.report.folder_error_uids": "  Hata alınan UID’ler (tam liste olmayabilir) : {uids}",

    "imap.report.section_totals": "---- Genel toplamlar ----",
    "imap.report.total_messages": "Bulunan mesajlar (tüm klasörler) : {count}",
    "imap.report.total_exported": "Dışa aktarılan mesajlar          : {count}",
    "imap.report.total_errors": "Alma hataları                    : {count}",
    "imap.report.total_bytes": "Toplam indirilen veri            : {bytes} bayt",

    "imap.report.section_forensic": "---- Metodoloji ve adli güvenceler ----",
    "imap.report.forensic_item_readonly": "- Araç yalnızca salt okunur IMAP komutlarını kullandı (SELECT readonly, SEARCH, FETCH). Analiz sırasında hiçbir mesaj değiştirilmedi, silinmedi veya okunmuş olarak işaretlenmedi.",
    "imap.report.forensic_item_eml": "- Mesajlar IMAP sunucusundan alındıkları haliyle dışa aktarıldı ve içerikleri değiştirilmeden .eml dosyaları olarak diske yazıldı.",
    "imap.report.forensic_item_hashes": "- Her dışa aktarılan mesaj hashes.txt dosyasında listelenen bir SHA-256 özetiyle ilişkilendirildi; ayrıca tüm tekil hash’lerin birleştirilmesiyle hesaplanan küresel bir özet üretildi.",
    "imap.report.forensic_item_report_hash": "- Bu analiz raporunun kendisi de SHA-256 ile özetlenmiştir ve rapor bütünlüğünü garanti altına almak için bu özet hashes.txt dosyasına eklenmiştir.",

    "imap.report.hashes_report_header": "ANALİZ RAPORU:",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Export worker (logs, errors, summary)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "Klasör seçilmedi.",
    "imap.worker.log_export_dir": "Dışa aktarma klasörü: {export_dir}",
    "imap.worker.tool_hash_error": "(araç hash’i hesaplanırken hata oluştu)",

    "imap.worker.log_connecting": "IMAP sunucusuna bağlanılıyor...",
    "imap.worker.greeting_not_available": "(IMAP banner mevcut değil)",
    "imap.worker.log_auth_classic": "Klasik IMAP kimlik doğrulama...",
    "imap.worker.error_auth_failed": "IMAP kimlik doğrulama hatası: {error}",
    "imap.worker.capability_error": "(CAPABILITY komutu sırasında hata)",

    "imap.worker.log_date_start_inclusive": "Başlangıç tarihi (dahil): {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "Başlangıç tarihi: ayarlanmadı → ilk mevcut mesajdan itibaren çıkarım.",
    "imap.worker.date_start_unset_label": "İlk mevcut mesaj (alt sınır yok)",

    "imap.worker.log_date_end_inclusive": "Bitiş tarihi (dahil): {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "Bitiş tarihi: ayarlanmadı → sunucudaki son tarihe kadar.",
    "imap.worker.date_end_unset_label": "Son mevcut mesaj (üst sınır yok)",

    "imap.worker.log_criteria": "Kullanılan IMAP arama ölçütleri: {criteria}",
    "imap.worker.log_selected_folders_header": "Seçilen klasörler ({count}):",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "Sayım aşaması sırasında durdurma isteği alındı.",
    "imap.worker.log_phase1_count": "[Aşama 1] {folder} içindeki mesajlar sayılıyor...",
    "imap.worker.log_select_folder_failed": "  ⚠️ Bu klasör seçilemedi, atlanıyor.",
    "imap.worker.log_search_folder_failed": "  ⚠️ Bu klasörde arama yapılırken hata oluştu, atlanıyor.",
    "imap.worker.log_messages_to_process": "  → {folder} içinde işlenecek {count} mesaj",

    "imap.worker.log_total_messages_to_download": "Tüm klasörlerde indirilecek toplam mesaj sayısı: {count}",

    "imap.worker.log_stop_during_export": "Durdurma istendi: dışa aktarma kesintisiz şekilde sonlandırılıyor.",
    "imap.worker.log_folder_header": "=== Klasör: {folder} ===",
    "imap.worker.log_no_messages_in_period": "  Bu dönem için {folder} klasöründe mesaj yok.",
    "imap.worker.log_folder_message_count": "  {folder} klasöründe bulunan mesaj sayısı: {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ Bu klasör yeniden seçilemedi, atlanıyor.",

    "imap.worker.log_first_message_download": "  İlk mesaj indiriliyor ({uid})...",
    "imap.worker.log_folder_progress": "  {folder} klasörü ilerleme durumu: {current}/{total} (son: {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ {uid} mesajı alınırken hata oluştu, devam ediliyor.",
    "imap.worker.log_folder_end": "  {folder} klasörü sonu",

    "imap.worker.hashes_header": "Dışa aktarılan dosyalar ve SHA-256 özetleri listesi",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "KÜRESEL ÖZET (yalnızca mesajlar):",

    "imap.worker.log_export_done_header": "=== Dışa aktarma tamamlandı ===",
    "imap.worker.log_export_done_count": "Dışa aktarılan toplam mesaj sayısı: {count}",
    "imap.worker.log_export_done_hashes_file": "Hash dosyası: {path}",
    "imap.worker.log_export_done_hash": "Küresel özet: {file_hash}",

    "imap.worker.summary": (
        "Dışa aktarma tamamlandı.\n\n"
        "Dışa aktarılan mesajlar: {count}\n"
        "Klasör: {export_dir}\n\n"
        "Küresel özet (mesajlar):\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "Analiz raporu üretildi ve özetlendi (rapport_imap_export.txt ve hashes.txt dosyalarına bakın).",
    "imap.worker.log_report_failed": "⚠️ Analiz raporu oluşturulamadı: {error}",

    "imap.worker.error_generic": "Bir hata oluştu: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (mailbox list)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "IMAP sunucusuna bağlanılıyor...",
    "imap.tk.log_auth_classic": "Klasik IMAP kimlik doğrulama...",
    "imap.tk.error_list_mailboxes_failed": "IMAP klasörleri listelenemedi.",

    "imap.tk.log_folders_found_header": "Sunucuda bulunan klasörler:",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "Toplam IMAP klasörü: {count}",

    "imap.tk.msgbox_error_title": "Hata",
    "imap.tk.msgbox_error_fetch_mailboxes": "IMAP klasörleri alınırken hata oluştu: {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ Klasörler alınırken hata: {error}",

    # ------------------------------------------------------------------
    # IMAP - Tk interface (full tab)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. IMAP dışa aktarma",

    "imap.tk.label_server": "IMAP sunucusu:",
    "imap.tk.label_email": "E-posta adresi:",
    "imap.tk.label_password": "Şifre:",
    "imap.tk.label_date_start": "Başlangıç tarihi (GG/AA/YYYY, isteğe bağlı):",
    "imap.tk.label_date_end": "Bitiş tarihi (GG/AA/YYYY, isteğe bağlı):",
    "imap.tk.label_log": "Günlük:",
    "imap.tk.label_mailboxes": "Dışa aktarılacak IMAP klasörleri:",
    "imap.tk.checkbox_select_all": "Tümünü seç / Tümünü kaldır",
    "imap.tk.label_progress": "İlerleme:",

    "imap.tk.msgbox_missing_fields_title": "Eksik alanlar",
    "imap.tk.msgbox_missing_fields_text": "Lütfen sunucu, e-posta ve şifreyi doldurun.",

    "imap.tk.log_fetch_mailboxes_start": "IMAP klasörleri alınıyor...",
    "imap.tk.log_no_mailboxes_or_error": "Klasör bulunamadı veya bir hata oluştu.",
    "imap.tk.log_select_mailboxes_hint": "Dışa aktarılacak klasörleri seçin.",

    "imap.tk.button_list_mailboxes": "IMAP klasörlerini listele",

    "imap.tk.msgbox_date_start_invalid_title": "Geçersiz başlangıç tarihi",
    "imap.tk.msgbox_date_start_invalid_text": "Başlangıç tarihi GG/AA/YYYY formatında olmalıdır.",

    "imap.tk.msgbox_date_end_invalid_title": "Geçersiz bitiş tarihi",
    "imap.tk.msgbox_date_end_invalid_text": "Bitiş tarihi GG/AA/YYYY formatında olmalıdır.",

    "imap.tk.msgbox_date_range_invalid_title": "Geçersiz tarih aralığı",
    "imap.tk.msgbox_date_range_invalid_text": (
        "Bitiş tarihi başlangıç tarihinden önce olamaz."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "Klasör seçilmedi",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "Lütfen en az bir IMAP klasörü seçin (\"IMAP klasörlerini listele\" üzerinden)."
    ),

    "imap.tk.log_export_start": "Dışa aktarma başlatılıyor...",
    "imap.tk.button_run_export": "Dışa aktarmayı çalıştır (seçili klasörler)",

    "imap.tk.log_stop_requested": (
        "Durdurma istendi, dışa aktarma temiz bir şekilde sonlandırılacak..."
    ),
    "imap.tk.button_stop_export": "Dışa aktarmayı durdur",

    "imap.tk.msgbox_export_done_title": "Dışa aktarma tamamlandı",


    # ------------------------------------------------------------------
    # IMAP logs
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "Klasörleri listelemek için IMAP sunucusuna bağlanılıyor…"
    ),
    "imap.log.fetch_error": "❌ Klasör alınırken hata:",
    "imap.log.no_mailboxes": "Bu hesapta IMAP klasörü bulunamadı.",
    "imap.log.mailboxes_found": "Sunucuda bulunan klasörler:",
    "imap.log.mailboxes_total": "Toplam IMAP klasörü: {count}",
    "imap.log.mailboxes_select_hint": (
        "Klasörleri salt okunur modda çıkarmak için seçin."
    ),
    "imap.log.start_export": (
        "IMAP çıkarımı başlatılıyor (adli mod, salt okunur)…"
    ),
    "imap.log.cancel_requested": (
        "İptal isteği IMAP işçisine gönderildi…"
    ),
    "imap.log.export_dir_saved": "Dışa aktarma dizini kaydedildi: {path}",
    "imap.log.done": "IMAP işlemesi tamamlandı.",

    # ------------------------------------------------------------------
    # Dashboard v3
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "Şüphe seviyeleri",
    "dashboard.tab_text": "EML indeks özeti",
    "dashboard.tab_graphs": "Grafikler",
    "dashboard.section_charts": "Grafiksel görselleştirmeler",

    "dashboard.chart_suspicion_title": "Şüphe seviyesi dağılımı",
    "dashboard.chart_folders_title": "IMAP klasörüne göre mesajlar",
    "dashboard.chart_domains_title": "En çok gönderen alan adları",
    "dashboard.chart_attachments_title": "Ek varlığı",
    "dashboard.chart_axis_count": "Sayı",
    "dashboard.chart_attachments_with": "Ekli",
    "dashboard.chart_attachments_without": "Eksiz",

    "dashboard.suspicion_distribution_line": (
        "E-postaların şüphe seviyesine göre dağılımı:"
    ),
    "dashboard.suspicion_level.LOW": "Düşük",
    "dashboard.suspicion_level.MEDIUM": "Orta",
    "dashboard.suspicion_level.HIGH": "Yüksek",
    "dashboard.suspicion_level.CRITICAL": "Kritik",
    "dashboard.suspicion_level.UNKNOWN": "Bilinmiyor",

    "dashboard.chart.folders.title": "IMAP klasörüne göre e-postalar",
    "dashboard.chart.domains.title": "En çok gönderen alan adları",
    "dashboard.chart.attachments.title": "Ek varlığı",
    "dashboard.chart.auth.title": "DKIM / SPF / DMARC sonuçları",
    "dashboard.chart.suspicion.title": "Şüphe seviyesine göre dağılım",

    "dashboard.chart.no_data": (
        "Bu grafik için yeterli veri yok."
    ),
    "dashboard.chart.axis.emails": "E-posta sayısı",
    "dashboard.chart.axis.folders": "IMAP klasörleri",
    "dashboard.chart.axis.domains": "Alan adları",
    "dashboard.chart.axis.levels": "Seviyeler",

    "dashboard.legend.safe": "Genelde güvenli kabul edilen alan",
    "dashboard.legend.suspicious": "İlk incelenmesi gereken alan",

    # ------------------------------------------------------------------
    # Viewer – scoring
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "Şüphe puanı",
    "viewer.col.suspicion_level": "Seviye",
    "viewer.col.suspicion_reasons": "Nedenler (özet)",

    "viewer.score.tooltip.base": (
        "Genel şüphe puanı DKIM/SPF/DMARC, Received anomalileri, "
        "başlık bütünlüğü ve ekler üzerinden hesaplanır."
    ),
    "viewer.score.level.LOW": (
        "Düşük şüphe: mevcut kurallara göre anormal bir şey tespit edilmedi."
    ),
    "viewer.score.level.MEDIUM": (
        "Orta şüphe: bazı öğeler kontrol edilmelidir "
        "(başlıklar, kimlik doğrulama veya ekler)."
    ),
    "viewer.score.level.HIGH": (
        "Yüksek şüphe: birden fazla teknik gösterge tutarsız veya tehlikeli."
    ),
    "viewer.score.level.CRITICAL": (
        "Kritik şüphe: e-postanın kötü amaçlı veya sahte olma olasılığı çok yüksek."
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth limits
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "Bu hesap, modern mekanizmalar (OAuth2, resmi dışa aktarma araçları) "
        "gerektiren bir sağlayıcı tarafından yönetiliyor gibi görünüyor "
        "(örn. Gmail, Outlook/Microsoft 365, Yahoo).\n\n"
        "Uyumluluğu korumak için bu sürüm bu servislerde doğrudan IMAP "
        "çıkarımı yapmaz.\n\n"
        "Mesajlara uyumlu bir şekilde erişmek için:\n"
        "  • Gmail: Google Takeout (MBOX) veya Thunderbird kullanın.\n"
        "  • Outlook / Microsoft 365: Outlook PST dışa aktarma araçlarını kullanın.\n"
        "  • Yahoo vb.: Sağlayıcının sunduğu dışa aktarma araçlarını kullanın.\n\n"
        "Gelecek sürümler MBOX, PST vb. formatları doğrudan analiz etmeyi hedefliyor."
    ),

    # ------------------------------------------------------------------
    # Viewer — search mini-language
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "Adli mini-dil:\n"
        "  from:alice@example.com\n"
        "  domain:bank.com\n"
        "  folder:\"INBOX/Önemli\"\n"
        "  attachment:true\n"
        "Operatörler: örtük AND, OR, NOT, parantezler."
    ),

    # ------------------------------------------------------------------
    # Viewer – CSV messages
    # ------------------------------------------------------------------
    "viewer.no_index_title": "İndeks yok",
    "viewer.no_index_body": (
        "Bu oturumda kullanılabilir bir indeks yok.\n"
        "Sekme 2’de indeks oluşturun veya bir CSV dosyası açın."
    ),
    "viewer.open_csv_title": "İndeks CSV dosyasını aç",
    "viewer.error_csv_title": "CSV okuma hatası",
    "viewer.error_csv_body": (
        "CSV dosyası okunamadı: {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – preview
    # ------------------------------------------------------------------
    "viewer.attach.preview": "Salt okunur önizleme",
    "viewer.attach.preview_failed_title": "Önizleme başarısız",
    "viewer.attach.preview_failed_body": (
        "Bu ekin önizlemesi gösterilemiyor."
    ),
    "viewer.attach.preview_unsupported_title": "Desteklenmeyen tür",
    "viewer.attach.preview_unsupported_body": (
        "Bu MIME türü için yerleşik önizleme yok: {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer — extraction
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "Mesaj yok",
    "viewer.attach.no_msg_body": "Şu anda seçili bir mesaj yok.",
    "viewer.attach.no_selection_title": "Ek seçilmedi",
    "viewer.attach.no_selection_body": (
        "Lütfen listeden bir ek seçin."
    ),
    "viewer.attach.no_root_title": "Çalışma dizini bulunamadı",
    "viewer.attach.no_root_body": (
        "Ek çıkarımı için yapılandırılmış bir adli / indeks dizini yok."
    ),
    "viewer.attach.extract_one_title": "Ek çıkarıldı",
    "viewer.attach.extract_one_body": (
        "Ek şu konuma çıkarıldı:\n{path}"
    ),
    "viewer.attach.extract_all_title": "Ekler çıkarıldı",
    "viewer.attach.extract_all_body": (
        "{count} ek çıkarıldı:\n{paths}"
    ),

    "viewer.attach.extract_one": "Seçili eki çıkar",
    "viewer.attach.extract_all": "Tüm ekleri çıkar",

    # ------------------------------------------------------------------
    # About
    # ------------------------------------------------------------------
    "about.version_label": "Sürüm:",
    "about.description": (
        "EML/IMAP e-postalarının adli analizine yönelik salt okunur araç."
    ),
}
