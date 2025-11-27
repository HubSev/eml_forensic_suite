from __future__ import annotations

import os
import hashlib
import mimetypes
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional
from datetime import datetime

from email.message import EmailMessage

from eml_forensic_suite.core.common_utils import VERSION


@dataclass
class AttachmentInfo:
    filename: str
    mime_type: str
    size: int
    sha256: str
    is_suspicious: bool
    suspicion_flags: str


def sha256_bytes(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def guess_mime(filename: str, data: bytes) -> str:
    mime, _ = mimetypes.guess_type(filename)
    if mime:
        return mime

    if data.startswith(b"%PDF"):
        return "application/pdf"
    if data[:4] in (b"\xFF\xD8\xFF\xE0", b"\xFF\xD8\xFF\xE1"):
        return "image/jpeg"
    if data.startswith(b"\x89PNG"):
        return "image/png"

    return "application/octet-stream"


def analyze_attachment(filename: str, data: bytes) -> AttachmentInfo:
    mime_detected = guess_mime(filename, data)
    sha = sha256_bytes(data)
    size = len(data)

    suspicious: List[str] = []
    ext = filename.lower().split(".")[-1] if "." in filename else ""

    if not filename:
        suspicious.append("NO_FILENAME")

    if "." not in filename:
        suspicious.append("NO_EXTENSION")

    if filename.count(".") >= 2:
        suspicious.append("DOUBLE_EXT")

    if ext == "pdf" and mime_detected != "application/pdf":
        suspicious.append("EXT_MISMATCH")

    if ext in ("jpg", "jpeg", "png") and not mime_detected.startswith("image/"):
        suspicious.append("EXT_MISMATCH")

    if mime_detected == "application/octet-stream" and ext in ("pdf", "docx", "xlsx"):
        suspicious.append("LOW_QUALITY_MIME")

    if size == 0:
        suspicious.append("EMPTY_FILE")

    return AttachmentInfo(
        filename=filename or "(no-name)",
        mime_type=mime_detected,
        size=size,
        sha256=sha,
        is_suspicious=bool(suspicious),
        suspicion_flags=";".join(suspicious),
    )


def extract_attachments(msg: EmailMessage) -> List[Tuple[AttachmentInfo, bytes]]:
    results: List[Tuple[AttachmentInfo, bytes]] = []

    if not msg.is_multipart():
        return results

    for part in msg.walk():
        if part is msg:
            continue

        disposition = part.get_content_disposition()
        if disposition not in ("attachment", "inline"):
            continue

        filename = part.get_filename() or "(no-name)"
        try:
            data = part.get_payload(decode=True) or b""
        except Exception:
            data = b""

        info = analyze_attachment(filename, data)
        results.append((info, data))

    return results


def _write_attachment_report(
    out_dir: str,
    info: AttachmentInfo,
    email_entry: Optional[Dict[str, str]],
    msg_id: str,
) -> None:
    report_name = f"{info.filename}.forensic_report.txt"
    report_path = os.path.join(out_dir, report_name)

    lines: List[str] = []
    lines.append("EML Forensic Suite - Attachment Extraction Report")
    lines.append(f"Tool version      : {VERSION}")
    lines.append(f"Extraction time   : {datetime.now().isoformat(timespec='seconds')}")
    lines.append("")

    lines.append("[Email metadata]")
    lines.append(f"Message-ID        : {msg_id}")
    if email_entry:
        lines.append(f"IMAP folder       : {email_entry.get('folder_imap', '')}")
        lines.append(f"Sequence number   : {email_entry.get('sequence_number', '')}")
        lines.append(f"Date header       : {email_entry.get('date_header', '')}")
        lines.append(f"From              : {email_entry.get('from_header', '')}")
        lines.append(f"To                : {email_entry.get('to_header', '')}")
        lines.append(f"Subject           : {email_entry.get('subject', '')}")
        lines.append(f"EML SHA-256       : {email_entry.get('sha256', '')}")
        lines.append(f"Relative path     : {email_entry.get('relative_path', '')}")
        lines.append(f"Filename          : {email_entry.get('filename', '')}")
    lines.append("")

    lines.append("[Attachment metadata]")
    lines.append(f"Filename          : {info.filename}")
    lines.append(f"MIME type         : {info.mime_type}")
    lines.append(f"Size (bytes)      : {info.size}")
    lines.append(f"SHA-256           : {info.sha256}")
    lines.append(f"Suspicious?       : {info.is_suspicious}")
    lines.append(f"Suspicion flags   : {info.suspicion_flags}")
    lines.append("")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def save_attachment(
    root_dir: str,
    subfolder: str,
    info: AttachmentInfo,
    data: bytes,
    *,
    email_entry: Optional[Dict[str, str]] = None,
    msg_id: str = "",
) -> str:
    out_dir = os.path.join(root_dir, "forensic_attachments", subfolder)
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, info.filename)

    with open(out_path, "wb") as f:
        f.write(data)

    _write_attachment_report(out_dir, info, email_entry, msg_id)

    return out_path
