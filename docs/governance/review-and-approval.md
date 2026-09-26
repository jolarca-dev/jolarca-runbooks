---
id: governance-review-and-approval
title: Review and Approval
category: governance
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - SOC2:CC7.3
  - ISO27001:A.5.24
description: Review cadence, out-of-cycle triggers, and how the approval trail is recorded as audit evidence.
---

# Review and Approval

Operational documents decay. A runbook that no longer matches production is worse than no
runbook, because it is trusted. This policy defines how documents stay current and how that is
proven to an auditor.

## Review cadence

- **Periodic:** every document is reviewed at least every **6 months**. `review_due` is set to
  `last_reviewed + 6 months`; `make validate` flags nothing, so reviewers track dates in the
  front-matter and the catalogue.
- **Event-driven (out-of-cycle):** review immediately when any of these occur:
  - The system, architecture, or tooling the document describes changes.
  - An incident or post-mortem reveals the document was wrong, unclear, or missing.
  - A control, legal, or regulatory obligation changes.
  - A drill or test of the procedure fails.

## What a review checks

1. Technical accuracy against current production.
2. Every command runs; every expected output is correct.
3. No secrets, no stale `<REPLACE: ...>` tokens, no dead links (`make lint`).
4. Front-matter is valid and `related_controls` still apply (`make validate`).
5. Ownership is still correct.

On completion, update `last_reviewed`, set the next `review_due`, and record an approval.

## Approval trail

Approval is captured in two places so it survives independently:

- **Front-matter `approvals`** — an explicit list of `{by, role, date}`.
- **The merged pull request** — the change, its diff, and the review conversation.

For a solo maintainer, approval is a **structured self-review**: complete the checklist above,
record yourself in `approvals` with `role: Maintainer`, and merge via pull request so the
timestamp and diff are preserved.

```yaml
approvals:
  - by: <REPLACE: approver identity>
    role: Maintainer
    date: "2026-09-26"
```

## Evidence

The review trail is audit evidence for change management and incident-preparation controls. It is
indexed in the [`evidence register`](../compliance/evidence-register.md). A document that is past
`review_due` is treated as **unverified** and must not be relied upon in an incident until
re-reviewed.
