---
id: on-call-rotation
title: On-Call Rotation
category: on-call
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.24
  - SOC2:CC7.4
description: How the on-call rotation is structured, scheduled, and swapped.
---

# On-Call Rotation

## Operating model

As a solo-maintainer organization, the rotation is intentionally simple:

- **Primary:** one engineer carries the pager at any given time.
- **Secondary:** the maintainer acts as the fallback and escalation point.
- **Coverage hours:** `<REPLACE: 24x7 or business hours>` — outside coverage hours, pages are
  acknowledged the next business day unless the incident is sev1.

## Schedule

| Week | Primary | Secondary |
|------|---------|-----------|
| `<REPLACE: week N>` | `<REPLACE: name>` | Maintainer |
| `<REPLACE: week N+1>` | `<REPLACE: name>` | Maintainer |
| `<REPLACE: week N+2>` | `<REPLACE: name>` | Maintainer |

The schedule is published in `<REPLACE: scheduling tool>` at least 4 weeks in advance.

## Swapping

- Swaps must be agreed by both parties and recorded in the scheduling tool at least 24h before the
  shift starts.
- The outgoing engineer remains responsible until the swap is recorded — an informal "can you cover
  me?" is not a swap.
- If no swap is recorded and the primary is unavailable, the secondary takes the shift.

## Prerequisites

No one carries the pager without completing
[`on-call onboarding`](../docs/onboarding/on-call-onboarding.md). This ensures the engineer can
classify severity, find the right runbook, and escalate effectively.

## Review

The rotation is reviewed quarterly:

- Are response-time targets being met?
- Is the primary overloaded? Is the secondary actually available?
- Are runbooks current enough that the primary can act without asking?

Record the review in the front-matter of this document and in the
[`evidence register`](../docs/compliance/evidence-register.md).
