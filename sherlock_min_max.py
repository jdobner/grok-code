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


from typing import List

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
    >>> sherlockAndMinimax([18, 22, 26, 46, 60, 64, 82, 106, 138, 194], 82, 182)
    166
    >>> sherlockAndMinimax([3, 24, 35, 6, 7, 45], 15, 20)
    15
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
    start_index = get_closest_index(arr, p)
    distance = arr[start_index] - p
    calc_furthest(distance, p)
    end_index = get_closest_index(arr, q)
    distance = arr[end_index] - q
    calc_furthest(distance, q)
    pr(f'arr={arr}')
    pr(f'start= {start_index} ({arr[start_index]}),  end={end_index} ({arr[end_index]}),  p={p}, q={q}')
    for index in range(start_index, end_index):
        distance = (arr[index + 1] - arr[index]) // 2
        calc_furthest(distance, arr[index] + distance)
    return calc_furthest.m


def get_closest_index(arr, target):
    '''
    >>> get_closest_index([3, 6, 7, 24, 35, 45], 20)
    3
    >>> get_closest_index([3, 6, 7, 24, 35, 45], 15)
    2
    >>> get_closest_index([3, 4, 8, 9], 1)
    0
    >>> get_closest_index([5, 8, 14], 9)
    1
    >>> get_closest_index([3, 4, 8, 9], 22)
    3
    >>> get_closest_index([1, 4, 8, 9], 6)
    1
    '''
    n = len(arr)
    left = 0
    right = n - 1
    mid = 0

    # edge case - last or above all
    if target >= arr[n - 1]:
        return n - 1
    # edge case - first or below all
    if target <= arr[0]:
        return 0
    # BSearch solution: Time & Space: Log(N)

    while left < right:
        mid = (left + right) // 2  # find the mid
        if target < arr[mid]:
            right = mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            return mid

    mid1 = mid if target > arr[mid] else mid - 1
    mid2 = mid1 + 1
    return mid2 if target - arr[mid1] >= arr[mid2] - target else mid1

