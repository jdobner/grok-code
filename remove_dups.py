def remove_duplicates(arr):
    """
    Given an array of sorted numbers, remove all duplicates from it.
    You should not use any extra space; after removing the duplicates in-place return
    the length of the subarray that has no duplicate in it.

    :param arr:
    :return:

    >>> a = [2, 3, 3, 3, 6, 9, 9]; remove_duplicates(a); a
    4
    [2, 3, 6, 9, 6, 9, 9]
    >>> a = [2, 2, 2, 11]; remove_duplicates(a); a
    2
    [2, 11, 2, 11]
    >>> a = [1, 1, 2, 2, 11, 12, 12, 12, 13]; remove_duplicates(a); a
    5
    [1, 2, 11, 12, 13, 12, 12, 12, 13]
    """

    prev = None
    next_elem = 0
    for i in range(len(arr)):
        if arr[i] != prev:
            # non-dup
            if next_elem != i:
                arr[next_elem] = arr[i]
            next_elem += 1
            prev = arr[i]

    return next_elem
