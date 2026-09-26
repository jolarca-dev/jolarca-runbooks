"""Markdown hygiene: verify every internal link resolves.

Style linting (headings, spacing, line length) is handled by markdownlint in pre-commit/CI. This
tool covers what markdownlint cannot: that relative links point at files that actually exist.

Usage:
    python -m tools.lint
"""

from __future__ import annotations

import re

from tools import iter_markdown_files, relative

_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`]*`")
_SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#", "//", "<")


def _strip_code(text: str) -> str:
    """Remove fenced and inline code so samples are not mistaken for real links."""
    text = _FENCE_RE.sub("", text)
    return _INLINE_CODE_RE.sub("", text)


def _link_targets(text: str) -> list[str]:
    targets = []
    for match in _LINK_RE.finditer(_strip_code(text)):
        target = match.group(1).strip()
        if target.startswith(_SKIP_PREFIXES):
            continue
        targets.append(target)
    return targets


def main(argv: list[str] | None = None) -> int:
    """Entry point. Returns a process exit code."""
    _ = argv  # the link check always scans the whole repository
    failures: list[str] = []
    scanned = 0
    for path in iter_markdown_files():
        scanned += 1
        base = path.parent
        text = path.read_text(encoding="utf-8")
        for target in _link_targets(text):
            file_part = target.split("#", 1)[0].strip()
            if not file_part:
                continue
            if not (base / file_part).resolve().exists():
                failures.append(f"{relative(path)}: broken link -> {target}")

    if failures:
        print("Markdown link check FAILED:")
        for failure in failures:
            print(f"  - {failure}")
        print(f"\n{len(failures)} broken link(s); {scanned} file(s) scanned.")
        return 1

    print(f"Markdown link check passed: {scanned} file(s) scanned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
