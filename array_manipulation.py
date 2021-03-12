from typing import List


def arrayManipulation(n: int, queries: List[int]):
    arr = [0] * n
    max_val = 0
    for a, b, k in queries:
        for i in range(a - 1, b):
            arr[i] += k
            max_val = max(max_val, arr[i])
    return max_val

