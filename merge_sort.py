#!/usr/bin/env python3
"""Simple merge sort implementation and small demo.

Usage:
  python3 merge_sort.py               # runs demo list
  python3 merge_sort.py "[3,1,4,1,5]"  # sorts provided Python list literal
"""

from typing import List, Iterable


def merge(left: List[int], right: List[int]) -> List[int]:
    i = j = 0
    out: List[int] = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    if i < len(left):
        out.extend(left[i:])
    if j < len(right):
        out.extend(right[j:])
    return out


def merge_sort(arr: Iterable[int]) -> List[int]:
    a = list(arr)
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


if __name__ == "__main__":
    import sys
    import ast

    if len(sys.argv) > 1:
        raw = sys.argv[1]
        try:
            arr = ast.literal_eval(raw)
            if not isinstance(arr, list):
                raise ValueError
        except Exception:
            arr = [int(x) for x in raw.split(",") if x.strip()]
    else:
        arr = [5, 2, 9, 1, 5, 6]

    print(merge_sort(arr))
