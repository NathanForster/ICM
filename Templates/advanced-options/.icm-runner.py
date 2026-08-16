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

    LLM_MODEL=claude-opus-4-8     # Anthropic
    LLM_MODEL=gpt-4o-mini         # OpenAI

Defaults (when LLM_MODEL is not set):
    Anthropic  →  claude-opus-4-8
    OpenAI     →  gpt-4o

OUTPUT TUNING
-------------
    LLM_MAX_TOKENS=16000     # max output tokens per stage call (default 16000)
    LLM_TEMPERATURE=0.1      # OpenAI only — current Anthropic models (Opus 4.7+)
                             # reject sampling parameters, so none are sent there

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
        resolved_model = model or "claude-opus-4-8"
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
    max_tokens  = int(os.environ.get("LLM_MAX_TOKENS", "16000"))
    temperature = float(os.environ.get("LLM_TEMPERATURE", "0.1"))

    try:
        if provider == "anthropic":
            # No sampling parameters: current Anthropic models (Opus 4.7+)
            # reject temperature/top_p/top_k with a 400.
            response = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}],
            )
            # Skip any leading thinking blocks; return the text content
            for block in response.content:
                if block.type == "text":
                    return block.text
            return ""

        else:  # openai
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user",   "content": user_prompt},
                ],
                temperature=temperature,
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

