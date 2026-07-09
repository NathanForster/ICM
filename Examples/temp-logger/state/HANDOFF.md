# temp-logger — Session Handoff
# Last updated: 2026-06-24 | Last REQ: REQ-02 | Last commit: (example — not tracked)

> Read this file first in every new session.

## 1. What This Project Is

A CLI utility that appends temperature sensor readings to a timestamped CSV
log. Single sensor, single process, standard library only. It does not chart,
aggregate, or transmit data.

## 2. Critical Paths

| What | Path |
|------|------|
| Source | `src/temp_logger.py` |
| Tests | `src/tests/test_temp_logger.py` |
| Requirements register | `requirements/workflows/03-baseline/requirements-register.md` |
| Traceability matrix | `requirements/workflows/04-trace/traceability-matrix.md` |
| Impl/val briefs | `source-development/workflows/03-implementation/`, `04-validation/` |

## 3. Key Commands

```bash
python -m pytest src/tests/ -q      # run tests (3 passing)
python -m py_compile src/temp_logger.py   # lint-lite
```

## 4. ICM Pipeline State

- **Next available REQ ID:** REQ-03 (last used: REQ-02)
- **Register:** v1.1 (2026-06-24) — REQ-01 and REQ-NF-01 Verified; REQ-02 Baselined
- Base instance (no advanced overlay): stage reviews are performed by the
  implementing agent per the stage contracts; no `.icm-runner.py`

## 5. Current State

### In-progress work
None — REQ-01 closed end-to-end.

### Next steps
- Implement REQ-02 (range validation −40…+85 °C): write
  `input_REQ-02_implementation.md` first, per the mandatory pipeline sequence
- On REQ-02 completion, bump register to v1.2 and update the matrix
