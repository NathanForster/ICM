# Implementation Brief — REQ-01
# Author: session 2026-06-17 | Requirement: REQ-01 (Baselined v1.0)

## Design Summary

Provide a single function `log_reading(log_path, sensor_id, temperature_c, now=None)`
that appends one reading to a CSV file. On first write (file absent) the function
writes the header row first. Timestamps are UTC ISO-8601 with seconds precision;
temperature is normalized to two decimal places. The `now` parameter allows tests
to inject a fixed datetime.

## Files to Be Modified

- `src/temp_logger.py` (new)
- `src/tests/test_temp_logger.py` (new)

## Key Functions / Classes / Constants

- `CSV_HEADER = ["timestamp_utc", "sensor_id", "temperature_c"]`
- `log_reading(log_path, sensor_id, temperature_c, now=None) -> list[str]` — returns the written row

## Constraints

- Standard library only (REQ-NF-01): `csv`, `datetime`, `pathlib`
- Appending must never rewrite existing rows; header written exactly once
- Edge cases: file created between existence check and open is acceptable to
  ignore at this scale (single-writer assumption — recorded in ADR-001)
