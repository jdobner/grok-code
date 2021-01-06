def length_of_longest_substring(arr: list, k):
    left, oneCount, maxLen = 0, 0, 0

    for i in range(len(arr)):
        if arr[i] == 1:
            oneCount += 1
        if i - left + 1 > k + oneCount:
            if arr[left] == 1:
                oneCount -= 1
            left += 1
        maxLen = max(maxLen, i - left + 1, oneCount)
        print(arr[left:i], i - left + 1)
    return maxLen


def length_of_longest_substring2(arr, k):
    window_start, max_length, max_ones_count = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        # Current window size is from window_start to window_end, overall we have a maximum of 1s
        # repeating 'max_ones_count' times, this means we can have a window with 'max_ones_count' 1s
        # and the remaining are 0s which should replace with 1s.
        # now, if the remaining 0s are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' 0s
        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
        print(arr[window_start:window_end], window_end - window_start + 1, max_ones_count)

    return max_length
