#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the marcsCakewalk function below.
from typing import List


def marcsCakeWalk(calorie : List[int]):
    '''

    :param calorie:
    :return:
    >>> marcsCakeWalk([7, 4, 9, 6])
    79
    '''
    calorie.sort(reverse=True)
    g = ((2 ** i) * j for i, j in enumerate(calorie))
    return sum(g)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()

