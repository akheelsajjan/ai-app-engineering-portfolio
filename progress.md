
---

Now update `progress.md`.

Append:

```md id="8b5hkr"
## Module Review — 0.1

### What I Built
- Local Python environment using uv
- Structured portfolio repository
- GitHub-connected project
- Basic Python execution workflow
- Dependency management setup
- Ruff linting configuration

### Key Concepts Learned
- Virtual environments isolate dependencies
- pyproject.toml defines project configuration
- Lock files improve reproducibility
- __name__ == "__main__" separates execution from imports
- Linters catch static issues automatically

### What Broke / Failure Modes
- .gitignore does not retroactively untrack files
- Lint auto-fix cannot safely change semantic behavior
- Environment activation mistakes can install packages globally

### Still Weak
- Python module/import system depth
- Packaging ecosystem understanding
- Tooling internals

### Next Module
0.2 — Python refresher:
- typing
- async
- dataclasses
- pydantic
- logging