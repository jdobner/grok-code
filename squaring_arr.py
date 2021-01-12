def make_squares(arr):
    """
    Given a sorted array, create a new array containing squares of
    all the numbers of the input array in the sorted order.
    :param arr:
    :return:

    >>> make_squares([-2, -1, 0, 2, 3])
    [0, 1, 4, 4, 9]
    >>> make_squares([-3, -1, 0, 1, 2])
    [0, 1, 1, 4, 9]
    """
    squares = []
    return sorted(map(lambda x: pow(x, 2), arr))


    def make_squares_eff(arr):
        """
        Given a sorted array, create a new array containing squares of
        all the numbers of the input array in the sorted order.
        :param arr:
        :return:

        >>> make_squares_eff([-2, -1, 0, 2, 3])
        [0, 1, 4, 4, 9]
        >>> make_squares_eff([-3, -1, 0, 1, 2])
        [0, 1, 1, 4, 9]
        """
        squares = []
        left = -1
        for j in range(len(arr)):
            if arr[j] < 0:
                left = j
            else:
                break
        right = left + 1
        for i in range(len(arr)):
            backwards = False
            if left >= 0:
                backwards = right >= len(arr) or abs(arr[left]) < arr[right]
            if backwards:
                squares.append(pow(arr[left], 2))
                left -= 1
            else:
                squares.append(pow(arr[right], 2))
                right += 1

        return squares
