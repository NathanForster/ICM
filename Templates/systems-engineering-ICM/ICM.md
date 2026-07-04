# Systems Engineering ICM

## Purpose

This repository is a systems-engineering-focused Interpretable Context Methodology (ICM) framework.

It is intended for:
- automation systems
- software engineering
- DAQ systems
- hardware/software integration
- engineering governance
- validation-heavy development

## Agent Instructions

1. Read `ICM.md`
2. Read top-level `CONTEXT.md`
3. Route into the correct workspace
4. Load local workspace context
5. Preserve engineering traceability
6. Operate only within workspace scope

## Architectural Principles

- deterministic routing
- workflow isolation
- engineering traceability
- validation-first execution
- explicit ownership
- persistent operational memory

---

## Workspace Routing

The **top-level `CONTEXT.md` is the single source of truth for workspace routing.**
Consult its Workspace Routing Table before starting any task. Do not route from
memory or from this file.

---

## Escalation Conditions (Global)

Escalate to human operator when:
- Requirements conflict across workspaces
- Approvals are missing for a release or deployment
- A dependency is unresolved and blocking progress
- System behaviour is ambiguous or undocumented
- A task does not match any row in the routing table

---

## Version Control

See the **Version Control** section of the top-level `CONTEXT.md` for the canonical
list of files that must be gitignored. Never commit credentials; the only committed
credential file should be the example template (`.env.example`).
