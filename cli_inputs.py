"""Shared CLI input parsing and prompt helpers."""

from __future__ import annotations

import random

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

DEFAULT_RANDOM_COUNT = 12
DEFAULT_RANDOM_MIN = 1
DEFAULT_RANDOM_MAX = 99
MAX_RANDOM_COUNT = 500


def parse_numbers(raw_text: str) -> list[int]:
    """Parse comma-separated integers from input text."""
    tokens = [token.strip() for token in raw_text.split(",")]
    if not tokens or any(token == "" for token in tokens):
        raise ValueError("Please provide comma-separated integers, for example: 8, 3, 5, 1, 4")
    return [int(token) for token in tokens]


def generate_random_values(count: int) -> list[int]:
    """Generate a random integer list of requested size."""
    return [random.randint(DEFAULT_RANDOM_MIN, DEFAULT_RANDOM_MAX) for _ in range(count)]


def parse_random_count_shortcut(raw_text: str) -> int | None:
    """Parse n=<count> shortcut. Returns None if format does not match."""
    if not raw_text.lower().startswith("n="):
        return None

    value_text = raw_text[2:].strip()
    if value_text == "":
        raise ValueError("Please provide a value after n=, for example n=20")

    count = int(value_text)
    if count <= 0:
        raise ValueError("n must be greater than 0")
    if count > MAX_RANDOM_COUNT:
        raise ValueError(f"n is too large; please use n <= {MAX_RANDOM_COUNT}")
    return count


def get_numbers_from_user(min_count: int = 1) -> list[int]:
    """Prompt until valid comma-separated integer input is provided."""
    while True:
        raw_text = input(
            "Enter numbers separated by commas (e.g., 8, 3, 5, 1, 4) "
            "or press Enter for random, or type n=<count> (e.g., n=25): "
        ).strip()

        if raw_text == "":
            values = generate_random_values(DEFAULT_RANDOM_COUNT)
            print(f"Using generated list: {values}")
            return values

        try:
            random_count = parse_random_count_shortcut(raw_text)
            if random_count is not None:
                values = generate_random_values(random_count)
                print(f"Using generated list (n={random_count}): {values}")
                return values
        except ValueError as error:
            print(f"Invalid input: {error}")
            continue

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
