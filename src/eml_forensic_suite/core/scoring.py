from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .authentication_verifier import AdvancedAuthResults
from .received_analysis import ReceivedAnalysisResult
from .integrity_checker import MessageIntegrityResult
from .attachments import AttachmentInfo


@dataclass
class SuspicionScore:

    score: int
    reasons: List[str] = field(default_factory=list)

    @property
    def level(self) -> str:
        if self.score >= 80:
            return "CRITICAL"
        if self.score >= 50:
            return "HIGH"
        if self.score >= 25:
            return "MEDIUM"
        if self.score > 0:
            return "LOW"
        return "NONE"


def _add(score: int, points: int, reasons: List[str], reason: str) -> int:
    if points <= 0:
        return score
    reasons.append(reason)
    return score + points



TRUSTED_INFRA_DOMAINS = {
    "lws.fr",
    "lwspanel.com",
    "ovh.net",
    "ovh.com",
    "infomaniak.com",
    "ionos.com",
    "1and1.com",
    "protonmail.com",
    "gmail.com",
    "googlemail.com",
    "google.com",
    "outlook.com",
    "hotmail.com",
    "live.com",
    "office365.com",
    "yahoo.com",
    "secureserver.net",
    "gandi.net",
}

HIGH_ALIGNMENT_EXPECTATION_DOMAINS = {
    "gmail.com",
    "googlemail.com",
    "outlook.com",
    "hotmail.com",
    "live.com",
    "office365.com",
    "yahoo.com",
    "yahoo.fr",
}


def _domain_in_list(domain: Optional[str], patterns: set[str]) -> bool:
    if not domain:
        return False
    d = domain.lower()
    for p in patterns:
        p = p.lower()
        if d == p or d.endswith("." + p):
            return True
    return False


def _extract_candidate_domains(
    index_entry: Dict[str, Any], auth: Optional[AdvancedAuthResults]
) -> List[str]:
    candidates: List[str] = []

    if auth is not None:
        for attr in (
            "from_domain",
            "return_path_domain",
            "spf_domain",
            "dkim_domain",
        ):
            val = getattr(auth, attr, None)
            if val:
                candidates.append(str(val))

    for key in ("from_domain", "from_addr_domain", "sender_domain"):
        val = index_entry.get(key)
        if val:
            candidates.append(str(val))

    return candidates


def _is_trusted_infra(
    index_entry: Dict[str, Any], auth: Optional[AdvancedAuthResults]
) -> bool:
    for dom in _extract_candidate_domains(index_entry, auth):
        if _domain_in_list(dom, TRUSTED_INFRA_DOMAINS):
            return True
    return False


def _is_high_alignment_expected(
    index_entry: Dict[str, Any], auth: Optional[AdvancedAuthResults]
) -> bool:
    for dom in _extract_candidate_domains(index_entry, auth):
        if _domain_in_list(dom, HIGH_ALIGNMENT_EXPECTATION_DOMAINS):
            return True
    return False


