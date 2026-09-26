# Changelog

All notable changes to this repository are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Nothing yet.

## [0.1.0] - 2026-09-26

### Added

- Initial docs-as-code scaffold for `jolarca-runbooks`.
- Directory structure: `docs/`, `runbooks/`, `on-call/`, `continuity/`, `incidents/`.
- YAML front-matter schema (`schemas/runbook-frontmatter.schema.json`).
- Python tooling: `validate`, `lint`, `render`, `control_map` under `tools/`.
- Test suite under `tests/` covering the front-matter validator.
- Compliance artifacts: control mapping, ISO 27001 A.5.29 narrative, evidence register,
  audit-readiness checklist.
- Automation: `Makefile`, `.pre-commit-config.yaml`, GitHub Actions CI workflow.
- Version-controlled generative blueprint: `docs/governance/scaffolding-prompt.md`.

[Unreleased]: https://github.com/jolarca/jolarca-runbooks/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/jolarca/jolarca-runbooks/releases/tag/v0.1.0
