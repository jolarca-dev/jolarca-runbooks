---
id: on-call-incident-response
title: Incident Response Procedure
category: incident
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.25
  - ISO27001:A.5.26
  - ISO27001:A.5.27
  - SOC2:CC7.4
  - SOC2:CC7.5
description: The step-by-step procedure from first page to incident close — detection, containment, recovery, and learning.
---

# Incident Response Procedure

This is the end-to-end procedure for responding to an incident. Follow it in order; adapt the
details to the situation, but do not skip steps.

## 1. Declare

- Acknowledge the alert within the response time for its severity (see
  [`severity-matrix.md`](severity-matrix.md)).
- Open the incident bridge: `<REPLACE: bridge details>`.
- Announce: severity, one-sentence summary, who is on the bridge.

## 2. Assess

- **What** is broken or at risk?
- **Who** is affected (users, services, data)?
- **When** did it start? Is it still growing?
- **Is data involved?** If personal data may be affected, notify the data-protection contact for
  GDPR Art. 33/34 assessment.

Reclassify severity if needed. Say it out loud on the bridge.

## 3. Contain

Stop the bleeding before you diagnose the root cause.

- Isolate the affected system or traffic.
- Disable the compromised credential.
- Roll back the bad deployment.

Containment may cause a controlled outage — that is almost always better than an uncontrolled one.

## 4. Recover

Execute the recovery runbook:

- Find the right runbook in [`../runbooks/README.md`](../runbooks/README.md).
- Follow it step by step; do not improvise under pressure.
- If no runbook exists, improvise carefully and record every action for the post-mortem.

Verify recovery objectively: health checks, error rates, data integrity.

## 5. Communicate

- Update the incident bridge every 15 minutes (or more often for sev1).
- Notify stakeholders per the [`escalation policy`](escalation-policy.md).
- If customer-impacting, draft a customer notification (do not send without maintainer approval).

## 6. Collect evidence

Before closing, collect evidence for the post-mortem and for audit:

- Logs, metrics, and traces from the incident window.
- Screenshots of dashboards and error states.
- Timeline of actions taken (with timestamps).
- Store in `<REPLACE: secure evidence location>` with a chain-of-custody log.

See [`../docs/compliance/evidence-register.md`](../docs/compliance/evidence-register.md) for what
must be retained.

## 7. Close

- Confirm the incident is resolved and monitoring is stable for at least 30 minutes.
- Announce closure on the bridge and in the incident channel.
- Assign the post-mortem author (usually the incident commander).

## 8. Learn

- Write the post-mortem using
  [`../runbooks/_templates/postmortem-template.md`](../runbooks/_templates/postmortem-template.md).
- Schedule a review within 5 business days.
- Every action item has an owner and a due date.
- Track action items to completion; untracked items are how the same incident happens twice.
