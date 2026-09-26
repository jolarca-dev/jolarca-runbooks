---
id: governance-runbook-standard
title: Runbook Standard
category: governance
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.24
  - SOC2:CC7.3
description: The mandatory structure, quality bar, and front-matter contract every runbook must meet before it is considered production-ready.
---

# Runbook Standard

A runbook is an operational document an engineer can follow **under pressure, without asking
anyone**. This standard defines the contract. `make validate` enforces the machine-readable
parts; reviewers enforce the rest.

## When a runbook is required

Create a runbook when a task is any of the following:

- Performed under time pressure during an incident.
- Error-prone, destructive, or hard to reverse (restarts, restores, rollbacks, failovers).
- Performed by more than one person, or by someone who did not write it.
- Required as evidence for a control (see [`control-mapping`](../compliance/control-mapping.md)).

## Front-matter contract

Every runbook starts with YAML front-matter validated against
[`../../schemas/runbook-frontmatter.schema.json`](../../schemas/runbook-frontmatter.schema.json).

| Field | Required | Meaning |
|-------|:--------:|---------|
| `id` | yes | Stable, unique kebab-case identifier (never reused). |
| `title` | yes | Human-readable name. |
| `category` | yes | One of the schema's enum values. |
| `owner` | yes | Accountable role/team (not an individual). |
| `status` | yes | `draft`, `active`, or `deprecated`. |
| `last_reviewed` | yes | ISO date of the last review. |
| `review_due` | yes | ISO date the next review is due. |
| `related_controls` | yes | ≥1 control reference, e.g. `ISO27001:A.5.29`. |
| `severity` | no | Typical incident severity addressed. |
| `rto` / `rpo` | no | Recovery objectives; required for continuity runbooks. |
| `approvals` | no | Approval trail (see [review-and-approval](review-and-approval.md)). |

## Required body structure

Use [`../../runbooks/_templates/runbook-template.md`](../../runbooks/_templates/runbook-template.md).
At minimum, a runbook contains:

1. **Purpose & scope** — what this covers and, explicitly, what it does not.
2. **Preconditions** — access, tools, and authority needed before starting.
3. **Impact & safety** — what breaks, blast radius, and how to abort/roll back.
4. **Steps** — numbered, copy-pasteable commands with expected output after each.
5. **Verification** — how to confirm success objectively.
6. **Escalation** — who to call and when, linking [`on-call`](../../on-call/README.md).
7. **References** — dashboards, upstream docs, related runbooks.

## Quality bar

- **Copy-pasteable.** Every command runs as-is; no pseudocode, no "figure out the rest".
- **No secrets.** Use a secret reference or `<REPLACE: ...>` token, never a literal credential.
- **Verifiable.** Each step states the expected result so the operator knows it worked.
- **Current.** `review_due` in the future; content matches production reality.
- **Tested.** The procedure has been executed at least once (or in a drill) by its author.

## Definition of done

A runbook is `status: active` only when it passes `make validate`, has no unresolved
`<REPLACE: ...>` tokens, has been executed or drilled once, and has a recorded approval.
