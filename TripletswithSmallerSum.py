import math


def triplet_with_smaller_sum(arr, target):
    """

    :param arr:
    :param target:
    :return:

    >>> triplet_with_smaller_sum([-1, 0, 2, 3], 3)
    2

    Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

    >>> triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5)
    4

    Explanation: There are four triplets whose sum is less than the target:
        [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
    """

    # print(arr, target)
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += search_pair(arr, target - arr[i], i)
    return count


def search_pair(arr, target_sum, first):
    count = 0
    left, right = first + 1, len(arr) - 1
    while (left < right):
        if arr[left] + arr[right] < target_sum:  # found the triplet
            # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
            # left and right to get a sum less than the target sum
            count += right - left
            # print(arr[first], arr[left:right + 1])
            left += 1
        else:
            right -= 1  # we need a pair with a smaller sum
    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3), "\n")
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5), "\n")
    print(triplet_with_smaller_sum([1, 2, 3, 7, 9, 10, 15], 12), "\n")
    print(triplet_with_smaller_sum([1, 2, 3, 4, 5, 6], 100), "\n")


main()
