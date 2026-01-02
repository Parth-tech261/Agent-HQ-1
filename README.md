# Agent-HQ-1

A tiny example Python project that provides simple math utilities and accompanying tests.

This repository is a minimal workspace used for demonstrations and CI/test automation.

**Contents**
- `app.py`: small module with `add()` and `divide()` functions.
- `test/`: pytest tests for the module.
- `.github/workflows/ci.yml`: GitHub Actions workflow that runs tests on push/PR.

## Setup

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies (if any) from `requirements.txt`:

```bash
pip install -r requirements.txt
```

3. (Optional) Upgrade `pip`:

```bash
pip install --upgrade pip
```

## Running tests

Run the test suite with `pytest` from the repository root:

```bash
pytest -q
```

The repository includes a CI workflow at `.github/workflows/ci.yml` that installs dependencies and runs the same tests on push and pull requests to `main`.

## Notes

- The `divide()` function will raise `ZeroDivisionError` for `b == 0` and `TypeError` for incompatible operand types; tests exercise those behaviors.
- If you want stricter input validation or type hints in `app.py`, I can update the module and tests accordingly.

