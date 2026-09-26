---
id: <category>-<short-name>
title: <Runbook Title>
category: <infrastructure|database|network|security|application>
severity: <sev1|sev2|sev3|sev4>
owner: Jolarca Ops
status: draft
last_reviewed: "<YYYY-MM-DD>"
review_due: "<YYYY-MM-DD>"
rto: <e.g. 30m>
rpo: <e.g. 1h>
tags:
  - <tag>
related_controls:
  - <FRAMEWORK:CONTROL e.g. ISO27001:A.5.29>
approvals: []
---

<!--
TEMPLATE — copy into runbooks/<category>/, fill every <...>, then delete this comment.
Rules: ../../docs/governance/runbook-standard.md
-->

# <Runbook Title>

## Purpose & scope

One or two sentences: what this runbook does and, explicitly, what it does **not** cover.

## Preconditions

- Access required: `<REPLACE: systems/roles>`
- Tools required: `<REPLACE: cli/console>`
- Authority to proceed: `<REPLACE: who must approve, or "on-call may proceed">`

## Impact & safety

- **Blast radius:** what is affected while this runs.
- **User impact:** degradation or outage expected.
- **Abort / rollback:** how to stop safely and revert. If irreversible, say so in bold.

## Steps

1. **<Step name>**

   ```bash
   <command>
   ```

   Expected: `<what confirms this step worked>`

2. **<Step name>**

   ```bash
   <command>
   ```

   Expected: `<...>`

## Verification

How to confirm the outcome objectively (health check, metric back to normal, test request).

## Escalation

When to escalate and to whom — see [`../../on-call/escalation-policy.md`](../../on-call/escalation-policy.md).

## References

- Dashboards: `<REPLACE: links>`
- Related runbooks: `<REPLACE: links>`
- Upstream docs: `<REPLACE: links>`
