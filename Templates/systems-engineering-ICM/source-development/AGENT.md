# Agent Contract — source-development

## Inputs

- Baselined requirements (from requirements register)
- Implementation briefs (`input_<REQ-ID>_implementation.md`)
- Validation briefs (`input_<REQ-ID>_validation.md`)
- Engineering tasks and change requests

## Outputs

- Source code in `src/`
- ICM stage output artifacts (`output_03-implementation.md`, `output_04-validation.md`)
- Updated requirements register (Status column)
- Updated traceability matrix (Trace column)

---

## Definition of Done — per requirement

Every requirement is Done when ALL of the following are true:

- [ ] Implementation brief written (`input_<REQ-ID>_implementation.md`)
      — includes: design summary, files modified, key functions/classes, constraints
- [ ] Stage 03 run — `output_03-implementation.md` produced
- [ ] Code written in `src/` with no linting errors
- [ ] Validation brief written (`input_<REQ-ID>_validation.md`)
      — includes: lint result, logic review, edge cases, test results, PASS/FAIL verdict
- [ ] Stage 04 run — `output_04-validation.md` produced
- [ ] Requirements register Status updated: `Baselined` → `Implemented`
- [ ] Traceability matrix Trace column updated with source file(s)
- [ ] Source code + ICM artifacts + register committed in a single git commit

A requirement must not be marked `Verified` until a test in `src/tests/` or
`testing-validation/` explicitly covers it, or the human operator confirms
manual verification.

---

## Escalation Conditions

Escalate to the human operator when:

- Requirements conflict or are ambiguous
- A required approval or sign-off is missing before release
- A dependency (library, service, schema) is unresolved and blocking progress
- Behaviour is undocumented and the correct approach is genuinely unclear

---

## Behavioural Constraints

- Never fabricate lint results or test pass counts
- Never bypass a pipeline stage to save time
- Never commit credentials, `.env` files, or runtime-modified config
- Never modify files outside `src/` and `source-development/` without explicit routing
