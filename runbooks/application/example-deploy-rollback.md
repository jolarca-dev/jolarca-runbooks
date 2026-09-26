---
id: app-example-deploy-rollback
title: Example — Roll Back a Deployment
category: application
severity: sev2
owner: Jolarca Ops
status: draft
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
rto: 15m
tags:
  - example
  - deploy
  - rollback
related_controls:
  - SOC2:CC7.3
  - SOC2:CC7.5
description: Illustrative runbook for rolling back a bad application deployment to the last known-good version.
---

> **Illustrative example.** Replace every `<REPLACE: ...>` token with verified production values
> before marking this `status: active`. See the
> [runbook standard](../../docs/governance/runbook-standard.md).

# Example — Roll Back a Deployment

## Purpose & scope

Revert `<REPLACE: service>` to the last known-good version when a deployment causes elevated errors,
latency, or data-integrity symptoms. Rolling back is almost always faster and safer than fixing
forward during an active incident.

## Preconditions

- On-call access to the deployment system: `<REPLACE: CD tool / cluster>`.
- Know the current and previous versions: `<REPLACE: how versions are tagged>`.
- Confirm whether the change included a **database migration** — if so, read Impact first.

## Impact & safety

- **Blast radius:** the deployed service; users see a brief blip during the swap.
- **Migrations:** if the bad release migrated the schema, a plain rollback may break. Migrations
  must be backward-compatible; if not, **stop and escalate** before rolling back.
- **Abort:** the previous version stays live until the rollback target reports healthy.

## Steps

1. Identify the current and previous revisions.

   ```bash
   <REPLACE: command to list deployed revisions, e.g. `helm history <release>`>
   ```

   Expected: a list showing the last known-good revision number.

2. Roll back to the last known-good revision.

   ```bash
   <REPLACE: rollback command, e.g. `helm rollback <release> <rev> -n <namespace>`>
   ```

   Expected: confirmation that the rollback was applied.

3. Confirm the running version.

   ```bash
   <REPLACE: command to show deployed image/version>
   ```

   Expected: the previous known-good version is now running.

## Verification

- Error rate and latency return to baseline on `<REPLACE: dashboard>`.
- A smoke test request succeeds: `<REPLACE: smoke test>`.
- Record the rollback as an **emergency change** per
  [change management](../../docs/governance/change-management.md).

## Escalation

If the rollback fails, or a migration makes it unsafe, declare a higher severity per the
[severity matrix](../../on-call/severity-matrix.md) and escalate per the
[escalation policy](../../on-call/escalation-policy.md).

## References

- Deployment log: `<REPLACE: link>`
- Related: [Restart a Service](../infrastructure/example-service-restart.md)
