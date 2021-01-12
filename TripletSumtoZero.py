from typing import List


def pair_with_targetsum(arr, target_sum, ignore):
    """
    Given an array of sorted numbers and a target sum, find a pair in the array whose
    sum is equal to the given target.
    :param arr:
    :param target_sum:
    :return:

    >>> pair_with_targetsum(arr=[1, 2, 3, 4, 6], target_sum=6, ignore=0)
    [1, 3]
    >>> print(pair_with_targetsum(arr=[1, 2, 3, 4, 6], target_sum=6, ignore=1))
    None
    >>> a = [2, 3, 5, 8, 9, 11]; target=11
    >>> pair_with_targetsum(arr=a, target_sum=target, ignore=-1)
    [0, 4]
    >>> pair_with_targetsum(arr=a, target_sum=target, ignore=0)
    [1, 3]
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        # print(f'left: {left}, right: {right}')
        my_sum = arr[left] + arr[right]
        if left == ignore or my_sum < target_sum:
            left += 1
        elif right == ignore or my_sum > target_sum:
            right -= 1
        else:
            return [left, right]
    return None


def search_triplets(arr: List[int]):
    """
    Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
    :param arr: 
    :return: 

    >>> search_triplets([-3, 0, 1, 2, -1, 1, -2])
    [(-1, 0, 1), (-3, 1, 2), (-2, 0, 2), (-2, 1, 1)]
    >>> search_triplets([-5, 2, -1, -2, 3])
    [(-2, -1, 3), (-5, 2, 3)]
    """
    arr = sorted(arr)
    triplets = set()
    for i in range(len(arr)):
        target = 0 - arr[i]
        left = 0
        right = len(arr) - 1
        while left < right:
            # print(f'i: {i} val: {arr[i]} target: {target} left: {left}/{arr[left]} right: {right}/{arr[right]}')
            my_sum = arr[left] + arr[right]
            if left == i or my_sum < target:
                left += 1
            elif right == i or my_sum > target:
                right -= 1
            else:
                if arr[i] < arr[left]:
                    triplets.add((arr[i], arr[left], arr[right]))
                elif arr[i] < arr[right]:
                    triplets.add((arr[left], arr[i], arr[right]))
                else:
                    triplets.add((arr[left], arr[right], arr[i]))
                left += 1
    return list(triplets)


def search_triplets_eff(arr: List[int]) -> List[List[int]]:
    """
    Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
    :param arr:
    :return:

    >>> a = search_triplets_eff([-3, 0, 1, 2, -1, 1, -2]); \
        b = [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]; \
        list(map(lambda x: b.__contains__(x), a))
    [True, True, True, True]
    >>> a = search_triplets_eff([-5, 2, -1, -2, 3]); \
        b = [[-5, 2, 3], [-2, -1, 3]];\
        list(map(lambda x: b.__contains__(x), a))
    [True, True]
    """
    triplets = set()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            looking_for = 0 - (arr[i] + arr[j])
            for k in range(j + 1, len(arr)):
                if arr[k] == looking_for:
                    triplets.add(tuple(sorted([arr[i], arr[j], arr[k]])))
    return [list(item) for item in triplets]


def search_triplets_official(arr):
    """
    this
    :param arr:
    :return:
    >>> sorted(search_triplets_official([-3, 0, 1, 2, -1, 1, -2]))
    [(-1, 0, 1), (-3, 1, 2), (-2, 0, 2), (-2, 1, 1)]
    >>> sorted(search_triplets_official([-5, 2, -1, -2, 3]))
    [(-2, -1, 3), (-5, 2, 3)]
    """
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:  # skip same element to avoid duplicate triplets
            continue
        search_pair(arr, -arr[i], i + 1, triplets)

    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append((-target_sum, arr[left], arr[right]))
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
