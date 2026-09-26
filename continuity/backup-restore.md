---
id: continuity-backup-restore
title: Backup and Restore
category: continuity
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
rto: 4h
rpo: 15m
related_controls:
  - ISO27001:A.5.29
  - SOC2:CC7.5
  - GDPR:Art.32
description: Backup schedule, retention, and restore procedure — the foundation of data recovery.
---

# Backup and Restore

Backups are the last line of defense against data loss. A backup that has never been restored is
not a backup — it is a hope. This policy ensures backups are taken, retained, tested, and can be
restored within the RPO/RTO.

## Schedule

| Data | Frequency | Retention | Location |
|------|:---------:|:---------:|----------|
| `<REPLACE: primary database>` | Every 15 min (WAL/archive) + daily full | 30 days | `<REPLACE: backup storage>` |
| `<REPLACE: object storage>` | Continuous replication | 90 days | `<REPLACE: secondary region>` |
| `<REPLACE: configuration / IaC>` | Every commit (git) | Indefinite | `<REPLACE: git remote>` |

## Retention

- **Daily backups:** retained for 30 days.
- **Weekly backups:** retained for 1 year.
- **Monthly backups:** retained for 3 years (or longer if required by legal/regulatory obligations).
- **GDPR Art. 32:** personal data backups are encrypted and access is logged.

## Restore procedure

The restore procedure is documented in
[`../runbooks/databases/example-backup-restore.md`](../runbooks/databases/example-backup-restore.md).
Key steps:

1. Identify the target backup (most recent before the incident).
2. Restore to a **new** instance (never overwrite the broken one).
3. Verify data integrity (row counts, checksums, smoke tests).
4. Switch the application to the restored instance.
5. Keep the broken instance for forensic review until the incident closes.

## Testing

- **Monthly:** restore a random daily backup to a test environment and verify integrity.
- **Quarterly:** full restore drill of the primary database, timed against the RTO.
- **After any backup-system change:** immediate restore test.

Test results are recorded in the [`evidence register`](../docs/compliance/evidence-register.md).

## Encryption and access

- All backups are encrypted at rest (`<REPLACE: encryption method, e.g. AES-256>`).
- Access to backups is restricted to `<REPLACE: roles>` and logged.
- Backup credentials are stored in `<REPLACE: secrets manager>` and rotated quarterly.

## What can go wrong

- **Backup job silent failure:** monitor backup success; alert on failure.
- **Retention too short:** review retention against legal/regulatory requirements annually.
- **Restore takes too long:** test restores regularly; optimize if RTO is at risk.
- **Encryption key lost:** store keys in the secrets manager with disaster-recovery access.
