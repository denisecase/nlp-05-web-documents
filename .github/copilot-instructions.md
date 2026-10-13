# AI Instructions (AGENTS / CLAUDE / Copilot)

## WHY

- This repo uses a uniform, reproducible workflow based on **uv** and **pyproject.toml**.
- These instructions exist to prevent tool drift (e.g., pip) and OS mismatch.

## Requirements

- Use **uv** for all environment, dependency, and run commands in this repo.
- Do **not** recommend or use `pip install ...` as the primary workflow.
- This repo targets **Python 3.14**, pinned via uv.
- Commands and guidance must work on Windows, macOS, and Linux.
- If shell-specific commands are unavoidable, provide both:
  - PowerShell (Windows)
  - bash/zsh (macOS/Linux)

## Quickstart

- Install **uv** using the official method for your OS.
- Keep uv current.
- Pin Python 3.14 for this project using uv.
- Sync dependencies (dev + docs) and upgrade.

```shell
uv self update
uv python pin 3.14
uv sync --upgrade
```

## pre-commit

- pre-commit runs only on tracked / staged files.
- Developers should `git add -A` files before expecting hooks to run.
- Developers may need to **repeat** the git add / git commit commands if files changed

```
uvx pre-commit install
git add -A
uvx pre-commit run --all-files
```

## Run Python as a Module (src/nlp/)

```
uv run python -m nlp.module_name
```

# Notebooks in notebooks/

Select the kernel and Run All.

## Common Tasks

Run all commands via **uv**.

Lint / format:

```shell
uv run ruff format .
uv run ruff check .
```

Build documentation:

```shell
uv run zensical build
```
