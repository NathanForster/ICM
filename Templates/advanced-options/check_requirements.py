"""check_requirements.py — ICM requirements register consistency checker.

Performs the mechanical checks of the icm-validate procedure without requiring
an LLM.  Reads the requirements register and cross-references it against the
ICM artifact directories to produce a findings report.

What this script checks:
  1. Every Implemented/Verified row has an implementation brief artifact.
  2. Every Implemented/Verified row has a validation brief artifact.
  3. Every Verified row has a non-empty Trace column (source file pointer).
  4. No artifact files exist without a corresponding register entry.
  5. Register Status values are from the allowed set.

What this script does NOT check (requires LLM or human):
  - Whether the source code actually implements the requirement.
  - Whether the test coverage is adequate.
  - Semantic correctness of the artifacts.

Usage:
    python check_requirements.py [--register PATH] [--impl-dir PATH] [--val-dir PATH]

Defaults (relative to this script's directory):
    --register  requirements/workflows/03-baseline/requirements-register.md
    --impl-dir  source-development/workflows/03-implementation/
    --val-dir   source-development/workflows/04-validation/

Exit codes:
    0  All checks passed (or only warnings).
    1  One or more errors found.
"""
import argparse
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration defaults
# ---------------------------------------------------------------------------

_ROOT = Path(__file__).resolve().parent

DEFAULT_REGISTER  = _ROOT / "requirements" / "workflows" / "03-baseline" / "requirements-register.md"
DEFAULT_IMPL_DIR  = _ROOT / "source-development" / "workflows" / "03-implementation"
DEFAULT_VAL_DIR   = _ROOT / "source-development" / "workflows" / "04-validation"

ALLOWED_STATUSES  = {"Baselined", "Implemented", "Verified", "Superseded"}
OPEN_STATUSES     = {"Baselined", "Implemented"}
CLOSED_STATUSES   = {"Verified", "Superseded"}

# ---------------------------------------------------------------------------
# Register parser
# ---------------------------------------------------------------------------

_ROW_RE = re.compile(
    r"^\|\s*(REQ-[\w-]+)\s*\|"   # REQ ID
    r"\s*([^|]+?)\s*\|"           # Title
    r"\s*([^|]+?)\s*\|"           # Priority
    r"\s*([^|]+?)\s*\|"           # Status
    r"\s*([^|]*?)\s*\|"           # Trace
)


def parse_register(path: Path) -> list[dict]:
    """Parse the requirements register and return a list of requirement dicts."""
    requirements = []
    if not path.exists():
        return requirements

    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = _ROW_RE.match(line)
            if not m:
                continue
            req_id, title, priority, status, trace = (g.strip() for g in m.groups())
            # Skip header separator rows
            if req_id.startswith("ID") or "---" in req_id:
                continue
            requirements.append({
                "id":       req_id,
                "title":    title,
                "priority": priority,
                "status":   status,
                "trace":    trace,
            })
    return requirements


# ---------------------------------------------------------------------------
# Artifact finder
# ---------------------------------------------------------------------------

def _artifact_exists(directory: Path, req_id: str, kind: str) -> bool:
    """Return True if an ICM artifact file for *req_id* exists in *directory*.

    Accepts both canonical uppercase form (input_REQ-42_implementation.md)
    and legacy lowercase form (input_req42_implementation.md).
    """
    if not directory.is_dir():
        return False

    # Build search patterns: try several normalisation forms
    canonical   = req_id                               # REQ-42
    lower_hyph  = req_id.lower()                       # req-42
    lower_nohyph = req_id.lower().replace("-", "")     # req42
    lower_under  = req_id.lower().replace("-", "_")    # req_42

    patterns = {canonical, lower_hyph, lower_nohyph, lower_under}

    for fname in os.listdir(directory):
        fname_lower = fname.lower()
        if kind not in fname_lower:
            continue
        for pat in patterns:
            if pat.lower() in fname_lower:
                return True
    return False


def find_orphan_artifacts(directory: Path, req_ids: set[str], kind: str) -> list[str]:
    """Return artifact filenames that have no matching register entry."""
    if not directory.is_dir():
        return []

    orphans = []
    for fname in os.listdir(directory):
        if kind not in fname.lower():
            continue
        # Check whether any known REQ ID appears in the filename
        fname_lower = fname.lower()
        matched = any(
            r.lower() in fname_lower or
            r.lower().replace("-", "") in fname_lower or
            r.lower().replace("-", "_") in fname_lower
            for r in req_ids
        )
        if not matched:
            orphans.append(fname)
    return orphans


