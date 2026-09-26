"""Shared pytest fixtures for the jolarca-runbooks tooling tests."""

from __future__ import annotations

from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from tools import load_schema, read_front_matter

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def validator() -> Draft202012Validator:
    """A JSON Schema validator for the runbook front-matter contract."""
    return Draft202012Validator(load_schema())


@pytest.fixture
def valid_front_matter() -> dict:
    """Front-matter from the valid fixture document."""
    front_matter, _ = read_front_matter(FIXTURES / "valid-runbook.md")
    assert front_matter is not None
    return front_matter


@pytest.fixture
def invalid_front_matter() -> dict:
    """Front-matter from the intentionally invalid fixture document."""
    front_matter, _ = read_front_matter(FIXTURES / "invalid-runbook.md")
    assert front_matter is not None
    return front_matter
