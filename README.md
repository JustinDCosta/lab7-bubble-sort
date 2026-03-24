# Bubble Sort Learning App

A small Python project to learn and practice Bubble Sort implementation with guided function structure and automated tests.

## Project Goals

- Understand Bubble Sort step by step.
- Practice writing clean Python functions with type hints.
- Validate behavior using basic pytest tests.

## Features

- Console app that accepts comma-separated integers.
- Bubble Sort implementation with early-stop optimization.
- Function-level decomposition:
  - `get_numbers_from_user`
  - `should_swap`
  - `swap_neighbors`
  - `bubble_pass`
  - `bubble_sort`
  - `print_results`
- Pytest suite covering normal and edge cases.

## Requirements

- Python 3.10+
- pytest

## Setup

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install test dependency:

```powershell
pip install pytest
```

## Run the App

```powershell
python main.py
```

Example input:

```text
5, 1, 4, 2, 8
```

Example output:

```text
Original: [5, 1, 4, 2, 8]
Sorted:   [1, 2, 4, 5, 8]
```

## Run Tests

Run all tests:

```powershell
python -m pytest -v
```

Run only this project's test file:

```powershell
python -m pytest test_main.py -v
```

## Project Structure

```text
.
|- main.py         # Bubble Sort application
|- test_main.py    # pytest test suite
|- README.md       # project documentation
|- JOURNAL.md      # interaction/change log
```

## Notes

- `bubble_sort` returns a sorted copy and keeps the original list unchanged.
- Input parsing expects integers separated by commas.
- Invalid input (non-integer tokens) will raise a `ValueError`.
