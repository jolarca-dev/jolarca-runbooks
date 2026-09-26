---
id: onboarding-on-call
title: On-Call Onboarding
category: onboarding
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.24
  - SOC2:CC7.4
description: How an engineer becomes ready to carry the pager — access, tooling, shadowing, and the sign-off checklist.
---

# On-Call Onboarding

Nobody should carry the pager before they can find, understand, and act on the runbooks. This is
the readiness checklist. Complete every item before joining the rotation in
[`on-call/rotation.md`](../../on-call/rotation.md).

## 1. Access

- [ ] Repository access to `jolarca-runbooks` and the service repos.
- [ ] Monitoring/dashboards: `<REPLACE: observability tool>`.
- [ ] Alerting/paging: `<REPLACE: paging tool>` — test page received and acknowledged.
- [ ] Incident channel and bridge: `<REPLACE: comms tool / bridge line>`.
- [ ] Credentials via the secrets manager only — never stored locally in plaintext.

## 2. Knowledge

- [ ] Read [`on-call/README.md`](../../on-call/README.md) end to end.
- [ ] Understand the [`severity matrix`](../../on-call/severity-matrix.md) and
      [`escalation policy`](../../on-call/escalation-policy.md).
- [ ] Walk through [`incident response`](../../on-call/incident-response.md) start to finish.
- [ ] Know where the [`runbooks`](../../runbooks/README.md) live and how to search them fast.

## 3. Practice

- [ ] Shadow one full rotation without taking the pager.
- [ ] Lead one drill or game-day using a runbook, observed by the maintainer.
- [ ] Perform one [`handover`](../../on-call/handover.md) as the outgoing engineer.

## 4. Sign-off

The maintainer confirms the engineer can: acknowledge a page, classify severity, find the right
runbook, execute a recovery step safely, and escalate when out of depth. Record the sign-off here:

| Engineer | Date | Confirmed by |
|----------|------|--------------|
| `<REPLACE: name>` | `<REPLACE: date>` | Maintainer |

> Readiness evidence supports ISO 27001 A.5.24 (incident management planning and preparation) and
> is indexed in the [`evidence register`](../compliance/evidence-register.md).
