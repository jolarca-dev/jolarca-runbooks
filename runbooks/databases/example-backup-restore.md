---
id: db-example-backup-restore
title: Example — Backup and Restore a Database
category: database
severity: sev2
owner: Jolarca Ops
status: draft
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
rto: 4h
rpo: 15m
tags:
  - example
  - database
  - backup
  - restore
related_controls:
  - ISO27001:A.5.29
  - SOC2:CC7.5
  - GDPR:Art.32
description: Illustrative runbook for verifying a backup and restoring a database to a point in time.
---

> **Illustrative example.** Replace every `<REPLACE: ...>` token with verified production values
> before marking this `status: active`. Restores are destructive — never run one against the wrong
> target. See the [runbook standard](../../docs/governance/runbook-standard.md).

# Example — Backup and Restore a Database

## Purpose & scope

Restore `<REPLACE: database>` to a known-good point in time after data loss, corruption, or a bad
migration. Covers the restore itself; for the backup schedule and retention policy see
[`../../continuity/backup-restore.md`](../../continuity/backup-restore.md).

## Preconditions

- On-call access to `<REPLACE: database host / managed service>`.
- A verified recent backup is available: `<REPLACE: backup location>`.
- Application traffic is drained or the database is taken offline.
- **Two people** on the restore: one operator, one verifier.

## Impact & safety

- **Blast radius:** the database and every service that reads/writes it.
- **Data loss:** up to the RPO (`15m` target; actual depends on last backup).
- **Abort / rollback:** do **not** delete the broken database until the restore is verified.
  Rename it to `<REPLACE: database>_broken_<timestamp>` for forensic review.

## Steps

1. Stop writes to the database.

   ```bash
   <REPLACE: command to disable writes, e.g. set read-only mode or stop app pods>
   ```

   Expected: no new write traffic; read traffic may continue.

2. Identify the target backup.

   ```bash
   <REPLACE: command to list available backups, e.g. `pgbackrest info` or cloud CLI>
   ```

   Expected: a list with timestamps; pick the most recent before the incident.

3. Restore to a **new** database instance (never overwrite the broken one in place).

   ```bash
   <REPLACE: restore command, e.g. `pg_restore -d <new_db> <backup_file>`>
   ```

   Expected: restore completes without errors.

4. Verify the restore.

   ```bash
   <REPLACE: smoke-test queries, row counts, checksums>
   ```

   Expected: results match the known-good state.

5. Switch the application to the restored database.

   ```bash
   <REPLACE: connection-string update / DNS cutover / restart command>
   ```

   Expected: application health checks pass; write traffic resumes.

6. Keep the broken database renamed for forensic review; delete only after the incident closes.

## Verification

- Row counts and checksums match the pre-incident baseline.
- Application smoke test passes end-to-end.
- Backup job for the restored database is scheduled and the next backup succeeds.

## Escalation

If the restore fails or data integrity cannot be confirmed, escalate per the
[escalation policy](../../on-call/escalation-policy.md) and treat as a data-loss incident per the
[incident response procedure](../../on-call/incident-response.md).

## References

- Backup policy: [`../../continuity/backup-restore.md`](../../continuity/backup-restore.md)
- Related: [Restart a Service](../infrastructure/example-service-restart.md)
