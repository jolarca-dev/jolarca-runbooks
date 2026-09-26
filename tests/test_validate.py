"""Tests for the front-matter validator and supporting tools."""

from __future__ import annotations

from tools import lint, render, validate
from tools.control_map import _split


def test_valid_front_matter_passes(validator, valid_front_matter):
    assert validate.validation_errors(valid_front_matter, validator) == []


def test_invalid_front_matter_is_rejected(validator, invalid_front_matter):
    errors = validate.validation_errors(invalid_front_matter, validator)
    assert errors, "the invalid fixture must produce at least one error"
    joined = " ".join(errors)
    assert "review_due" in joined
    assert "related_controls" in joined


def test_repository_front_matter_is_valid():
    # Integration check: every committed document must satisfy the contract.
    assert validate.main([]) == 0


def test_link_targets_skips_external_and_code():
    text = "See [docs](docs/index.md) and [site](https://example.com) plus `x](y)`."
    targets = lint._link_targets(text)
    assert "docs/index.md" in targets
    assert "https://example.com" not in targets
    assert all("y" not in target for target in targets)


def test_control_split_maps_framework_names():
    framework, name = _split("ISO27001:A.5.29")
    assert framework == "ISO/IEC 27001:2022"
    assert name == "A.5.29"


def test_render_runbooks_readme_is_deterministic():
    first = render._runbooks_readme()
    second = render._runbooks_readme()
    assert first == second
    assert first.startswith("<!-- GENERATED")
