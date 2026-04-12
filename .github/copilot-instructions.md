# Project Guidelines

## Workspace Focus
- This workspace is a Japanese-first weekly tech news writing project with article folders that bundle Markdown, exported HTML, images, and small verification code.
- Prefer minimal, task-focused changes inside the target article folder instead of repo-wide refactors.
- Treat generated outputs as disposable unless the task explicitly asks to update them. HTML and PDF exports are gitignored in [.gitignore](.gitignore).

## Article Workflow
- Shared article conventions live in [00_共通/template.md](00_共通/template.md) and topic tracking lives in [00_共通/weekly_tech_news.md](00_共通/weekly_tech_news.md). Link to those files instead of duplicating their content.
- Preserve the frontmatter used by Markdown Preview Enhanced: offline HTML export, TOC, and embedded local images.
- Keep article prose, headings, notes, and callout text in Japanese unless the file already uses a different style.
- When adding images to Markdown, use the workspace copy rule that places assets under each article's img directory.

## Python And C Support Code
- Python support code for the current article lives under [20260413_Why_use_Python_in_AI_project/Python](20260413_Why_use_Python_in_AI_project/Python).
- Use Python 3.12 or newer as defined in [20260413_Why_use_Python_in_AI_project/Python/pyproject.toml](20260413_Why_use_Python_in_AI_project/Python/pyproject.toml).
- Preferred Python checks in that folder:
  - ruff check .
  - ruff format .
- Typical script runs in that folder:
  - uv run .\benchmark_loop.py
  - uv run .\simple_loop.py
  - uv run .\Generate_Graph\plot_result.py
- C examples under [20260413_Why_use_Python_in_AI_project/C](20260413_Why_use_Python_in_AI_project/C) do not have a build system. Compile them explicitly when needed instead of assuming Makefile or CMake exists.

## Conventions
- Respect the existing Ruff setup: line length 150, Python target version 3.12, Google-style docstrings, and Japanese full-width punctuation allowed in comments and strings.
- Keep Python code simple and typed. [20260413_Why_use_Python_in_AI_project/Python/pyproject.toml](20260413_Why_use_Python_in_AI_project/Python/pyproject.toml) enables disallow_untyped_defs in mypy config even though mypy is not currently installed.
- Match the repository's VS Code workflow in [weekly_tech_news.code-workspace](weekly_tech_news.code-workspace): Markdown word wrap enabled, Ruff as the Python formatter, and Markdown Preview Enhanced as the expected preview/export tool.

## Known Gaps
- [.vscode/launch.json](.vscode/launch.json) points to a non-existent src/main.py template path. Do not rely on it without fixing it first.
- There is no test suite configured. If validation is needed, run the relevant script directly and report what you executed.
- Search results can be noisy because generated HTML exports are present in article folders. Prefer Markdown, Python, C, and config files when gathering context.