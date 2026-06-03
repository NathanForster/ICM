#!/bin/bash
# run_data_pipeline.sh — ICM data pipeline runner
#
# Executes every data pipeline stage in sequence (ingest → transform →
# validate → load), pausing after each one so a human operator can inspect
# and optionally edit the output before the next stage begins.
#
# Usage:
#   bash run_data_pipeline.sh
#
# Prerequisites:
#   - LLM credentials set in src/config/.env  (or as environment variables)
#   - Stage folders named  01-<name>/  02-<name>/  …  in the workflow directory
#
# See CLAUDE.md for provider configuration options.
# See run_source_dev.sh for the source-code development pipeline.

set -e

WORKSPACE_ROOT="."
RUNNER_SCRIPT="./.icm-runner.py"

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
NC='\033[0m'

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
pause_for_review() {
    local stage="$1"
    local output_file="$2"
    echo ""
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}  [PAUSED] Stage '${stage}' complete.${NC}"
    echo ""
    echo -e "  Review output: ${output_file}"
    echo -e "  Edit the file directly if corrections are needed."
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    read -p "  Press [Enter] to proceed to the next stage..."
}

promote() {
    # Copy <src> to <dst>, creating the destination directory if needed.
    local src="$1"
    local dst="$2"
    mkdir -p "$(dirname "$dst")"
    cp "$src" "$dst"
    echo -e "  Promoted: $(basename "$src") → $(basename "$dst")"
}

# ---------------------------------------------------------------------------
# Pipeline
#
# Customise the stage list and promotion paths for your project.
# Each entry follows this pattern:
#
#   STAGE_N:   folder name under the workflow directory
#   OUTPUT_N:  output file written by the runner
#   INPUT_N+1: input file expected by the next stage
# ---------------------------------------------------------------------------

WORKFLOW_DIR="$WORKSPACE_ROOT"   # adjust if stages live in a sub-directory

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  ICM Data Pipeline — Starting${NC}"
echo -e "${CYAN}  Python: ${PYTHON}${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# ── Stage 1 ──────────────────────────────────────────────────────────────────
STAGE1="01-ingest"
echo ""
echo -e "${GREEN}[1/?] Running: ${STAGE1}...${NC}"
"$PYTHON" "$RUNNER_SCRIPT" "$WORKFLOW_DIR" "$STAGE1"

OUTPUT1="${WORKFLOW_DIR}/${STAGE1}/output_${STAGE1}.md"
INPUT2="${WORKFLOW_DIR}/02-transform/input_stage1.md"
promote "$OUTPUT1" "$INPUT2"
pause_for_review "$STAGE1" "$OUTPUT1"

# ── Stage 2 ──────────────────────────────────────────────────────────────────
STAGE2="02-transform"
echo ""
echo -e "${GREEN}[2/?] Running: ${STAGE2}...${NC}"
"$PYTHON" "$RUNNER_SCRIPT" "$WORKFLOW_DIR" "$STAGE2"

OUTPUT2="${WORKFLOW_DIR}/${STAGE2}/output_${STAGE2}.md"
INPUT3="${WORKFLOW_DIR}/03-validate/input_stage2.md"
promote "$OUTPUT2" "$INPUT3"
pause_for_review "$STAGE2" "$OUTPUT2"

# ── Stage 3 ──────────────────────────────────────────────────────────────────
STAGE3="03-validate"
echo ""
echo -e "${GREEN}[3/?] Running: ${STAGE3}...${NC}"
"$PYTHON" "$RUNNER_SCRIPT" "$WORKFLOW_DIR" "$STAGE3"

OUTPUT3="${WORKFLOW_DIR}/${STAGE3}/output_${STAGE3}.md"
INPUT4="${WORKFLOW_DIR}/04-load/input_stage3.md"
promote "$OUTPUT3" "$INPUT4"
pause_for_review "$STAGE3" "$OUTPUT3"

# ── Stage 4 ──────────────────────────────────────────────────────────────────
STAGE4="04-load"
echo ""
echo -e "${GREEN}[4/?] Running: ${STAGE4}...${NC}"
"$PYTHON" "$RUNNER_SCRIPT" "$WORKFLOW_DIR" "$STAGE4"

OUTPUT4="${WORKFLOW_DIR}/${STAGE4}/output_${STAGE4}.md"
pause_for_review "$STAGE4" "$OUTPUT4"

# ── Complete ──────────────────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  Data pipeline complete.${NC}"
echo -e "${GREEN}  Final output: ${OUTPUT4}${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
