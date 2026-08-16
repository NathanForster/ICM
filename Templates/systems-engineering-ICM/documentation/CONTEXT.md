# documentation CONTEXT

## Workspace Mission

This workspace owns all tasks related to technical documentation and plans.

## Operational Rules

- preserve traceability
- document assumptions
- maintain deterministic behavior
- follow workflow stages

## Never

- fabricate results
- bypass validation
- modify unrelated workspaces

## Formal Deliverables

For DoD-contract or formally governed deliverables (SRS, SDD, STP, STR, RTVM, user
manuals, UAT records, etc.):

- Load the relevant DID digest or template from the companion **SE-Deliverables**
  library (`.ai/SE-Deliverables/`) — see `DIDs/GUIDE.md` there for DoD selection
  guidance and the document dependency map.
- **Do not copy library files into this project.** Generate the deliverable documents
  themselves in the project's `docs/` folder, named `docs/<ACRONYM>-<PROJECT>.md`
  (e.g. `docs/SRS-<PROJECT>.md`), structured per the governing DID or template. The map
  of documents to their definitions is `docs/DELIVERABLES.md`.
