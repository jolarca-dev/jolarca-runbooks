# Security Policy

## Reporting a vulnerability

Please report security vulnerabilities **privately**. Do **not** open a public issue or pull
request, and do not commit details to this repository.

- Email: `<REPLACE: security contact, e.g. security@jolarca.example>`
- PGP key: `<REPLACE: public key fingerprint / URL>`
- Response target: acknowledgment within 2 business days.

## Scope

This repository contains operational documentation, not running services. A "vulnerability" here
means: committed secrets or credentials, exposure of internal infrastructure details, personal
data (GDPR), or instructions that would cause an operator to weaken a security control.

## Handling

1. The maintainer triages and confirms the finding.
2. Sensitive content is removed from history if required (see below).
3. Any exposed secret is rotated immediately — removal from a file does not un-leak it.
4. A fix and, where warranted, a post-mortem under `incidents/postmortems/` are recorded.

## Secret exposure / history rewriting

If a secret is committed, treat it as compromised. Rotate it first, then purge it from history
with `git filter-repo` or BFG, and force-push under the maintainer's explicit approval. Record the
event in the evidence register (`docs/compliance/evidence-register.md`).

## Disclosure

We follow coordinated disclosure. We will not publish details until a fix is available and, where
applicable, affected parties have been notified in line with GDPR Art. 33/34 timelines.
