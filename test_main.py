"""Smoke tests for project entrypoints after refactor."""

import main
import terminal_visualizer


def test_main_exposes_callable_entrypoint():
    assert callable(main.main)


def test_main_entrypoint_is_terminal_main():
    assert main.main is terminal_visualizer.main

