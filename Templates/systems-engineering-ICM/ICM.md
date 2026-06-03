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

## Workspace Routing Table

| Workspace | Route When |
|-----------|-----------|
| `source-development/` | Writing, modifying, or reviewing source code |
| `data-pipeline/` | Ingesting, transforming, validating, or loading data |
| `testing-validation/` | Writing or running unit, integration, or system tests |
| `documentation/` | Creating or updating any technical document |
| `requirements/` | Capturing, triaging, or tracing requirements |
| `risk-management/` | Identifying, assessing, or mitigating project risks |
| `metrics/` | Defining, collecting, or reporting on KPIs |
| `devops-release/` | Building, packaging, deploying, or monitoring releases |
| `sales/` | Creating customer-facing materials or proposals |
| `inbox/` | Any unrouted or unclassified incoming task |

---

## Escalation Conditions (Global)

Escalate to human operator when:
- Requirements conflict across workspaces
- Approvals are missing for a release or deployment
- A dependency is unresolved and blocking progress
- System behaviour is ambiguous or undocumented

---

## Version Control

Files that MUST be gitignored:
- Any file containing credentials (`.env`, `*.key`, `*.pem`, `secrets.*`)
- Runtime-modified configuration files (`settings.json`, user data files)
- Build output directories (`dist/`, `build/`, `__pycache__/`)
- Virtual environments (`.venv/`, `node_modules/`)
- IDE and local settings (`*.local.json`, `.DS_Store`)

The only committed credential file should be the example template (`.env.example`).
