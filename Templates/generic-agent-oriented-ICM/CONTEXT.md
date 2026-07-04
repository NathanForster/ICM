# Global Routing Context

## writing-room/
Use for:
- tutorials
- documentation
- blog posts
- content creation

## production/
Use for:
- implementation
- software builds
- engineering work
- technical execution

## community/
Use for:
- outreach
- marketing
- customer communication
- social content

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
