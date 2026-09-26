"""Validate runbook front-matter against the JSON Schema.

Usage:
    python -m tools.validate [path ...]

Walks the repository (or the given paths), validates every Markdown file that declares YAML
front-matter, and asserts that runbooks outside ``_templates/`` declare front-matter. Exits
non-zero if anything fails so it can gate CI.
"""

from __future__ import annotations

import datetime
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from tools import iter_markdown_files, load_schema, read_front_matter, relative


def _coerce_dates(data: dict) -> dict:
    """YAML parses unquoted ISO dates as date objects; the schema expects strings."""
    coerced = {}
    for key, value in data.items():
        if isinstance(value, (datetime.date, datetime.datetime)):
            coerced[key] = value.isoformat()
        else:
            coerced[key] = value
    return coerced


def validation_errors(front_matter: dict, validator: Draft202012Validator) -> list[str]:
    """Return human-readable validation errors for *front_matter* (empty when valid)."""
    data = _coerce_dates(front_matter)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    messages = []
    for err in errors:
        location = "/".join(str(part) for part in err.path) or "<root>"
        messages.append(f"{location}: {err.message}")
    return messages


def _requires_front_matter(path: Path) -> bool:
    rel = relative(path)
    if not rel.startswith("runbooks/"):
        return False
    if rel == "runbooks/README.md" or "_templates/" in rel:
        return False
    return True


def _is_excluded(path: Path) -> bool:
    rel = relative(path)
    return rel.startswith("tests/") or "_templates/" in rel


def main(argv: list[str] | None = None) -> int:
    """Entry point. Returns a process exit code."""
    args = list(sys.argv[1:] if argv is None else argv)
    validator = Draft202012Validator(load_schema())
    files = [Path(item) for item in args] if args else list(iter_markdown_files())

    failures: list[str] = []
    checked = 0
    for path in files:
        if _is_excluded(path):
            continue
        front_matter, _ = read_front_matter(path)
        if front_matter is None:
            if _requires_front_matter(path):
                failures.append(f"{relative(path)}: missing required YAML front-matter")
            continue
        checked += 1
        for message in validation_errors(front_matter, validator):
            failures.append(f"{relative(path)}: {message}")

    if failures:
        print("Front-matter validation FAILED:")
        for failure in failures:
            print(f"  - {failure}")
        print(f"\n{len(failures)} problem(s); {checked} document(s) checked.")
        return 1

    print(f"Front-matter validation passed: {checked} document(s) checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
