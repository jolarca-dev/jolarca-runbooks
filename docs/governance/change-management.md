---
id: governance-change-management
title: Change Management
category: governance
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - SOC2:CC7.3
description: How changes to production and to these documents are classified, approved, recorded, and reversed.
---

# Change Management

Most outages are caused by change. This policy ensures every change is intentional, reviewed,
reversible, and recorded — the evidence base for SOC 2 CC7.3 and a precondition for safe
incident response.

## Change types

| Type | Definition | Approval |
|------|------------|----------|
| **Standard** | Pre-authorized, low-risk, repeatable, with a documented rollback. | None beyond the runbook. |
| **Normal** | Any other planned change. | Recorded approval before deploy. |
| **Emergency** | Urgent change to restore or protect service. | Verbal/self approval now, recorded **within 24h**. |

## Required for every normal/emergency change

1. **What & why** — a one-paragraph description and motivation.
2. **Risk & blast radius** — what could break and who is affected.
3. **Rollback plan** — the exact steps to revert, tested where possible. Destructive or
   irreversible changes must say so explicitly and require a second review.
4. **Verification** — how success is confirmed objectively.
5. **Window & owner** — when it happens and who is accountable.

## Recording

- Changes to production are recorded in the deployment/change log
  (`<REPLACE: change log location>`).
- Changes to this repository are the pull request itself: the diff, the review, and the merge
  timestamp form the record (see [review-and-approval](review-and-approval.md)).
- A change that causes an incident produces a post-mortem under
  [`../../incidents/postmortems/`](../../incidents/postmortems/).

## Emergency changes

In an incident, restoring service outranks process. Make the safest effective change, then record
it within 24 hours. Never skip the rollback plan, even under pressure — an emergency change
without a way back turns one incident into two.
