# Stage Contract — 03-implementation

## Stage Purpose

Review an implementation brief for a Baselined requirement and produce an
implementation review that either clears the brief for coding or lists the
gaps that must be resolved first.

## Input Schema

An `input_<REQ-ID>_implementation.md` file containing:

1. **Design summary** — what will be built and why this approach
2. **Files to be modified** — exact paths
3. **Key functions / classes / constants** — signatures or names
4. **Constraints** — edge cases, performance limits, interface contracts

## Transformation Behaviour

For the brief in this folder:

- Verify the design addresses the requirement text as written in the register
- Check that every file to be modified is consistent with the design summary
- Identify unstated edge cases, error paths, or interface impacts
- Confirm constraints do not conflict with the standards quoted in the brief (the brief
  author copies the applicable rules from `standards/` into the brief — the runner does not
  load `standards/`)

## Output Schema

Write `output_03-implementation.md` containing exactly these sections:

```
# Implementation Review — <REQ-ID>
## Verdict          (CLEARED | GAPS FOUND)
## Design Assessment (2-5 bullets)
## Risks and Edge Cases (bulleted; "None identified" if empty)
## Preconditions Before Coding (bulleted; "None" if empty)
```

Do not invent requirements not present in the brief. If information required
by this contract is missing from the brief, output
`[ERROR: DATA_NOT_FOUND_IN_ARTIFACT]` for that section.