# ---------------------------------------------------------------------------
# Reporter
# ---------------------------------------------------------------------------

class Reporter:
    def __init__(self):
        self.errors   = []
        self.warnings = []
        self.infos    = []

    def error(self, msg: str):
        self.errors.append(msg)
        print(f"  ❌  {msg}")

    def warn(self, msg: str):
        self.warnings.append(msg)
        print(f"  ⚠️   {msg}")

    def info(self, msg: str):
        self.infos.append(msg)
        print(f"  ✅  {msg}")

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0


# ---------------------------------------------------------------------------
# Main checks
# ---------------------------------------------------------------------------

def run_checks(register_path: Path, impl_dir: Path, val_dir: Path) -> bool:
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("  ICM Requirements Consistency Check")
    print(f"  Register : {register_path}")
    print(f"  Impl dir : {impl_dir}")
    print(f"  Val dir  : {val_dir}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()

    r = Reporter()

    # -- Parse register -------------------------------------------------------
    if not register_path.exists():
        print(f"ERROR: Register not found: {register_path}")
        return False

    reqs = parse_register(register_path)
    if not reqs:
        r.warn("Register parsed but contains no requirement rows.")
        return True

    req_ids = {req["id"] for req in reqs}

    # -- Per-requirement checks -----------------------------------------------
    backfill_needed  = []
    open_count       = 0
    verified_count   = 0
    superseded_count = 0

    for req in reqs:
        rid    = req["id"]
        status = req["status"]
        trace  = req["trace"]

        # Unknown status
        if status not in ALLOWED_STATUSES:
            r.error(f"{rid}: unknown Status '{status}' — expected one of {sorted(ALLOWED_STATUSES)}")
            continue

        # Superseded: skip
        if status == "Superseded":
            superseded_count += 1
            continue

        # Verified: count
        if status == "Verified":
            verified_count += 1
            if not trace or trace == "—":
                r.warn(f"{rid}: Status=Verified but Trace column is empty")

        # Baselined: no artifacts required yet
        if status == "Baselined":
            open_count += 1
            continue

        # Implemented or Verified: artifacts required
        has_impl = _artifact_exists(impl_dir, rid, "implementation")
        has_val  = _artifact_exists(val_dir,  rid, "validation")

        if not has_impl and not has_val:
            r.error(f"{rid} ({status}): both implementation and validation artifacts are missing — backfill needed")
            backfill_needed.append(rid)
        elif not has_impl:
            r.error(f"{rid} ({status}): implementation artifact missing — backfill needed")
            backfill_needed.append(rid)
        elif not has_val:
            r.error(f"{rid} ({status}): validation artifact missing — backfill needed")
            backfill_needed.append(rid)
        else:
            r.info(f"{rid} ({status}): artifacts ✓")

    # -- Orphan artifact checks -----------------------------------------------
    print()
    print("  Checking for orphan artifacts...")
    impl_orphans = find_orphan_artifacts(impl_dir, req_ids, "implementation")
    val_orphans  = find_orphan_artifacts(val_dir,  req_ids, "validation")

    for fname in impl_orphans:
        r.warn(f"Orphan impl artifact (no register entry): {fname}")
    for fname in val_orphans:
        r.warn(f"Orphan val artifact  (no register entry): {fname}")

    # -- Summary --------------------------------------------------------------
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("  Summary")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  Total requirements : {len(reqs)}")
    print(f"  Verified           : {verified_count}")
    print(f"  Open (Baselined)   : {open_count}")
    print(f"  Superseded         : {superseded_count}")
    print(f"  Backfill needed    : {len(backfill_needed)}")
    print(f"  Errors             : {len(r.errors)}")
    print(f"  Warnings           : {len(r.warnings)}")

    if backfill_needed:
        print()
        print("  Requirements needing backfill:")
        for rid in backfill_needed:
            print(f"    {rid}")

    print()
    if r.ok:
        print("  RESULT: PASS — no errors found.")
    else:
        print("  RESULT: FAIL — see errors above.")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()

    return r.ok


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="ICM requirements register consistency checker.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--register",  type=Path, default=DEFAULT_REGISTER,
                   help="Path to requirements-register.md")
    p.add_argument("--impl-dir",  type=Path, default=DEFAULT_IMPL_DIR,
                   help="Path to 03-implementation/ artifact directory")
    p.add_argument("--val-dir",   type=Path, default=DEFAULT_VAL_DIR,
                   help="Path to 04-validation/ artifact directory")
    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    ok   = run_checks(args.register, args.impl_dir, args.val_dir)
    sys.exit(0 if ok else 1)
