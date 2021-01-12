import math

def triplet_sum_close_to_target(arr, target_sum):
    """

    :param arr:
    :param target_sum:
    :return:

    >>> triplet_sum_close_to_target([-3, 2,  -1, 1], target_sum=1)
    0
    >>> triplet_sum_close_to_target([50, 1, 0, 1, 64, 1], target_sum=100)
    114
    """
    arr = sorted(arr)
    best_diff = math.inf
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current_diff = (arr[i] + arr[left] + arr[right]) - target_sum
            if abs(current_diff) < abs(best_diff) or (abs(current_diff) == abs(best_diff) and current_diff < best_diff):
                best_diff = current_diff
            if current_diff < 0:
                left += 1  # we need a pair with a bigger sum
            else:
                right -= 1  # we need a pair with a smaller sum

    return target_sum + best_diff
