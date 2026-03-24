"""Test suite for Bubble Sort implementation using pytest."""

import pytest
from main import (
    should_swap,
    swap_neighbors,
    bubble_pass,
    bubble_sort,
    print_results,
)


class TestShouldSwap:
    """Tests for the comparison rule."""

    def test_should_swap_when_left_greater(self):
        """Left > Right should return True."""
        assert should_swap(5, 3) is True

    def test_should_swap_when_left_equal(self):
        """Left == Right should return False."""
        assert should_swap(3, 3) is False

    def test_should_swap_when_left_smaller(self):
        """Left < Right should return False."""
        assert should_swap(2, 4) is False


class TestSwapNeighbors:
    """Tests for in-place neighbor swapping."""

    def test_swap_neighbors_basic(self):
        """Swap two adjacent items in a list."""
        values = [5, 3]
        swap_neighbors(values, 0)
        assert values == [3, 5]

    def test_swap_neighbors_middle(self):
        """Swap neighbors in the middle of a list."""
        values = [1, 5, 3, 2]
        swap_neighbors(values, 1)
        assert values == [1, 3, 5, 2]


class TestBubblePass:
    """Tests for a single pass of Bubble Sort."""

    def test_bubble_pass_zero_swaps_already_sorted(self):
        """A sorted list should return False (no swaps)."""
        values = [1, 2, 3, 4]
        result = bubble_pass(values, 0)
        assert result is False
        assert values == [1, 2, 3, 4]

    def test_bubble_pass_with_swaps(self):
        """An unsorted list should return True and move largest to end."""
        values = [3, 1, 2]
        result = bubble_pass(values, 0)
        assert result is True
        assert values == [1, 2, 3]

    def test_bubble_pass_respects_pass_index(self):
        """Pass index should limit the range of comparisons."""
        values = [1, 4, 2, 3]
        # Pass 1 means last 1 item is already sorted, so compare [1, 4, 2]
        result = bubble_pass(values, 1)
        assert result is True
        assert values == [1, 2, 4, 3]


class TestBubbleSort:
    """Tests for complete Bubble Sort function."""

    def test_bubble_sort_empty_list(self):
        """Empty list should return empty list."""
        assert bubble_sort([]) == []

    def test_bubble_sort_single_element(self):
        """Single element list should return as-is."""
        assert bubble_sort([5]) == [5]

    def test_bubble_sort_two_elements_unsorted(self):
        """Two element unsorted list should sort correctly."""
        assert bubble_sort([2, 1]) == [1, 2]

    def test_bubble_sort_already_sorted(self):
        """Already sorted list should return sorted (early termination)."""
        assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

    def test_bubble_sort_reverse_sorted(self):
        """Reverse sorted list should sort correctly."""
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_bubble_sort_random_unsorted(self):
        """Random unsorted list should sort correctly."""
        assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]

    def test_bubble_sort_with_duplicates(self):
        """List with duplicate values should sort correctly."""
        assert bubble_sort([3, 1, 3, 1, 2]) == [1, 1, 2, 3, 3]

    def test_bubble_sort_preserves_original(self):
        """bubble_sort should not modify the original list."""
        original = [5, 1, 4]
        sorted_list = bubble_sort(original)
        assert original == [5, 1, 4]  # Original unchanged
        assert sorted_list == [1, 4, 5]  # New sorted list

    def test_bubble_sort_negative_numbers(self):
        """List with negative numbers should sort correctly."""
        assert bubble_sort([2, -1, 0, 3]) == [-1, 0, 2, 3]

    def test_bubble_sort_large_list(self):
        """Larger list should sort correctly."""
        unsorted = [9, 3, 7, 1, 5, 8, 2, 6, 4]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert bubble_sort(unsorted) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
