---
id: incident-<YYYY-MM-DD>-<short-name>
title: <Post-Mortem Title>
category: incident
severity: <sev1|sev2|sev3|sev4>
owner: Jolarca Ops
status: draft
last_reviewed: "<YYYY-MM-DD>"
review_due: "<YYYY-MM-DD>"
related_controls:
  - ISO27001:A.5.27
  - ISO27001:A.5.28
approvals: []
---

<!--
TEMPLATE — copy into incidents/postmortems/YYYY-MM-DD-<name>.md, fill every <...>, delete this comment.
Post-mortems are BLAMELESS: focus on systems and process, not individuals.
-->

# <Post-Mortem Title>

| Field | Value |
|-------|-------|
| Date | `<YYYY-MM-DD>` |
| Severity | `<sev1..sev4>` |
| Duration | `<start–end, total>` |
| Author | `<role>` |
| Status | Draft / Final |

## Summary

Two or three sentences: what happened, the impact, and how it was resolved.

## Impact

- **Customer/user impact:** who was affected and how.
- **Duration & scope:** how long, how much (requests, data, revenue, SLO burn).
- **Data / security impact:** any confidentiality, integrity, or GDPR implications.

## Timeline (UTC)

| Time | Event |
|------|-------|
| `HH:MM` | First alert / detection |
| `HH:MM` | Acknowledged by on-call |
| `HH:MM` | Diagnosis / mitigation started |
| `HH:MM` | Service restored |
| `HH:MM` | Monitoring confirmed stable |

## Root cause

The technical root cause, and the contributing conditions. Use the "5 Whys" until you reach a
systemic cause, not a human error.

## What went well

Detection, response, communication, tooling — reinforce what worked.

## What went wrong

Gaps in monitoring, runbooks, access, or process.

## Where we got lucky

Things that could have made this worse but did not.

## Action items

| # | Action | Type | Owner | Due | Link |
|---|--------|------|-------|-----|------|
| 1 | `<prevent recurrence>` | Preventive | `<role>` | `<date>` | `<issue/PR>` |
| 2 | `<improve detection>` | Detective | `<role>` | `<date>` | `<issue/PR>` |
| 3 | `<update runbook>` | Process | `<role>` | `<date>` | `<issue/PR>` |

Every action item has an owner and a date. Untracked action items are how the same incident
happens twice.
