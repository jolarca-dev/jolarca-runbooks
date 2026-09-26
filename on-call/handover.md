---
id: on-call-handover
title: On-Call Handover
category: on-call
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.24
  - SOC2:CC7.4
description: What to pass to the next on-call engineer so nothing falls through the cracks.
---

# On-Call Handover

A bad handover is how incidents start in the next shift. Take 10 minutes; do not skip it.

## When to hand over

- End of your on-call shift.
- You are going to be unavailable for more than 30 minutes during your shift.
- You are swapping shifts with someone.

## What to cover

### 1. Active incidents

- What is happening, severity, current status.
- What has been tried and what worked or did not.
- What the next steps are and who is owning them.
- If the incident is still open, the incoming engineer takes ownership — confirm they accept.

### 2. Open alerts or degraded services

- Alerts that fired but did not become incidents.
- Services running in a degraded state with a known workaround.
- Any monitoring gaps (e.g. a dashboard is broken, so you are flying blind on X).

### 3. Pending changes or maintenance

- Deployments scheduled during the incoming shift.
- Maintenance windows in progress.
- Changes that need monitoring after deployment.

### 4. Runbook or tooling issues

- Runbooks that were wrong, missing, or hard to follow during your shift.
- Tooling that is broken or slow.
- Create issues for these if they do not exist; hand over the issue numbers.

## Handover record

Write a short handover note in `<REPLACE: handover channel or document>`:

```markdown
## Handover — <YYYY-MM-DD> <HH:MM>

**Outgoing:** <name>
**Incoming:** <name>

### Active incidents
- <incident or "none">

### Open alerts / degraded services
- <alert or "none">

### Pending changes
- <change or "none">

### Runbook / tooling issues
- <issue or "none">
```

Both engineers confirm the handover is complete before the outgoing engineer disengages.
