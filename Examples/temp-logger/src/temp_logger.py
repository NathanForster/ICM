"""temp_logger — append temperature sensor readings to a timestamped CSV log.

Implements REQ-01 (timestamped CSV logging). Range validation (REQ-02) is
baselined but not yet implemented. Standard library only (REQ-NF-01).
"""
from datetime import datetime, timezone
from pathlib import Path
import csv

CSV_HEADER = ["timestamp_utc", "sensor_id", "temperature_c"]


def log_reading(log_path, sensor_id, temperature_c, now=None):
    """Append one reading to *log_path*, creating the file with a header first.

    Args:
        log_path:      Path to the CSV log file.
        sensor_id:     Identifier of the reporting sensor.
        temperature_c: Reading in degrees Celsius (numeric or numeric string).
        now:           Optional datetime for the timestamp (tests inject a
                       fixed value); defaults to the current UTC time.

    Returns:
        The row written, as a list of strings.
    """
    path = Path(log_path)
    timestamp = (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")
    row = [timestamp, str(sensor_id), f"{float(temperature_c):.2f}"]

    write_header = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        if write_header:
            writer.writerow(CSV_HEADER)
        writer.writerow(row)
    return row
