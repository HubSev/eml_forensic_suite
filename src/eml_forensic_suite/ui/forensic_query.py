from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import shlex

from PySide6.QtCore import QSortFilterProxyModel, QModelIndex

from eml_forensic_suite.ui.index_model import IndexTableModel


@dataclass
class ForensicQueryTerm:
    field: str | None
    value: str
    negated: bool = False

@dataclass
class ForensicQueryExpr:
    op: str
    term: Optional[ForensicQueryTerm] = None
    left: Optional["ForensicQueryExpr"] = None
    right: Optional["ForensicQueryExpr"] = None


def parse_forensic_query(text: str) -> Optional[ForensicQueryExpr]:

    normalized = (
        text.replace("(", " ( ")
        .replace(")", " ) ")
        .strip()
    )
    if not normalized:
        return None

    tokens = shlex.split(normalized)

    class TokenStream:
        def __init__(self, toks: list[str]) -> None:
            self.toks = toks
            self.pos = 0

        def peek(self) -> str | None:
            if self.pos >= len(self.toks):
                return None
            return self.toks[self.pos]

        def next(self) -> str | None:
            tok = self.peek()
            if tok is not None:
                self.pos += 1
            return tok

        def eof(self) -> bool:
            return self.pos >= len(self.toks)

    stream = TokenStream(tokens)

    known_fields = {
        "from",
        "to",
        "cc",
        "subject",
        "hash",
        "folder",
        "domain",
        "attachment",
        "date",
    }

    def parse_expr() -> Optional[ForensicQueryExpr]:
        return parse_or()

    def parse_or() -> Optional[ForensicQueryExpr]:
        left = parse_and()
        if left is None:
            return None
        while True:
            tok = stream.peek()
            if tok is None:
                break
            if tok.lower() == "or":
                stream.next()
                right = parse_and()
                if right is None:
                    break
                left = ForensicQueryExpr(op="OR", left=left, right=right)
            else:
                break
        return left

    def parse_and() -> Optional[ForensicQueryExpr]:
        left = parse_unary()
        if left is None:
            return None

        while True:
            tok = stream.peek()
            if tok is None:
                break
            low = tok.lower()

            if low == "and":
                stream.next()
                right = parse_unary()
                if right is None:
                    break
                left = ForensicQueryExpr(op="AND", left=left, right=right)
                continue

            if low == "or" or tok == ")":
                break

            right = parse_unary()
            if right is None:
                break
            left = ForensicQueryExpr(op="AND", left=left, right=right)

        return left

    def parse_unary() -> Optional[ForensicQueryExpr]:
        tok = stream.peek()
        if tok is None:
            return None

        if tok.lower() == "not":
            stream.next()
            child = parse_unary()
            if child is None:
                return None
            return ForensicQueryExpr(op="NOT", left=child)

        return parse_primary()

    def parse_primary() -> Optional[ForensicQueryExpr]:
        tok = stream.peek()
        if tok is None:
            return None

        if tok == "(":
            stream.next()
            inner = parse_expr()
            if stream.peek() == ")":
                stream.next()
            return inner

        stream.next()
        raw = tok
        field: str | None = None
        value = raw

        if ":" in raw:
            prefix, val = raw.split(":", 1)
            if prefix.lower() in known_fields:
                field = prefix.lower()
                value = val

        term = ForensicQueryTerm(
            field=field,
            value=value.lower(),
            negated=False,
        )
        return ForensicQueryExpr(op="TERM", term=term)

    expr = parse_expr()

    return expr


class ForensicFilterProxyModel(QSortFilterProxyModel):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._expr: Optional[ForensicQueryExpr] = None

    def set_query_text(self, text: str) -> None:
        self._expr = parse_forensic_query(text)
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        if self._expr is None:
            return True

        model = self.sourceModel()
        if not isinstance(model, IndexTableModel):
            return super().filterAcceptsRow(source_row, source_parent)

        row = model.row_at(source_row)
        if row is None:
            return False

        return self._eval_expr(row, self._expr)


    def _eval_expr(self, row: dict[str, Any], expr: ForensicQueryExpr) -> bool:
        op = expr.op.upper()

        if op == "TERM":
            if expr.term is None:
                return True
            return self._term_matches(row, expr.term)

        if op == "NOT":
            if expr.left is None:
                return True
            return not self._eval_expr(row, expr.left)

        if op == "AND":
            left = self._eval_expr(row, expr.left) if expr.left is not None else True
            right = self._eval_expr(row, expr.right) if expr.right is not None else True
            return left and right

        if op == "OR":
            left = self._eval_expr(row, expr.left) if expr.left is not None else False
            right = self._eval_expr(row, expr.right) if expr.right is not None else False
            return left or right

        return True



    def _term_matches(self, row: dict[str, Any], term: ForensicQueryTerm) -> bool:
        val = term.value

        def col(name: str) -> str:
            return str(row.get(name, "")).lower()

        if term.field == "from":
            return val in col("from_header")
        if term.field == "to":
            return val in col("to_header")
        if term.field == "cc":
            return val in (col("cc_header") + " " + col("cci_header"))
        if term.field == "subject":
            return val in col("subject")
        if term.field == "hash":
            return val in col("sha256")
        if term.field == "folder":
            return val in col("folder_imap")
        if term.field == "date":
            return val in col("date_header")
        if term.field == "domain":
            from_h = col("from_header")
            return (
                f"@{val}" in from_h
                or from_h.endswith(val)
                or f"{val}>" in from_h
                or f"{val})" in from_h
            )
        if term.field == "attachment":
            v_bool = val in {"1", "true", "yes", "oui"}
            has_attach = (
                col("has_attachments") in {"1", "true", "yes"}
                or col("attachment_count") not in {"", "0", "0.0"}
            )
            return has_attach == v_bool

        haystack_cols = [
            "subject",
            "from_header",
            "to_header",
            "cc_header",
            "cci_header",
            "attachment_filenames",
            "filename",
            "sha256",
        ]
        for name in haystack_cols:
            if val in col(name):
                return True

        return False
