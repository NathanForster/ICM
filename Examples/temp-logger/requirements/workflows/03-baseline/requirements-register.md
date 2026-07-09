# Requirements Register — Baseline v1.1
# Project: temp-logger | Baselined: 2026-06-10 | Updated: 2026-06-24

## Status Key

| Status | Meaning |
|--------|---------|
| Baselined | Approved and frozen — ready to implement |
| Implemented | Code exists in `src/`; ICM artifacts written |
| Verified | Tested or manually confirmed working |
| Superseded | Replaced by a newer requirement — do not implement |

## Functional Requirements

| ID | Title | Priority | Status | Trace |
|----|-------|----------|--------|-------|
| REQ-01 | Append readings to a timestamped CSV log, creating the file with a header row on first write | Must Have | Verified | `src/temp_logger.py` |
| REQ-02 | Reject readings outside −40 °C … +85 °C and log a warning instead of a data row | Must Have | Baselined | — |

## Non-Functional Requirements

| ID | Title | Priority | Status | Trace |
|----|-------|----------|--------|-------|
| REQ-NF-01 | Pure standard library — no third-party runtime dependencies | Must Have | Verified | `src/temp_logger.py` (imports: csv, datetime, pathlib) |

## Supersessions

| ID | Title | Priority | Status | Superseded By |
|----|-------|----------|--------|---------------|
| *(none)* | | | | |
