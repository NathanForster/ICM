# Global Systems Engineering Context

## source-development/
Use for:
- software development
- automation systems
- DAQ systems
- instrumentation integration
- validation

## documentation/
Use for:
- user manuals
- development plans
- validation documentation
- release notes

## sales/
Use for:
- customer proposals
- technical collateral
- presentations
- capability summaries

Always load local CONTEXT.md files before execution.

---

## Version Control — Files That Must Be Gitignored

| Category | Examples |
|----------|---------|
| Credentials | `.env`, `*.key`, `*.pem`, `secrets.*` |
| Runtime config | `settings.json`, user data files modified at runtime |
| Build output | `dist/`, `build/`, `__pycache__/`, `*.pyc` |
| Virtual environments | `.venv/`, `node_modules/`, `.conda/` |
| IDE / local state | `*.local.json`, `.DS_Store`, `*.user`, `Thumbs.db` |

The **only** committed credential file should be the example template (e.g. `.env.example`
with placeholder values). Never commit real keys, tokens, or passwords.
