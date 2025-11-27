# 📂 EML / IMAP Forensic Suite – v1.0.1

[![Licencia](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)  
![Estado](https://img.shields.io/badge/Status-Active-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![Plataforma](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 Acerca de

**EML / IMAP Forensic Suite** es una suite profesional dedicada al  
**análisis forense de correos electrónicos**, diseñada para investigaciones como:

- BEC (Business Email Compromise)
- Fraude financiero
- Compromiso de buzones
- Investigaciones legales y peritajes judiciales

La aplicación permite:

- realizar **extracción IMAP de solo lectura**
- **indexar un corpus EML** en un archivo CSV estructurado
- ejecutar **análisis forense automático** (headers, cadena Received, DKIM/SPF/DMARC, adjuntos…)
- **inspeccionar en profundidad** correos individuales
- producir un **resumen estadístico completo**

Todas las operaciones son no destructivas:  
🛡 **los archivos EML originales nunca se modifican.**

---

## 🧰 Funciones principales (v1.0.1)

### ✔ Exportación IMAP de solo lectura

- IMAP sobre SSL
- Exportación a `.eml` sin escribir nunca en el servidor
- Selección de carpetas IMAP
- Filtrado por fecha
- Hash SHA-256 por mensaje
- Hash global de la exportación
- Informe forense completo: carpetas, tamaños, periodos, errores, hashing, saludo del servidor

### ✔ Indexación EML

- Análisis completo de una carpeta de archivos `.eml`
- Extracción automática de:

  - Fecha
  - From / To / CC / Bcc
  - Asunto
  - Message-ID
  - Carpeta IMAP original
  - Hash correspondiente (via `hashes.txt`)
  - Indicadores forenses:
    - DKIM / SPF / DMARC
    - Cadena Received (detección de anomalías)
    - Flags de integridad (fecha faltante, Message-ID faltante, etc.)
    - Adjuntos

- Generación de un **CSV indexado** + índice interno en Python
- Indexación multihilo para un rendimiento fluido

### ✔ Visor forense avanzado (nuevo)

- Visualización completa:
  - Headers sin procesar
  - Cuerpo de texto + HTML sanitizado
  - Adjuntos (lista + metadatos)
- Extracción forense de adjuntos:
  - Hash SHA-256
  - Informe individual por adjunto
- Vista previa de imágenes / PDFs / archivos simples
- Potente sistema de búsqueda forense (mini-lenguaje):
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - Booleanos: **AND / OR / NOT**
  - **Paréntesis**: `(cond1 or cond2) and not cond3`
  - AND implícito
  - Búsqueda global de texto completo (headers + adjuntos + hash)

### ✔ Panel forense (nuevo)

- Vista estadística global de un corpus EML
- Análisis de:
  - Dominios remitentes
  - Distribución por carpeta IMAP
  - Período temporal
  - DKIM/SPF/DMARC
  - Anomalías Received
  - Flags de integridad
  - Adjuntos
- Resumen textual claro y exportable

### ✔ Interfaz gráfica moderna (PySide6)

- 4 pestañas: IMAP • Indexación • Visor • Panel
- Tema claro / oscuro
- Multilenguaje:
  - Francés, Inglés
  - - Árabe, Alemán, Español, Hindi, Italiano, Japonés, Coreano, Neerlandés, Portugués, Ruso, Turco, Ucraniano, Chino
- Gestión de estado compartido (último índice, última exportación…)

---

## 📦 Instalación (desde código fuente)

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
```
