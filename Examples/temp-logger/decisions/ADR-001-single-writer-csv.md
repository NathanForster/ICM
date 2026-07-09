# ADR-001: Single-writer CSV storage

**Date:** 2026-06-17
**Status:** Accepted
**Deciders:** project owner
**Related requirements:** REQ-01, REQ-NF-01

## Context

REQ-01 requires appending readings to a persistent log. The utility targets a
single bench sensor read by one process; REQ-NF-01 forbids third-party
dependencies, ruling out database drivers.

## Options Considered

| Option | Pros | Cons |
|--------|------|------|
| A. CSV via stdlib `csv` | Zero dependencies; human-readable; trivially imported by analysis tools | No concurrent-writer safety; no schema enforcement |
| B. SQLite via stdlib `sqlite3` | Concurrent-safe; queryable | Binary artifact; heavier than the requirement needs |

## Decision

Option A (CSV). The single-writer assumption holds for the target deployment,
and human-readability of the log was valued by the operator.

## Consequences

- Concurrent writers are out of scope — revisit this ADR if a second sensor
  process is ever added
- Header-integrity risk under concurrency is accepted (noted in the REQ-01
  implementation review)
- REQ-02 range validation will emit warnings rather than schema violations
