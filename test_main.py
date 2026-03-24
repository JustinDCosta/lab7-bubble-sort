"""Tests for the terminal Bubble Sort visualizer."""

import main


class TestGetSpeedDelay:
    def test_slow_speed(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "slow")
        assert main.get_speed_delay() == 0.65

    def test_fast_speed(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "fast")
        assert main.get_speed_delay() == 0.10

    def test_default_speed_on_unknown(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "turbo")
        assert main.get_speed_delay() == 0.35


class TestGetVisualMode:
    def test_swap_only_mode(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "swap-only")
        assert main.get_visual_mode() == "swap-only"

    def test_default_comparison_mode(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "anything")
        assert main.get_visual_mode() == "comparison"


class TestScaledBarLength:
    def test_equal_min_max(self):
        assert main.scaled_bar_length(5, 5, 5, width=30) == 15

    def test_scales_to_at_least_one(self):
        value = main.scaled_bar_length(0, 0, 10, width=30)
        assert value >= 1

    def test_scales_upper_value(self):
        assert main.scaled_bar_length(10, 0, 10, width=30) == 30


class TestBubbleSortVisual:
    def setup_method(self):
        self.render_calls = []

    def _patch_visual_side_effects(self, monkeypatch):
        monkeypatch.setattr(main, "clear_screen", lambda: None)
        monkeypatch.setattr(main.time, "sleep", lambda _: None)

        def fake_render(*args, **kwargs):
            self.render_calls.append((args, kwargs))

        monkeypatch.setattr(main, "render_frame", fake_render)

    def test_sorts_unsorted_values(self, monkeypatch):
        self._patch_visual_side_effects(monkeypatch)
        values = [5, 1, 4, 2, 8]
        sorted_values = main.bubble_sort_visual(values, delay=0.0, mode="comparison")
        assert sorted_values == [1, 2, 4, 5, 8]
        assert values == [5, 1, 4, 2, 8]

    def test_sorts_with_negative_numbers(self, monkeypatch):
        self._patch_visual_side_effects(monkeypatch)
        values = [2, -1, 0, 3]
        assert main.bubble_sort_visual(values, delay=0.0, mode="comparison") == [-1, 0, 2, 3]

    def test_early_break_on_sorted_input_has_limited_frames(self, monkeypatch):
        self._patch_visual_side_effects(monkeypatch)
        values = [1, 2, 3, 4]
        sorted_values = main.bubble_sort_visual(values, delay=0.0, mode="comparison")
        assert sorted_values == [1, 2, 3, 4]
        # 3 comparison frames on first pass + 1 final frame
        assert len(self.render_calls) == 4

    def test_swap_only_mode_renders_less_than_comparison_mode(self, monkeypatch):
        self._patch_visual_side_effects(monkeypatch)
        values = [5, 1, 4, 2, 8]

        main.bubble_sort_visual(values, delay=0.0, mode="comparison")
        comparison_frames = len(self.render_calls)

        self.render_calls.clear()
        main.bubble_sort_visual(values, delay=0.0, mode="swap-only")
        swap_only_frames = len(self.render_calls)

        assert swap_only_frames < comparison_frames

