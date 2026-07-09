# requirements Workflows

Stage folders for the requirements lifecycle.

## Stage Numbering Convention

Stage numbers follow the **project-wide requirement lifecycle**, shared with
`source-development/workflows/` (see its README for the full table):

| # | Phase | Artifact here |
|---|-------|---------------|
| 01 | Capture | *(performed directly in the register — new row, Status blank until triaged)* |
| 02 | Triage | *(performed directly in the register — priority assigned, duplicates merged)* |
| 03 | Baseline | `03-baseline/requirements-register.md` — the master register |
| 04 | Trace | `04-trace/traceability-matrix.md` — requirement ↔ artifact mapping |

Capture and triage are lightweight register operations, so they have no stage
folders — the register itself is their artifact. Folders exist only where a
distinct document is produced.
