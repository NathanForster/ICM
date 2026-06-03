# PROJECT BLUEPRINT & ROUTING MAP

This document establishes the macro-workflow, execution ordering, and data handoff
contracts for the active project workspace. All execution scripts and processing
layers look to this blueprint to navigate the repository.

> **Customise this file when creating a new project instance.**
> Replace every `[PLACEHOLDER]` with project-specific content.
> Delete this instruction block when the file is complete.

---

## 1. PROJECT OBJECTIVE

**Name:** `[PROJECT NAME]`

**Purpose:** `[One-paragraph description of what this project produces and why.]`

**Primary output:** `[Deliverable type — e.g. software application, data report, document, API]`

---

## 2. REPOSITORY PIPELINE TOPOLOGY

The workflow is strictly decoupled into linear, isolated execution stages.
Each stage folder contains its own local `CONTEXT.md` governing its internal
transformation behaviour.

```
  [Raw Input / Requirements]
          │
          ▼
  ┌───────────────────┐
  │  01-<stage-name>/ │  ──►  output_01-<stage-name>.md
  └────────┬──────────┘
           │  (promoted by run_pipeline.sh)
           ▼
  ┌───────────────────┐
  │  02-<stage-name>/ │  ──►  output_02-<stage-name>.md
  └────────┬──────────┘
           │  (promoted by run_pipeline.sh)
           ▼
  ┌───────────────────┐
  │  03-<stage-name>/ │  ──►  output_03-<stage-name>.md  (final deliverable)
  └───────────────────┘
```

Replace the stage names above with the actual stages for this project.

---

## 3. STAGE EXECUTION MATRIX

### STAGE 1: `01-[stage-name]/`

- **Purpose:** `[What this stage does to its inputs]`
- **Primary input:** `input_[name].[ext]`
- **Expected output:** `output_01-[stage-name].md`
- **Downstream consumer:** Stage 2

### STAGE 2: `02-[stage-name]/`

- **Purpose:** `[What this stage does to its inputs]`
- **Primary input:** `input_[name].md` (promoted from Stage 1 output)
- **Expected output:** `output_02-[stage-name].md`
- **Downstream consumer:** Stage 3

### STAGE 3: `03-[stage-name]/`

- **Purpose:** `[What this stage does to its inputs]`
- **Primary input:** `input_[name].md` (promoted from Stage 2 output)
- **Expected output:** `output_03-[stage-name].md`
- **Downstream consumer:** End consumer / release

---

## 4. HUMAN INTERVENTION GATE POLICY

This pipeline enforces a **strict gate pattern** between stages.

1. When a stage completes, `run_pipeline.sh` pauses automatically.
2. A human operator inspects the output file in that stage's folder.
3. The operator may edit the output directly to correct errors or adjust scope.
4. On confirmation, the runner promotes the (possibly edited) output to become
   the immutable `input_*.md` for the next stage — preventing hallucinated drift
   across stage boundaries.

---

## 5. WORKSPACE ROUTING

| Workspace | Route When |
|-----------|-----------|
| `source-development/` | Writing, modifying, or reviewing source code |
| `data-pipeline/` | Ingesting, transforming, validating, or loading data |
| `testing-validation/` | Writing or running tests |
| `documentation/` | Creating or updating any technical document |
| `requirements/` | Capturing, triaging, or tracing requirements |

---

## 6. VERSION CONTROL

Files that MUST be gitignored:
- Any file containing credentials (`.env`, `*.key`, `*.pem`, `secrets.*`)
- Runtime-modified configuration files (`settings.json`, user data files)
- Build output directories (`dist/`, `build/`, `__pycache__/`)
- Virtual environments (`.venv/`, `node_modules/`)
- IDE and local settings (`*.local.json`, `.DS_Store`, `*.user`)

The only committed credential file should be the example template (`.env.example`).
