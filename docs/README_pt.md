📂 EML / IMAP Forensic Suite – v1.0.1

[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 Sobre

**EML / IMAP Forensic Suite** é um conjunto profissional dedicado à  
**análise forense de e-mails**, concebido para investigações como:

- BEC (Business Email Compromise)
- Fraudes financeiras
- Comprometimento de caixas de e-mail
- Investigações jurídicas e perícias judiciais

A aplicação permite:

- realizar **extração IMAP em modo somente leitura**,
- **indexar um conjunto de EML** em um arquivo CSV estruturado,
- executar **análise forense automática** (headers, cadeia Received, DKIM/SPF/DMARC, anexos…),
- **inspecionar e-mails em profundidade**,
- gerar um **resumo estatístico completo**.

Todas as operações são não destrutivas:  
🛡 **os arquivos EML originais nunca são modificados.**

---

## 🧰 Funcionalidades principais (v1.0.1)

### ✔ Exportação IMAP somente leitura

- IMAP via SSL
- Exportação para `.eml` sem nunca escrever no servidor
- Seleção de pastas IMAP
- Filtro por data
- Hash SHA-256 por mensagem
- Hash global da exportação
- Relatório forense completo: pastas, tamanhos, períodos, erros, hashing, saudação do servidor

### ✔ Indexação EML

- Análise completa de uma pasta de arquivos `.eml`
- Extração automática de:

  - Data
  - From / To / CC / Bcc
  - Assunto
  - Message-ID
  - Pasta IMAP original
  - Hash correspondente (`hashes.txt`)
  - Indicadores forenses:
    - DKIM / SPF / DMARC
    - Cadeia Received (detecção de anomalias)
    - Flags de integridade (data ausente, Message-ID ausente, etc.)
    - Anexos

- Geração de um **índice CSV** + índice interno em Python
- Indexação multithread para melhor desempenho

### ✔ Visualizador forense avançado (novo)

- Exibição completa:
  - Headers brutos
  - Corpo de texto + HTML sanitizado
  - Anexos (lista + metadados)
- Extração forense de anexos:
  - Hash SHA-256
  - Relatório individual por anexo
- Pré-visualização de imagens / PDFs / arquivos simples
- Sistema de pesquisa forense poderoso (mini-linguagem):
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - Booleanos: **AND / OR / NOT**
  - **Parênteses**: `(cond1 or cond2) and not cond3`
  - AND implícito
  - Pesquisa global em texto (headers + anexos + hash)

### ✔ Painel forense (novo)

- Visão estatística global de um conjunto de EML
- Análise de:
  - Domínios dos remetentes
  - Distribuição por pasta IMAP
  - Período temporal
  - DKIM/SPF/DMARC
  - Anomalias Received
  - Flags de integridade
  - Anexos
- Resumo textual claro e exportável

### ✔ Interface gráfica moderna (PySide6)

- 4 abas: IMAP • Indexação • Viewer • Dashboard
- Tema claro / escuro
- Suporte multilíngue:
  - Francês, Inglês
  - Árabe, Alemão, Espanhol, Hindi, Italiano, Japonês, Coreano, Neerlandês, Português, Russo, Turco, Ucraniano, Chinês
- Gestão de estado compartilhado (último índice, última exportação…)

---

## 📦 Instalação (via código-fonte)

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
```
