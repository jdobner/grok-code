import math
from typing import List


def sherlockAndMinimax(arr: List[int], p: int, q: int) -> int:
    '''
    >>> sherlockAndMinimax([5, 8, 14], 4, 9)
    4
    >>> sherlockAndMinimax([3,5,7,9], 6, 8)
    6
    >>> sherlockAndMinimax([1], 0, 1)
    0
    >>> sherlockAndMinimax([1 , 5], 5, 6)
    6
    '''
    arr.sort()
    max_min = -1
    best_m = None
    start = 0
    m = p
    while m <= q:
        prev = None
        abs_prev = None
        for i in range(start, len(arr)):
            diff = arr[i] - m
            abs_diff = abs(diff)
            if prev is None or abs_diff < abs_prev:
                prev = diff
                abs_prev = abs_diff
                start = i
            else:
                break

        if abs_prev > max_min:
            max_min = prev
            best_m = m
        if prev > 0:
            m += prev * 2 + 1
        else:
            m += 1
        # print(f"m={m} prev={prev}")
    return best_m


# Returns element closest to target in arr[]
def findClosest(arr: List[int], target: int):
    # Corner cases

    # Doing binary search
    i = 0
    j = len(arr)
    n = len(arr)
    mid = 0
    while i < j:
        mid = (i + j) // 2

        if arr[mid] == target:
            return arr[mid]

        # If target is less than array
        # element, then search in left
        if target < arr[mid]:

            # If target is greater than previous
            # to mid, return closest of two
            if mid > 0 and target > arr[mid - 1]:
                return getClosest(arr[mid - 1], arr[mid], target)

            # Repeat for left half
            j = mid

        # If target is greater than mid
        else:
            if mid < n - 1 and target < arr[mid + 1]:
                return getClosest(arr[mid], arr[mid + 1], target)

            # update i
            i = mid + 1

    # Only single element left after search
    return arr[mid]


def getClosest(val1: int, val2: int, target : int):
    if target - val1 >= val2 - target:
        return val2
    else:
        return val1

