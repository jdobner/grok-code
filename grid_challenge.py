#!/bin/python3
# Complete the gridChallenge function below.
from typing import List


def gridChallenge(grid : List[str]):
    '''
    >>> gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])
    'YES'
    >>> gridChallenge(['ebacd', 'aaaaa', 'olmkn', 'trpqs', 'xywuv'])
    'NO'

    '''
    m = map(sorted, grid)
    prev = None
    for curr in m:
        if prev:
            for i in range(len(prev)):
                if curr[i] < prev[i]:
                    return "NO"
        prev = curr
    return "YES"
