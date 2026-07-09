# Examples

Worked ICM project instances, for reference only.

These are **filled-in examples**, not templates. They show what a generated
instance looks like after real work has flowed through it — routing decided,
requirements captured, briefs written, code implemented, evidence recorded,
and state handed off.

| Example | Template basis | What it demonstrates |
|---------|----------------|----------------------|
| [temp-logger/](temp-logger/) | systems-engineering-ICM (base, no overlay) | One requirement (REQ-01) taken through the full lifecycle — Baselined → Implemented → Verified — with implementation/validation briefs, register, traceability matrix, ADR, source, test, and session handoff. A second requirement (REQ-02) left Baselined to show the open state. |

## How to Read an Example

1. Start with the instance's `CONTEXT.md` — the routing map
2. Read `requirements/workflows/03-baseline/requirements-register.md` — the state of work
3. Follow REQ-01 through: implementation brief → code → validation brief → matrix row
4. Finish with `state/HANDOFF.md` — how a session hands context to the next

Real project instances should live **outside** this repository (sibling folders
under `.ai/`) — these examples live here only because they document the methodology.
