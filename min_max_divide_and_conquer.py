#!/usr/bin/env python3
"""
Find minimum and maximum of an array using divide and conquer.

Usage:
    python3 min_max_divide_and_conquer.py

Time complexity: O(n)
"""

from typing import Tuple, List


def find_min_max(arr: List[float]) -> Tuple[float, float]:
    """Return (min, max) of `arr` using a divide-and-conquer approach.

    Raises ValueError for empty arrays.
    """
    if not arr:
        raise ValueError("arr must not be empty")

    def dc(left: int, right: int) -> Tuple[float, float]:
        # If only one element
        if left == right:
            return arr[left], arr[left]

        # If two elements
        if right == left + 1:
            if arr[left] < arr[right]:
                return arr[left], arr[right]
            else:
                return arr[right], arr[left]

        # More than two: split
        mid = (left + right) // 2
        min1, max1 = dc(left, mid)
        min2, max2 = dc(mid + 1, right)
        return (min1 if min1 < min2 else min2, max1 if max1 > max2 else max2)

    return dc(0, len(arr) - 1)


if __name__ == "__main__":
    examples = [
        [3, 5, 1, 2, 4, 8],
        [10],
        [-2, -5, -1, -7],
        [2.5, 3.1, 0.0, -1.2],
    ]

    for i, ex in enumerate(examples, 1):
        mn, mx = find_min_max(ex)
        print(f"Example {i}: array={ex} -> min={mn}, max={mx}")
