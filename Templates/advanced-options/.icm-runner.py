"""ICM pipeline stage runner.

Executes a single named stage folder against the layered ICM context system.

PROVIDER SELECTION
------------------
Set the ``LLM_PROVIDER`` environment variable to choose explicitly:

    LLM_PROVIDER=anthropic   →  Anthropic Claude
    LLM_PROVIDER=openai      →  OpenAI GPT

When ``LLM_PROVIDER`` is not set the runner auto-detects from available keys:

    ANTHROPIC_API_KEY  →  Anthropic Claude
    OPENAI_API_KEY     →  OpenAI GPT

MODEL SELECTION
---------------
Override the model via:

    LLM_MODEL=claude-sonnet-4-5   # Anthropic
    LLM_MODEL=gpt-4o-mini         # OpenAI

Defaults (when LLM_MODEL is not set):
    Anthropic  →  claude-sonnet-4-5
    OpenAI     →  gpt-4o

CREDENTIALS
-----------
Keys are loaded automatically from ``src/config/.env`` (relative to this
file) using python-dotenv when available, or a built-in fallback parser.
Existing shell variables are not overwritten.

USAGE
-----
    python .icm-runner.py <workspace_root> <stage_folder_name>

EXAMPLES
--------
    python .icm-runner.py source-development/workflows 03-implementation
    python .icm-runner.py data-pipeline/workflows      01-ingest
"""
import os
import re
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Credential loader
# ---------------------------------------------------------------------------

def _load_env_file(path: Path) -> None:
    """Inject variables from a .env file into os.environ.

    Uses python-dotenv when available for full spec compliance.
    Falls back to a built-in line-by-line parser for zero-dependency operation.
    Existing environment variables are not overwritten (shell takes precedence
    unless the variable is empty, in which case the .env value wins).
    """
    try:
        from dotenv import load_dotenv as _dotenv_load
        _dotenv_load(path, override=False)
        return
    except ImportError:
        pass

    try:
        with open(path, encoding="utf-8") as fh:
            for raw in fh:
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, val = line.partition("=")
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key and not os.environ.get(key):
                    os.environ[key] = val
    except OSError:
        pass


# Auto-load .env from the conventional location (src/config/.env)
_env_candidates = [
    Path(__file__).resolve().parent / "src" / "config" / ".env",
    Path(__file__).resolve().parent / ".env",
]
for _env_path in _env_candidates:
    if _env_path.exists():
        _load_env_file(_env_path)
        break


# ---------------------------------------------------------------------------
# Provider detection
# ---------------------------------------------------------------------------

def _detect_provider():
    """Return ``(provider_name, client)`` based on LLM_PROVIDER or available keys.

    Resolution order:
    1. ``LLM_PROVIDER`` environment variable (explicit)
    2. ``ANTHROPIC_API_KEY`` present  →  anthropic
    3. ``OPENAI_API_KEY``    present  →  openai

    Exits with a clear error message if no provider can be resolved.
    """
    explicit   = os.environ.get("LLM_PROVIDER", "").strip().lower()
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    openai_key    = os.environ.get("OPENAI_API_KEY",    "").strip()
    model         = os.environ.get("LLM_MODEL", "").strip()

    provider = explicit or ("anthropic" if anthropic_key else ("openai" if openai_key else ""))

    if provider == "anthropic":
        if not anthropic_key:
            _exit_no_key("anthropic", "ANTHROPIC_API_KEY")
        import anthropic  # noqa: PLC0415
        resolved_model = model or "claude-sonnet-4-5"
        print(f"[ICM] Provider : Anthropic  |  Model: {resolved_model}")
        return "anthropic", anthropic.Anthropic(api_key=anthropic_key), resolved_model

    if provider == "openai":
        if not openai_key:
            _exit_no_key("openai", "OPENAI_API_KEY")
        from openai import OpenAI  # noqa: PLC0415
        resolved_model = model or "gpt-4o"
        print(f"[ICM] Provider : OpenAI     |  Model: {resolved_model}")
        return "openai", OpenAI(api_key=openai_key), resolved_model

    # No provider could be determined
    print(
        "ERROR: No LLM provider configured.\n"
        "\n"
        "Option 1 — set LLM_PROVIDER explicitly:\n"
        "    LLM_PROVIDER=anthropic   (requires ANTHROPIC_API_KEY)\n"
        "    LLM_PROVIDER=openai      (requires OPENAI_API_KEY)\n"
        "\n"
        "Option 2 — set an API key and let the runner detect the provider:\n"
        "    ANTHROPIC_API_KEY=<your-key>\n"
        "    OPENAI_API_KEY=<your-key>\n"
        "\n"
        "Keys can be stored in src/config/.env (loaded automatically)."
    )
    sys.exit(1)


