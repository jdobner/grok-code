def find_substring(str, pattern):
    """ Given a string and a pattern, find the smallest substring in
    the given string which has all the characters of the given pattern.
    :param str:
    :param pattern:
    :return: str

>>> find_substring("aabdec", 'abc')
'abdec'
>>> find_substring("abdbca", 'abc')
'bca'
>>> find_substring('adcad','abc')
''
    """
    freq_map = dict.fromkeys(pattern, 0)
    found_indexes = None
    window_start = 0
    chars_found = 0

    for window_end in range(len(str)):
        nextChar = str[window_end]
        if nextChar in freq_map:
            if nextChar in freq_map:
                freq = freq_map[nextChar] + 1
                freq_map[nextChar] = freq
                if freq == 1:
                    chars_found += 1
            while chars_found == len(freq_map):
                charToRemove = str[window_start]
                if charToRemove in freq_map:
                    newFreq = freq_map[charToRemove] - 1
                    freq_map[charToRemove] = newFreq
                    if newFreq == 0:
                        chars_found -= 1
                        newLen = window_end - window_start + 1
                        if not found_indexes or found_indexes[0] > newLen:
                            found_indexes = (newLen, window_start, window_end + 1)
                window_start += 1
    if found_indexes:
        return str[found_indexes[1]:found_indexes[2]]
    else:
        return ""


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)