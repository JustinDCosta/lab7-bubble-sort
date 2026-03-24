"""Shared CLI input parsing and prompt helpers."""

from __future__ import annotations

from sorting_logic import MODE_OPTIONS


TERMINAL_SPEED_SECONDS = {
    "slow": 1.00,
    "normal": 0.55,
    "fast": 0.22,
}

PYGAME_SPEED_MS = {
    "slow": 1000,
    "normal": 550,
    "fast": 220,
}


def parse_numbers(raw_text: str) -> list[int]:
    """Parse comma-separated integers from input text."""
    tokens = [token.strip() for token in raw_text.split(",")]
    if not tokens or any(token == "" for token in tokens):
        raise ValueError("Please provide comma-separated integers, for example: 8, 3, 5, 1, 4")
    return [int(token) for token in tokens]


def get_numbers_from_user(min_count: int = 1) -> list[int]:
    """Prompt until valid comma-separated integer input is provided."""
    while True:
        raw_text = input("Enter numbers separated by commas (e.g., 8, 3, 5, 1, 4): ").strip()
        try:
            values = parse_numbers(raw_text)
            if len(values) < min_count:
                print(f"Please enter at least {min_count} numbers.")
                continue
            return values
        except ValueError as error:
            print(f"Invalid input: {error}")


def get_visual_mode() -> str:
    """Prompt and return visualization mode."""
    choice = input("Choose mode [comparison/swap-only] (default: comparison): ").strip().lower()
    if choice in MODE_OPTIONS:
        return choice
    return "comparison"


def get_terminal_speed_delay() -> float:
    """Prompt and return terminal animation frame delay in seconds."""
    choice = input("Choose speed [slow/normal/fast] (default: normal): ").strip().lower()
    return TERMINAL_SPEED_SECONDS.get(choice, TERMINAL_SPEED_SECONDS["normal"])


def get_pygame_speed_delay_ms() -> int:
    """Prompt and return pygame animation frame delay in milliseconds."""
    choice = input("Choose speed [slow/normal/fast] (default: normal): ").strip().lower()
    return PYGAME_SPEED_MS.get(choice, PYGAME_SPEED_MS["normal"])
