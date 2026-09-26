# Continuity (BCP / DR)

How Jolarca keeps running when things go badly wrong. This is the single source of truth for
business continuity and disaster recovery.

## Documents

| Document | Purpose |
|----------|---------|
| [`rto-rpo-register.md`](rto-rpo-register.md) | Recovery objectives for every critical service. |
| [`backup-restore.md`](backup-restore.md) | Backup schedule, retention, and restore procedure. |
| [`bcp/business-continuity-plan.md`](bcp/business-continuity-plan.md) | How the business continues during a disruption. |
| [`dr/disaster-recovery-plan.md`](dr/disaster-recovery-plan.md) | How to recover from a disaster. |

## When to use these

- **Routine incident** (sev3/sev4): use the [runbooks](../runbooks/README.md).
- **Major incident** (sev1/sev2): follow the [incident response procedure](../on-call/incident-response.md);
  if recovery cannot be achieved within the RTO, escalate to the DR plan.
- **Disaster** (region failure, data-center loss, prolonged outage): activate the DR plan.
- **Business continuity** (supply-chain failure, key-person unavailability, regulatory change):
  activate the BCP.

## Testing

Every plan in this section must be tested at least once per year. Test records are indexed in the
[`evidence register`](../docs/compliance/evidence-register.md).

## Compliance

These documents satisfy ISO/IEC 27001:2022 A.5.29 (ICT readiness for business continuity) and
support SOC 2 CC9.1 and GDPR Art. 32. See
[`../docs/compliance/iso-27001-a5-29.md`](../docs/compliance/iso-27001-a5-29.md) for the full
conformance narrative.
