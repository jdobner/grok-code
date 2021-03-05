from collections import namedtuple
from typing import List


class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        Heights = namedtuple('Heights', ['H', 'N', 'S', 'E', 'W'])
        dummy = Heights()
        effectiveHeights: List[List[Heights]] = []
        prev = dummy
        for ()



