from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional
import re
from email.message import EmailMessage

try:
    import dkim
except Exception:
    dkim = None


@dataclass
class AdvancedAuthResults:

    from_domain: str = ""
    return_path_domain: str = ""
    dkim_domain: str = ""
    spf_domain: str = ""
    dmarc_domain: str = ""

    dkim_result: str = "none"
    spf_result: str = "none"
    dmarc_result: str = "none"
    dmarc_policy: str = ""

    dkim_verified_cryptographically: Optional[bool] = None

    smtp_ip: Optional[str] = None

    dkim_aligned: Optional[bool] = None
    spf_aligned: Optional[bool] = None
    dmarc_aligned: Optional[bool] = None

    alignment_issues: List[str] = field(default_factory=list)




def _extract_domain_from_addr(header_value: str) -> str:
    if not header_value:
        return ""

    candidate = header_value.strip()

    if "<" in candidate and ">" in candidate:
        try:
            candidate = candidate.split("<", 1)[1].split(">", 1)[0]
        except Exception:
            pass

    candidate = candidate.strip().strip('"').strip("'")

    if "@" not in candidate:
        return ""

    domain = candidate.split("@")[-1].strip().lower()
    return domain


def _extract_domain_simple(value: str) -> str:
    if not value:
        return ""
    value = value.strip().strip("<>").strip()
    if "@" in value:
        value = value.split("@", 1)[1]
    return value.lower()


def _parse_authentication_results(headers: List[str]) -> dict:
    res = {
        "dkim_result": "none",
        "spf_result": "none",
        "dmarc_result": "none",
        "dmarc_policy": "",
        "spf_domain": "",
        "dmarc_domain": "",
    }

    if not headers:
        return res

    joined = "\n".join(headers)

    def _find_token(token: str) -> str:
        lower = joined.lower()
        idx = lower.find(token + "=")
        if idx == -1:
            return ""
        after = lower[idx + len(token) + 1 :]
        first = after.split()[0].strip(";,")
        return first

    dkim_val = _find_token("dkim")
    spf_val = _find_token("spf")
    dmarc_val = _find_token("dmarc")
    if dkim_val:
        res["dkim_result"] = dkim_val
    if spf_val:
        res["spf_result"] = spf_val
    if dmarc_val:
        res["dmarc_result"] = dmarc_val

    policy = _find_token("policy")
    if policy:
        res["dmarc_policy"] = policy

    m = re.search(r"smtp\.mailfrom=([^;\s]+)", joined, re.IGNORECASE)
    if not m:
        m = re.search(r"mailfrom=([^;\s]+)", joined, re.IGNORECASE)
    if m:
        res["spf_domain"] = _extract_domain_simple(m.group(1))

    m = re.search(r"header\.from=([^;\s]+)", joined, re.IGNORECASE)
    if m:
        res["dmarc_domain"] = _extract_domain_simple(m.group(1))

    return res


def _extract_dkim_domain(msg: EmailMessage) -> str:
    sig_headers = msg.get_all("DKIM-Signature", []) or msg.get_all(
        "Dkim-Signature", []
    )
    for sig in sig_headers:
        m = re.search(r"\bd=([^;]+)", sig, re.IGNORECASE)
        if m:
            return _extract_domain_simple(m.group(1))
    return ""


def _verify_dkim_cryptographically(raw_email_bytes: bytes | None) -> Optional[bool]:
    if raw_email_bytes is None or dkim is None:
        return None

    try:
        valid = bool(dkim.verify(raw_email_bytes))
        return valid
    except Exception:
        return False




def verify_authentication(
    msg: EmailMessage,
    raw_email_bytes: bytes | None = None,
    smtp_ip: str | None = None,
) -> AdvancedAuthResults:
    from_header = msg.get("From", "") or msg.get("from", "") or ""
    return_path = msg.get("Return-Path", "") or msg.get("return-path", "") or ""

    from_domain = _extract_domain_from_addr(from_header)
    return_path_domain = _extract_domain_simple(return_path)

    auth_headers = msg.get_all("Authentication-Results", []) or []
    parsed_auth = _parse_authentication_results(auth_headers)

    dkim_domain = _extract_dkim_domain(msg)
    spf_domain = parsed_auth.get("spf_domain", "") or return_path_domain
    dmarc_domain = parsed_auth.get("dmarc_domain", "") or from_domain

    dkim_result = parsed_auth.get("dkim_result", "none").lower() or "none"
    spf_result = parsed_auth.get("spf_result", "none").lower() or "none"
    dmarc_result = parsed_auth.get("dmarc_result", "none").lower() or "none"
    dmarc_policy = parsed_auth.get("dmarc_policy", "")

    dkim_crypto = _verify_dkim_cryptographically(raw_email_bytes)

    res = AdvancedAuthResults(
        from_domain=from_domain,
        return_path_domain=return_path_domain,
        dkim_domain=dkim_domain,
        spf_domain=spf_domain,
        dmarc_domain=dmarc_domain,
        dkim_result=dkim_result,
        spf_result=spf_result,
        dmarc_result=dmarc_result,
        dmarc_policy=dmarc_policy,
        dkim_verified_cryptographically=dkim_crypto,
        smtp_ip=smtp_ip,
        alignment_issues=[],
    )

    def _aligned(child: str, parent: str) -> bool:
        if not child or not parent:
            return False
        if child == parent:
            return True
        return child.endswith("." + parent)

    if dkim_domain and from_domain:
        res.dkim_aligned = _aligned(dkim_domain, from_domain)
    if spf_domain and from_domain:
        res.spf_aligned = _aligned(spf_domain, from_domain)

    if dmarc_result.startswith("pass"):
        res.dmarc_aligned = bool(res.dkim_aligned or res.spf_aligned)
    else:
        res.dmarc_aligned = False

    if return_path_domain and from_domain and return_path_domain != from_domain:
        res.alignment_issues.append("RETURN_PATH_MISMATCH")

    if dkim_domain and from_domain and not _aligned(dkim_domain, from_domain):
        res.alignment_issues.append("DKIM_FROM_MISMATCH")

    if spf_domain and from_domain and not _aligned(spf_domain, from_domain):
        res.alignment_issues.append("SPF_FROM_MISMATCH")

    if dmarc_result.startswith("fail"):
        res.alignment_issues.append("DMARC_FAIL")

    if dkim_crypto is False:
        res.alignment_issues.append("DKIM_CRYPTO_FAIL")

    if dkim_result in ("fail", "softfail", "temperror", "permerror"):
        res.alignment_issues.append("DKIM_RESULT_FAIL")
    if spf_result in ("fail", "softfail", "temperror", "permerror"):
        res.alignment_issues.append("SPF_RESULT_FAIL")
    if dmarc_result in ("fail", "temperror", "permerror"):
        res.alignment_issues.append("DMARC_RESULT_FAIL")

    if from_domain and dkim_domain and not res.dkim_aligned:
        res.alignment_issues.append("DKIM_MISALIGNED")
    if from_domain and spf_domain and not res.spf_aligned:
        res.alignment_issues.append("SPF_MISALIGNED")

    if "none" in (dkim_result, spf_result, dmarc_result):
        res.alignment_issues.append("AUTH_PARTIAL_OR_NONE")

    res.alignment_issues = sorted(set(res.alignment_issues))

    return res
