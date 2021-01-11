import random
import string

from random import randrange
from pprint import pprint as prp
from time import perf_counter as pc


def permutate(word_list):
    start = pc()
    from itertools import permutations
    perms = permutations(word_list)
    perm_list = ["".join(perm) for perm in perms]
    duration = pc() - start
    # print(f'{len(perm_list)} permutations generated in {duration:0.04f}s')
    return perm_list


def permutate2(word_list):
    word_list = word_list.copy()
    perm_list = []
    for n in range(len(word_list)):
        for i in range(len(word_list) - 1):
            word_list[i], word_list[i + 1] = word_list[i + 1], word_list[i]
            perm_list.append("".join(word_list))
    return perm_list



def findAllInString(s: str, sub: str) -> list:
    rv = []
    index = -1
    while True:
        index = s.find(sub, index + 1)
        if index == -1:
            break
        rv.append(index)
    return rv


def find_word_concatenation(String: str, Words: list) -> list:

    assert all([len(s) == len(Words[0]) for s in Words])

    return find_word_concatenation_jd1(String, Words)


def find_word_concatenation_brute(String: str, Words: list) -> list:
    """
    Given a string and a list of words, find all the starting indices of substrings in the given string
    that are a concatenation of all the given words exactly once without any overlapping of words.

    It is given that all words are of the same length.

    :param String:
    :param Words:
    :return:

    >>> find_word_concatenation_brute(String="catfoxcat", Words=["cat", "fox"])
    [0, 3]
    >>> find_word_concatenation_brute(String="catcatfoxfox", Words=["cat", "fox"])
    [3]
    >>> find_word_concatenation_brute(String="fgfgfgftrotcattrotcatfoxfox", Words=["cat", "fox", "trot"])
    [14]
    """

    permutations = permutate(Words)
    # prp(permutations)
    indices = []
    for permutation in permutations:
        indices.extend(findAllInString(String, permutation))
    return sorted(indices)


def find_word_concatenation_jd1(String: str, Words: list) -> list:
    """
    Given a string and a list of words, find all the starting indices of substrings in the given string
    that are a concatenation of all the given words exactly once without any overlapping of words.

    It is given that all words are of the same length.

    :param String:
    :param Words:
    :return:

    >>> find_word_concatenation_jd1(String="catfoxcat", Words=["cat", "fox"])
    [0, 3]
    >>> find_word_concatenation_jd1(String="catcatfoxfox", Words=["cat", "fox"])
    [3]
    >>> find_word_concatenation_jd1(String="fgfgfgfjvhfgjfghftrotcattrtcatfoxfoxfgfrgrgwr", Words=["cat", "fox", "trt"])
    [24]
    """

    word_len = len(Words[0])
    assert all(len(w) == word_len for w in Words)
    return [i for i in range(len(String) - word_len) if find_in_string(String, i, word_len, Words)]


def find_in_string(s: str, pos: int, word_len: int, words: list) -> bool:
    # if s == "fgfgfgfjvhfgjfghftrotcattrtcatfoxfoxfgfrgrgwr":
    #     print("hi")
    if len(s) - pos < len(words) * word_len:
        return False
    for word in words:
        if s.find(word, pos, pos + word_len) == pos:
            smaller_list = [w for w in words if w != word]
            if len(smaller_list) == 0 or find_in_string(s, pos + word_len, word_len, smaller_list):
                return True
    return False


def find_word_concatenation_official(str1, words):
    """
    Given a string and a list of words, find all the starting indices of substrings in the given string
    that are a concatenation of all the given words exactly once without any overlapping of words.

    It is given that all words are of the same length.

    :param String:
    :param Words:
    :return:

    >>> find_word_concatenation_official("catfoxcat", ["cat", "fox"])
    [0, 3]
    >>> find_word_concatenation_official("catcatfoxfox", ["cat", "fox"])
    [3]
    """

    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(str1) - words_count * word_length) + 1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_length
            # Get the next word from the string
            word = str1[next_word_index: next_word_index + word_length]
            if word not in word_frequency:  # Break if we don't need this word
                break

            # Add the word to the 'words_seen' map
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # No need to process further if the word has higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_count:  # Store index if we have found all the words
                result_indices.append(i)

    return result_indices


def genWords(word_size: int, word_count: int, repeat_count: int) -> list:
    words = []
    for i in range(word_count):
        word = ''.join(random.choice(string.ascii_letters) for i in range(word_size))
        words.append(word)
    words.extend((words[i % word_count] for i in range(word_count * repeat_count)))
    return words


def generateData(size=100_000, fluff_size=10_000, word_count=10, repat_count=0, word_size=6):
    words = genWords(word_size, word_count, repat_count)

    full_string = \
        "".join((random.choice(words) for _ in range(size)))
    fluff_string = \
        "".join((random.choice(string.ascii_letters) for i in range(fluff_size * word_size)))
    full_string += fluff_string
    prp(words)
    prev_result = None
    for f in [
        find_word_concatenation_jd1,
        find_word_concatenation_official,
        find_word_concatenation_brute,
        find_word_concatenation_jd1
    ]:
        print(f.__name__)
        start = pc()
        found = f(full_string, words)
        duration = pc() - start
        if prev_result and prev_result != found:
            raise AssertionError(f"{found} != {prev_result}")
        prev_result = found
        print(f'    completed in {duration:04f}s found={len(found)}')

        # found = [(i, full_string[i:i + len(words) * word_size]) for i in found]
        # prp(found)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
