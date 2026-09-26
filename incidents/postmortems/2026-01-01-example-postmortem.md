---
id: incident-2026-01-01-example
title: Example Post-Mortem — 2026-01-01 Database Connection Pool Exhaustion
category: incident
severity: sev2
owner: Jolarca Ops
status: draft
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.27
  - ISO27001:A.5.28
  - SOC2:CC7.4
  - SOC2:CC7.5
description: Illustrative post-mortem for a database connection pool exhaustion incident.
---

> **Illustrative example.** This is a fictional post-mortem to demonstrate the structure and
> quality bar. Replace with real incidents as they occur.

# Example Post-Mortem — 2026-01-01 Database Connection Pool Exhaustion

| Field | Value |
|-------|-------|
| Date | 2026-01-01 |
| Severity | sev2 |
| Duration | 14:32–15:17 UTC (45 min) |
| Author | On-call engineer |
| Status | Draft |

## Summary

The primary application experienced elevated error rates (30% of requests failing) for 45 minutes
due to database connection pool exhaustion. The root cause was a slow query introduced in a
deployment at 14:00 UTC that held connections longer than expected. Recovery was achieved by
rolling back the deployment.

## Impact

- **Customer/user impact:** ~30% of checkout requests failed with 500 errors; users saw error
  pages and could not complete purchases.
- **Duration & scope:** 45 minutes; estimated 1,200 failed transactions, ~€15k revenue impact.
- **Data / security impact:** no data loss or security implications.

## Timeline (UTC)

| Time | Event |
|------|-------|
| 14:00 | Deployment of `v2.3.1` with a new reporting query. |
| 14:32 | Alert fires: `checkout_error_rate > 5%`. |
| 14:35 | On-call acknowledges; opens incident bridge. |
| 14:40 | Diagnosis: database connection pool at 100%; slow query identified. |
| 14:45 | Decision: rollback deployment. |
| 14:50 | Rollback initiated; `v2.3.0` deploying. |
| 14:55 | Rollback complete; error rate dropping. |
| 15:00 | Error rate back to baseline; monitoring stable. |
| 15:17 | Incident declared resolved; bridge closed. |

## Root cause

The deployment at 14:00 introduced a reporting query that performed a full table scan on a large
table (`orders`). The query held database connections for 10–15 seconds each, exhausting the
connection pool (max 100 connections). Under load, the pool could not serve normal checkout queries,
causing timeouts and 500 errors.

Contributing factors:

- The query was not reviewed for performance before deployment.
- No staging environment test with production-scale data.
- Connection pool monitoring did not alert on high utilization (only on exhaustion).

## What went well

- Alert fired within 2 minutes of threshold breach.
- On-call responded within 3 minutes; bridge opened quickly.
- Rollback was straightforward and completed in 5 minutes.
- No data loss or security impact.

## What went wrong

- New query was not performance-reviewed; no CI check for slow queries.
- Staging environment has a small dataset; the slow query was not caught in testing.
- Connection pool utilization alert was missing; only exhaustion (100%) alerted.
- Post-deployment monitoring did not catch the elevated query latency early enough.

## Where we got lucky

- The incident occurred during business hours with the maintainer available.
- The slow query was in a non-critical reporting feature; core checkout logic was unaffected.
- No cascading failures (other services did not depend on the exhausted pool).

## Action items

| # | Action | Type | Owner | Due | Link |
|---|--------|------|-------|-----|------|
| 1 | Add CI check to reject queries without an index or with estimated cost > threshold. | Preventive | Maintainer | 2026-01-15 | `<REPLACE: issue>` |
| 2 | Add connection pool utilization alert at 80% threshold. | Detective | On-call | 2026-01-10 | `<REPLACE: issue>` |
| 3 | Populate staging database with production-scale data for performance testing. | Process | Maintainer | 2026-02-01 | `<REPLACE: issue>` |
| 4 | Update deployment runbook to include post-deploy query latency check. | Process | On-call | 2026-01-08 | `<REPLACE: issue>` |

All action items have owners and due dates. The maintainer will track completion in the weekly
review.
