# source-development Workflows

Stage folders for the per-requirement development pipeline.

## Stage Numbering Convention

Stage numbers follow the **project-wide requirement lifecycle**, shared with
`requirements/workflows/`:

| # | Lifecycle phase | Owning workspace | Stage folder |
|---|-----------------|------------------|--------------|
| 01 | Capture | `requirements/` | *(performed directly in the register — no stage folder)* |
| 02 | Triage | `requirements/` | *(performed directly in the register — no stage folder)* |
| 03 | Baseline / Implementation | `requirements/` + `source-development/` | `03-baseline/` (register), `03-implementation/` (briefs) |
| 04 | Trace / Validation | `requirements/` + `source-development/` | `04-trace/` (matrix), `04-validation/` (briefs) |

The same number in two workspaces means the same lifecycle phase viewed from two
sides: `03-baseline` freezes *what* to build while `03-implementation` records *how*
it was built; `04-trace` maps requirements to artifacts while `04-validation` records
the evidence.

## Stage Folder Anatomy

Each stage folder contains:

| File | Role |
|------|------|
| `CONTEXT.md` | The **stage contract** — what this stage does, its required input and output schema. Loaded as Layer 2 by the advanced overlay's `.icm-runner.py`. |
| `input_<REQ-ID>_<stage>.md` | Input brief written by the agent/human before the stage runs |
| `output_<stage-folder>.md` | Stage output *(produced by `.icm-runner.py` in advanced instances; written manually in base instances)* |

Keep completed artifacts in the stage folder — they are the audit trail.
