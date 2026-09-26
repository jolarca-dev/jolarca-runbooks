## Description

<!-- What does this PR do? Why is it needed? -->

## Type of change

- [ ] New runbook
- [ ] Update to existing runbook
- [ ] On-call / incident procedure change
- [ ] Continuity (BCP/DR) change
- [ ] Governance / compliance documentation
- [ ] Tooling or CI change
- [ ] Other (describe below)

## Checklist

Before requesting review, confirm:

- [ ] Every new/updated runbook has valid YAML front-matter (`make validate` passes).
- [ ] No `<REPLACE: ...>` tokens remain in committed content (or they are explicitly logged as known gaps).
- [ ] No secrets, credentials, or personal data are included.
- [ ] Internal links resolve (`make lint` passes).
- [ ] `make render control-map` has been run and the regenerated files are committed.
- [ ] Tests pass (`make test`).
- [ ] The change has been reviewed against [`docs/governance/runbook-standard.md`](../docs/governance/runbook-standard.md).

## Related issues

<!-- Link any related issues, incidents, or runbooks. -->

## Reviewer notes

<!-- Anything the reviewer should pay special attention to? -->
