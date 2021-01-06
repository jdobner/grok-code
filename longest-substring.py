from collections import defaultdict


def non_repeat_substring(s: str) -> int:
    longest = 0
    sub = ""
    for c in s:
        found = sub.find(c)
        sub = sub[found + 1:] + c
        longest = max(len(sub), longest)
    return longest


def find_longest(s: str, max_repeat: int) -> int:
    char_to_freq = defaultdict(int)
    max_count = 0
    current_char = ''
    window_left = 0
    window_right = 0
    for c in s:
        window_right += 1
        count = char_to_freq[c] + 1
        char_to_freq[c] = count
        if count > char_to_freq[current_char]:
            current_char = c
        while window_right - window_left > char_to_freq[current_char] + max_repeat:
            char_to_remove = s[window_left]
            window_left += 1
            print(c, "popping", char_to_remove)
            char_to_freq[char_to_remove] -= 1
            if char_to_remove == current_char:
                # find next largest
                new_char_tu = ('', 0)
                for tu in char_to_freq.items():
                    if tu[1] > new_char_tu[1]:
                        new_char_tu = tu
                current_char = new_char_tu[0]
        max_count = max(max_count, window_right - window_left)
        print(c, "max_count:", max_count)
    return max_count


def length_of_longest_substring2(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char])

        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring2("aabccbb", 2))
    print(length_of_longest_substring2("abbcb", 1))
    print(length_of_longest_substring2("abccde", 1))
    print(length_of_longest_substring2("aabacxjkl", 2))


main()
