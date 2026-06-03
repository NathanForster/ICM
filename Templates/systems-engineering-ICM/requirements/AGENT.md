# Agent Contract — requirements

## Workspace Mission

Own all requirements capture, triage, traceability, and status validation.
This workspace is the single source of truth for what has been committed to,
what has been built, and what has been verified.

---

## Inputs

- New feature requests or change requests (from inbox or human operator)
- Source code changes (to update Trace column)
- ICM artifact directories (to check for missing briefs)
- Test results (to advance Status to Verified)

## Outputs

- Updated requirements register (`requirements-register.md`)
- Updated traceability matrix (`traceability-matrix.md`)
- Validation findings report (when running the validate procedure below)

---

## Definition of Done — per requirement

A requirement is fully closed when:

- [ ] Status = `Verified` in the register
- [ ] Trace column contains the implementing source file(s)
- [ ] `input_<REQ-ID>_implementation.md` exists in `source-development/workflows/03-implementation/`
- [ ] `input_<REQ-ID>_validation.md` exists in `source-development/workflows/04-validation/`
- [ ] At least one test in `src/tests/` covers the requirement (or human operator confirms manual verification)
- [ ] Register and matrix are in sync (Status matches between both documents)

---

## Requirements Validation Procedure (icm-validate)

Run this procedure on demand to audit the register against source code and ICM artifacts.
Produce a findings table, confirm with the human operator, then update the documents.

### Step 1 — Identify open rows

Read the register in full. Identify every row where Status is `Baselined` or `Implemented`
(i.e. not yet `Verified` or `Superseded`).

### Step 2 — For each open row, perform two checks

**2a. Code check**
- Use the Trace column as the starting point.
- Read the relevant source file(s) or grep for key symbols.
- Determine: fully implemented / partially implemented / not implemented.

**2b. Artifact check**
- Check for `input_<REQ-ID>_implementation.md` in `source-development/workflows/03-implementation/`
- Check for `input_<REQ-ID>_validation.md` in `source-development/workflows/04-validation/`
- Accept both `input_REQ-<N>_*.md` (uppercase) and `input_req<N>_*.md` (lowercase legacy) forms.
- Flag any `Implemented` row that is missing either artifact as needing backfill.

### Step 3 — Produce a findings table

Present this table to the human operator before writing anything:

| REQ ID | Title | Current Status | Code | Impl artifact | Val artifact | Proposed Status |
|--------|-------|----------------|------|---------------|--------------|-----------------|
| REQ-XX | ... | Baselined | ✅ present | ✅ present | ✅ present | Implemented |
| REQ-YY | ... | Implemented | ✅ present | ❌ missing | ❌ missing | Implemented (backfill needed) |

### Step 4 — On human confirmation, update both documents

**In the register:**
- Change the `Status` cell for each affected row.
- Append `(backfill needed)` to the Trace cell for any row missing artifacts.
- Update the `Updated:` datestamp in the file header.

**In the matrix:**
- Add or update the `Source File(s)` and artifact columns for affected rows.
- Update the `Updated:` datestamp in the file header.

Do not change titles, priorities, ADR references, or any other content.

### Step 5 — Report summary

- How many moved to Implemented
- How many moved to Verified
- How many remain Baselined (with reason)
- How many need artifact backfill
- How many code gaps found

---

## Rules

- **Never mark a requirement Verified** unless a test exists or the human confirms manual verification.
- **Superseded rows:** skip entirely — do not check for code or artifacts.
- **Partial implementation:** set Status to `Implemented` but append
  `(partial — <gap description>)` in the Trace column.
- **New code with no register entry:** flag to the human operator — do not silently assign a REQ ID.
- **Date stamps:** always use the current date from the system context (`currentDate` if available).
