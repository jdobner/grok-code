from collections import deque


def find_subarrays_off(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while (product >= target and left < len(arr)):
            product /= arr[left]
            left += 1
        # since the product of all numbers from left to right is less than the target therefore,
        # all subarrays from left to right will have a product less than the target too; to avoid
        # duplicates, we will start with a subarray containing only arr[right] and then extend it
        temp_list = deque()
        for i in range(right, left - 1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result


def find_subarrays(arr, target):
    """
    Given an array with positive numbers and a target number,
    find all of its contiguous subarrays whose product is less than the target number.

    :param arr:
    :param target:
    :return:


    >>> sorted(find_subarrays([2, 5, 3, 10], target=30))
    [[2], [2, 5], [3], [5], [5, 3], [10]]
    >>> sorted(find_subarrays([8, 2, 6, 5], target=50))
    [[2], [2, 6], [5], [6], [6, 5], [8], [8, 2]]
    """
    subarrays = []
    left = 0
    right = 0
    product = arr[0]

    len_arr = len(arr)
    while right < len_arr:
        # print(f'idx={left}:{right} product={product}  {arr[left:right+1]}')
        if product < target:
            for x in range(left, right + 1):
                subarrays.append(arr[x: right + 1])
            right += 1
            if right < len_arr:
                product *= arr[right]
        else:
            # print(f'product={product}')
            product /= arr[left]
            left += 1
            if left > right:
                right += 1

    return subarrays
