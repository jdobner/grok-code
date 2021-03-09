from typing import List


def luckBalance(k: int, contests : List[List[int]]):
    '''
    >>> luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])
    29
    '''
    bal = 0
    imp = []
    for l in contests:
        if l[1] == 0:
            bal += l[0]
        else:
            imp.append(l[0])
    imp.sort(reverse=True)
    bal += sum(imp[:k])
    bal -= sum(imp[k:])

    return bal
