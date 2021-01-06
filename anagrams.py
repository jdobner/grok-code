def find_string_anagrams(str, pattern):
    print(str, pattern)
    freqMap = {}
    for c in pattern:
        if c not in freqMap:
            freqMap[c] = 0
        freqMap[c] += 1
    window_start, matched = 0, 0
    match_indexes = []
    for window_end in range(len(str)):
        c = str[window_end]
        if c in freqMap:
            freqMap[c] -= 1
            matched += 1
        window_size = window_end - window_start + 1
        if window_size > len(pattern):
            charToRemove = str[window_start]
            print("rem", charToRemove)
            if charToRemove in freqMap:
                freqMap[charToRemove] += 1
                matched -= 1
            window_start += 1
        print(c, len(pattern), matched, freqMap)
        if matched == len(pattern):
            match_indexes.append(window_start)
    return match_indexes
