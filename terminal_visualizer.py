"""Terminal renderer for Bubble Sort frames."""

from __future__ import annotations

import time

from cli_inputs import get_numbers_from_user, get_terminal_speed_delay, get_visual_mode
from sorting_logic import SortFrame, build_sort_frames


RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BAR_WIDTH = 30


def clear_screen() -> None:
    """Clear terminal without spawning a shell."""
    print("\033[2J\033[H", end="")


def scaled_bar_length(value: int, min_val: int, max_val: int, width: int = BAR_WIDTH) -> int:
    """Scale a value into terminal bar width range."""
    if max_val == min_val:
        return max(1, width // 2)
    normalized = (value - min_val) / (max_val - min_val)
    return max(1, int(normalized * width))


def render_frame(frame: SortFrame) -> None:
    """Render one frame of sorting state."""
    values = frame.values
    if not values:
        print(f"{CYAN}Bubble Sort Visualization (auto-play){RESET}")
        print("No values to sort.")
        return

    min_val = min(values)
    max_val = max(values)

    print(f"{CYAN}Bubble Sort Visualization (auto-play){RESET}")
    print(
        f"Pass: {frame.pass_index} | Comparisons: {frame.compare_count} | "
        f"Swaps: {frame.swap_count} | Event: {frame.event}\n"
    )

    numeric_cells = []
    for i, value in enumerate(values):
        if i == frame.left_idx or i == frame.right_idx:
            color = GREEN if frame.event == "swap" else YELLOW
            numeric_cells.append(f"{color}[{value}]{RESET}")
        else:
            numeric_cells.append(f" {value} ")
    print("Numbers:", " ".join(numeric_cells), "\n")

    for i, value in enumerate(values):
        bar_len = scaled_bar_length(value, min_val, max_val, width=BAR_WIDTH)
        bar = "#" * bar_len
        if i == frame.left_idx or i == frame.right_idx:
            color = GREEN if frame.event == "swap" else YELLOW
            marker = frame.event if frame.event in {"compare", "swap"} else "active"
            print(f"{i:>2}: {value:>4} |{color}{bar:<{BAR_WIDTH}}{RESET}| <-- {marker}")
        else:
            print(f"{i:>2}: {value:>4} |{bar:<{BAR_WIDTH}}|")


def bubble_sort_visual(values: list[int], delay: float, mode: str) -> list[int]:
    """Animate Bubble Sort in terminal and return sorted values."""
    frames = build_sort_frames(values, mode)
    for frame in frames:
        clear_screen()
        render_frame(frame)
        time.sleep(delay)

    return frames[-1].values if frames else values.copy()


def print_results(original: list[int], sorted_values: list[int]) -> None:
    """Display before/after lists."""
    print("\nOriginal:", original)
    print("Sorted:  ", sorted_values)


def main() -> None:
    """Entry point for terminal visualization app."""
    original = get_numbers_from_user(min_count=1)
    delay = get_terminal_speed_delay()
    mode = get_visual_mode()
    sorted_values = bubble_sort_visual(original, delay=delay, mode=mode)
    print_results(original, sorted_values)
