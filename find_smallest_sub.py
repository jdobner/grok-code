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
    patternSet = set(pattern)
    match_indexes = {}
    found_indexes = None

    for window_end in range(len(str)):
        nextChar = str[window_end]
        if nextChar in patternSet:
            match_indexes[nextChar] = window_end
            # print(nextChar, "char found", match_indexes)
            if len(match_indexes) == len(patternSet):
                window_start = min(match_indexes.values())
                # print(nextChar, "full match found", match_indexes, "starting at", window_start)
                len_match = window_end - window_start + 1
                if not found_indexes or len_match < found_indexes[0]:
                    found_indexes = (len_match, window_start, window_end + 1)
    if found_indexes:
        return str[found_indexes[1]:found_indexes[2]]
    else:
        return ""


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)