---
id: sec-example-suspected-breach
title: Example — Respond to a Suspected Breach
category: security
severity: sev1
owner: Jolarca Ops
status: draft
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
rto: 1h
tags:
  - example
  - security
  - incident
related_controls:
  - ISO27001:A.5.26
  - SOC2:CC7.4
  - GDPR:Art.32
description: Illustrative runbook for the first hour of a suspected security breach.
---

> **Illustrative example.** Replace every `<REPLACE: ...>` token with verified production values
> before marking this `status: active`. A real breach response is time-critical — rehearse this
> before you need it. See the [runbook standard](../../docs/governance/runbook-standard.md).

# Example — Respond to a Suspected Breach

## Purpose & scope

Contain and investigate a suspected security breach (unauthorized access, credential leak, data
exfiltration, ransomware). Covers the **first hour**; long-term forensics and regulatory
notification are separate processes.

## Preconditions

- Authority to isolate systems: `<REPLACE: who can authorize isolation>`.
- Access to the incident bridge: `<REPLACE: bridge details>`.
- The [`security policy`](../../SECURITY.md) for disclosure obligations.

## Impact & safety

- **Blast radius:** unknown until contained — assume worst case.
- **Containment may cause outages.** Isolating a compromised host or network segment will affect
  legitimate traffic. Containment first, availability second for security incidents.
- **Do not** power off or reboot suspected systems — preserve volatile evidence.

## Steps

1. **Declare the incident.** Open the incident bridge and set severity to `sev1` per the
   [severity matrix](../../on-call/severity-matrix.md).

2. **Identify the scope.**

   ```bash
   <REPLACE: commands to check auth logs, active sessions, unusual processes>
   ```

   Expected: a list of affected systems and accounts.

3. **Contain.** Isolate the affected systems from the network.

   ```bash
   <REPLACE: isolation command, e.g. security group change, firewall rule>
   ```

   Expected: no inbound or outbound traffic from the isolated systems.

4. **Preserve evidence.** Collect volatile data before anything else changes.

   ```bash
   <REPLACE: evidence collection commands, e.g. memory dump, process list, open connections>
   ```

   Expected: evidence stored in `<REPLACE: secure evidence location>` with chain-of-custody log.

5. **Rotate credentials.** For every account or key that may be compromised, rotate immediately.

   ```bash
   <REPLACE: credential rotation commands>
   ```

   Expected: old credentials no longer accepted; new credentials in use.

6. **Communicate.** Notify stakeholders per the [escalation policy](../../on-call/escalation-policy.md).
   If personal data may be involved, notify the data-protection contact for GDPR Art. 33/34
   assessment.

## Verification

- Isolated systems have no network connectivity to production.
- Rotated credentials are in use and old credentials are revoked.
- Evidence is securely stored with a documented chain of custody.
- The incident is recorded as a post-mortem under
  [`../../incidents/postmortems/`](../../incidents/postmortems/).

## Escalation

If the breach scope exceeds initial containment, or if personal data is confirmed to be involved,
escalate immediately per the [escalation policy](../../on-call/escalation-policy.md) and follow the
[incident response procedure](../../on-call/incident-response.md).

## References

- Security policy: [`../../SECURITY.md`](../../SECURITY.md)
- Incident response: [`../../on-call/incident-response.md`](../../on-call/incident-response.md)
- Evidence register: [`../../docs/compliance/evidence-register.md`](../../docs/compliance/evidence-register.md)
