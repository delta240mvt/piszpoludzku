#!/usr/bin/env python3
"""Conservative, explainable audit for Polish prose in Markdown or plain text."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0"
EXCERPT_LIMIT = 160
CONTRAST_PATTERN = re.compile(
    r"\bnie\s+(?:chodzi\s+o|jest|oznacza)\b[^.?!]{0,120}[.?!]\s*(?:chodzi\s+o|jest|oznacza)\b",
    re.IGNORECASE,
)
META_PATTERN = re.compile(r"\b(?:w tej (?:części|sekcji)|poniżej (?:pokażę|opisuję)|teraz (?:pokażę|omówię))\b", re.IGNORECASE)
EMPHASIS_PATTERN = re.compile(r"\b(?:kluczow\w*|fundamentaln\w*|przełomow\w*|ważn\w*)\b", re.IGNORECASE)
FENCE_PATTERN = re.compile(r"^\s*(`{3,}|~{3,})")
LINK_DEFINITION_PATTERN = re.compile(r"^\s*\[[^\]]+\]:\s*\S+")
INLINE_CODE_PATTERN = re.compile(r"`[^`]*`")
URL_PATTERN = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
HTML_COMMENT_PATTERN = re.compile(r"<!--.*?-->")


def _normalize(value: str) -> str:
    return unicodedata.normalize("NFC", value).casefold()


def _excerpt(line: str) -> str:
    clean = line.strip()
    return clean if len(clean) <= EXCERPT_LIMIT else clean[: EXCERPT_LIMIT - 1].rstrip() + "…"


def _finding(rule_id: str, line_no: int, column: int, severity: str, category: str, line: str, message: str) -> dict[str, Any]:
    return {
        "rule_id": rule_id,
        "line": line_no,
        "column": max(1, column),
        "severity": severity,
        "category": category,
        "excerpt": _excerpt(line),
        "message": message,
    }


def _prose_lines(text: str) -> tuple[list[tuple[int, str]], list[dict[str, Any]]]:
    lines = text.splitlines()
    prose: list[tuple[int, str]] = []
    findings: list[dict[str, Any]] = []
    in_frontmatter = bool(lines and lines[0].lstrip("\ufeff").strip() == "---")
    fence: str | None = None
    comment_open = False

    for index, raw_line in enumerate(lines, start=1):
        line = raw_line.lstrip("\ufeff") if index == 1 else raw_line
        if in_frontmatter:
            if index > 1 and line.strip() == "---":
                in_frontmatter = False
            continue

        fence_match = FENCE_PATTERN.match(line)
        if fence:
            if fence_match and fence_match.group(1)[0] == fence[0] and len(fence_match.group(1)) >= len(fence):
                fence = None
            continue
        if fence_match:
            fence = fence_match.group(1)
            continue

        if "<!--" in line and "-->" not in line:
            comment_open = True
        if comment_open:
            if "-->" in line:
                comment_open = False
            continue

        stripped = line.strip()
        if not stripped or stripped.startswith("|") or LINK_DEFINITION_PATTERN.match(line):
            continue
        cleaned = HTML_COMMENT_PATTERN.sub("", line)
        cleaned = INLINE_CODE_PATTERN.sub("", cleaned)
        cleaned = URL_PATTERN.sub("", cleaned)
        if cleaned.strip():
            prose.append((index, cleaned))

    if fence:
        findings.append(
            _finding(
                "markdown-unclosed-fence",
                len(lines) or 1,
                1,
                "error",
                "integralność-markdown",
                lines[-1] if lines else "",
                "Blok kodu Markdown nie ma zamykającego ogrodzenia.",
            )
        )
    return prose, findings


def _first_location(matches: list[tuple[int, str]], pattern: re.Pattern[str]) -> tuple[int, int, str]:
    for line_no, line in matches:
        match = pattern.search(line)
        if match:
            return line_no, match.start() + 1, line
    return 1, 1, ""


def audit_text(text: str, source: str = "<memory>") -> dict[str, Any]:
    """Return an explainable report. It never changes text or assigns authorship."""
    prose, findings = _prose_lines(text)
    normalized = [(line_no, _normalize(line)) for line_no, line in prose]

    contrast_locations = [(line_no, line) for line_no, line in normalized if CONTRAST_PATTERN.search(line)]
    if len(contrast_locations) >= 3:
        line_no, column, line = _first_location(contrast_locations, CONTRAST_PATTERN)
        findings.append(
            _finding(
                "serial-contrast",
                line_no,
                column,
                "notice",
                "powtarzalny-kontrast",
                line,
                "W dokumencie powtarza się konstrukcja kontrastowa; sprawdź, czy każda odsłona wnosi nową różnicę.",
            )
        )

    meta_locations = [(line_no, line) for line_no, line in normalized if META_PATTERN.search(line)]
    if len(meta_locations) >= 3:
        line_no, column, line = _first_location(meta_locations, META_PATTERN)
        findings.append(
            _finding(
                "serial-meta-commentary",
                line_no,
                column,
                "notice",
                "metakomentarz",
                line,
                "W tekście często pojawia się zapowiadanie struktury; sprawdź, czy można przejść od razu do treści.",
            )
        )

    emphasis_locations = [(line_no, line) for line_no, line in normalized if EMPHASIS_PATTERN.search(line)]
    emphasis_count = sum(len(EMPHASIS_PATTERN.findall(line)) for _, line in normalized)
    if emphasis_count >= 3 and emphasis_locations:
        line_no, column, line = _first_location(emphasis_locations, EMPHASIS_PATTERN)
        findings.append(
            _finding(
                "empty-emphasis-series",
                line_no,
                column,
                "notice",
                "puste-wzmocnienie",
                line,
                "Wzmocnienia występują seryjnie; sprawdź, czy można je zastąpić konkretnym skutkiem albo usunąć.",
            )
        )

    headings = Counter()
    heading_lines: dict[str, tuple[int, str]] = {}
    for line_no, line in prose:
        heading = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", line)
        if heading:
            key = _normalize(heading.group(1))
            headings[key] += 1
            heading_lines.setdefault(key, (line_no, line))
    for heading, count in sorted(headings.items()):
        if count >= 3:
            line_no, line = heading_lines[heading]
            findings.append(
                _finding(
                    "repeated-heading",
                    line_no,
                    line.find("#") + 1,
                    "notice",
                    "powtarzalny-szablon",
                    line,
                    "Ten sam nagłówek występuje wielokrotnie; sprawdź, czy to celowy szablon czy mechaniczne powtórzenie.",
                )
            )

    findings.sort(key=lambda item: (item["line"], item["column"], item["rule_id"]))
    severity_counts = Counter(item["severity"] for item in findings)
    return {
        "schema_version": SCHEMA_VERSION,
        "source": source,
        "summary": {
            "findings": len(findings),
            "errors": severity_counts.get("error", 0),
            "notices": severity_counts.get("notice", 0),
        },
        "findings": findings,
    }


def _render_text(report: dict[str, Any]) -> str:
    lines = [f"Audyt: {report['source']}", f"Uwagi: {report['summary']['findings']}"]
    for item in report["findings"]:
        lines.append(f"{item['severity'].upper()} {item['rule_id']} L{item['line']}:C{item['column']}: {item['message']}")
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audytuje polską prozę bez przypisywania autorstwa.")
    parser.add_argument("path", type=Path, help="Plik .md lub .txt do audytu")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--output", type=Path, help="Opcjonalny plik raportu")
    parser.add_argument("--fail-on", choices=("error",), help="Zwraca kod 3, gdy raport zawiera wskazany poziom")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.output and (
            args.output.resolve() == args.path.resolve()
            or (args.output.exists() and args.output.samefile(args.path))
        ):
            print("Raport musi mieć inną ścieżkę niż tekst źródłowy.", file=sys.stderr)
            return 1
        text = args.path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as error:
        print(f"Błąd odczytu pliku: {error}", file=sys.stderr)
        return 1

    report = audit_text(text, str(args.path))
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n" if args.format == "json" else _render_text(report)
    try:
        if args.output:
            args.output.write_text(rendered, encoding="utf-8")
        else:
            print(rendered, end="")
    except OSError as error:
        print(f"Błąd zapisu raportu: {error}", file=sys.stderr)
        return 1

    if args.fail_on == "error" and report["summary"]["errors"]:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
