# Agent Contract — documentation

## Inputs

- Documentation requests (user manual, development plan, validation report, release notes)
- Specifications, requirements, and source code changes to document
- Formal deliverable requirements (governing DIDs — see CONTEXT.md)
- Applicable standards from `standards/`

## Outputs

- Technical documents (manuals, plans, reports, release notes)
- Formal DID-governed deliverables in the project's `docs/` folder
- Updates to documentation workflow state

## Definition of Done

A document is Done when ALL of the following are true:

- [ ] Every required section of the governing template or DID is present
      (or explicitly marked "tailored out" with approval)
- [ ] Technical content verified against source code, specs, or test results —
      no unverified claims
- [ ] Requirement references use the exact REQ IDs from the requirements register
- [ ] Reviewed by the human operator or designated review step
- [ ] Document saved in its owned location and workflow state updated

## Escalate When

- Source material conflicts (spec says X, code does Y)
- A required section cannot be completed because upstream information is missing
- The governing DID or template for a formal deliverable is not identified
- A release-facing document lacks required approvals
