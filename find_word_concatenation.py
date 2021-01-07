def permutate(iterable):
    l = [item for item in iterable]
    return_list = []
    for n in range(len(l)):
        for i in range(len(l) - 1):
            l[i], l[i + 1] = l[i + 1], l[i]
            return_list.append(list(l))
    return return_list


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
    """
    Given a string and a list of words, find all the starting indices of substrings in the given string
    that are a concatenation of all the given words exactly once without any overlapping of words.

    It is given that all words are of the same length.

    :param String:
    :param Words:
    :return:

>>> find_word_concatenation(String="catfoxcat", Words=["cat", "fox"])
[0, 3]
>>> find_word_concatenation(String="catcatfoxfox", Words=["cat", "fox"])
[3]

    """

    assert all([len(s) == len(Words[0]) for s in Words])

    return find_word_concatenation_jd1(String, Words)


def find_word_concatenation_brute(String: str, Words: list) -> list:
    permutations = ["".join(i) for i in permutate(Words)]
    indices = []
    for permutation in permutations:
        for index in findAllInString(String, permutation):
            indices.append(index)
    return sorted(indices)


def find_word_concatenation_jd1(String: str, Words: list) -> list:
    word_len = len(Words[0])
    return [i for i in range(len(String) - word_len) if find_in_string(String, i, word_len, Words)]


def find_in_string(s: str, pos: int, word_len: int, words: list) -> bool:
    if len(s) - pos < len(words) * word_len:
        return False
    for word in words:
        if s.find(word, pos, pos + word_len):
            smaller_list = [s for s in words if s != word]
            if len(smaller_list) == 0 or find_in_string(s, pos + word_len, word_len, smaller_list):
                return True
    return False


def find_word_concatenation_official(str1, words):
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


def generateData(size=100_000, pct_fluff=50, word_count=0):
    words = ["tyhgf", "yghji", "yghji", "12345", "54231", "ghjjj", "yuids"]
    stuff = ["kfjkrjgkrejfkrj", "jkj", "wdqwdqwhdkh", "iuixjijixwg", "ashjhj"]
    from random import randrange
    from pprint import pprint as prp
    from time import perf_counter as pc
    word_list = []
    assert 0 < pct_fluff < 100
    for i in range(size):
        if randrange(0, 99) < pct_fluff:
            word_list.append(words[randrange(0, len(words) - 1)])
        else:
            word_list.append(stuff[randrange(0, len(stuff) - 1)])
    full_string = "".join(word_list)
    word_count = max(word_count, len(words))
    words_list = [words[i % len(words)] for i in range(word_count)]
    tot_len = sum([len(word) for word in words])
    prev_result = None
    for f in [find_word_concatenation_jd1, find_word_concatenation_brute, find_word_concatenation_official]:
        start = pc()
        found = find_word_concatenation_jd1(full_string, words)
        duration = pc() - start
        if prev_result:
            assert prev_result == found
        prev_result = found
        found = [(i, full_string[i:i + tot_len]) for i in found]
        print(f'\n\n-------{f.__name__} completed in {duration:04f}-------')
        # prp(found)
        print(len(found))


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
