#!/bin/bash
# run_source_dev.sh — Source-development ICM pipeline runner
#
# Guides you through the mandatory source-development pipeline sequence for a
# single requirement.  Each step pauses so you can review, edit, or write
# the required artifact before the next stage runs.
#
# Usage:
#   bash run_source_dev.sh <REQ-ID>
#
# Example:
#   bash run_source_dev.sh REQ-42
#
# Steps guided by this script:
#   1. Check / create the implementation brief  (03-implementation)
#   2. Run stage 03-implementation
#   3. Pause — write the code in src/
#   4. Check / create the validation brief      (04-validation)
#   5. Run stage 04-validation
#   6. Remind you to update the register and commit
#
# See CLAUDE.md § MANDATORY SOURCE-DEVELOPMENT PIPELINE for the full process.

set -e

REQ_ID="${1:-}"

if [ -z "$REQ_ID" ]; then
    echo "Usage: bash run_source_dev.sh <REQ-ID>"
    echo "  e.g. bash run_source_dev.sh REQ-42"
    exit 1
fi

# Normalise to lowercase+underscore for file matching (REQ-42 → req_42)
REQ_LOWER=$(echo "$REQ_ID" | tr '[:upper:]' '[:lower:]' | tr '-' '_')

WORKSPACE_ROOT="."
RUNNER_SCRIPT="./.icm-runner.py"
IMPL_DIR="source-development/workflows/03-implementation"
VAL_DIR="source-development/workflows/04-validation"

# ---------------------------------------------------------------------------
# Locate the project venv Python (cross-platform)
# ---------------------------------------------------------------------------
VENV_PY="./src/.venv/Scripts/python.exe"          # Windows
if [ ! -f "$VENV_PY" ]; then
    VENV_PY="./src/.venv/bin/python"               # Linux / macOS
fi
if [ ! -f "$VENV_PY" ]; then
    VENV_PY="python3"                              # system fallback
fi
PYTHON="$VENV_PY"

# ---------------------------------------------------------------------------
# Colour codes
# ---------------------------------------------------------------------------
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

pause() {
    echo ""
    echo -e "${YELLOW}[PAUSED] $1${NC}"
    read -p "  Press [Enter] to continue..."
}

fail() {
    echo -e "${RED}[ERROR] $1${NC}"
    exit 1
}

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  Source-Development Pipeline — ${REQ_ID}${NC}"
echo -e "${CYAN}  Python: ${PYTHON}${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# ── Step 1: Implementation brief ─────────────────────────────────────────────
echo ""
echo -e "${GREEN}[1/5] Checking for implementation brief...${NC}"

IMPL_INPUT=$(find "$IMPL_DIR" -maxdepth 1 \
    \( -name "*${REQ_LOWER}*implementation*" -o -name "*${REQ_ID}*implementation*" \) \
    2>/dev/null | head -1)

if [ -z "$IMPL_INPUT" ]; then
    echo -e "${YELLOW}  No implementation brief found for ${REQ_ID}.${NC}"
    echo ""
    echo "  Create the file:"
    echo "    ${IMPL_DIR}/input_${REQ_ID}_implementation.md"
    echo ""
    echo "  Required content:"
    echo "    - Design summary (what will be built)"
    echo "    - Files to be modified"
    echo "    - Key functions / classes / constants"
    echo "    - Constraints or edge cases"
    pause "Create the brief, then press [Enter]."

    IMPL_INPUT=$(find "$IMPL_DIR" -maxdepth 1 \
        \( -name "*${REQ_LOWER}*implementation*" -o -name "*${REQ_ID}*implementation*" \) \
        2>/dev/null | head -1)
    [ -z "$IMPL_INPUT" ] && fail "Still no implementation brief found. Aborting."
fi

echo -e "  Found: ${IMPL_INPUT}"

# ── Step 2: Run stage 03-implementation ──────────────────────────────────────
echo ""
echo -e "${GREEN}[2/5] Running: source-development/workflows/03-implementation...${NC}"
"$PYTHON" "$RUNNER_SCRIPT" "source-development/workflows" "03-implementation"

pause "Stage 03 complete. Review output_03-implementation.md if needed."

# ── Step 3: Write the code ───────────────────────────────────────────────────
echo ""
echo -e "${GREEN}[3/5] Code phase${NC}"
echo ""
echo "  Write (or confirm) the implementation in src/ now."
echo ""
echo "  Checklist:"
echo "    [ ] Code written in src/"
echo "    [ ] Lint passes (ruff check . or equivalent)"
echo "    [ ] Manual smoke test done"
pause "Code is ready. Press [Enter] to proceed to validation."

# ── Step 4: Validation brief ─────────────────────────────────────────────────
echo ""
echo -e "${GREEN}[4/5] Checking for validation brief...${NC}"

VAL_INPUT=$(find "$VAL_DIR" -maxdepth 1 \
    \( -name "*${REQ_LOWER}*validation*" -o -name "*${REQ_ID}*validation*" \) \
    2>/dev/null | head -1)

if [ -z "$VAL_INPUT" ]; then
    echo -e "${YELLOW}  No validation brief found for ${REQ_ID}.${NC}"
    echo ""
    echo "  Create the file:"
    echo "    ${VAL_DIR}/input_${REQ_ID}_validation.md"
    echo ""
    echo "  Required content:"
    echo "    - Lint result (pass/fail)"
    echo "    - Logic review (key conditions verified)"
    echo "    - Edge cases tested"
    echo "    - Test results (file, count, pass/fail)"
    echo "    - Overall result: PASS or FAIL"
    pause "Create the brief, then press [Enter]."

    VAL_INPUT=$(find "$VAL_DIR" -maxdepth 1 \
        \( -name "*${REQ_LOWER}*validation*" -o -name "*${REQ_ID}*validation*" \) \
        2>/dev/null | head -1)
    [ -z "$VAL_INPUT" ] && fail "Still no validation brief found. Aborting."
fi

echo -e "  Found: ${VAL_INPUT}"

# ── Step 5: Run stage 04-validation ──────────────────────────────────────────
echo ""
echo -e "${GREEN}[5/5] Running: source-development/workflows/04-validation...${NC}"
"$PYTHON" "$RUNNER_SCRIPT" "source-development/workflows" "04-validation"

pause "Stage 04 complete. Review output_04-validation.md if needed."

# ── Done ─────────────────────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  Pipeline complete for ${REQ_ID}${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "  Next steps:"
echo ""
echo "    1. Update the requirements register:"
echo "         Status: Baselined → Implemented"
echo "         Trace: add source file(s)"
echo ""
echo "    2. Commit everything together:"
echo "         git add src/ source-development/workflows/ requirements/"
echo "         git commit -m \"feat(${REQ_ID}): <description>\""
echo ""
echo "    3. Run check_requirements.py to verify register consistency:"
echo "         python check_requirements.py"
echo ""
