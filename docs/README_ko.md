📂 EML / IMAP Forensic Suite – v1.0.1

**IMAP 읽기 전용 내보내기 · CSV 인덱싱 · 고급 포렌식 뷰어 · 첨부파일 분석 · 통계 대시보드 · 불리언 검색**

[![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-orange)](LICENSE)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.12-blue)  
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)

---

## 🔍 소개

**EML / IMAP Forensic Suite**는 다음과 같은 조사를 위해 설계된  
**전문 이메일 포렌식 분석 도구**입니다:

- BEC(비즈니스 이메일 사기)
- 금융 사기
- 메일박스 침해
- 법률 조사 및 법원 감정

이 애플리케이션은 다음 기능을 제공합니다:

- **IMAP 읽기 전용 추출**
- **EML 데이터 세트의 CSV 인덱싱**
- **자동 포렌식 분석** (헤더, Received, DKIM/SPF/DMARC, 첨부파일 등)
- 이메일의 **심층 분석**
- **완전한 통계 요약 생성**

모든 작업은 비파괴적입니다.  
🛡 **원본 EML 파일은 절대 수정되지 않습니다.**

---

## 🧰 주요 기능 (v1.0.1)

### ✔ IMAP 읽기 전용 추출

- SSL 기반 IMAP
- 서버에 기록 없이 `.eml` 파일로 저장
- IMAP 폴더 선택
- 날짜 필터링
- 메시지별 SHA-256 해시
- 전체 내보내기의 글로벌 해시
- 포렌식 보고서: 폴더, 크기, 기간, 오류, 해시, 서버 greeting

### ✔ EML 인덱싱

- `.eml` 파일 폴더 전체 분석
- 자동 추출:

  - 날짜
  - From / To / CC / Bcc
  - 제목
  - Message-ID
  - 원본 IMAP 폴더
  - 해당 해시 (`hashes.txt`)
  - 포렌식 지표:
    - DKIM / SPF / DMARC
    - Received 이상 탐지
    - 무결성 플래그 (날짜 없음, Message-ID 없음 등)
    - 첨부파일 정보

- **CSV 인덱스** 및 내부 Python 인덱스 생성
- 멀티스레드 인덱싱으로 빠른 처리

### ✔ 고급 포렌식 뷰어 (신규)

- 전체 표시:
  - 원본 헤더
  - 텍스트 + 안전한 HTML 본문
  - 첨부파일 목록 및 메타데이터
- 포렌식 첨부파일 추출:
  - SHA-256 해시
  - 첨부파일별 개별 보고서
- 이미지 / PDF / 기본 파일 미리보기
- 강력한 포렌식 검색(미니 언어):
  - `from:`, `to:`, `cc:`, `subject:`, `domain:`, `attachment:true`, `hash:`, `folder:`, `date:`
  - 불리언 연산: **AND / OR / NOT**
  - **괄호 사용**: `(cond1 or cond2) and not cond3`
  - 암시적 AND
  - 전체 텍스트 검색(헤더 + 첨부 + 해시)

### ✔ 포렌식 대시보드 (신규)

- EML 데이터셋의 전체 통계 보기
- 분석 항목:
  - 발신 도메인
  - IMAP 폴더 분포
  - 기간
  - DKIM/SPF/DMARC
  - Received 이상
  - 무결성 플래그
  - 첨부파일 통계
- 명확하고 내보낼 수 있는 텍스트 요약

### ✔ 현대적 GUI (PySide6)

- 4개 탭: IMAP • 인덱싱 • 뷰어 • 대시보드
- 라이트 / 다크 테마
- 다국어 지원:
  - 한국어, 일본어, 영어, 프랑스어 등
- 상태 공유 관리 (마지막 인덱스, 마지막 내보내기 등)

---

## 📦 설치 (소스에서 실행)

```sh
git clone https://github.com/HubSev/eml_forensic_suite.git
cd eml_forensic_suite
pip install -r requirements.txt
python -m eml_forensic_suite
```
