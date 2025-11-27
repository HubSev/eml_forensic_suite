from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Any, Optional


@dataclass
class ForensicStats:
    total_emails: int
    distinct_senders: int
    date_min: Optional[str]
    date_max: Optional[str]

    per_folder: Dict[str, int]
    per_domain: Dict[str, int]

    total_with_attachments: int
    total_attachments: int

    dkim_counts: Dict[str, int]
    spf_counts: Dict[str, int]
    dmarc_counts: Dict[str, int]

    integrity_flag_counts: Dict[str, int]
    received_anomaly_counts: Dict[str, int]

    suspicion_level_counts: Dict[str, int]
    suspicion_score_min: Optional[int]
    suspicion_score_max: Optional[int]
    suspicion_score_avg: Optional[float]


def _extract_domain(from_header: str) -> str:
    if not from_header:
        return "(unknown)"

    candidate = from_header
    if "<" in candidate and ">" in candidate:
        try:
            candidate = candidate.split("<", 1)[1].split(">", 1)[0]
        except Exception:
            pass

    candidate = candidate.strip().strip('"').strip()

    if "@" not in candidate:
        return "(no-domain)"

    domain = candidate.split("@")[-1].strip().lower()
    if not domain:
        return "(no-domain)"

    return domain


def _parse_date_header(date_str: str) -> Optional[datetime]:
    if not date_str:
        return None

    candidates = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S",
        "%d %b %Y %H:%M:%S",
    ]

    for fmt in candidates:
        try:
            return datetime.strptime(date_str, fmt)
        except Exception:
            continue

    return None


def compute_forensic_stats(entries: List[Dict[str, Any]]) -> ForensicStats:

    total_emails = len(entries)
    if total_emails == 0:
        return ForensicStats(
            total_emails=0,
            distinct_senders=0,
            date_min=None,
            date_max=None,
            per_folder={},
            per_domain={},
            total_with_attachments=0,
            total_attachments=0,
            dkim_counts={},
            spf_counts={},
            dmarc_counts={},
            integrity_flag_counts={},
            received_anomaly_counts={},
            suspicion_level_counts={},
            suspicion_score_min=None,
            suspicion_score_max=None,
            suspicion_score_avg=None,
        )

    senders: List[str] = []
    folders: Counter[str] = Counter()
    domains: Counter[str] = Counter()

    dates: List[datetime] = []

    total_with_attachments = 0
    total_attachments = 0

    dkim_counts: Counter[str] = Counter()
    spf_counts: Counter[str] = Counter()
    dmarc_counts: Counter[str] = Counter()

    integrity_flag_counts: Counter[str] = Counter()
    received_anomaly_counts: Counter[str] = Counter()

    suspicion_level_counts: Counter[str] = Counter()
    suspicion_scores: List[int] = []

    for entry in entries:
        from_header = str(entry.get("from_header", "") or "")
        folder = str(entry.get("folder_imap", "") or "")
        date_header = str(entry.get("date_header", "") or "")

        senders.append(from_header)
        folders[folder] += 1

        domain = _extract_domain(from_header)
        domains[domain] += 1

        dt = _parse_date_header(date_header)
        if dt is not None:
            dates.append(dt)

        has_att = str(entry.get("has_attachments", "") or "")
        att_count_str = str(entry.get("attachment_count", "") or "")
        try:
            att_count = int(att_count_str)
        except Exception:
            att_count = 0

        if has_att in ("1", "true", "True"):
            total_with_attachments += 1
        total_attachments += max(att_count, 0)

        dkim = str(entry.get("dkim_result", "") or "").lower() or "none"
        spf = str(entry.get("spf_result", "") or "").lower() or "none"
        dmarc = str(entry.get("dmarc_result", "") or "").lower() or "none"

        dkim_counts[dkim] += 1
        spf_counts[spf] += 1
        dmarc_counts[dmarc] += 1

        flags_str = str(entry.get("integrity_flags", "") or "")
        if flags_str:
            for flag in flags_str.split(";"):
                f = flag.strip()
                if f:
                    integrity_flag_counts[f] += 1

        recv_str = str(entry.get("received_anomalies", "") or "")
        if recv_str:
            for flag in recv_str.split(";"):
                f = flag.strip()
                if f:
                    received_anomaly_counts[f] += 1

        score_str = str(entry.get("suspicion_score", "") or "").strip()
        if score_str:
            try:
                score_val = int(score_str)
                if score_val >= 0:
                    suspicion_scores.append(score_val)
            except Exception:
                pass

        level = str(entry.get("suspicion_level", "") or "").strip().upper()
        if level:
            suspicion_level_counts[level] += 1

    distinct_senders = len({s.strip() for s in senders if s.strip()})

    if dates:
        date_min = min(dates).isoformat()
        date_max = max(dates).isoformat()
    else:
        date_min = None
        date_max = None

    if suspicion_scores:
        suspicion_score_min = min(suspicion_scores)
        suspicion_score_max = max(suspicion_scores)
        suspicion_score_avg = sum(suspicion_scores) / len(suspicion_scores)
    else:
        suspicion_score_min = None
        suspicion_score_max = None
        suspicion_score_avg = None

    return ForensicStats(
        total_emails=total_emails,
        distinct_senders=distinct_senders,
        date_min=date_min,
        date_max=date_max,
        per_folder=dict(sorted(folders.items(), key=lambda kv: kv[0].lower())),
        per_domain=dict(sorted(domains.items(), key=lambda kv: kv[1], reverse=True)),
        total_with_attachments=total_with_attachments,
        total_attachments=total_attachments,
        dkim_counts=dict(dkim_counts),
        spf_counts=dict(spf_counts),
        dmarc_counts=dict(dmarc_counts),
        integrity_flag_counts=dict(integrity_flag_counts),
        received_anomaly_counts=dict(received_anomaly_counts),
        suspicion_level_counts=dict(suspicion_level_counts),
        suspicion_score_min=suspicion_score_min,
        suspicion_score_max=suspicion_score_max,
        suspicion_score_avg=suspicion_score_avg,
    )
