from typing import List

def arrayManipulation(n: int, queries: List[List[int]]):
    """
    >>> arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])
    200
    >>> arrayManipulation(10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]])
    31
    >>> n, a = load(); arrayManipulation(n, a)
    2484930878
    """

    def insert(key: int, v: int):
        i = d.setdefault(key, 0)
        d[key] = i + v

    d = dict()
    for a, b, k in queries:
        insert(a, k)
        insert(b + 1, -k)

    sorted_keys = sorted(d.keys())
    max_val = 0
    cur_val = 0
    for key in sorted_keys:
        cur_val += d[key]
        max_val = max(max_val, cur_val)
        # pr(key, d[key], cur_val, max_val)
    return max_val

def pr(*args):
    if True:
        print(*args)


def load():
    with open("array_manipulation_8.txt", 'r') as p:
        n = int(p.readline().split()[0])
        arr = []
        for line in p:
            arr.append(list(map(int, line.split())))
        return n, arr


def test1():
    n, a = load()
    r = arrayManipulation(n, a)
    assert r == 2484930878


def test2():
    r = arrayManipulation(50, [[1, 3, 5], [4, 5, 5], [6, 7, 5]])
    pr(r)

