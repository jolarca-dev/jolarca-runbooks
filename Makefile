.DEFAULT_GOAL := help
PY ?= $(shell if [ -x .venv/bin/python ]; then echo .venv/bin/python; else echo python3; fi)

.PHONY: help install lint validate render control-map test drift ci clean

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

install:  ## Install dev dependencies (editable)
	$(PY) -m pip install -e ".[dev]"
	$(PY) -m pre_commit install

lint:  ## Python lint (ruff) + Markdown internal-link check
	$(PY) -m ruff check tools tests
	$(PY) -m ruff format --check tools tests
	$(PY) -m tools.lint

validate:  ## Validate runbook front-matter against the JSON schema
	$(PY) -m tools.validate

render:  ## Regenerate catalogs (runbooks/README.md, docs/index.md)
	$(PY) -m tools.render

control-map:  ## Regenerate docs/compliance/control-mapping.md
	$(PY) -m tools.control_map

test:  ## Run the test suite
	$(PY) -m pytest

drift: render control-map  ## Fail if generated catalogs or the control map are stale
	@git diff --exit-code runbooks/README.md docs/index.md docs/compliance/control-mapping.md \
		|| { echo "ERROR: generated files are stale; commit the regenerated output."; exit 1; }

ci: lint validate test drift  ## Everything CI runs
	@echo "CI checks passed."

clean:  ## Remove tooling caches
	rm -rf .pytest_cache .ruff_cache .mypy_cache
	find . -type d -name __pycache__ -not -path './.venv/*' -exec rm -rf {} +
