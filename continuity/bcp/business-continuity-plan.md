---
id: continuity-bcp
title: Business Continuity Plan (BCP)
category: continuity
owner: Jolarca Ops
status: active
last_reviewed: "2026-09-26"
review_due: "2027-03-26"
rto: varies
rpo: varies
related_controls:
  - ISO27001:A.5.29
  - SOC2:CC9.1
description: How the business continues to operate during a disruption — people, processes, and priorities.
---

# Business Continuity Plan (BCP)

The BCP ensures the business can continue to deliver critical services during a disruption. It is
broader than the DR plan: it covers people, processes, suppliers, and communication — not just
technology.

## Purpose

- Maintain critical business functions during a disruption.
- Minimize impact to customers, revenue, and reputation.
- Provide a clear decision framework for the maintainer and stakeholders.

## Scope

This plan covers:

- **People:** key-person dependencies, remote-work capability, succession.
- **Processes:** critical workflows that must continue (e.g. customer support, billing).
- **Suppliers:** dependencies on third-party services and contingency plans.
- **Technology:** covered in detail by the [DR plan](../dr/disaster-recovery-plan.md).

## Activation criteria

Activate the BCP when:

- A critical service is unavailable for longer than its RTO.
- A key person is unavailable and no successor is immediately ready.
- A supplier failure impacts critical business functions.
- A regulatory or legal obligation requires immediate action (e.g. data-breach notification).

## Roles and responsibilities

| Role | Responsibility |
|------|----------------|
| **Maintainer** | Activate the plan; make go/no-go decisions; communicate to stakeholders. |
| **On-call engineer** | Execute technical recovery per the [DR plan](../dr/disaster-recovery-plan.md). |
| **Customer support** | Communicate with customers; manage expectations. |
| **Legal / data-protection** | Assess regulatory obligations (e.g. GDPR Art. 33/34 notification). |

## Communication

- **Internal:** announce activation on `<REPLACE: internal comms channel>`.
- **Customers:** draft a notification; send only after maintainer approval.
- **Regulators:** if personal data is involved, notify the data-protection authority within 72h
  (GDPR Art. 33).

## Recovery priorities

Recover services in order of tier (see [`rto-rpo-register.md`](../rto-rpo-register.md)):

1. **Critical** (RTO ≤ 4h): primary database, primary application, authentication.
2. **Standard** (RTO ≤ 24h): batch processing, non-critical services.
3. **Low** (RTO ≤ 8h): internal tools, non-urgent workflows.

## Testing

- **Annual tabletop exercise:** walk through the BCP with all roles; identify gaps.
- **After any major change:** re-test if the change affects critical functions.
- **Test records:** indexed in the [`evidence register`](../../docs/compliance/evidence-register.md).

## Review

This plan is reviewed every 6 months or after any activation. The review is recorded in the
front-matter and the evidence register.
