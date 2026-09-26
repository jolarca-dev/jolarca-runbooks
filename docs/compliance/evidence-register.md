---
id: compliance-evidence-register
title: Evidence Register
category: compliance
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.28
  - SOC2:CC7.5
  - GDPR:Art.32
description: Where the evidence for each control lives, who owns it, and how fresh it must be.
---

# Evidence Register

Auditors do not accept "we do this" — they accept **artifacts with an owner and a timestamp**.
This register says where each piece of evidence lives so it can be produced on demand.

## How to read this

- **Evidence** is anything that proves a control operated: a merged PR, a drill record, a log
  export, a signed approval, a monitoring screenshot.
- **Retention** follows the records policy — default **3 years** unless a longer legal or
  contractual period applies.
- Anything marked `<REPLACE: ...>` is not yet collected and is an open audit gap.

## Register

| Control | Evidence | Location | Owner | Retention |
|---------|----------|----------|-------|-----------|
| ISO 27001 A.5.24–A.5.28 | Incident records and post-mortems | [`../../incidents/postmortems/`](../../incidents/postmortems/) | Jolarca Ops | 3 years |
| ISO 27001 A.5.28 | Evidence-collection procedure | [`../../incidents/README.md`](../../incidents/README.md) | Jolarca Ops | 3 years |
| ISO 27001 A.5.29 | BCP/DR plans, RTO/RPO register | [`../../continuity/`](../../continuity/README.md) | Jolarca Ops | 3 years |
| ISO 27001 A.5.29 | Drill/test records | `<REPLACE: drill log location>` | Jolarca Ops | 3 years |
| SOC 2 CC7.3 | Change records (PRs, change log) | Git history + `<REPLACE: change log>` | Jolarca Ops | 3 years |
| SOC 2 CC7.4 | Monitoring/alert configuration | `<REPLACE: observability tool export>` | Jolarca Ops | 1 year |
| SOC 2 CC7.5 | Incident response & recovery records | [`../../on-call/incident-response.md`](../../on-call/incident-response.md) | Jolarca Ops | 3 years |
| SOC 2 CC9.1 | Risk register / BIA | `<REPLACE: risk register location>` | Jolarca Ops | 3 years |
| GDPR Art. 32 | Backup/restore test results | [`../../continuity/backup-restore.md`](../../continuity/backup-restore.md) | Jolarca Ops | 3 years |

## Review trail

Document reviews and approvals are themselves evidence. See
[`../governance/review-and-approval.md`](../governance/review-and-approval.md); the front-matter
`last_reviewed` / `approvals` fields plus the merged pull request form the record.

## Freshness rule

Evidence older than the review cadence, or a document past `review_due`, is **not** admissible as
proof of a currently-operating control. Refresh it before relying on it. The generated
[`control-mapping.md`](control-mapping.md) shows which controls currently have artifacts.
