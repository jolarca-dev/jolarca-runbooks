---
id: infra-example-service-restart
title: Example — Restart a Service
category: infrastructure
severity: sev3
owner: Jolarca Ops
status: draft
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
rto: 30m
tags:
  - example
  - restart
related_controls:
  - ISO27001:A.5.29
  - SOC2:CC7.5
description: Illustrative runbook for safely restarting a degraded stateless service.
---

> **Illustrative example.** Replace every `<REPLACE: ...>` token and the sample commands with
> verified production values before marking this `status: active`. See the
> [runbook standard](../../docs/governance/runbook-standard.md).

# Example — Restart a Service

## Purpose & scope

Safely restart `<REPLACE: service name>` to clear a degraded state (memory leak, stuck workers,
unresponsive health checks). Covers a single replica set only — **not** a region failover (see the
[DR plan](../../continuity/dr/disaster-recovery-plan.md)).

## Preconditions

- On-call access to `<REPLACE: orchestration platform, e.g. Kubernetes>`.
- Confirm the service is stateless, or that draining connections is safe.
- Check the current alert state in `<REPLACE: monitoring tool>`.

## Impact & safety

- **Blast radius:** one replica set; the load balancer should shed traffic during the restart.
- **User impact:** brief latency or errors if capacity drops below the serving threshold.
- **Abort / rollback:** stop the rollout; previous instances remain until new ones report healthy.

## Steps

1. Confirm current state.

   ```bash
   kubectl get pods -n <REPLACE: namespace> -l app=<REPLACE: service>
   ```

   Expected: pods listed with current `READY`/`STATUS`.

2. Restart with a rolling update (preserves capacity).

   ```bash
   kubectl rollout restart deployment/<REPLACE: service> -n <REPLACE: namespace>
   ```

   Expected: `deployment.apps/<service> restarted`.

3. Watch the rollout to completion.

   ```bash
   kubectl rollout status deployment/<REPLACE: service> -n <REPLACE: namespace>
   ```

   Expected: `deployment "<service>" successfully rolled out`.

## Verification

- Health endpoint returns `200`: `<REPLACE: health check URL>`.
- Error rate and latency are back to baseline on `<REPLACE: dashboard>`.
- No pending alerts remain for the service.

## Escalation

If the rollout does not complete within `<REPLACE: N>` minutes, or errors persist, escalate per the
[escalation policy](../../on-call/escalation-policy.md) and consider a
[deploy rollback](../application/example-deploy-rollback.md).

## References

- Dashboard: `<REPLACE: link>`
- Related: [Roll Back a Deployment](../application/example-deploy-rollback.md)
