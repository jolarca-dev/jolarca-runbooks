# Incidents

Records of incidents and the lessons learned from them. This is how Jolarca gets better at
responding to failure.

## Structure

- [`postmortems/`](postmortems/) — post-incident reviews, written using the
  [`post-mortem template`](../runbooks/_templates/postmortem-template.md).

## How to write a post-mortem

After every sev1 or sev2 incident (and any sev3 with a lesson), write a post-mortem:

1. Copy [`../runbooks/_templates/postmortem-template.md`](../runbooks/_templates/postmortem-template.md)
   into `postmortems/YYYY-MM-DD-<short-name>.md`.
2. Fill in every section; be specific about timelines and impact.
3. **Blameless:** focus on systems and processes, not individuals.
4. Every action item has an owner and a due date.
5. Schedule a review within 5 business days.
6. Track action items to completion.

## Evidence collection

During an incident, collect evidence for the post-mortem and for audit:

- Logs, metrics, and traces from the incident window.
- Screenshots of dashboards and error states.
- Timeline of actions taken (with timestamps).
- Store in `<REPLACE: secure evidence location>` with a chain-of-custody log.

See the [`evidence register`](../docs/compliance/evidence-register.md) for retention requirements.

## Compliance

Post-mortems are evidence for ISO 27001 A.5.27 (learning from incidents) and A.5.28 (collection of
evidence), and support SOC 2 CC7.4/CC7.5. They are indexed in the
[`control mapping`](../docs/compliance/control-mapping.md).
