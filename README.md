# Bubble Sort Learning App

A Python terminal app that visualizes Bubble Sort as it runs, with selectable playback speed and visualization mode.

## Project Goals

- Understand Bubble Sort step by step.
- Explore how each comparison and swap changes the list.
- Practice writing clean Python functions with type hints and tests.

## Features

- Console app that accepts comma-separated integers.
- Animated terminal visualization (auto-play).
- Two visualization modes:
  - comparison: render every comparison
  - swap-only: render only comparison steps that swap
- Two synchronized views per frame:
  - numeric list with highlighted pair
  - scaled bar chart with highlighted pair
- Playback speed presets: slow, normal, fast.
- Bubble Sort implementation with early-stop optimization.
- Pytest suite for input helpers, scaling, and visual sorting behavior.

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

You will then be asked for:

```text
Choose speed [slow/normal/fast] (default: normal)
Choose mode [comparison/swap-only] (default: comparison)
```

Example final output:

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
|- main.py         # terminal visualizer and sorting logic
|- test_main.py    # pytest test suite
|- README.md       # project documentation
|- JOURNAL.md      # interaction/change log
```

## Notes

- bubble_sort_visual returns a sorted copy and keeps the original input list unchanged.
- Input parsing expects integers separated by commas.
- Invalid input (non-integer tokens) will raise a `ValueError`.
- ANSI colors are used for highlights and may render differently depending on terminal support.
