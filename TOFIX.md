# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pyclassifiers/values.py:41` - `Environment__GPU__NVIDIACUDA__11` is defined twice (line 17 = "NVIDIA CUDA :: 1.1", line 41 = "NVIDIA CUDA :: 11"), so the 1.1 classifier is silently shadowed and unreachable; the generator at `scripts/create.py:26` strips `.` and collapses distinct versions into one name - map `.` to `_` (or otherwise disambiguate), make the script fail on a duplicate name, and regenerate.

## Medium

- `src/pyclassifiers/values.py:1` - the generated list is stale: about 20 classifiers PyPI publishes today are missing (e.g. `Programming Language :: Python :: 3.16`, `Framework :: Django :: 6`, `Environment :: Cygwin (MS Windows)`, `Programming Language :: Zig`); rerun `scripts/create.py` and release.
- `pyproject.toml:37` - `requests` is a runtime dependency of the published package, but only the maintainer script `scripts/create.py:9` uses it; nothing under `src/` imports it - move it to the dev dependency group (with `types-requests`) so every consumer stops pulling it in.
- `pyproject.toml:85` - `[[tool.mypy.overrides]]` sets `ignore_missing_imports` for `pyclassifiers.*`, i.e. the package itself (which even ships `py.typed`), not a third-party library without stubs; remove the override.

## Low

- `scripts/create.py:11` - uses the legacy `pypi.python.org/pypi?%3Aaction=list_classifiers` endpoint (now only a redirect to pypi.org); point it at `https://pypi.org/pypi?%3Aaction=list_classifiers` or generate from the `trove-classifiers` package. Same URL in `tera.snippets/main.md.tera:6`.
- `scripts/create.py:30` - escapes `'` as `\'` inside double-quoted strings (e.g. `values.py:60` `"Handhelds/PDA\'s"`), an unnecessary escape in generated code; drop that substitution.
- `pyproject.toml:80` - `mypy_path = "src:python:scripts"` names a `python/` directory that does not exist; drop it.
- `rsconstruct.toml:28` - `[processor.ruff]` and `[processor.mypy]` (line 32) list `config` in `src_dirs`, but `config/` holds only `.lua` files; drop it.
- `pyproject.toml:23` - keyword `distutils` refers to a module removed in Python 3.12 while the package requires 3.14; drop it (and from `config/project.lua:8`).
- `doc/TODO.txt:1` - the file is empty; delete it.
