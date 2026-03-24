"""Terminal Bubble Sort visualizer.

The app animates Bubble Sort in the terminal using numeric and bar views,
supports speed selection, and supports comparison vs swap-only modes.
"""

import time

RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BAR_WIDTH = 30


def get_numbers_from_user() -> list[int]:
    """Ask the user for comma-separated integers and return them as a list."""
    user_input = input("Enter numbers separated by commas (e.g., 8, 3, 5, 1, 4): ")
    return [int(x.strip()) for x in user_input.split(",")]


def get_speed_delay() -> float:
    """Get playback speed and convert it to a delay value in seconds."""
    speed = input("Choose speed [slow/normal/fast] (default: normal): ").strip().lower()
    if speed == "slow":
        return 0.65
    if speed == "fast":
        return 0.10
    return 0.35


def get_visual_mode() -> str:
    """Get visualization mode from the user."""
    mode = input("Choose mode [comparison/swap-only] (default: comparison): ").strip().lower()
    if mode == "swap-only":
        return "swap-only"
    return "comparison"


def clear_screen() -> None:
    """Clear the terminal screen for animation frames without spawning a shell."""
    # ANSI escape sequence: clear screen + move cursor to top-left.
    print("\033[2J\033[H", end="")


def scaled_bar_length(value: int, min_val: int, max_val: int, width: int = 30) -> int:
    """Scale a value into a terminal bar length."""
    if max_val == min_val:
        return max(1, width // 2)
    normalized = (value - min_val) / (max_val - min_val)
    return max(1, int(normalized * width))


def render_frame(
    values: list[int],
    left_idx: int,
    right_idx: int,
    pass_index: int,
    compare_count: int,
    swap_count: int,
    did_swap: bool,
) -> None:
    """Render one visualization frame for the current comparison."""
    if not values:
        print(f"{CYAN}Bubble Sort Visualization (auto-play){RESET}")
        print("No values to sort.")
        return

    min_val = min(values)
    max_val = max(values)

    print(f"{CYAN}Bubble Sort Visualization (auto-play){RESET}")
    print(f"Pass: {pass_index} | Comparisons: {compare_count} | Swaps: {swap_count}\n")

    numeric_cells = []
    for i, v in enumerate(values):
        if i == left_idx or i == right_idx:
            color = GREEN if did_swap else YELLOW
            numeric_cells.append(f"{color}[{v}]{RESET}")
        else:
            numeric_cells.append(f" {v} ")
    print("Numbers:", " ".join(numeric_cells), "\n")

    for i, v in enumerate(values):
        bar_len = scaled_bar_length(v, min_val, max_val, width=BAR_WIDTH)
        bar = "#" * bar_len
        if i == left_idx or i == right_idx:
            color = GREEN if did_swap else YELLOW
            marker = "swap" if did_swap else "compare"
            print(f"{i:>2}: {v:>4} |{color}{bar:<{BAR_WIDTH}}{RESET}| <-- {marker}")
        else:
            print(f"{i:>2}: {v:>4} |{bar:<{BAR_WIDTH}}|")


def bubble_sort_visual(values: list[int], delay: float, mode: str) -> list[int]:
    """Bubble Sort with terminal visualization and auto-play."""
    if mode not in {"comparison", "swap-only"}:
        mode = "comparison"

    result = values.copy()
    n = len(result)
    compare_count = 0
    swap_count = 0

    for pass_index in range(n - 1):
        swapped = False

        for j in range(n - 1 - pass_index):
            compare_count += 1
            will_swap = result[j] > result[j + 1]

            if mode == "comparison" or (mode == "swap-only" and will_swap):
                clear_screen()
                render_frame(
                    result,
                    j,
                    j + 1,
                    pass_index,
                    compare_count,
                    swap_count,
                    did_swap=False,
                )
                time.sleep(delay)

            if will_swap:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
                swap_count += 1

                clear_screen()
                render_frame(
                    result,
                    j,
                    j + 1,
                    pass_index,
                    compare_count,
                    swap_count,
                    did_swap=True,
                )
                time.sleep(delay)

        if not swapped:
            break

    clear_screen()
    print(f"{GREEN}Final sorted result:{RESET}")
    render_frame(
        result,
        -1,
        -1,
        pass_index=n - 1 if n > 0 else 0,
        compare_count=compare_count,
        swap_count=swap_count,
        did_swap=False,
    )
    return result


def print_results(original: list[int], sorted_values: list[int]) -> None:
    """Display before/after values for easy visual checking."""
    print("\nOriginal:", original)
    print("Sorted:  ", sorted_values)


def main() -> None:
    """Program entry point for the Bubble Sort learning app."""
    original = get_numbers_from_user()
    delay = get_speed_delay()
    mode = get_visual_mode()
    sorted_values = bubble_sort_visual(original, delay=delay, mode=mode)
    print_results(original, sorted_values)


if __name__ == "__main__":
    main()
