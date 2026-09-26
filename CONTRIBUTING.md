# Contributing to jolarca-runbooks

This repository is operational documentation relied upon during incidents and audits. Treat
every change as if an auditor — or an on-call engineer at 03:00 — will read it under pressure.

## Ground rules

- **No secrets, ever.** No credentials, tokens, private keys, internal hostnames, or customer
  data. Pre-commit runs `detect-private-key`; keep it that way.
- **No placeholders in committed content.** Every `<REPLACE: ...>` token must be resolved before
  merge. `make validate` and review enforce this.
- **Verify before you write.** If you cannot confirm a command, threshold, or contact, say so in
  the pull request rather than guessing.

## Making a change

1. Create a branch: `git switch -c <type>/<short-description>` (e.g. `runbook/db-failover`).
2. For a new runbook, copy `runbooks/_templates/runbook-template.md` into the right category.
3. Fill in valid front-matter (see `docs/governance/runbook-standard.md`).
4. Run the checks locally:

   ```bash
   make install   # first time only
   make ci        # lint + validate + test
   make render control-map   # regenerate catalogs and the control map
   ```

5. Commit the regenerated files (`runbooks/README.md`, `docs/index.md`,
   `docs/compliance/control-mapping.md`) so CI sees no drift.
6. Open a pull request and complete the template.

## Review & approval

Changes to runbooks, on-call, and continuity documents require review and an recorded approval
per `docs/governance/review-and-approval.md`. As a solo-maintainer repo, the maintainer performs
a structured self-review against that checklist; the trail is captured in the front-matter
(`last_reviewed`, `review_due`, `approvals`) and the merged pull request.

## Commit conventions

Use [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`,
`chore:`. Keep the `CHANGELOG.md` up to date for anything notable.
