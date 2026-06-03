# [PROJECT NAME] — Session Handoff Document
# Last updated: [DATE] | Last REQ: [REQ-ID] | Last commit: [SHA]

> **Purpose:** Preserve critical context across LLM session boundaries.
> Update sections 7 and 9 at the end of every working session.
> Keep this file committed to the repository so it travels with the code.

---

## 1. What This Project Is

`[One paragraph describing the project: what it does, what it does not do,
its deployment target, and its primary user.]`

---

## 2. Critical Paths

| What | Path |
|------|------|
| **Project root** | `[ABSOLUTE PATH]` |
| **Source root** | `[ABSOLUTE PATH]/src/` |
| **Venv Python** | `[ABSOLUTE PATH]/src/.venv/Scripts/python` (Windows) |
| **Venv Python** | `[ABSOLUTE PATH]/src/.venv/bin/python` (Linux/macOS) |
| **Credentials (NEVER COMMIT)** | `[ABSOLUTE PATH]/src/config/.env` |
| **Credentials example (safe)** | `[ABSOLUTE PATH]/src/config/.env.example` |
| **Requirements register** | `[ABSOLUTE PATH]/requirements/workflows/03-baseline/requirements-register.md` |
| **Traceability matrix** | `[ABSOLUTE PATH]/requirements/workflows/04-trace/traceability-matrix.md` |
| **ICM impl briefs** | `[ABSOLUTE PATH]/source-development/workflows/03-implementation/` |
| **ICM val briefs** | `[ABSOLUTE PATH]/source-development/workflows/04-validation/` |
| **Test files** | `[ABSOLUTE PATH]/src/tests/` |
| **This handoff file** | `[ABSOLUTE PATH]/state/HANDOFF.md` |

---

## 3. Runtime Versions

| Component | Version |
|-----------|---------|
| Language (e.g. Python) | `[VERSION]` |
| Key framework | `[VERSION]` |
| Test runner | `[VERSION]` |
| Linter | `[VERSION]` |
| OS | `[VERSION]` |

---

## 4. Key Terminal Commands

All commands assume `CWD = [project root]` unless noted.

```bash
# Lint
[lint command]

# Run regression / fast tests
[test command — headless / no UI]

# Run full test suite
[test command — full]

# Run the application
[run command]

# Full data/content pipeline
bash run_pipeline.sh

# Source-development pipeline (single REQ)
bash run_source_dev.sh <REQ-ID>

# Isolated ICM stage
python .icm-runner.py source-development/workflows 03-implementation
python .icm-runner.py source-development/workflows 04-validation

# Check requirements register consistency
python check_requirements.py
```

---

## 5. Security Constraints — NEVER Violate

- `src/config/.env` — contains live API keys and service credentials.
  **Gitignored. Never read its contents into a response. Never commit it.**
- Any `*.env.bak` or similar backup — same rule.
- All credentials flow via environment variables or `python-dotenv` at runtime.
- The only committed credential file is `src/config/.env.example` (placeholders only).

---

## 6. Architecture Overview

`[Brief description of major components, modules, or services.
A table or bullet list with file paths is ideal.]`

| Component | File / Path | Notes |
|-----------|-------------|-------|
| `[name]` | `src/[path]` | `[one-line description]` |

### Key patterns

```python
# [Document any non-obvious patterns that a new session must know]
# e.g. settings access, DB connection, LLM calls, signal patterns
```

---

## 7. ICM Pipeline State

### Next available REQ ID

**REQ-`[N+1]`** (last used: REQ-`[N]`)

### Register

- Location: `requirements/workflows/03-baseline/requirements-register.md`
- Current version: **v`[X.Y]`** (`[DATE]`)
- All requirements status: `[e.g. "All Verified or Superseded — no open Baselined rows"]`

### Pipeline sequence (mandatory for every Baselined requirement)

1. Write `input_<REQ-ID>_implementation.md` in `source-development/workflows/03-implementation/`
2. Run: `python .icm-runner.py source-development/workflows 03-implementation`
3. Write the code in `src/`
4. Run lint + tests
5. Write `input_<REQ-ID>_validation.md` in `source-development/workflows/04-validation/`
6. Run: `python .icm-runner.py source-development/workflows 04-validation`
7. Update register (Baselined → Implemented)
8. Commit source + artifacts + register in one commit

---

## 8. Test Infrastructure

| Marker / Suite | What | Count |
|----------------|------|-------|
| `[marker]` | `[description]` | `[N]` |
| (no marker) | Unit / integration | `[N]` |
| **Total** | | `[N]` |

---

## 9. Current State

### Recent commits

| SHA | Description |
|-----|-------------|
| `[SHA]` | `[message]` |
| `[SHA]` | `[message]` |

### In-progress work

`[Describe any work that was started but not completed, or leave "None".]`

### Known limitations / follow-up items

- `[item 1]`
- `[item 2]`

---

## 10. Updating This Document

Update at the end of every working session:

- Header line: `Last updated`, `Last REQ`, `Last commit`
- Section 7: Next available REQ ID, register version
- Section 9: Recent commits, in-progress work, known limitations

The handoff document should be committed with every session-end commit so that
context is never lost between LLM sessions.
