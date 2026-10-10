---
id: infra-jolarca-pci-docker-daemon
title: Operate the Jolarca PCI Docker Daemon
category: infrastructure
severity: sev2
owner: Jolarca Ops
status: draft
last_reviewed: "2026-10-10"
review_due: "2027-04-10"
rto: 15m
rpo: 0m
tags:
  - docker
  - pci
  - marketplace
  - daemon
  - migration
  - rollback
related_controls:
  - ISO27001:A.8.13
  - ISO27001:A.5.29
  - GDPR:Art.32
approvals: []
---

# Operate the Jolarca PCI Docker Daemon

## Purpose & scope

Day-2 operations for the **isolated marketplace Docker daemon** (`docker-jolarca`) that carries
PCI-scope marketplace workloads away from the shared church/host `docker.service`, plus the
one-time **marketplace cutover** onto it and its rollback (see `ADR-0008`).

This runbook does **not** cover the church/host daemon, application deploys (see
[Roll Back a Deployment](../application/example-deploy-rollback.md)), or database restores (see
[Backup and Restore](../../continuity/backup-restore.md)).

## Key isolation constants

| Item | Value |
|------|-------|
| Socket | `unix:///run/docker-jolarca/docker.sock` |
| dockerd unit | `docker-jolarca.service` |
| containerd unit | `docker-jolarca-containerd.service` |
| Daemon config | `/etc/docker-jolarca/daemon.json` |
| Data root | `/opt/jolarca/data/docker` (on `lv_jolarca`) |
| Containerd root | `/opt/jolarca/data/containerd` |
| Exec root / pidfile | `/run/docker-jolarca` |
| Address pool | `172.31.0.0/16`, size `/24` |
| Compose project | `jolarca-marketplace-prod` |
| Compose file | `/opt/jolarca/repos/jolarca/docker-compose.prod.yml` + `.env.prod` |

## Preconditions

- **Access:** shell as user `jol` on the marketplace host; `pkexec` available for root systemd
  actions and for reading the root-only church data-root during cutover.
- **Tools:** `docker` CLI (its default socket is the church daemon), `systemctl`/`journalctl`,
  `docker compose`. Every marketplace command must set
  `DOCKER_HOST=unix:///run/docker-jolarca/docker.sock` or pass `-H unix:///run/docker-jolarca/docker.sock`.
- **Authority:** day-2 read/restart may be run by on-call; the **cutover** requires an approved
  maintenance window with the operator physically present (typed confirmation + pkexec dialogs).

## Impact & safety

- **Blast radius:** the `docker-jolarca` units and every marketplace container. The church/host
  daemon (`jol-vaultwarden`, `jol-prometheus`, `terraform-mcp`) is a separate `dockerd` +
  containerd pair and is **unaffected** by anything in this runbook.
- **User impact:** a `dockerd` restart is non-disruptive to running containers
  (`live-restore: true`). The one-time cutover stops the marketplace for roughly 2–10 minutes.
- **Abort / rollback:** cutover rollback is `~/docker-jolarca-phase1/migrate.sh rollback`. Old
  volumes and images on the church daemon are **never deleted during the window**, so reverting is
  a re-`up` under the old project name. **Reversible** until the later Phase 4 cleanup removes them.

## Steps — day-2 operations

1. **Confirm the daemon is healthy.**

   ```bash
   systemctl is-active docker-jolarca.service docker-jolarca-containerd.service
   docker -H unix:///run/docker-jolarca/docker.sock info --format '{{.DockerRootDir}}'
   ```

   Expected: two `active`; root path `/opt/jolarca/data/docker`.

2. **List marketplace workloads.**

   ```bash
   docker -H unix:///run/docker-jolarca/docker.sock ps --format '{{.Names}}  {{.Status}}'
   ```

   Expected: the `jolarca-marketplace-prod-*` containers (app, backend, worker, beat, nginx,
   postgres, redis, elasticsearch) all `Up`.

3. **Restart the daemon (containers survive via live-restore).**

   ```bash
   pkexec systemctl restart docker-jolarca.service
   ```

   Expected: `active` after a re-check of `is-active`; running containers unchanged. Only restart
   containerd if dockerd cannot reach its socket:
   `pkexec systemctl restart docker-jolarca-containerd.service docker-jolarca.service`.