def compute_suspicion_score(
    index_entry: Dict[str, Any],
    auth: Optional[AdvancedAuthResults] = None,
    received: Optional[ReceivedAnalysisResult] = None,
    integrity: Optional[MessageIntegrityResult] = None,
    attachments: Optional[List[AttachmentInfo]] = None,
) -> SuspicionScore:
    score = 0
    reasons: List[str] = []

    trusted_infra = _is_trusted_infra(index_entry, auth)
    high_align_expected = _is_high_alignment_expected(index_entry, auth)

    if auth is not None:
        dkim_res = (auth.dkim_result or "").lower()
        spf_res = (auth.spf_result or "").lower()
        dmarc_res = (auth.dmarc_result or "").lower()

        dkim_pass = dkim_res == "pass"
        dmarc_pass = dmarc_res == "pass"

        dkim_fail_like = {"fail", "permerror"}
        spf_fail_like = {"fail", "permerror"}
        dmarc_fail_like = {"fail", "permerror"}
        softfail_like = {"softfail"}
        temperror_like = {"temperror"}

        if dkim_res in dkim_fail_like:
            pts = 25
            if trusted_infra:
                pts = 12
            score = _add(score, pts, reasons, "DKIM_FAIL")
        elif dkim_res in softfail_like:
            pts = 8
            if trusted_infra:
                pts = 3
            score = _add(score, pts, reasons, "DKIM_SOFTFAIL")
        elif dkim_res in temperror_like:
            score = _add(score, 5, reasons, "DKIM_TEMPERROR")

        if spf_res in spf_fail_like:
            pts = 15
            if trusted_infra:
                pts = 8
            score = _add(score, pts, reasons, "SPF_FAIL")
        elif spf_res in softfail_like:
            pts = 5
            if trusted_infra:
                pts = 2
            score = _add(score, pts, reasons, "SPF_SOFTFAIL")
        elif spf_res in temperror_like:
            score = _add(score, 3, reasons, "SPF_TEMPERROR")

        if dmarc_res in dmarc_fail_like:
            pts = 30
            if trusted_infra:
                pts = 15
            score = _add(score, pts, reasons, "DMARC_FAIL")
        elif dmarc_res in temperror_like:
            score = _add(score, 5, reasons, "DMARC_TEMPERROR")

        for flag in getattr(auth, "flags", []):
            if flag == "DKIM_MISALIGNED":
                if high_align_expected and not trusted_infra:
                    score = _add(score, 10, reasons, "DKIM_MISALIGNED")
                elif not trusted_infra:
                    score = _add(score, 5, reasons, "DKIM_MISALIGNED")
            elif flag == "SPF_MISALIGNED":
                if high_align_expected and not trusted_infra:
                    score = _add(score, 8, reasons, "SPF_MISALIGNED")
                elif not trusted_infra:
                    score = _add(score, 4, reasons, "SPF_MISALIGNED")
            elif flag == "AUTH_PARTIAL_OR_NONE":
                if not (dkim_pass or dmarc_pass) and high_align_expected and not trusted_infra:
                    score = _add(score, 5, reasons, "AUTH_PARTIAL_OR_NONE")
            else:
                score = _add(score, 3, reasons, f"AUTH_FLAG_{flag}")

        alignment_issues = getattr(auth, "alignment_issues", None)
        if alignment_issues:
            for flag in alignment_issues:
                if flag in {"RETURN_PATH_MISMATCH", "SPF_FROM_MISMATCH", "SPF_MISALIGNED"}:
                    if high_align_expected and not trusted_infra:
                        pts = 10
                    elif not trusted_infra:
                        pts = 5
                    else:
                        pts = 2
                    score = _add(score, pts, reasons, f"AUTH_ALIGN_{flag}")
                else:
                    score = _add(score, 3, reasons, f"AUTH_ALIGN_{flag}")

    if received is not None:
        for flag in received.anomalies:
            if flag == "NO_RECEIVED":
                pts = 20
                if trusted_infra:
                    pts = 15
                score = _add(score, pts, reasons, "NO_RECEIVED")

            elif flag == "MANY_HOPS":
                score = _add(score, 5, reasons, "MANY_HOPS")

            elif flag == "RECEIVED_TIME_BACKWARDS":
                pts = 25
                if trusted_infra:
                    pts = 20
                score = _add(score, pts, reasons, "RECEIVED_TIME_BACKWARDS")

            elif flag in {"RECEIVED_LOCALHOST", "RECEIVED_PRIVATE_IP_EXTERNAL"}:
                if trusted_infra:
                    pts = 2
                else:
                    pts = 10
                score = _add(score, pts, reasons, flag)

            elif flag == "RECEIVED_SUSPICIOUS_HELO":
                pts = 10
                if trusted_infra:
                    pts = 5
                score = _add(score, pts, reasons, "RECEIVED_SUSPICIOUS_HELO")

            else:
                score = _add(score, 3, reasons, f"RECEIVED_{flag}")

    if integrity is not None:
        for flag in integrity.flags:
            if flag == "MISSING_DATE":
                score = _add(score, 10, reasons, "MISSING_DATE")
            elif flag == "MISSING_FROM":
                score = _add(score, 20, reasons, "MISSING_FROM")
            elif flag == "MISSING_MESSAGE_ID":
                score = _add(score, 15, reasons, "MISSING_MESSAGE_ID")

            elif flag in {"INVALID_MESSAGE_ID", "INVALID_DATE_HEADER"}:
                score = _add(score, 10, reasons, flag)

            elif flag.startswith("HTML_"):
                score = _add(score, 25, reasons, flag)

            elif flag.startswith("EXOTIC_HEADER_"):
                score = _add(score, 3, reasons, flag)

            elif flag == "DATE_OUTSIDE_RECEIVED_RANGE":
                score = _add(score, 15, reasons, flag)

            elif flag.startswith("RECEIVED_"):
                score = _add(score, 10, reasons, flag)

            elif flag.startswith(("DKIM_", "SPF_", "DMARC_")):
                score = _add(score, 15, reasons, flag)

            else:
                score = _add(score, 2, reasons, flag)

        if getattr(integrity, "html_suspicious", False):
            score = _add(score, 10, reasons, "HTML_SUSPICIOUS")

    if attachments:
        for att in attachments:
            name = (att.filename or "").lower()
            mime = (att.mime_type or "").lower()

            dangerous_ext = (".exe", ".js", ".vbs", ".ps1", ".bat", ".cmd", ".scr", ".jar")
            if any(name.endswith(ext) for ext in dangerous_ext):
                score = _add(score, 35, reasons, "DANGEROUS_ATTACHMENT_EXT")

            macro_ext = (".docm", ".xlsm", ".pptm")
            if any(name.endswith(ext) for ext in macro_ext):
                score = _add(score, 25, reasons, "MACRO_ATTACHMENT")

            if "application/x-msdownload" in mime:
                score = _add(score, 35, reasons, "DANGEROUS_ATTACHMENT_MIME")

            if name.endswith(".pdf") and mime not in ("application/pdf", ""):
                score = _add(score, 10, reasons, "PDF_MIME_MISMATCH")

            if getattr(att, "is_suspicious", False):
                score = _add(score, 10, reasons, "ATTACHMENT_MARKED_SUSPICIOUS")

            flags = getattr(att, "suspicion_flags", None) or []
            if "POSSIBLE_EXECUTABLE" in flags:
                score = _add(score, 10, reasons, "ATTACHMENT_EXECUTABLE")
            if "EXT_MISMATCH" in flags:
                score = _add(score, 5, reasons, "ATTACHMENT_EXT_MISMATCH")

    subject = str(index_entry.get("subject", "") or "").lower()
    finance_keywords = [
        "urgent",
        "urgence",
        "paiement",
        "payment",
        "facture",
        "invoice",
        "iban",
        "virement",
        "bank",
    ]
    if any(word in subject for word in finance_keywords):
        score = _add(score, 5, reasons, "SUBJECT_FINANCE_KEYWORD")

    score = max(0, min(100, score))
    return SuspicionScore(score=score, reasons=reasons)
