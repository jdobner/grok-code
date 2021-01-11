def pair_with_targetsum(arr, target_sum):
    """
    Given an array of sorted numbers and a target sum, find a pair in the array whose
    sum is equal to the given target.
    :param arr:
    :param target_sum:
    :return:

    >>> pair_with_targetsum([1, 2, 3, 4, 6], 6)
    [1, 3]
    >>> pair_with_targetsum([2, 5, 9, 11], 11)
    [0, 2]
    """
    left = 0
    right = len(arr) - 1

    while left != right:
        my_sum = arr[left] + arr[right]
        if my_sum < target_sum:
            left += 1
        elif my_sum > target_sum:
            right -= 1
        else:
            return [left, right]
    return [-1, -1]


def pair_with_targetsum_ht(arr, target_sum):
    """
    Given an array of sorted numbers and a target sum, find a pair in the array whose
    sum is equal to the given target.
    :param arr:
    :param target_sum:
    :return:

    >>> pair_with_targetsum_ht([1, 2, 3, 4, 6], 6)
    [1, 3]
    >>> pair_with_targetsum_ht([2, 5, 9, 11], 11)
    [0, 2]
    """

    d = {}
    for pos, num in enumerate(arr):
        if target_sum - num in d:
            return [d[target_sum - num], pos]
        else:
            d[num] = pos
    return [-1, -1]
