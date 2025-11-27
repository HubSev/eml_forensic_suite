from __future__ import annotations

from dataclasses import dataclass
from email.message import EmailMessage
from typing import List, Dict, Any, Optional

from .attachments import extract_attachments, AttachmentInfo
from .received_analysis import (
    analyze_received_chain as analyze_received_chain_adv,
    extract_client_ip,
    ReceivedAnalysisResult,
)
from .authentication_verifier import (
    verify_authentication,
    AdvancedAuthResults,
)
from .integrity_checker import (
    check_message_integrity,
    MessageIntegrityResult,
)
from .scoring import (
    compute_suspicion_score,
    SuspicionScore,
)


@dataclass
class EmailAnalysisResult:

    has_attachments: bool
    attachment_count: int
    attachment_filenames: str

    dkim_result: str
    spf_result: str
    dmarc_result: str
    auth_comment: str

    received_count: int
    received_anomalies: str
    integrity_flags: str

    advanced_auth: Optional[AdvancedAuthResults] = None
    advanced_received: Optional[ReceivedAnalysisResult] = None
    advanced_integrity: Optional[MessageIntegrityResult] = None

    suspicion_score: int = 0
    suspicion_level: str = ""
    suspicion_reasons: str = ""




def _analyze_authentication_simple(msg: EmailMessage) -> tuple[str, str, str, str]:
    auth_headers = msg.get_all("Authentication-Results", [])
    if not auth_headers:
        return "none", "none", "none", ""

    joined = "\n".join(auth_headers)

    def extract_result(token: str) -> str:
        lower = joined.lower()
        idx = lower.find(token + "=")
        if idx == -1:
            return "none"
        after = lower[idx + len(token) + 1 :]
        first = after.split()[0].strip(";,")
        return first or "unknown"

    dkim = extract_result("dkim")
    spf = extract_result("spf")
    dmarc = extract_result("dmarc")

    comment = joined
    if len(comment) > 200:
        comment = comment[:200] + "..."

    return dkim, spf, dmarc, comment




def _analyze_attachments(msg: EmailMessage) -> tuple[bool, int, str, List[AttachmentInfo]]:
    infos_with_data = extract_attachments(msg)
    infos: List[AttachmentInfo] = [info for info, _ in infos_with_data]

    has_attachments = len(infos) > 0
    count = len(infos)
    names = ";".join(info.filename for info in infos) if infos else ""

    return has_attachments, count, names, infos




def _analyze_received_basic(msg: EmailMessage) -> tuple[int, str]:
    received_headers = msg.get_all("Received", [])
    received_count = len(received_headers)
    anomalies: List[str] = []

    if received_count == 0:
        anomalies.append("NO_RECEIVED")

    if received_count > 30:
        anomalies.append("MANY_HOPS")

    return received_count, ";".join(anomalies)




def _analyze_basic_integrity(msg: EmailMessage) -> str:
    flags: List[str] = []

    if not (msg.get("Date") or msg.get("date")):
        flags.append("MISSING_DATE")

    if not (msg.get("From") or msg.get("from")):
        flags.append("MISSING_FROM")

    if not (msg.get("Message-ID") or msg.get("Message-Id") or msg.get("message-id")):
        flags.append("MISSING_MESSAGE_ID")

    return ";".join(flags)




def analyze_email(msg: EmailMessage, raw_email_bytes: bytes | None = None) -> EmailAnalysisResult:
    has_att, att_count, att_names, attachment_infos = _analyze_attachments(msg)

    dkim_simple, spf_simple, dmarc_simple, auth_comment = _analyze_authentication_simple(msg)

    received_count_basic, received_anomalies_basic = _analyze_received_basic(msg)
    integrity_basic = _analyze_basic_integrity(msg)

    advanced_received: Optional[ReceivedAnalysisResult] = None
    advanced_auth: Optional[AdvancedAuthResults] = None
    advanced_integrity: Optional[MessageIntegrityResult] = None
    suspicion_score_val: int = 0
    suspicion_level: str = ""
    suspicion_reasons_str: str = ""

    try:
        advanced_received = analyze_received_chain_adv(msg)
        smtp_ip = extract_client_ip(advanced_received.hops)

        advanced_auth = verify_authentication(
            msg,
            raw_email_bytes=raw_email_bytes,
            smtp_ip=smtp_ip,
        )

        advanced_integrity = check_message_integrity(
            msg,
            received_analysis=advanced_received,
            auth_results=advanced_auth,
        )

        idx_like: Dict[str, Any] = {
            "from_header": msg.get("From", "") or msg.get("from", ""),
            "subject": msg.get("Subject", "") or msg.get("subject", ""),
            "date_header": msg.get("Date", "") or msg.get("date", ""),
        }

        score_obj: SuspicionScore = compute_suspicion_score(
            index_entry=idx_like,
            auth=advanced_auth,
            received=advanced_received,
            integrity=advanced_integrity,
            attachments=attachment_infos,
        )

        suspicion_score_val = int(score_obj.score)
        suspicion_level = score_obj.level
        suspicion_reasons_str = ";".join(score_obj.reasons)

    except Exception as e:
        suspicion_score_val = 0
        suspicion_level = "ERROR"
        suspicion_reasons_str = f"advanced_analysis_error:{type(e).__name__}"


    received_flags: List[str] = []
    if received_anomalies_basic:
        received_flags.extend(
            f.strip() for f in received_anomalies_basic.split(";") if f.strip()
        )
    if advanced_received is not None and advanced_received.anomalies:
        received_flags.extend(advanced_received.anomalies)
    received_flags = sorted(set(received_flags))
    received_anomalies_merged = ";".join(received_flags)

    integrity_flags_list: List[str] = []
    if integrity_basic:
        integrity_flags_list.extend(
            f.strip() for f in integrity_basic.split(";") if f.strip()
        )
    if advanced_integrity is not None and advanced_integrity.flags:
        integrity_flags_list.extend(advanced_integrity.flags)
    integrity_flags_list = sorted(set(integrity_flags_list))
    integrity_flags_merged = ";".join(integrity_flags_list)

    return EmailAnalysisResult(
        has_attachments=has_att,
        attachment_count=att_count,
        attachment_filenames=att_names,
        dkim_result=dkim_simple,
        spf_result=spf_simple,
        dmarc_result=dmarc_simple,
        auth_comment=auth_comment,
        received_count=received_count_basic,
        received_anomalies=received_anomalies_merged,
        integrity_flags=integrity_flags_merged,
        advanced_auth=advanced_auth,
        advanced_received=advanced_received,
        advanced_integrity=advanced_integrity,
        suspicion_score=suspicion_score_val,
        suspicion_level=suspicion_level,
        suspicion_reasons=suspicion_reasons_str,
    )
