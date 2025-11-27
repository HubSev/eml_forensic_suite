from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from email.message import EmailMessage
from ipaddress import ip_address
from typing import List, Optional
import re


@dataclass
class ReceivedHop:

    index: int
    raw: str
    ip: Optional[str] = None
    from_host: str = ""
    by_host: str = ""
    date_str: str = ""
    parsed_date: Optional[datetime] = None

    is_private_ip: bool = False
    is_localhost: bool = False
    suspect_reasons: List[str] = field(default_factory=list)


@dataclass
class ReceivedAnalysisResult:

    hop_count: int
    hops: List[ReceivedHop] = field(default_factory=list)
    anomalies: List[str] = field(default_factory=list)




def _parse_received_header(raw: str, index: int) -> ReceivedHop:
    hop = ReceivedHop(index=index, raw=raw)

    m_ip = re.search(r"(\d{1,3}(?:\.\d{1,3}){3})", raw)
    if m_ip:
        ip_str = m_ip.group(1)
        hop.ip = ip_str
        try:
            ip_obj = ip_address(ip_str)
            hop.is_private_ip = bool(
                ip_obj.is_private or ip_obj.is_link_local
            )
            hop.is_localhost = bool(ip_obj.is_loopback)
        except ValueError:
            hop.is_private_ip = False
            hop.is_localhost = False

    m_from = re.search(r"\bfrom\s+([^\s]+)", raw, re.IGNORECASE)
    if m_from:
        hop.from_host = m_from.group(1)

    m_by = re.search(r"\bby\s+([^\s]+)", raw, re.IGNORECASE)
    if m_by:
        hop.by_host = m_by.group(1)

    if ";" in raw:
        hop.date_str = raw.rsplit(";", 1)[-1].strip()

        for fmt in (
            "%a, %d %b %Y %H:%M:%S %z",
            "%d %b %Y %H:%M:%S %z",
            "%a, %d %b %Y %H:%M:%S",
            "%d %b %Y %H:%M:%S",
        ):
            try:
                hop.parsed_date = datetime.strptime(hop.date_str, fmt)
                break
            except Exception:
                continue

    lower = raw.lower()
    if "localhost" in lower or "127.0.0.1" in lower:
        hop.suspect_reasons.append("LOCALHOST")
        hop.is_localhost = True
    if "unknown" in lower:
        hop.suspect_reasons.append("UNKNOWN_HOST")

    return hop




def analyze_received_chain(msg: EmailMessage) -> ReceivedAnalysisResult:
    headers = msg.get_all("Received", []) or []
    if not headers:
        return ReceivedAnalysisResult(hop_count=0, hops=[], anomalies=["NO_RECEIVED"])

    hops: List[ReceivedHop] = []
    for idx, raw in enumerate(headers):
        hop = _parse_received_header(raw, index=idx)
        hops.append(hop)

    anomalies: List[str] = []
    hop_count = len(hops)

    if hop_count > 30:
        anomalies.append("MANY_HOPS")

    dates = [h.parsed_date for h in hops if h.parsed_date is not None]
    if len(dates) >= 2:
        for current, nxt in zip(dates, dates[1:]):
            if current is not None and nxt is not None and nxt > current:
                anomalies.append("RECEIVED_CHRONO_INCONSISTENT")
                break

    for hop in hops:
        if "LOCALHOST" in hop.suspect_reasons or hop.is_localhost:
            anomalies.append("RECEIVED_LOCALHOST")
            break

    for hop in hops:
        if "UNKNOWN_HOST" in hop.suspect_reasons:
            anomalies.append("RECEIVED_UNKNOWN_HOST")
            break

    for hop in hops:
        if hop.is_private_ip and hop.from_host:
            lower = hop.from_host.lower()
            if "." in lower and "localhost" not in lower:
                anomalies.append("RECEIVED_PRIVATE_IP_EXTERNAL")
                break

    anomalies = sorted(set(anomalies))

    return ReceivedAnalysisResult(
        hop_count=hop_count,
        hops=hops,
        anomalies=anomalies,
    )



def extract_client_ip(hops: List[ReceivedHop]) -> Optional[str]:
    if not hops:
        return None

    for hop in reversed(hops):
        if hop.ip and not hop.is_private_ip and not hop.is_localhost:
            return hop.ip

    for hop in reversed(hops):
        if hop.ip:
            return hop.ip

    return None
