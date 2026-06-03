# source-development CONTEXT

## Workspace Mission

This workspace owns all tasks related to software engineering and automation systems.
It is the single authoritative location for source code, implementation briefs,
validation briefs, and ICM pipeline stage outputs.

---

## Operational Rules

- Preserve requirements traceability (every implementation links to a REQ ID)
- Document assumptions in the implementation brief before writing code
- Maintain deterministic behaviour — no logic that differs between runs without reason
- Follow workflow stages — do not skip from requirements directly to code
- Run lint before writing the validation brief; include the result

---

## Mandatory Pipeline Sequence

When implementing any Baselined requirement, follow this sequence exactly.

| Step | Action | Artifact |
|------|--------|---------|
| 1 | Write implementation brief | `input_<REQ-ID>_implementation.md` |
| 2 | Run stage 03 | `output_03-implementation.md` |
| 3 | Write the code in `src/` | source files |
| 4 | Run lint; run regression tests | (results recorded in step 5) |
| 5 | Write validation brief | `input_<REQ-ID>_validation.md` |
| 6 | Run stage 04 | `output_04-validation.md` |
| 7 | Update requirements register | Status: Baselined → Implemented |
| 8 | Commit source + ICM artifacts + register | single git commit |

> Do not write code until step 2 is complete.
> Do not commit until step 6 is complete.

---

## Artifact Naming Convention

```
input_<REQ-ID>_implementation.md    e.g.  input_REQ-42_implementation.md
input_<REQ-ID>_validation.md        e.g.  input_REQ-42_validation.md

Grouped REQs:  input_REQ-<N>-<M>_implementation.md
               input_REQ-<N>-<M>_validation.md
```

Both uppercase (`REQ-42`) and legacy lowercase (`req42`) forms are accepted by
the runner and validation tooling for backwards compatibility, but new artifacts
should always use the uppercase hyphenated form.

---

## Validation Brief Required Content

Every `input_<REQ-ID>_validation.md` must include:

1. **Lint result** — pass/fail and any warnings
2. **Logic review** — key conditions verified manually
3. **Edge cases tested** — what boundary/error scenarios were exercised
4. **Test results** — test file, count, pass/fail
5. **Overall result** — `PASS` or `FAIL`

---

## Backfill Policy

If code was implemented without following the mandatory pipeline sequence:

1. Write the implementation brief describing what was actually built
2. Run stage 03
3. Write the validation brief covering actual test results
4. Run stage 04
5. Update the requirements register (do NOT skip Implemented — Baselined → Implemented → Verified)
6. Commit all artifacts together

Do not mark a requirement Verified until all pipeline artifacts exist.

---

## Never

- Fabricate lint or test results
- Bypass validation stages
- Modify files outside `src/` and this workspace without explicit routing
- Commit credentials or runtime-modified config files
