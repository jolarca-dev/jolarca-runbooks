---
id: continuity-dr
title: Disaster Recovery Plan (DR)
category: continuity
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
rto: varies
rpo: varies
related_controls:
  - ISO27001:A.5.29
  - SOC2:CC7.4
  - SOC2:CC7.5
  - SOC2:CC9.1
description: How to recover from a disaster — region failure, data-center loss, or prolonged outage.
---

# Disaster Recovery Plan (DR)

The DR plan is the technical counterpart to the [BCP](../business-continuity-plan.md). It defines
how to recover infrastructure and data when a disaster exceeds the capacity of routine incident
response.

## Purpose

- Recover critical services within their RTO.
- Minimize data loss to within the RPO.
- Provide a clear, tested procedure for the worst-case scenarios.

## Disaster scenarios

| Scenario | Impact | Primary recovery strategy |
|----------|--------|---------------------------|
| **Single-instance failure** | Service down; no data loss if stateless. | Restart from image; see [runbooks](../../runbooks/README.md). |
| **Database corruption** | Data loss or inconsistency. | Restore from backup per [`backup-restore.md`](../backup-restore.md). |
| **Availability-zone failure** | Services in one AZ down. | Failover to secondary AZ (if multi-AZ) or restore from backup. |
| **Region failure** | Entire region unavailable. | Failover to secondary region (if multi-region) or restore from backup. |
| **Data-center loss** | Physical infrastructure destroyed. | Restore from off-site backups; rebuild infrastructure from IaC. |
| **Ransomware / data destruction** | Data encrypted or deleted. | Isolate affected systems; restore from clean backups; rotate all credentials. |

## Activation criteria

Activate the DR plan when:

- A sev1 incident cannot be resolved within the RTO using routine runbooks.
- An entire availability zone or region is unavailable.
- Data loss is confirmed or suspected and backups are the only recovery path.
- The maintainer explicitly declares a disaster.

## Recovery procedures

### 1. Assess and declare

- Confirm the scope: what is down, what data is at risk.
- Declare a disaster on the incident bridge; activate the [BCP](../business-continuity-plan.md).

### 2. Isolate (if security-related)

- If the disaster is security-related (ransomware, data destruction), isolate affected systems
  before attempting recovery. See
  [`../../runbooks/security/example-suspected-breach.md`](../../runbooks/security/example-suspected-breach.md).

### 3. Recover infrastructure

- If using IaC, rebuild infrastructure from source: `<REPLACE: IaC apply command>`.
- If multi-region, failover DNS / load balancer to the secondary region.
- If single-region, restore from backups per [`backup-restore.md`](../backup-restore.md).

### 4. Recover data

- Restore databases from the most recent backup before the disaster.
- Verify data integrity (row counts, checksums).
- Switch applications to the restored database.

### 5. Verify and communicate

- Confirm all critical services are operational and meeting RTO.
- Announce recovery on the incident bridge and to stakeholders.
- If customer-impacting, send a customer notification (approved by maintainer).

### 6. Post-disaster

- Write a post-mortem using
  [`../../runbooks/_templates/postmortem-template.md`](../../runbooks/_templates/postmortem-template.md).
- Review the DR plan: what worked, what did not, what needs to change.
- Update the plan and re-test within 30 days.

## Failback

After a disaster recovery, plan the failback to the primary environment:

- Do not failback under pressure; stabilize first.
- Test failback in a maintenance window.
- Communicate the failback plan to stakeholders.

## Testing

- **Annual DR drill:** simulate a region failure; measure actual RTO/RPO vs. targets.
- **After any major infrastructure change:** re-test if the change affects recovery.
- **Test records:** indexed in the [`evidence register`](../../docs/compliance/evidence-register.md).

## Review

This plan is reviewed every 6 months or after any activation or drill. The review is recorded in
the front-matter and the evidence register.
