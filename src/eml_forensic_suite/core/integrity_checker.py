from __future__ import annotations

from dataclasses import dataclass, field
from email.message import EmailMessage
from typing import List, Dict, Any, Optional
import re
from datetime import datetime
from email.utils import parsedate_to_datetime

from .received_analysis import ReceivedAnalysisResult
from .authentication_verifier import AdvancedAuthResults



@dataclass
class IntegrityIssue:
    code: str
    message: str


@dataclass
class MessageIntegrityResult:
    issues: List[IntegrityIssue] = field(default_factory=list)

    @property
    def flags(self) -> List[str]:
        return sorted({issue.code for issue in self.issues})



def _check_message_id(msg: EmailMessage, result: MessageIntegrityResult) -> None:
    mid = msg.get("Message-ID") or msg.get("Message-Id") or msg.get("message-id") or ""
    if not mid:
        result.issues.append(IntegrityIssue(
            "MISSING_MESSAGE_ID",
            "Message-ID manquant"
        ))
        return

    if "@" not in mid:
        result.issues.append(IntegrityIssue(
            "INVALID_MESSAGE_ID",
            f"Message-ID invalide: {mid!r}"
        ))


def _check_date_header(msg: EmailMessage, result: MessageIntegrityResult) -> Optional[datetime]:
    date_str = msg.get("Date") or msg.get("date") or ""
    if not date_str:
        result.issues.append(IntegrityIssue("MISSING_DATE", "Date manquante"))
        return None

    try:
        return parsedate_to_datetime(date_str)
    except Exception:
        result.issues.append(IntegrityIssue("INVALID_DATE_HEADER", f"Date invalide: {date_str!r}"))
        return None


def _check_html_danger(msg: EmailMessage, result: MessageIntegrityResult) -> None:
    html_parts = []

    if msg.is_multipart():
        for part in msg.walk():
            if part.is_multipart():
                continue

            ctype = part.get_content_type().lower()
            if ctype == "text/html":
                try:
                    html = part.get_content()
                except Exception:
                    payload = part.get_payload(decode=True) or b""
                    html = payload.decode("utf-8", errors="replace")
                html_parts.append(html)
    else:
        if msg.get_content_type().lower() == "text/html":
            try:
                html = msg.get_content()
            except Exception:
                payload = msg.get_payload(decode=True) or b""
                html = payload.decode("utf-8", errors="replace")
            html_parts.append(html)

    if not html_parts:
        return

    html_all = "\n".join(html_parts).lower()

    patterns = {
        "HTML_SCRIPT_TAG": r"<\s*script",
        "HTML_JAVASCRIPT_URL": r"javascript\s*:",
        "HTML_IFRAME": r"<\s*iframe",
        "HTML_BASE64_EMBED": r"data:\s*text/html;base64",
        "HTML_ONERROR": r"onerror\s*=",
        "HTML_ONLOAD": r"onload\s*=",
        "HTML_EVAL": r"eval\s*\(",
    }

    for code, pattern in patterns.items():
        if re.search(pattern, html_all, re.IGNORECASE):
            result.issues.append(IntegrityIssue(
                code,
                f"HTML suspect détecté : {code}"
            ))


def _check_exotic_headers(msg: EmailMessage, result: MessageIntegrityResult) -> None:
    exotic = [
        "X-Mailer",
        "X-Originating-IP",
        "X-MSMail-Priority",
        "X-Priority",
        "X-Spam-Flag",
        "X-Spam-Status",
        "X-Spam-Level",
        "X-Spam-Score",
    ]

    for h in exotic:
        if msg.get(h) is not None:
            code = f"EXOTIC_HEADER_{h.upper().replace('-', '_')}"
            result.issues.append(IntegrityIssue(
                code,
                f"Présence d’un header exotique : {h}"
            ))



def check_message_integrity(
    msg: EmailMessage,
    received_analysis: Optional[ReceivedAnalysisResult] = None,
    auth_results: Optional[AdvancedAuthResults] = None,
) -> MessageIntegrityResult:
    result = MessageIntegrityResult()

    _check_message_id(msg, result)

    msg_dt = _check_date_header(msg, result)

    _check_html_danger(msg, result)

    _check_exotic_headers(msg, result)

    if received_analysis is not None:
        for code in received_analysis.anomalies:
            result.issues.append(IntegrityIssue(
                code,
                f"Anomalie Received : {code}"
            ))

    if auth_results is not None:
        for flag in auth_results.alignment_issues:
            result.issues.append(IntegrityIssue(
                flag,
                f"Anomalie auth : {flag}"
            ))

    if received_analysis and received_analysis.hops and msg_dt:
        hop_times = [
            h.parsed_date
            for h in received_analysis.hops
            if getattr(h, "parsed_date", None) is not None
        ]
        if hop_times:
            first = min(hop_times)
            last = max(hop_times)
            if msg_dt < first or msg_dt > last:
                result.issues.append(
                    IntegrityIssue(
                        "DATE_OUTSIDE_RECEIVED_RANGE",
                        "Date de l'en-tête 'Date' en dehors de l'intervalle des timestamps Received.",
                    )
                )

    return result




@dataclass
class CorpusIntegrityIssue:
    code: str
    message: str
    affected_indices: List[int] = field(default_factory=list)


def analyze_index_corpus(index_entries: List[Dict[str, Any]]) -> List[CorpusIntegrityIssue]:
    issues: List[CorpusIntegrityIssue] = []

    seq_list = [(i, entry.get("sequence_number")) for i, entry in enumerate(index_entries)
                if isinstance(entry.get("sequence_number"), int)]

    if seq_list:
        seq_sorted = sorted(seq_list, key=lambda x: x[1])
        prev = seq_sorted[0][1]
        gap_indices = []

        for i, seq in seq_sorted[1:]:
            if seq > prev + 1:
                gap_indices.append(i)
            prev = seq

        if gap_indices:
            issues.append(CorpusIntegrityIssue(
                code="SEQUENCE_GAPS",
                message="Des gaps ont été détectés dans les numéros de séquence IMAP.",
                affected_indices=gap_indices
            ))

    mid_map: Dict[str, List[int]] = {}
    for i, entry in enumerate(index_entries):
        mid = entry.get("message_id")
        if mid:
            mid_map.setdefault(str(mid), []).append(i)

    dup_indices = [i for mid, idxs in mid_map.items() if len(idxs) > 1 for i in idxs]

    if dup_indices:
        issues.append(CorpusIntegrityIssue(
            code="DUPLICATE_MESSAGE_ID",
            message="Des Message-ID dupliqués ont été détectés.",
            affected_indices=sorted(set(dup_indices))
        ))

    return issues
