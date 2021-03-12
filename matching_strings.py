from collections import defaultdict


def matchingStrings(strings, queries):
    """
    >>> matchingStrings(['aba', 'baba', 'aba', 'xzxb'],['aba', 'xzxb', 'ab'])
    [2, 1, 0]
    """
    d = defaultdict(int)
    for s in strings:
        d[s] += 1
    answer = []
    for q in queries:
        count = d.get(q, 0)
        answer.append(count)
    return answer
