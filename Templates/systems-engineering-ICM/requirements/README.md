# Requirements

Requirements management — capture, triage, traceability, and status tracking.

## Contents

| Path | Purpose |
|------|---------|
| `workflows/03-baseline/requirements-register.md` | Master register — every requirement with ID, title, priority, status, trace |
| `workflows/04-trace/traceability-matrix.md` | Maps REQ IDs to source files, test files, and ICM artifacts |
| `AGENT.md` | Agent contract — includes the full icm-validate procedure |

## Status Lifecycle

```
Baselined → Implemented → Verified
                         (or Superseded at any point)
```

## Automated Consistency Check

Run from the project root:

```bash
python check_requirements.py
```

This checks every Implemented/Verified row for missing ICM artifacts and
flags orphan artifact files with no register entry.
For semantic validation (does the code actually implement the requirement?)
follow the icm-validate procedure in `AGENT.md`.
