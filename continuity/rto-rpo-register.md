---
id: continuity-rto-rpo-register
title: RTO/RPO Register
category: continuity
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
rto: varies
rpo: varies
related_controls:
  - ISO27001:A.5.29
  - SOC2:CC9.1
description: Recovery objectives for every critical service — the targets the BCP and DR plan must meet.
---

# RTO/RPO Register

Recovery objectives are the contract between the business and the technology. Every service has a
**Recovery Time Objective** (RTO: how fast it must be back) and a **Recovery Point Objective**
(RPO: how much data loss is acceptable). These targets drive the design of backups, redundancy,
and disaster-recovery procedures.

> **Status:** at scaffold time these values are **illustrative**. They must be validated by a
> business impact analysis (BIA) before being relied upon. Update this register after the BIA and
> re-review every 6 months.

## Register

| Service | RTO | RPO | Tier | Notes |
|---------|:---:|:---:|:----:|-------|
| `<REPLACE: primary database>` | 4h | 15m | Critical | Point-in-time restore; tested quarterly. |
| `<REPLACE: primary application>` | 1h | — | Critical | Stateless; restart from image. |
| `<REPLACE: authentication service>` | 30m | — | Critical | No data loss; session state is ephemeral. |
| `<REPLACE: batch processing>` | 24h | 1h | Standard | Can be re-run; data loss acceptable up to 1h. |
| `<REPLACE: internal tools>` | 8h | 24h | Low | Manual workarounds exist. |

## Tier definitions

| Tier | RTO | RPO | Design requirement |
|:----:|:---:|:---:|--------------------|
| **Critical** | ≤ 4h | ≤ 15m | Automated failover or rapid manual recovery; frequent backups. |
| **Standard** | ≤ 24h | ≤ 1h | Manual recovery acceptable; daily backups. |
| **Low** | ≤ 8h | ≤ 24h | Manual recovery; weekly backups or re-creation from source. |

## How to use this

- **When designing a new service:** assign a tier and ensure the architecture can meet the RTO/RPO.
- **When writing a runbook:** reference the RTO/RPO so the operator knows the urgency.
- **When testing DR:** measure actual recovery time and point; compare to targets.
- **When an incident exceeds the RTO:** escalate immediately per the
  [`escalation policy`](../on-call/escalation-policy.md).

## Review

This register is reviewed every 6 months or when a new critical service is added. The review is
recorded in the [`evidence register`](../docs/compliance/evidence-register.md).
