# 📂 EML / IMAP Forensic Suite – v1.0.1

### **IMAP 読み取り専用エクスポート · CSV インデックス化 · 高度なフォレンジックビューア · 添付ファイル解析 · 統計ダッシュボード · ブール検索**

[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 概要

**EML / IMAP Forensic Suite** は、以下のような調査向けに設計された  
**メールフォレンジック解析専用のプロフェッショナルツール**です：

- BEC（ビジネスメール詐欺）
- 金融詐欺
- メールボックス侵害
- 法的調査や司法鑑定

本アプリケーションでは次のことが可能です：

- **IMAP 読み取り専用エクスポート**
- **EML コーパスの CSV インデックス化**
- **自動フォレンジック解析**（ヘッダー、Received、DKIM/SPF/DMARC、添付ファイルなど）
- メールの**詳細な解析ビュー**
- **統計レポートの生成**

すべての操作は非破壊的です：  
🛡 **元の EML ファイルは一切変更されません。**

---

## 🧰 主な機能（v1.0.1）

### ✔ IMAP 読み取り専用エクスポート

- SSL 対応 IMAP
- サーバーに書き込みを行わず `.eml` 形式で保存
- IMAP フォルダ選択
- 日付フィルタリング
- メッセージごとの SHA-256 ハッシュ
- エクスポート全体のハッシュ
- フォレンジックレポート（フォルダ・サイズ・期間・エラー・ハッシュ・サーバー Greeting）

### ✔ EML インデックス化

- `.eml` ファイルフォルダの完全解析
- 自動抽出：

  - 日付
  - From / To / CC / Bcc
  - 件名
  - Message-ID
  - 元の IMAP フォルダ
  - 対応するハッシュ（`hashes.txt`）
  - フォレンジック指標：
    - DKIM / SPF / DMARC
    - Received 異常検知
    - 完整性フラグ（日時欠落、Message-ID 欠落など）
    - 添付ファイル情報

- **CSV インデックス**と内部 Python インデックスを生成
- マルチスレッド処理で高速動作

### ✔ 高度なフォレンジックビューア（新機能）

- 完全表示：
  - 生ヘッダー
  - テキスト本文 + サニタイズ済み HTML
  - 添付ファイル（一覧 + メタデータ）
- フォレンジック添付抽出：
  - SHA-256 ハッシュ
  - 添付ファイルごとのレポート
- 画像 / PDF プレビュー
- 強力なフォレンジック検索（ミニ言語）：
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - ブール演算：**AND / OR / NOT**
  - **括弧**：`(cond1 or cond2) and not cond3`
  - 暗黙の AND
  - 全文検索（ヘッダー + 添付 + ハッシュ）

### ✔ フォレンジック・ダッシュボード（新機能）

- EML コーパスの統計ビュー
- 以下の解析が可能：
  - 送信者ドメイン
  - IMAP フォルダ分布
  - 期間統計
  - DKIM/SPF/DMARC
  - Received 異常
  - 完整性フラグ
  - 添付ファイル
- わかりやすいテキスト統計を生成可能

### ✔ モダンな GUI（PySide6）

- 4 タブ：IMAP / インデックス / ビューア / ダッシュボード
- ライト/ダークテーマ
- 多言語対応：
  - 日本語、英語、フランス語、他多数
- 共有状態管理（最新インデックス・最新エクスポートなど）

---

## 📦 インストール（ソース）

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
```