def execute_icm_stage(
    workspace_root: str,
    stage_folder_name: str,
    only_inputs=None,
    extra_artifacts=None,
) -> None:
    """Run one ICM pipeline stage.

    Assembles the layered context hierarchy by walking UP from the stage
    folder to the project root, collecting every ICM.md / CONTEXT.md found:

        Layer 0  —  ICM.md          (project root — global framework constraints)
        Layer 1  —  CONTEXT.md      (project root — routing / blueprint)
        Layer 1a —  ICM.md / CONTEXT.md at each intermediate level between root
                    and the stage folder (e.g. the owning workspace's), so a
                    workspace's local context authority is honoured
        Layer 2  —  CONTEXT.md      (stage folder — the stage contract)
        Layer 3  —  reference files (stage folder, filenames containing
                                     'reference', 'style', or 'config')
        Layer 4  —  input artifacts  (stage folder, filenames containing
                                     'input' or 'artifact')

    The walk supports both layouts the overlay is used with: a flat pipeline
    (``<root>/01-ingest/`` with ICM.md/CONTEXT.md at ``<root>``) and the
    systems-engineering layout (``<root>/source-development/workflows/03-…``
    with ICM.md/CONTEXT.md at ``<root>`` and at ``<root>/source-development/``).
    The project root is the **topmost** ancestor in the contiguous run of
    ancestors holding ICM.md that begins at the first ICM.md met on the way up
    (once one is found, the walk stops at the first ancestor *without* one), and
    never above a directory holding ``.git``. "Nearest" would be wrong: sys-eng
    active workspaces carry their own ICM.md, and stopping there would silently
    drop the project-level layers. The contiguity rule means a project that has
    not been ``git init``-ed yet cannot be hijacked by an unrelated ICM.md higher
    up the filesystem.

    The assembled system prompt (layers 0–2) and user prompt (layers 3–4)
    are sent to the active LLM.  The response is written to
    ``<stage_folder>/output_<stage_folder_name>.md``.

    When the input exceeds the model's context window the runner automatically
    chunks the largest ``.txt`` input file and consolidates the results.

    Args:
        workspace_root:     Path to the folder that CONTAINS the stage folder
                            (e.g. ``source-development/workflows``). It need not
                            itself hold ICM.md — the runner walks up to find it.
        stage_folder_name:  Name of the stage sub-folder (e.g. ``"03-implementation"``).
        only_inputs:        Optional list of file names inside the stage folder.
                            When given, ONLY these are loaded as Layer 4 (instead
                            of every ``input``/``artifact`` file present) — used
                            by per-requirement pipelines so earlier briefs do not
                            pollute the run.
        extra_artifacts:    Optional list of paths (relative to CWD) loaded as
                            additional Layer 4 artifacts from anywhere — e.g. the
                            previous stage's ``output_*.md``.
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

    # Walk up from the stage folder's parent, collecting every ancestor.
    # Root = the TOPMOST ancestor holding ICM.md, but never above a directory
    # that holds .git (the repository root). Workspaces have their own ICM.md,
    # so "nearest ICM.md" would stop one level too low in nested layouts.
    stage_abs = os.path.abspath(stage_path)
    chain = []
    root_idx = None
    cur = os.path.dirname(stage_abs)
    while True:
        chain.append(cur)
        has_icm = os.path.exists(os.path.join(cur, "ICM.md"))
        if has_icm:
            root_idx = len(chain) - 1  # keep going — we want the highest one …
        elif root_idx is not None:
            break                      # … but only within a contiguous run
        if os.path.exists(os.path.join(cur, ".git")):
            break                      # repository root — do not climb further
        parent = os.path.dirname(cur)
        if parent == cur:
            break                      # filesystem root
        cur = parent
    # chain[0] is the stage folder's parent; chain[root_idx] the project root.
    if root_idx is None:
        root_idx = 0                   # nothing found; warn below
    ancestors = list(reversed(chain[: root_idx + 1]))  # root first, then down

    parts = []
    root = ancestors[0]
    l0 = _read(os.path.join(root, "ICM.md"))
    l1 = _read(os.path.join(root, "CONTEXT.md"))
    if l0: parts.append(f"### LAYER 0: GLOBAL FRAMEWORK CONSTRAINTS (ICM.md)\n{l0}")
    if l1: parts.append(f"### LAYER 1: PROJECT BLUEPRINT (CONTEXT.md)\n{l1}")
    if not l0 and not l1:
        print("[ICM] WARNING: no ICM.md/CONTEXT.md found in any ancestor of the "
              "stage folder — layers 0/1 are empty. Is this stage inside an ICM project?")

    # Intermediate levels (e.g. the owning workspace) — local context authority
    for level in ancestors[1:]:
        for fname, label in (("ICM.md", "ICM.md"), ("CONTEXT.md", "CONTEXT.md")):
            txt = _read(os.path.join(level, fname))
            if txt:
                rel = os.path.relpath(level, root).replace(os.sep, "/")
                parts.append(f"### LAYER 1a: LOCAL CONTEXT ({rel}/{label})\n{txt}")

    l2 = _read(os.path.join(stage_path, "CONTEXT.md"))
    if l2: parts.append(f"### LAYER 2: ACTIVE STAGE CONTRACT (stage CONTEXT.md)\n{l2}")
    print(f"[ICM] Context  : {len(parts)} layer(s) loaded from {root}")
    system_prompt = "\n\n".join(parts)

    # Assemble user prompt from stage files (layers 3–4)
    layer_3, layer_4 = "", ""
    for fname in sorted(os.listdir(stage_path)):
        if fname == "CONTEXT.md" or fname.startswith("."):
            continue
        content = _read(os.path.join(stage_path, fname))
        if only_inputs is not None and fname in only_inputs:
            # An explicitly named brief is ALWAYS a Layer 4 artifact, whatever
            # its name contains (a brief about the "config tool" must not be
            # demoted to reference material by the keyword rule below).
            if content:
                layer_4 += f"\n\n--- LAYER 4: WORKING ARTIFACT ({fname}) ---\n{content}"
            continue
        if not content:
            continue
        if any(k in fname.lower() for k in ("reference", "style", "config")):
            layer_3 += f"\n\n--- LAYER 3: REFERENCE MATERIAL ({fname}) ---\n{content}"
        elif only_inputs is None and any(k in fname.lower() for k in ("input", "artifact")):
            layer_4 += f"\n\n--- LAYER 4: WORKING ARTIFACT ({fname}) ---\n{content}"
    if only_inputs is not None:
        bad = [f for f in only_inputs if not _read(os.path.join(stage_path, f))]
        if bad:
            print(f"ERROR: --input file(s) missing or empty in {stage_path}: {', '.join(bad)}")
            sys.exit(1)
    for apath in extra_artifacts or []:
        content = _read(apath)
        if not content:
            print(f"ERROR: --artifact file not found or empty: {apath}")
            sys.exit(1)
        rel = os.path.relpath(os.path.abspath(apath), root).replace(os.sep, "/")
        layer_4 += f"\n\n--- LAYER 4: WORKING ARTIFACT ({rel}) ---\n{content}"
    n_l4 = layer_4.count("--- LAYER 4:")
    print(f"[ICM] Inputs   : {n_l4} artifact(s) loaded"
          + (" (explicit selection)" if only_inputs is not None
             else " (all input/artifact files in stage folder)"))

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

def _usage() -> None:
    print("Usage: python .icm-runner.py <workspace_root> <stage_folder_name> "
          "[--input <file>]... [--artifact <path>]...")
    print("")
    print("  --input <file>     load ONLY the named file(s) from the stage folder as")
    print("                     Layer 4 (default: every file whose name contains")
    print("                     'input' or 'artifact'). Repeatable.")
    print("  --artifact <path>  also load <path> (relative to CWD) as a Layer 4")
    print("                     artifact, e.g. the previous stage's output. Repeatable.")
    print("")
    print("Examples:")
    print("  python .icm-runner.py data-pipeline/workflows      01-ingest")
    print("  python .icm-runner.py source-development/workflows 03-implementation \\")
    print("      --input input_REQ-42_implementation.md")
    print("  python .icm-runner.py source-development/workflows 04-validation \\")
    print("      --input input_REQ-42_validation.md \\")
    print("      --artifact source-development/workflows/03-implementation/output_03-implementation.md")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) < 2:
        _usage()
        sys.exit(1)
    ws, stage = argv[0], argv[1]
    only, extra = None, []
    i = 2
    while i < len(argv):
        if argv[i] == "--input" and i + 1 < len(argv):
            only = (only or []) + [argv[i + 1]]
            i += 2
        elif argv[i] == "--artifact" and i + 1 < len(argv):
            extra.append(argv[i + 1])
            i += 2
        else:
            print(f"ERROR: unrecognised argument: {argv[i]}")
            _usage()
            sys.exit(1)
    execute_icm_stage(ws, stage, only_inputs=only, extra_artifacts=extra)
