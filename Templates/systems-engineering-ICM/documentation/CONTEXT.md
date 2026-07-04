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

## Formal (DID-Based) Deliverables

For DoD-contract or formally governed deliverables (SRS, SDD, STP, STR, RTVM, etc.):

- Load the relevant digest from the ICM templates repository at
  `Templates/advanced-options/DIDs/` — see its `GUIDE.md` for selection guidance
  and the document dependency map.
- **Do not copy DID digest files into this project.** Generate the deliverable
  documents themselves in the project's `docs/` folder (e.g. `docs/SRS.md`),
  structured per the governing DID.
