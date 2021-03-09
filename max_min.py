from typing import List


def maxMin(k: int, arr: List[int]):
    '''
    >>> maxMin(3, [10, 100, 300, 200, 1000, 20, 30])
    20
    '''
    k -= 1
    arr.sort()
    lowest_unfairness = (10 ** 9) + 1
    for n in range(len(arr) - k):
        unfairness = arr[n + k] - arr[n]
        if unfairness < lowest_unfairness:
            lowest_unfairness = unfairness
    return lowest_unfairness
