# Traceability Matrix
# Project: [PROJECT NAME] | Updated: [DATE]

---

## Purpose

Maps every requirement to the source file(s), test file(s), and ICM artifacts that
implement and verify it.  Used by `check_requirements.py` and manual audits to
confirm that no requirement is implemented without documentation, and no
documentation exists without a corresponding implementation.

---

## Matrix

| REQ ID | Title | Status | Source File(s) | Test File(s) | Impl Artifact | Val Artifact |
|--------|-------|--------|----------------|--------------|---------------|--------------|
| REQ-01 | [title] | Baselined | — | — | — | — |
| REQ-02 | [title] | Baselined | — | — | — | — |
| REQ-NF-01 | [title] | Baselined | — | — | — | — |

---

## Column Definitions

| Column | Content |
|--------|---------|
| REQ ID | Unique identifier matching the requirements register |
| Title | Short title copied from the register |
| Status | Copied from the register — keep in sync |
| Source File(s) | `src/` paths of files that implement the requirement |
| Test File(s) | `src/tests/` paths of test files that cover the requirement |
| Impl Artifact | `input_<REQ-ID>_implementation.md` — present or `—` |
| Val Artifact | `input_<REQ-ID>_validation.md` — present or `—` |

---

## Maintenance Rules

- Update this matrix whenever the register Status column changes.
- A row where Status is `Implemented` or `Verified` must have non-empty Source File(s),
  Impl Artifact, and Val Artifact columns.
- A row where Status is `Baselined` may have all trace columns as `—`.
- `Superseded` rows: keep the row, set all trace columns to `—` (no new implementation needed).
