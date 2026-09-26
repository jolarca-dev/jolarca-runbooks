---
id: on-call-severity-matrix
title: Severity Matrix
category: on-call
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.25
  - SOC2:CC7.4
description: How to classify incident severity so the response matches the impact.
---

# Severity Matrix

Classify **early and honestly**. A misclassified incident either wastes resources (over-classified)
or delays the right response (under-classified). You can always change the severity as facts
emerge — say so out loud on the bridge.

| Severity | Definition | Response time | Examples |
|:--------:|------------|:-------------:|----------|
| **sev1** | Critical service down or severely degraded; data loss or security breach suspected or confirmed. | Immediate, all hands. | Production database unreachable; confirmed credential leak; ransomware detected. |
| **sev2** | Major feature broken for a significant user cohort; workaround unavailable or painful. | Within 15 minutes. | Checkout failing for 30% of users; backup job failed and RPO is at risk. |
| **sev3** | Minor feature broken or degraded; workaround exists; no data loss. | Within 1 hour. | Non-critical batch job late; elevated error rate on a low-traffic endpoint. |
| **sev4** | Cosmetic or non-urgent; no user impact. | Next business day. | Typo in a non-critical page; log noise with no functional effect. |

## When in doubt

- **Escalate up.** It is always better to declare a higher severity and downgrade later than to
  sit on a sev1 for twenty minutes.
- **Security is always sev1 or sev2.** Suspected breaches, credential leaks, and data-exposure
  events start at sev2 minimum; confirmed impact is sev1.
- **Data loss is always sev1 or sev2.** If you cannot prove no data was lost, assume it was.

## Response-time expectations

"Response time" means a human acknowledges the alert and opens the incident bridge — not that the
incident is resolved. Resolution time depends on the root cause; the goal is to stop the bleeding
fast enough to meet the RTO in the [`RTO/RPO register`](../continuity/rto-rpo-register.md).
