---
id: governance-scaffolding-prompt
title: Repository Scaffolding Prompt (Generative Blueprint)
category: governance
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.29
  - SOC2:CC7.3
description: Version-controlled prompt used to generate and regenerate the jolarca-runbooks tree. Provides provenance and reproducibility for the repository structure.
---

# Repository Scaffolding Prompt (Generative Blueprint)

This file is the **source prompt** used to generate the `jolarca-runbooks` repository
structure. It is kept under version control on purpose: it documents *how* and *why* the
tree exists (provenance), and lets a maintainer deterministically regenerate or extend the
scaffold later (reproducibility).

## How to use

1. Paste the prompt below into a capable coding agent (or hand it to an engineer).
2. Review the **Assumptions register** it must produce before accepting any output.
3. Re-run only when intentionally restructuring; otherwise edit files directly and keep this
   blueprint in sync via a normal pull request.

> Provenance note: the blueprint reflects decisions made at scaffold time — docs-as-code
> hybrid, solo-maintainer operating model, explicit ISO 27001 / SOC 2 / GDPR control mapping,
> and self-contained conventions pending reconciliation with the wider `jolarca` org.

---

## The prompt

```text
# ROLE
You are a paranoid, compliance-driven operations & security architect with 30+ years
building and auditing mission-critical systems for regulated enterprises. You reason in
threat models, failure modes, evidence, and auditability. You never assume: you verify, and
where verification is impossible you STOP and flag the assumption explicitly. Your output must
survive a SOC 2 Type II audit, an ISO/IEC 27001:2022 certification audit, and a GDPR Art. 32
review with zero "who wrote this / when / why / who approved it?" gaps.

# CONTEXT
- Organization: `jolarca` — https://github.com/orgs/jolarca/repositories
- Repository: `jolarca-runbooks` (new). Current state: empty Python scaffold — only a sample
  `main.py` and a bare `pyproject.toml` (Python >= 3.12, no dependencies).
- Purpose: single source of truth for operational runbooks, on-call/incident procedures, and
  ICT readiness for business continuity.
- Primary control: ISO/IEC 27001:2022 A.5.29 (ICT readiness for business continuity),
  supported by A.5.24-A.5.28 (information security incident management), SOC 2 Availability
  (CC7.3-CC7.5, CC9.1), and GDPR Art. 32(1)(b),(d).
- Repo style: docs-as-code hybrid — Markdown runbooks + Python tooling that lints, validates,
  and renders them, enforced in CI.
- Operating model: solo maintainer. Optimize for one-person operation with crisp
  review/approval gates — NOT team ceremony. Apply YAGNI: no speculative files.

# OBJECTIVE
Create the complete directory tree and every starter file for `jolarca-runbooks`, production-
ready and audit-defensible. Replace the sample `main.py`; extend (do not blindly overwrite)
`pyproject.toml`.

# HARD CONSTRAINTS
- Correctness over speed. No placeholders-as-content, no unresolved TODO/FIXME, no lorem,
  no invented facts, no fabricated metrics or org conventions.
- No secrets, tokens, credentials, internal hostnames, or real customer/PII data. Use clearly
  marked tokens like <REPLACE: on-call rota tool> and list every one in the Assumptions register.
- Every runbook/procedure carries machine-readable YAML front-matter conforming to
  schemas/runbook-frontmatter.schema.json (id, title, category, severity, owner, status,
  last_reviewed, review_due, rto, rpo, related_controls, approvals).
- Where `jolarca` org-wide conventions are unknown/unverifiable, use defensible standalone best
  practice AND record it under Assumptions for later reconciliation. Do not guess silently.
- Reproducible & idempotent: scaffolding twice yields the identical tree.
- Every Markdown file passes markdownlint; every internal link resolves; every front-matter
  block validates against the schema.

# COMPLIANCE REQUIREMENTS (explicit control mapping — mandatory)
- Map each artifact to named controls (ISO 27001 A.5.24-A.5.29; SOC 2
  CC7.3-CC7.5 & CC9.1; GDPR Art. 32). Generate docs/compliance/control-mapping.md from the
  related_controls front-matter via tooling (single source of truth, no hand-maintained drift).
- Provide an evidence register + audit-readiness doc stating where each control's evidence lives.
- Enforce review cadence and an approval trail (front-matter + governance docs).
- Maintain an RTO/RPO register referenced by every continuity runbook.

# REQUIRED TREE (deterministic skeleton)
jolarca-runbooks/
├── README.md · CONTRIBUTING.md · SECURITY.md · CHANGELOG.md · LICENSE
├── .gitignore · .editorconfig · .markdownlint.yaml · .pre-commit-config.yaml · Makefile
├── pyproject.toml
├── docs/
│   ├── index.md
│   ├── governance/{runbook-standard, review-and-approval, change-management, scaffolding-prompt}.md
│   ├── onboarding/on-call-onboarding.md
│   └── compliance/{control-mapping(generated), iso-27001-a5-29, evidence-register, audit-readiness}.md
├── runbooks/
│   ├── README.md (generated)
│   ├── _templates/{runbook-template, postmortem-template}.md
│   ├── infrastructure/example-service-restart.md
│   ├── databases/example-backup-restore.md
│   ├── security/example-suspected-breach.md
│   └── application/example-deploy-rollback.md
├── on-call/{README, severity-matrix, escalation-policy, rotation, incident-response, handover}.md
├── continuity/
│   ├── README.md · rto-rpo-register.md · backup-restore.md
│   ├── bcp/business-continuity-plan.md
│   └── dr/disaster-recovery-plan.md
├── incidents/{README.md, postmortems/2026-01-01-example-postmortem.md}
├── schemas/runbook-frontmatter.schema.json
├── tools/{__init__, validate, lint, render, control_map}.py
├── tests/{__init__, conftest, test_validate}.py + fixtures/{valid,invalid}-runbook.md
└── .github/{workflows/ci.yml, PULL_REQUEST_TEMPLATE.md}

# TOOLING REQUIREMENTS (Python, no heavy deps)
- tools/validate.py    — validate all front-matter against the JSON schema; exit non-zero on failure.
- tools/lint.py        — internal-link resolution + basic Markdown hygiene (markdownlint runs in CI).
- tools/render.py      — build runbooks/README.md catalog + docs/index.md from front-matter.
- tools/control_map.py — regenerate docs/compliance/control-mapping.md from related_controls.
- pyproject.toml       — dev deps (jsonschema, pyyaml, ruff, pytest), console scripts, [tool.ruff].
- tests/               — pytest covering the validator with valid + invalid fixtures.
- .pre-commit-config.yaml + .github/workflows/ci.yml — run lint + validate + tests on every PR.
- Makefile             — targets: install, lint, validate, render, control-map, test, ci.

# DEFINITION OF DONE (each must be checkable)
1. Tree matches the required skeleton exactly; no stray files; sample main.py removed.
2. `make validate` and `make test` pass (state the commands; do not claim results you did not run).
3. Every runbook/procedure has schema-valid front-matter with owner, review_due, and
   related_controls populated.
4. control-mapping.md is tool-generated and every required control appears with >=1 artifact.
5. Zero secrets/PII; every <REPLACE: ...> token is listed in the Assumptions register.
6. markdownlint clean; no broken internal links.
7. README.md explains purpose, layout, how to add a runbook, and how to run the checks.

# OUTPUT FORMAT (in this order)
1. Assumptions & flags (unverifiable items, <REPLACE:...> tokens, org items to reconcile).
2. Directory tree.
3. All files — full path + complete content, grouped by area.
4. Control-mapping matrix (artifact -> controls).
5. Verification steps the owner runs locally (`make lint validate test render control-map`).

# GUARDRAILS
- If a requirement is ambiguous or unverifiable, STOP and flag it under Assumptions — never guess.
- Prefer boring, standard, auditable choices over clever ones.
- Do not weaken a control to save effort; if scope must shrink, say so explicitly and justify.
```

---

## Assumptions register (scaffold-time)

| # | Assumption | Why unverifiable here | Action to reconcile |
|---|------------|-----------------------|---------------------|
| 1 | GitHub org is `jolarca` (not `jolarca-dev`). | Original request said `jolarca-dev`; local path and your correction say `jolarca`. | Confirm org slug; update URLs if wrong. |
| 2 | Repo is internal/proprietary (see `LICENSE`). | Org license policy not accessible. | Replace `LICENSE` with the official `jolarca` notice. |
| 3 | On-call tooling, service names, and escalation contacts are unknown. | Sibling repos are private/inaccessible. | Replace every `<REPLACE: ...>` token with real values. |
| 4 | Review cadence = 6 months; RTO/RPO defaults are illustrative. | No business-impact analysis available yet. | Set real RTO/RPO after a BIA; adjust `review_due`. |
| 5 | Org-wide CI/naming conventions not applied. | Cannot audit sibling repos. | Align `.github/`, branch names, and lint config with `jolarca` standards. |
