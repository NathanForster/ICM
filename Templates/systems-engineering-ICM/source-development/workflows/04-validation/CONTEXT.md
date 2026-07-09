# Stage Contract — 04-validation

## Stage Purpose

Review a validation brief for an implemented requirement and produce a
validation assessment that either confirms the evidence supports marking the
requirement Implemented, or lists what evidence is missing.

## Input Schema

An `input_<REQ-ID>_validation.md` file containing:

1. **Lint result** — pass/fail and any warnings
2. **Logic review** — key conditions verified manually
3. **Edge cases tested** — boundary/error scenarios exercised
4. **Test results** — test file, count, pass/fail
5. **Overall result** — PASS or FAIL

## Transformation Behaviour

For the brief in this folder:

- Confirm every section of the input schema is present and non-empty
- Check the claimed edge cases against the risks listed in the corresponding
  `output_03-implementation.md` review — flag any risk without matching evidence
- Verify the overall PASS/FAIL verdict is consistent with the individual results
- Flag any vague evidence ("works fine", "tested manually") that lacks specifics

## Output Schema

Write `output_04-validation.md` containing exactly these sections:

```
# Validation Assessment — <REQ-ID>
## Verdict            (EVIDENCE SUFFICIENT | EVIDENCE INSUFFICIENT)
## Evidence Summary   (table: check | result | evidence cited)
## Gaps               (bulleted; "None" if empty)
## Register Action    (e.g. "Advance REQ-42 to Implemented" or "Hold at Baselined")
```

Never output EVIDENCE SUFFICIENT when a required input section is missing —
use `[ERROR: DATA_NOT_FOUND_IN_ARTIFACT]` and verdict EVIDENCE INSUFFICIENT.
