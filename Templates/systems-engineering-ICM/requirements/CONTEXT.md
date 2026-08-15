# requirements CONTEXT

## Workspace Mission

This workspace owns requirements management — capture, triage, baselining,
traceability, and status tracking.

## Allowed

- add, triage, and baseline requirements in the register
- update requirement status through the lifecycle (Baselined → Implemented → Verified)
- maintain the traceability matrix
- run `check_requirements.py` consistency checks

## Never

- change a requirement's status without the corresponding ICM artifacts
- skip lifecycle states (a register row must pass through Implemented before Verified)
- modify source code (route to `source-development/`)
- modify unrelated workspaces

## Formal Deliverable Note

For projects with formal or contractual traceability requirements, the DoD counterpart
of the traceability matrix is the **RTVM** (Requirements Traceability Verification
Matrix, DI-MGMT-82133A). A digest is available in the companion SE-Deliverables
library (`.ai/SE-Deliverables/DIDs/`) — see its `GUIDE.md` for related requirement
specification DIDs (SSS, SRS, IRS).
