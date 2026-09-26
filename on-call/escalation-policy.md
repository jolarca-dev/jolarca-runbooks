---
id: on-call-escalation-policy
title: Escalation Policy
category: on-call
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
related_controls:
  - ISO27001:A.5.24
  - ISO27001:A.5.26
  - SOC2:CC7.4
description: When and how to escalate an incident — the right person, at the right time, with the right information.
---

# Escalation Policy

Escalation is not a failure — it is the mechanism that keeps incidents from growing. Escalate
**early, clearly, and without apology**.

## When to escalate

- You have been working for **15 minutes** with no clear diagnosis.
- The impact is growing or you cannot confirm it is contained.
- The incident is **sev1** or **sev2**.
- You need authority you do not have (isolate a production network, engage a vendor, notify
  customers, involve legal or data-protection).
- You are the on-call engineer and you are too close to the problem to think clearly.

## Escalation ladder

| Level | Who | When | Contact |
|:-----:|-----|------|---------|
| **L1** | On-call engineer | First responder. | `<REPLACE: paging tool>` |
| **L2** | Subject-matter expert for the affected domain | L1 cannot diagnose or contain within 15 min. | `<REPLACE: SME contact / secondary on-call>` |
| **L3** | Maintainer / engineering lead | Sev1/sev2 unresolved after 30 min, or blast radius expanding. | `<REPLACE: maintainer contact>` |
| **L4** | Executive / legal / data-protection | Confirmed or suspected data breach, regulatory obligation, or customer-impacting outage > 1h. | `<REPLACE: executive / legal / DPO contact>` |

## How to escalate

Use the **WWHW** format on the incident bridge and in the written record:

- **What** is happening (one sentence).
- **Who** is affected (users, services, data).
- **How bad** (severity, duration, growth).
- **What you need** from the person you are pulling in.

Example:

> "Production checkout is failing for ~30% of users (sev2, 20 min, growing). I need a database
> SME to help diagnose — I suspect a connection-pool exhaustion but cannot confirm."

## Do not

- Wait until you are sure. Escalate on suspicion; certainty comes from more eyes.
- Escalate silently (a Slack message is not enough for sev1/sev2 — use the bridge and page).
- Assume someone else is escalating. If you see the need, own the escalation or confirm who has it.