def _exit_no_key(provider: str, var: str) -> None:
    print(f"ERROR: LLM_PROVIDER={provider} but {var} is not set.")
    print(f"  Add {var}=<your-key> to your environment or to src/config/.env")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Token chunker (fallback for large inputs)
# ---------------------------------------------------------------------------

def _chunk_file_by_tokens(
    input_path: str,
    output_dir: str,
    max_tokens_per_chunk: int = 4000,
) -> None:
    """Split *input_path* into token-bounded text chunks.

    Chunks are written as ``chunk_01.txt``, ``chunk_02.txt``, … inside
    *output_dir*.  Split points are chosen at sentence or paragraph boundaries
    to avoid cutting mid-sentence.

    Args:
        input_path:           Path to the large input text file.
        output_dir:           Directory to write chunk files into (created if absent).
        max_tokens_per_chunk: Approximate token ceiling per chunk (1 token ≈ 4 chars).
    """
    os.makedirs(output_dir, exist_ok=True)
    max_chars = max_tokens_per_chunk * 4

    with open(input_path, encoding="utf-8") as fh:
        text = fh.read()

    total = len(text)
    start = 0
    count = 1

    while start < total:
        if total - start <= max_chars:
            end = total
        else:
            target = start + max_chars
            window = text[target - 500: target]
            m = list(re.finditer(r'([.!?]\s+|\n+)', window))
            if m:
                end = (target - 500) + m[-1].end()
            else:
                sw = text[target - 100: target]
                sm = list(re.finditer(r'\s+', sw))
                end = (target - 100) + sm[-1].end() if sm else target

        out_file = os.path.join(output_dir, f"chunk_{count:02d}.txt")
        with open(out_file, "w", encoding="utf-8") as fh:
            fh.write(text[start:end].strip())
        start  = end
        count += 1


# ---------------------------------------------------------------------------
# LLM request dispatcher
# ---------------------------------------------------------------------------

_TOKEN_ERROR_KEYWORDS = [
    "context_length_exceeded",
    "prompt is too long",
    "prompt_too_long",
    "prompt_token_count",
    "maximum context length",
    "tokens > ",          # Anthropic: "N tokens > M maximum"
    "reduce the length",
    "input is too long",
]


def _send_request(
    provider: str,
    client,
    model: str,
    system_prompt: str,
    user_prompt: str,
) -> str:
    """Dispatch a completion request and return the response text.

    Returns the sentinel ``"__TRIGGER_SPLIT_FALLBACK__"`` when the input
    exceeds the model's context window so the caller can retry with chunked
    input.

    Args:
        provider:      ``"anthropic"`` or ``"openai"``.
        client:        Provider SDK client object.
        model:         Model identifier string.
        system_prompt: Static system / instruction context (layers 0–2).
        user_prompt:   Dynamic working content for this call (layers 3–4).
    """
    try:
        if provider == "anthropic":
            response = client.messages.create(
                model=model,
                max_tokens=4096,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}],
                temperature=0.1,
            )
            return response.content[0].text

        else:  # openai
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user",   "content": user_prompt},
                ],
                temperature=0.1,
            )
            return response.choices[0].message.content

    except Exception as exc:
        if any(kw in str(exc).lower() for kw in _TOKEN_ERROR_KEYWORDS):
            print("\n[ICM CHUNKER TRIGGERED] Input exceeds context window — switching to chunked mode.")
            return "__TRIGGER_SPLIT_FALLBACK__"
        raise


# ---------------------------------------------------------------------------
# Stage executor
# ---------------------------------------------------------------------------

