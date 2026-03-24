"""Tests for separated Bubble Sort core logic and input helpers."""

import cli_inputs
import sorting_logic
import terminal_visualizer


class TestInputHelpers:
    def test_parse_numbers_success(self):
        assert cli_inputs.parse_numbers("8, 3, 5") == [8, 3, 5]

    def test_parse_numbers_invalid_empty_token(self):
        try:
            cli_inputs.parse_numbers("1,,2")
            assert False
        except ValueError:
            assert True

    def test_terminal_speed_default(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "unknown")
        assert cli_inputs.get_terminal_speed_delay() == 0.55

    def test_visual_mode_default(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "nope")
        assert cli_inputs.get_visual_mode() == "comparison"


class TestSortingLogic:
    def test_normalize_mode(self):
        assert sorting_logic.normalize_mode("swap-only") == "swap-only"
        assert sorting_logic.normalize_mode("bad") == "comparison"

    def test_build_sort_frames_sorts_values(self):
        values = [5, 1, 4, 2, 8]
        frames = sorting_logic.build_sort_frames(values, "comparison")
        assert frames[-1].values == [1, 2, 4, 5, 8]
        assert values == [5, 1, 4, 2, 8]

    def test_swap_only_generates_fewer_frames(self):
        values = [5, 1, 4, 2, 8]
        frames_cmp = sorting_logic.build_sort_frames(values, "comparison")
        frames_swap = sorting_logic.build_sort_frames(values, "swap-only")
        assert len(frames_swap) < len(frames_cmp)


class TestTerminalVisualizer:
    def test_scaled_bar_length_equal_bounds(self):
        assert terminal_visualizer.scaled_bar_length(3, 3, 3, width=30) == 15

    def test_bubble_sort_visual_with_no_sleep(self, monkeypatch):
        monkeypatch.setattr(terminal_visualizer, "clear_screen", lambda: None)
        monkeypatch.setattr(terminal_visualizer.time, "sleep", lambda _: None)
        monkeypatch.setattr(terminal_visualizer, "render_frame", lambda _: None)

        result = terminal_visualizer.bubble_sort_visual([3, 1, 2], delay=0.0, mode="comparison")
        assert result == [1, 2, 3]