4. **Tail daemon logs (filtered to the current run).**

   ```bash
   journalctl -u docker-jolarca.service -n 100 --since "$(
     systemctl show docker-jolarca.service -p ActiveEnterTimestamp --value)"
   ```

   Expected: no `failed to process event ... namespace=moby` lines — that error means dockerd fell
   back to the shared system containerd (see Troubleshooting).

5. **Compose up/down on the PCI daemon.**

   ```bash
   cd /opt/jolarca/repos/jolarca
   DOCKER_HOST=unix:///run/docker-jolarca/docker.sock \
     docker compose -p jolarca-marketplace-prod -f docker-compose.prod.yml --env-file .env.prod up -d
   ```

   Expected: services re-created with the `jolarca-marketplace-prod` prefix. Always pass
   `-p jolarca-marketplace-prod`; the pre-rename container working_dir labels are stale.

## Steps — marketplace cutover (one-time, maintenance window)

Closes findings D-03/D-04 (see `ADR-0008`). Data migrates by **physical volume copy** after a clean
`down`, not logical restore: the postgres image runs initdb scripts and redis runs with AOF, so a
`pg_dump`/`dump.rdb` restore would collide with pre-created objects or be ignored.

1. **Pre-flight (read-only).**

   ```bash
   cd ~/docker-jolarca-phase1 && ./migrate.sh preflight
   ```

   Expected: `PREFLIGHT OK` and a `rows=<N> tables=<M>` baseline. Exits non-zero if the isolated
   daemon is unreachable, an image is missing, `lv_jolarca` has under 20 G free, or the crontab
   holds a non-marketplace `docker` line.

2. **Run the window (operator present).**

   ```bash
   ./migrate.sh run
   ```

   Type `MIGRATE` at the prompt and approve the pkexec dialogs for the volume `rsync`s. Expected:
   images loaded onto the PCI daemon, old stack `down`, three volumes copied, infra then app `up`,
   and `fingerprint MATCH — data preserved` (equal to the baseline). Answer `y` at
   `Repoint cron now?` only after the match.

3. **If verification fails, roll back.**

   ```bash
   ./migrate.sh rollback
   ```

   Expected: old stack back up on the church daemon, PCI stack `down`, cron unfrozen. The script
   aborts before repointing cron on any fingerprint mismatch.

## Verification

- **Serving:** `curl -sk https://localhost/healthz` returns the app health payload (nginx runs on
  the PCI daemon after cutover).
- **Data preserved:** `./migrate.sh verify` prints the same `rows=`/`tables=` as the window baseline.
- **Scope:** church `docker info --format '{{.DockerRootDir}}'` still reports
  `/opt/jol/data/docker`, while the PCI socket reports `/opt/jolarca/data/docker`.

## Troubleshooting

- **`No such container ... namespace=moby` flooding the journal:** dockerd is on the shared system
  containerd. Confirm the unit `ExecStart` has
  `--containerd /run/docker-jolarca/containerd.sock` and containerd is `active`.
- **`process with PID ... is still running`:** pidfile/exec-root collision with the church daemon.
  Confirm `--pidfile /run/docker-jolarca/docker.pid --exec-root /run/docker-jolarca`.
- **`You specified -b & --bip, mutually exclusive`:** `daemon.json` must use `"bridge": "none"` and
  rely on `default-address-pools`, not a named bridge plus `--bip`.
- **Units fail on boot:** both carry `RequiresMountsFor=/opt/jolarca`; verify the LV mount with
  `findmnt /opt/jolarca` before restarting.

## Escalation

If the marketplace cannot be restored on the PCI daemon within the window, run rollback (above) and
escalate per the [escalation policy](../../on-call/escalation-policy.md).

## References

- `ADR-0008` — `jolarca-infrastructure/docs/adr/0008-per-org-docker-daemon.md` (proposed).
- Migration tooling — `~/docker-jolarca-phase1/` (`migrate.sh`, staged unit + `daemon.json` copies).
- Related: [Restart a Service](example-service-restart.md),
  [Roll Back a Deployment](../application/example-deploy-rollback.md),
  [Backup and Restore](../../continuity/backup-restore.md).
