import math
from typing import List

test_data = "263044060 323471968 60083128 764550014 209332334 735326740 558683912 626871620 232673588 428805364 " \
            "221674872 261029278 139767646 146996700 200921412 121542678 96223500 239197414 407346706 143348970 " \
            "60722446 664904326 352123022 291011666 594294166 397870656 60694236 376586636 486260888 114933906 " \
            "493037208 5321608 90019990 601686988 712093982 575851770 411329684 462785470 563110618 232790384 " \
            "511246848 521904074 550301294 142371172 241067834 14042944 249208926 36834004 69321106 467588012 " \
            "92173320 360474676 221615472 340320496 62541478 360772498 372355942 445408968 342087972 685617022 " \
            "307398890 437939090 720057720 718957462 387059594 583359512 589920332 500463226 770726204 434976772 " \
            "567860154 510626506 614077600 620953322 570332092 623026436 502427638 640333172 370673998"

test_arr = list(map(int, test_data.split()))

should_print = False

from pprint import pprint as p

for n in sorted(test_arr):
    print("{:15,}".format(n))


def pr(*args):
    if should_print:
        print(args)


class CalcFurthest(object):
    def __init__(self):
        self.furthest = 0
        self.m = -1

    def __call__(self, distance: int, m: int):
        distance = abs(distance)
        pr(f'furthest = {self.furthest:11,}, distance = {distance:11,}')
        if distance > self.furthest:
            self.furthest = distance
            self.m = m


def sherlockAndMinimax(arr: List[int], p: int, q: int) -> int:
    """
    >>> sherlockAndMinimax([5, 8, 14], 4, 9)
    4
    >>> "{:,}".format(sherlockAndMinimax(test_arr, 70_283_784, 302_962_359))
    '173,959,056'
    >>> sherlockAndMinimax([1 , 5], 5, 6)
    6
    >>> sherlockAndMinimax([3,5,7,9], 6, 8)
    6
    >>> sherlockAndMinimax([1], 0, 1)
    0
    """
    arr.sort()
    calc_furthest = CalcFurthest()
    start_index = findClosest(arr, p)
    distance = arr[start_index] - p
    calc_furthest(distance, p)
    end_index = findClosest(arr, q)
    distance = arr[end_index] - q
    calc_furthest(distance, q)
    for index in range(start_index, end_index - 2):
        distance = (arr[index + 1] - arr[index]) // 2
        calc_furthest(distance, arr[index] + distance)
    return calc_furthest.m


def sherlockAndMinimax2(arr: List[int], p: int, q: int) -> int:
    """
    >>> sherlockAndMinimax([1 , 5], 5, 6)
    6
    >>> "{:,}".format(sherlockAndMinimax(test_arr, 70_283_784, 302_962_359))
    '173,959,056'
    >>> sherlockAndMinimax([3,5,7,9], 6, 8)
    6
    >>> sherlockAndMinimax([5, 8, 14], 4, 9)
    4
    >>> sherlockAndMinimax([1], 0, 1)
    0
    """
    arr.sort()
    max_min = -1
    best_m = None
    start = findClosest(arr, p)
    m = p
    while m <= q:
        prev = None
        abs_prev = None

        pr(f"m={m} abs_prev={abs_prev}")
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
            max_min = abs_prev
            best_m = m
            pr(f"max={max_min:,}")
        if prev > 0:
            skip = prev * 2
            pr("skipping ", skip)
            m += skip
        elif start + 1 < len(arr):
            mid = (arr[start + 1] - arr[start]) // 2
            m += mid
        else:
            m = max(q, m + 1)
        pr(f"m={m} prev={prev}")
    return best_m


# Returns element closest to target in arr[]
def findClosest(arr: List[int], target: int) -> int:
    '''
    >>> findClosest([3, 4, 8, 9], 1)
    0
    >>> findClosest([3, 4, 8, 9], 22)
    3
    >>> findClosest([1, 4, 8, 9], 6)
    1
    '''
    # Corner cases

    # Doing binary search
    i = 0
    j = len(arr)
    n = len(arr)
    mid = 0
    while i < j:
        mid = (i + j) // 2

        if arr[mid] == target:
            return mid

        # If target is less than array
        # element, then search in left
        if target < arr[mid]:

            # If target is greater than previous
            # to mid, return closest of two
            if mid > 0 and target > arr[mid - 1]:
                return getClosest(mid - 1, target, arr)

            # Repeat for left half
            j = mid

        # If target is greater than mid
        else:
            if mid < n - 1 and target < arr[mid + 1]:
                return getClosest(mid, target, arr)

            # update i
            i = mid + 1

    # Only single element left after search
    return mid


def getClosest(index: int, target: int, arr: List[int]) -> int:
    return index if target - arr[index] >= arr[index + 1] - target else index + 1
