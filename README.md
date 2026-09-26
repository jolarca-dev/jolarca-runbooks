# jolarca-runbooks

Operational runbooks, on-call procedures, and ICT readiness for business continuity for the
`jolarca` organization. This repository is the single source of truth for how Jolarca operates,
responds to incidents, and keeps services running.

Primary control objective: **ISO/IEC 27001:2022 A.5.29 — ICT readiness for business continuity**,
supported by A.5.24–A.5.28 (incident management), SOC 2 Availability (CC7.3–CC7.5, CC9.1), and
GDPR Art. 32.

## Layout

| Path | Purpose |
|------|---------|
| [`docs/`](docs/index.md) | Governance, onboarding, and compliance documentation. |
| [`runbooks/`](runbooks/README.md) | Task-oriented procedures to operate and recover services. |
| [`on-call/`](on-call/README.md) | On-call rota, severity matrix, escalation, and incident response. |
| [`continuity/`](continuity/README.md) | Business continuity (BCP), disaster recovery (DR), RTO/RPO. |
| [`incidents/`](incidents/README.md) | Incident records and post-mortems. |
| [`schemas/`](schemas/runbook-frontmatter.schema.json) | JSON Schema for runbook front-matter. |
| [`tools/`](tools/) | Python tooling that validates, lints, and renders the docs. |
| [`tests/`](tests/) | Automated checks for the tooling. |

## Quickstart

```bash
make install   # pip install -e .[dev]  (jsonschema, pyyaml, ruff, pytest)
make ci        # lint + validate + test — the same checks CI runs
```

Individual targets: `make lint`, `make validate`, `make test`, `make render`, `make control-map`.

## Adding a runbook

1. Copy [`runbooks/_templates/runbook-template.md`](runbooks/_templates/runbook-template.md) into
   the right `runbooks/<category>/` folder.
2. Fill in the YAML front-matter (`id`, `owner`, `related_controls`, `review_due`, …). It must
   conform to [`schemas/runbook-frontmatter.schema.json`](schemas/runbook-frontmatter.schema.json).
3. Replace every `<REPLACE: ...>` token — committed content must contain no placeholders.
4. Run `make validate render control-map` and open a pull request.

See [`docs/governance/runbook-standard.md`](docs/governance/runbook-standard.md) for the full
standard, and [`docs/governance/review-and-approval.md`](docs/governance/review-and-approval.md)
for the review cadence and approval trail.

## Compliance

Control-to-artifact mapping is generated from front-matter, never hand-maintained:

- [`docs/compliance/control-mapping.md`](docs/compliance/control-mapping.md) — artifact ↔ control matrix.
- [`docs/compliance/iso-27001-a5-29.md`](docs/compliance/iso-27001-a5-29.md) — A.5.29 conformance narrative.
- [`docs/compliance/evidence-register.md`](docs/compliance/evidence-register.md) — where each control's evidence lives.
- [`docs/compliance/audit-readiness.md`](docs/compliance/audit-readiness.md) — audit preparation checklist.

## Provenance

The structure of this repository is generated from a version-controlled blueprint:
[`docs/governance/scaffolding-prompt.md`](docs/governance/scaffolding-prompt.md).

## Contributing & security

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to propose changes.
- [`SECURITY.md`](SECURITY.md) — how to report a vulnerability.
- [`CHANGELOG.md`](CHANGELOG.md) — notable changes.

> Status: scaffold. Content marked `<REPLACE: ...>` must be completed with real, verified values
> before this repository is relied upon during an incident or presented to an auditor.
