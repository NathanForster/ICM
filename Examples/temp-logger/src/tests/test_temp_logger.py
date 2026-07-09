"""Tests for temp_logger — covers REQ-01 (and REQ-NF-01 by construction)."""
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from temp_logger import CSV_HEADER, log_reading  # noqa: E402

FIXED_NOW = datetime(2026, 6, 24, 12, 0, 0, tzinfo=timezone.utc)


def _read_rows(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.reader(fh))


def test_first_write_creates_file_with_header(tmp_path):
    log = tmp_path / "log.csv"
    log_reading(log, "S1", 21.5, now=FIXED_NOW)
    rows = _read_rows(log)
    assert rows[0] == CSV_HEADER
    assert rows[1] == ["2026-06-24T12:00:00+00:00", "S1", "21.50"]


def test_append_does_not_duplicate_header(tmp_path):
    log = tmp_path / "log.csv"
    log_reading(log, "S1", 21.5, now=FIXED_NOW)
    log_reading(log, "S2", -3.25, now=FIXED_NOW)
    rows = _read_rows(log)
    assert len(rows) == 3                       # header + two data rows
    assert rows[0] == CSV_HEADER
    assert CSV_HEADER not in rows[1:]


def test_returned_row_matches_written_row(tmp_path):
    log = tmp_path / "log.csv"
    returned = log_reading(log, "S1", "19.7", now=FIXED_NOW)
    assert _read_rows(log)[-1] == returned
    assert returned[2] == "19.70"               # normalized to two decimals
