"""Shared helpers for the jolarca-runbooks docs-as-code tooling."""

from __future__ import annotations

import json
import re
from collections.abc import Iterator
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas" / "runbook-frontmatter.schema.json"

SKIP_DIRS = {
    ".git",
    ".idea",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    "node_modules",
    "venv",
}

_FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)


def repo_root() -> Path:
    """Absolute path to the repository root."""
    return REPO_ROOT


def iter_markdown_files(root: Path | None = None) -> Iterator[Path]:
    """Yield every Markdown file under *root*, skipping vendored and tooling dirs."""
    base = root or REPO_ROOT
    for path in sorted(base.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def parse_front_matter(text: str) -> tuple[dict | None, str]:
    """Split a document into (front_matter_mapping_or_None, body)."""
    match = _FRONT_MATTER_RE.match(text)
    if match is None:
        return None, text
    data = yaml.safe_load(match.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError("front-matter must be a YAML mapping")
    return data, text[match.end():]


def read_front_matter(path: Path) -> tuple[dict | None, str]:
    """Read *path* and split it into (front_matter_or_None, body)."""
    return parse_front_matter(path.read_text(encoding="utf-8"))


def load_schema() -> dict:
    """Load the runbook front-matter JSON Schema."""
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def relative(path: Path) -> str:
    """POSIX-style path relative to the repo root (falls back to the given path)."""
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()
