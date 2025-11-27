# 📂 EML / IMAP Forensic Suite – v1.0.1

### **IMAP 只读导出 · CSV 索引 · 高级取证查看器 · 附件分析 · 统计面板 · 布尔搜索**

[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 关于

**EML / IMAP Forensic Suite** 是一款专业的  
**电子邮件取证分析工具套件**，适用于以下调查场景：

- BEC（商业邮件入侵）
- 金融欺诈
- 邮箱泄露 / 入侵
- 法律调查与司法鉴定

本应用可实现：

- **IMAP 只读提取**
- 将 EML 邮件集 **索引为结构化 CSV**
- 执行 **自动取证分析**（邮件头、Received 链、DKIM/SPF/DMARC、附件等）
- **深度检查**单独邮件
- 生成 **完整统计摘要**

所有操作均为非破坏性：  
🛡 **原始 EML 文件永不被修改。**

---

## 🧰 主要功能（v1.0.1）

### ✔ IMAP 只读导出

- SSL IMAP
- 导出为 `.eml` 文件，不会对服务器进行写入
- 选择 IMAP 文件夹
- 日期过滤
- 每封邮件的 SHA-256 哈希
- 全局导出哈希
- 完整取证报告：文件夹、大小、时间范围、错误、哈希、服务器问候语

### ✔ EML 索引

- 全面分析 `.eml` 文件夹
- 自动提取：

  - 日期
  - 发件人 / 收件人 / CC / Bcc
  - 主题
  - Message-ID
  - 原始 IMAP 文件夹
  - 对应哈希（来自 `hashes.txt`）
  - 取证指标：
    - DKIM / SPF / DMARC
    - Received 链异常检测
    - 完整性标记
    - 附件

- 生成 **CSV 索引** + 内部 Python 索引
- 多线程处理以提升性能

### ✔ 高级取证查看器（新增）

- 完整显示：

  - 原始邮件头
  - 文本与安全 HTML 内容
  - 附件及其元数据

- 取证附件导出：

  - SHA-256 哈希
  - 单附件详细报告

- 图像预览 / PDF 打开
- 强大的布尔搜索引擎（迷你语言）：
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - AND / OR / NOT
  - 括号
  - 全局全文搜索

### ✔ 取证统计面板（新增）

- 邮件集的全局统计视图
- 分析内容：

  - 发件域名
  - IMAP 文件夹分布
  - 时间范围
  - DKIM/SPF/DMARC
  - Received 异常
  - 完整性标记
  - 附件

- 清晰可导出的文本摘要

### ✔ 现代图形界面（PySide6）

- 4 个标签页：IMAP • 索引 • 查看器 • 面板
- 明亮 / 暗色主题
- 多语言：

  - 法语、英语
  - 阿拉伯语、德语、西班牙语、印地语、意大利语、日语、韩语、荷兰语、葡萄牙语、俄语、土耳其语、乌克兰语、中文

- 状态共享管理（上次索引、上次导出等）

---

## 📦 源码安装

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
```
