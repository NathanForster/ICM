# Requirements Register — Baseline v1.0
# Project: [PROJECT NAME] | Baselined: [DATE] | Updated: [DATE]

---

## Status Key

| Status | Meaning |
|--------|---------|
| Baselined | Approved and frozen — ready to implement |
| Implemented | Code exists in `src/`; ICM artifacts written |
| Verified | Tested or manually confirmed working |
| Superseded | Replaced by a newer requirement — do not implement |

---

## How to Use This Register

1. **Add a requirement** — assign the next available REQ ID, set Status to `Baselined`.
2. **Start implementation** — leave Status as `Baselined` until both ICM artifacts exist.
3. **After stage 04 runs** — change Status to `Implemented`; add source file(s) to Trace.
4. **After tests confirm** — change Status to `Verified`.
5. **If superseded** — set Status to `Superseded` and note the replacement REQ ID in Trace.

Run `python check_requirements.py` at any time to verify register consistency and detect
missing ICM artifacts.

---

## Functional Requirements

| ID | Title | Priority | Status | Trace |
|----|-------|----------|--------|-------|
| REQ-01 | [Requirement title] | Must Have | Baselined | — |
| REQ-02 | [Requirement title] | Should Have | Baselined | — |
| REQ-03 | [Requirement title] | Nice to Have | Baselined | — |

---

## Non-Functional Requirements

| ID | Title | Priority | Status | Trace |
|----|-------|----------|--------|-------|
| REQ-NF-01 | [Constraint title] | Must Have | Baselined | — |
| REQ-NF-02 | [Constraint title] | Must Have | Baselined | — |

---

## Priority Definitions

| Value | Meaning |
|-------|---------|
| Must Have | Core to the system — cannot ship without it |
| Should Have | High value — include unless blocked by a Must Have |
| Nice to Have | Low risk to defer — implement only when other work is clear |

---

## Supersessions

List requirements that have been replaced here, retaining the original row for traceability.

| ID | Title | Priority | Status | Superseded By |
|----|-------|----------|--------|---------------|
