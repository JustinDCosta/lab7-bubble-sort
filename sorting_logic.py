"""Core Bubble Sort logic with no UI dependencies."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


EventType = Literal["compare", "swap", "pass_done", "done"]
MODE_OPTIONS = {"comparison", "swap-only"}


@dataclass(frozen=True)
class SortFrame:
    """Snapshot of Bubble Sort state at one visualization step."""

    values: list[int]
    left_idx: int
    right_idx: int
    pass_index: int
    compare_count: int
    swap_count: int
    event: EventType


def normalize_mode(mode: str) -> str:
    """Normalize user-provided mode into a supported value."""
    if mode in MODE_OPTIONS:
        return mode
    return "comparison"


def build_sort_frames(values: list[int], mode: str) -> list[SortFrame]:
    """Generate Bubble Sort frames for either comparison or swap-only mode."""
    result = values.copy()
    n = len(result)
    compare_count = 0
    swap_count = 0
    frames: list[SortFrame] = []

    mode = normalize_mode(mode)

    for pass_index in range(n - 1):
        swapped = False

        for j in range(n - 1 - pass_index):
            compare_count += 1
            will_swap = result[j] > result[j + 1]

            if mode == "comparison" or (mode == "swap-only" and will_swap):
                frames.append(
                    SortFrame(
                        values=result.copy(),
                        left_idx=j,
                        right_idx=j + 1,
                        pass_index=pass_index,
                        compare_count=compare_count,
                        swap_count=swap_count,
                        event="compare",
                    )
                )

            if will_swap:
                result[j], result[j + 1] = result[j + 1], result[j]
                swap_count += 1
                swapped = True
                frames.append(
                    SortFrame(
                        values=result.copy(),
                        left_idx=j,
                        right_idx=j + 1,
                        pass_index=pass_index,
                        compare_count=compare_count,
                        swap_count=swap_count,
                        event="swap",
                    )
                )

        frames.append(
            SortFrame(
                values=result.copy(),
                left_idx=-1,
                right_idx=-1,
                pass_index=pass_index,
                compare_count=compare_count,
                swap_count=swap_count,
                event="pass_done",
            )
        )

        if not swapped:
            break

    frames.append(
        SortFrame(
            values=result.copy(),
            left_idx=-1,
            right_idx=-1,
            pass_index=max(0, n - 1),
            compare_count=compare_count,
            swap_count=swap_count,
            event="done",
        )
    )
    return frames
