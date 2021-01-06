
def find_permutation(str, pattern):
    print(str, pattern)
    if len(str) < len(pattern):
        return False
    freqMap = {}
    for c in pattern:
        if c not in freqMap:
            freqMap[c] = 0
        freqMap[c] += 1
    window_start, matched = 0, 0
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
            return True
    return False


assert find_permutation('oidbcaf', 'abc')
assert find_permutation("aaacb", "abc")
assert not find_permutation("odicf", "dc")
assert find_permutation("bcdxabcdy", "bcdyabcdx")