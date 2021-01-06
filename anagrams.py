def find_string_anagrams(str, pattern):
    """
    find the anagram
    :param str:
    :param pattern:
    :return: int

    >>> find_string_anagrams("ppqp", 'pq')
    [1, 2]
    >>> find_string_anagrams('abbcabc','abc')
    [2, 3, 4]
    """
    # print(str, pattern)
    freqMap = {}
    for nextChar in pattern:
        if nextChar not in freqMap:
            freqMap[nextChar] = 0
        freqMap[nextChar] += 1
    window_start, matched = 0, 0
    match_indexes = []
    for window_end in range(len(str)):
        nextChar = str[window_end]
        if nextChar in freqMap:
            freq = freqMap[nextChar]
            if freq > 0:
                matched += 1
            freqMap[nextChar] = freq - 1
        window_size = window_end - window_start + 1
        if window_size > len(pattern):
            charToRemove = str[window_start]
            # print("rem", charToRemove)
            if charToRemove in freqMap:
                freq = freqMap[charToRemove]
                if freq >= 0:
                    matched -= 1
                freqMap[charToRemove] = freq + 1
            window_start += 1
        # print(nextChar, len(pattern), matched, freqMap)
        if matched == len(pattern):
            match_indexes.append(window_start)
    return match_indexes


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)