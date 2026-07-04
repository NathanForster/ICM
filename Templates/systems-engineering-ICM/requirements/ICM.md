# requirements ICM

## Purpose

Defines the interpretable structure of the `requirements` workspace.

## Context Loading Rules

Load:
- local CONTEXT.md
- `workflows/03-baseline/requirements-register.md` (the master register)
- `workflows/04-trace/traceability-matrix.md` (when tracing)
- AGENT.md (for the icm-validate procedure)

Avoid:
- unrelated workspaces
- source code (route implementation work to `source-development/`)
- unnecessary global state

## Operational Scope

Operate only within this workspace unless explicitly instructed.
