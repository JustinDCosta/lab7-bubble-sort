"""Bubble Sort learning skeleton.

Fill in each TODO in order. Run after each step to verify behavior.
"""


def get_numbers_from_user() -> list[int]:
	"""Ask the user for comma-separated integers and return them as a list.

	Example input: 5, 1, 4, 2, 8
	"""
	# TODO 1:
	# 1) Read a line from input().
	# 2) Split by comma.
	# 3) Strip spaces from each piece.
	# 4) Convert each piece to int.
	# 5) Return the resulting list.
	return [int(x.strip()) for x in input().split(',')]


def should_swap(left: int, right: int) -> bool:
	"""Return True when two neighbors are in the wrong ascending order."""
	# TODO 2:
	# Return True if left should come after right.
	return left > right


def swap_neighbors(values: list[int], index: int) -> None:
	"""Swap values[index] with values[index + 1] in-place."""
	# TODO 3:
	# Use tuple unpacking to swap these two items.
	# Example: a, b = b, a
	values[index], values[index + 1] = values[index + 1], values[index]


def bubble_pass(values: list[int], pass_index: int) -> bool:
	"""Run one pass of Bubble Sort.

	Returns True if at least one swap happened; otherwise False.
	"""
	swapped = False

	# TODO 4:
	# Complete one pass over the UNSORTED part only.
	# Hint: last pass_index items are already in final position.
	# For each j in the pass range:
	# - if should_swap(values[j], values[j + 1]) is True:
	#     - call swap_neighbors(values, j)
	#     - set swapped = True

	for j in range(len(values) - 1 - pass_index):
		if should_swap(values[j], values[j + 1]):
			swap_neighbors(values, j)
			swapped = True

	return swapped


def bubble_sort(values: list[int]) -> list[int]:
	"""Return a sorted copy of values using Bubble Sort (ascending)."""
	result = values.copy()

	# TODO 5:
	# Outer loop over pass_index from 0 to len(result) - 2.
	# Call bubble_pass(result, pass_index) each time.
	# If no swap happened in a pass, break early (already sorted).
	for pass_index in range(len(result) - 1):
		if not bubble_pass(result, pass_index):
			break

	return result


def print_results(original: list[int], sorted_values: list[int]) -> None:
	"""Display before/after values for easy visual checking."""
	print("Original:", original)
	print("Sorted:  ", sorted_values)


def main() -> None:
	"""Program entry point for the Bubble Sort learning app."""
	# TODO 6:
	# 1) Get numbers from the user.
	# 2) Sort them with bubble_sort().
	# 3) Print both original and sorted lists.
	original = get_numbers_from_user()
	sorted_values = bubble_sort(original)
	print_results(original, sorted_values)


if __name__ == "__main__":
	main()
