# Bubble Sort Learning App

A Python terminal app that visualizes Bubble Sort as it runs, with selectable playback speed and visualization mode.

## Project Goals

- Understand Bubble Sort step by step.
- Explore how each comparison and swap changes the list.
- Practice writing clean Python functions with type hints and tests.

## Features

- Console app that accepts comma-separated integers.
- Animated terminal visualization (auto-play).
- Refactored architecture with separation of concerns:
  - core sorting logic in `sorting_logic.py`
  - user input parsing/prompts in `cli_inputs.py`
  - terminal UI rendering in `terminal_visualizer.py`
  - pygame UI rendering in `pygame_visualizer.py`
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
- Dependencies listed in `requirements.txt`

## Setup

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install project dependencies:

```powershell
pip install -r requirements.txt
```

Note:

- The graphics dependency uses `pygame-ce`, which is imported in code as `pygame`.
- This provides reliable compatibility with newer Python versions (including Python 3.14).

## Run the Terminal Visualizer (main.py)

```powershell
python main.py
```

`main.py` is the terminal visualizer entrypoint.

Example input:

```text
5, 1, 4, 2, 8
```

Quick start option:

- Press `Enter` at the numbers prompt to auto-generate a random demo list.
- Type `n=<count>` (for example `n=25`) to auto-generate a random list of that size.

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

## Run the Pygame Visualizer

```powershell
python pygame_visualizer.py
```

This starts a windowed 2D Bubble Sort animation with bars and highlighted comparisons/swaps.

`pygame_visualizer.py` is separate from `main.py` and launches the graphics window.

Quick start option:

- Press `Enter` at the numbers prompt to auto-generate a random demo list.
- Type `n=<count>` (for example `n=25`) to auto-generate a random list of that size.

Controls:

- `Space`: pause/resume
- `Right Arrow`: single-step forward (when paused)
- `Left Arrow`: single-step backward (when paused)
- `Up Arrow`: faster playback
- `Down Arrow`: slower playback
- `R`: restart
- `Q` or `Esc`: quit

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
|- main.py                 # thin terminal entrypoint
|- sorting_logic.py        # pure bubble sort/frame generation logic
|- cli_inputs.py           # shared input parsing and prompt helpers
|- terminal_visualizer.py  # terminal-only rendering/UI
|- pygame_visualizer.py    # pygame-only rendering/UI
|- test_main.py            # entrypoint smoke tests
|- test_sorting_logic.py   # core/input/terminal unit tests
|- README.md       # project documentation
|- JOURNAL.md      # interaction/change log
```

## Notes

- bubble_sort_visual returns a sorted copy and keeps the original input list unchanged.
- Input parsing expects integers separated by commas.
- You can generate random input with `Enter` (default size) or `n=<count>`.
- Invalid input is handled with a retry prompt.
- ANSI colors are used for highlights and may render differently depending on terminal support.
