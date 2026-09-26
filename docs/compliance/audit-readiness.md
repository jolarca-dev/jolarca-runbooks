---
id: compliance-audit-readiness
title: Audit Readiness
category: compliance
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.28
  - SOC2:CC7.4
description: How to prepare for and survive a SOC 2 / ISO 27001 / GDPR audit using this repository.
---

# Audit Readiness

An audit is a search for evidence, not a surprise inspection. If the evidence is indexed and
fresh, the audit is routine. This is the pre-audit checklist and the map of what auditors ask for.

## What auditors ask, and where it lives

| Typical request | Where to point them |
|-----------------|--------------------|
| "Show me your incident process." | [`../../on-call/incident-response.md`](../../on-call/incident-response.md) |
| "Show me incidents and what you learned." | [`../../incidents/postmortems/`](../../incidents/postmortems/) |
| "How do you ensure continuity / recovery?" | [`iso-27001-a5-29.md`](iso-27001-a5-29.md) and [`../../continuity/`](../../continuity/README.md) |
| "Prove these controls are covered." | [`control-mapping.md`](control-mapping.md) |
| "Where is the evidence and who owns it?" | [`evidence-register.md`](evidence-register.md) |
| "How are changes reviewed and approved?" | [`../governance/review-and-approval.md`](../governance/review-and-approval.md) |

## Pre-audit checklist

- [ ] Run `make ci` — lint, front-matter validation, and tests all pass.
- [ ] Run `make render control-map` and commit — no drift in generated files.
- [ ] No document is past its `review_due` date; refresh any that are.
- [ ] Every required control shows **Covered** in [`control-mapping.md`](control-mapping.md)
      (the tool exits non-zero on a gap).
- [ ] Every `<REPLACE: ...>` token is resolved **or** explicitly logged as a known gap with a
      remediation date — never presented as complete.
- [ ] At least one drill/test record exists for each critical recovery procedure.
- [ ] [`evidence-register.md`](evidence-register.md) locations are reachable and current.

## Honesty rule

Never present an untested plan as a tested control, and never back-date a review. If something is
incomplete, say so and show the remediation plan. Auditors tolerate known gaps with owners and
dates; they do not tolerate fabricated evidence — that converts a finding into a credibility
problem across the whole report.