def execute_icm_stage(workspace_root: str, stage_folder_name: str) -> None:
    """Run one ICM pipeline stage.

    Assembles the four-layer context hierarchy:

        Layer 0  —  ICM.md          (workspace root)
        Layer 1  —  CONTEXT.md      (workspace root)
        Layer 2  —  CONTEXT.md      (stage folder)
        Layer 3  —  reference files (stage folder, filenames containing
                                     'reference', 'style', or 'config')
        Layer 4  —  input artifacts  (stage folder, filenames containing
                                     'input' or 'artifact')

    The assembled system prompt (layers 0–2) and user prompt (layers 3–4)
    are sent to the active LLM.  The response is written to
    ``<stage_folder>/output_<stage_folder_name>.md``.

    When the input exceeds the model's context window the runner automatically
    chunks the largest ``.txt`` input file and consolidates the results.

    Args:
        workspace_root:     Path to the workspace root that contains ``ICM.md``.
        stage_folder_name:  Name of the stage sub-folder (e.g. ``"03-implementation"``).
    """
    provider, client, model = _detect_provider()
    stage_path = os.path.join(workspace_root, stage_folder_name)

    if not os.path.isdir(stage_path):
        print(f"ERROR: Stage folder not found: {stage_path}")
        sys.exit(1)

    print(f"[ICM] Stage    : {stage_folder_name}")
    print(f"[ICM] Workspace: {workspace_root}")

    def _read(path: str) -> str:
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                return fh.read().strip()
        return ""

    # Assemble layered system prompt (layers 0–2)
    parts = []
    l0 = _read(os.path.join(workspace_root, "ICM.md"))
    l1 = _read(os.path.join(workspace_root, "CONTEXT.md"))
    l2 = _read(os.path.join(stage_path,     "CONTEXT.md"))
    if l0: parts.append(f"### LAYER 0: GLOBAL FRAMEWORK CONSTRAINTS (ICM.md)\n{l0}")
    if l1: parts.append(f"### LAYER 1: PROJECT BLUEPRINT (CONTEXT.md)\n{l1}")
    if l2: parts.append(f"### LAYER 2: ACTIVE STAGE CONTRACT (stage CONTEXT.md)\n{l2}")
    system_prompt = "\n\n".join(parts)

    # Assemble user prompt from stage files (layers 3–4)
    layer_3, layer_4 = "", ""
    for fname in sorted(os.listdir(stage_path)):
        if fname == "CONTEXT.md" or fname.startswith("."):
            continue
        content = _read(os.path.join(stage_path, fname))
        if not content:
            continue
        if any(k in fname.lower() for k in ("reference", "style", "config")):
            layer_3 += f"\n\n--- LAYER 3: REFERENCE MATERIAL ({fname}) ---\n{content}"
        elif any(k in fname.lower() for k in ("input", "artifact")):
            layer_4 += f"\n\n--- LAYER 4: WORKING ARTIFACT ({fname}) ---\n{content}"

    user_prompt = (
        "Execute your stage contract obligations now. "
        "Output ONLY the generated artifact text — no preamble, no meta-commentary."
        f"\n{layer_3}\n{layer_4}"
    )

    result      = _send_request(provider, client, model, system_prompt, user_prompt)
    output_path = os.path.join(stage_path, f"output_{stage_folder_name}.md")

    if result == "__TRIGGER_SPLIT_FALLBACK__":
        # Find the largest input .txt file to chunk
        large_input = next(
            (
                os.path.join(stage_path, f)
                for f in sorted(os.listdir(stage_path))
                if "input" in f.lower() and f.endswith(".txt")
            ),
            None,
        )
        if not large_input:
            print("ERROR: Chunked mode triggered but no *.txt input file found in stage folder.")
            sys.exit(1)

        chunks_dir = os.path.join(stage_path, "_temporary_chunks")
        _chunk_file_by_tokens(large_input, chunks_dir)

        parts_out = []
        for chunk_file in sorted(os.listdir(chunks_dir)):
            with open(os.path.join(chunks_dir, chunk_file), encoding="utf-8") as fh:
                sub_prompt = f"Processing chunk — output ONLY the artifact fragment.\nData:\n{fh.read()}"
            parts_out.append(_send_request(provider, client, model, system_prompt, sub_prompt))

        shutil.rmtree(chunks_dir)
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write("\n\n---\n\n".join(parts_out))
    else:
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write(result)

    print(f"[ICM] Output   : {output_path}")
    print(f"[ICM] Stage {stage_folder_name} complete.\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python .icm-runner.py <workspace_root> <stage_folder_name>")
        print("")
        print("Examples:")
        print("  python .icm-runner.py source-development/workflows 03-implementation")
        print("  python .icm-runner.py data-pipeline/workflows      01-ingest")
        sys.exit(1)
    execute_icm_stage(sys.argv[1], sys.argv[2])
