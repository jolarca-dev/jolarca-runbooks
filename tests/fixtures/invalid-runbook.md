---
id: Fixture Invalid Example
title: x
category: not-a-category
owner: ""
status: published
last_reviewed: 26-09-2026
related_controls: []
---

# Fixture — Invalid Runbook

This fixture is intentionally invalid. It omits the required `review_due` field, violates the
`id` pattern, the `title` minimum length, the `category`/`status` enums, the `owner` minimum
length, the `last_reviewed` date pattern, and the `related_controls` minimum item count. The
test suite asserts the validator rejects all of it.
