# 📂 EML / IMAP Forensic Suite – v1.0.1

[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 Hakkında

**EML / IMAP Forensic Suite**,  
**e-posta adli analizine** yönelik profesyonel bir araç setidir ve şu tür soruşturmalar için tasarlanmıştır:

- BEC (Business Email Compromise)
- Finansal dolandırıcılık
- E-posta hesabı ele geçirilmesi
- Hukuki soruşturmalar ve bilirkişi incelemeleri

Uygulama şunları sağlar:

- **salt-okunur IMAP dışa aktarma**,
- bir EML korpusunun **CSV formatında indekslenmesi**,
- **otomatik adli analiz** (başlıklar, Received zinciri, DKIM/SPF/DMARC, ekler…),
- e-postaların **derin incelemesi**,
- kapsamlı bir **istatistiksel özet** oluşturma.

Tüm işlemler güvenlidir:  
🛡 **orijinal EML dosyalarına asla dokunulmaz.**

---

## 🧰 Ana özellikler (v1.0.1)

### ✔ Salt-okunur IMAP dışa aktarma

- SSL üzerinden IMAP
- `.eml` biçiminde dışa aktarma (sunucuya asla yazmaz)
- IMAP klasör seçimi
- Tarihe göre filtreleme
- Her mesaj için SHA-256 hash
- Genel dışa aktarma hash’i
- Klasörler, boyutlar, dönem, hatalar, hash’ler ve sunucu bilgileri içeren tam adli rapor

### ✔ EML indeksleme

- `.eml` klasörlerinin tam analizi
- Otomatik çıkarım:

  - Tarih
  - From / To / CC / Bcc
  - Subject
  - Message-ID
  - Orijinal IMAP klasörü
  - `hashes.txt` üzerinden eşleşen hash
  - Adli göstergeler:
    - DKIM / SPF / DMARC
    - Received zinciri (anomali tespiti)
    - Bütünlük bayrakları (eksik tarih, eksik Message-ID, vb.)
    - Ek dosyaları

- **CSV indeks** + dahili Python indeksi
- Çok iş parçacıklı hızlı indeksleme

### ✔ Gelişmiş adli görüntüleyici (yeni)

- Tam görüntüleme:
  - Ham başlıklar
  - Metin + temizlenmiş HTML
  - Ek listesi + meta veriler
- Eklerin adli çıkarımı:
  - SHA-256 hash
  - Her ek için ayrı rapor
- Görseller, PDF’ler ve basit dosyalar için önizleme
- Güçlü boole arama dili:
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - Operatörler: **AND / OR / NOT**
  - **Parantezler**: `(şart1 or şart2) and not şart3`
  - Örtük AND
  - Küresel tam metin arama

### ✔ Adli pano (yeni)

- EML korpusunun genel istatistiksel görünümü
- Analiz:
  - Gönderen alan adları
  - IMAP klasör dağılımı
  - Zaman aralığı
  - DKIM/SPF/DMARC
  - Received anomalileri
  - Bütünlük bayrakları
  - Ekler
- Net, dışa aktarılabilir metinsel özet

### ✔ Modern grafik arayüz (PySide6)

- 4 sekme: IMAP • Indexing • Viewer • Dashboard
- Açık / koyu tema
- Çoklu dil desteği:
  - Fransızca, İngilizce
  - Arapça, Almanca, İspanyolca, Hintçe, İtalyanca, Japonca, Korece, Hollandaca, Portekizce, Rusça, Türkçe, Ukraynaca, Çince
- Paylaşılan durum yönetimi (son indeks, son dışa aktarma…)

---

## 📦 Kurulum (kaynak koddan)

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
```
