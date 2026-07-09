# temp-logger — Global Routing Context

Single source of truth for workspace routing. A task that matches no row is
escalated to the human operator.

## Workspace Routing Table

### Active workspaces

| Workspace | Route When |
|-----------|-----------|
| `source-development/` | Writing, modifying, or reviewing `src/` code; writing implementation/validation briefs |
| `requirements/` | Capturing, triaging, baselining, or tracing requirements |

### Registry workspaces

| Workspace | Route When |
|-----------|-----------|
| `decisions/` | Recording engineering decisions (ADRs) |
| `state/` | Session handoff and persistent operational state |

## Version Control — Files That Must Be Gitignored

Credentials (`.env`), build output (`__pycache__/`), virtual environments
(`.venv/`), IDE state. No credential files exist in this example.
