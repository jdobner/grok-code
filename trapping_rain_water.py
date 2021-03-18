from collections import defaultdict
from re import search
from typing import Tuple, List, Set
import typing

test_data = [[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]
test_data_2 = [[9,9,9,9,9,9],[9,2,1,1,2,9],[9,2,8,8,2,9],[9,2,3,3,2,9],[9,9,9,9,9,9]]
test_data_3 = [[9,9,9,9,9,9,8,9,9,9,9],[9,0,0,0,0,0,1,0,0,0,9],[9,0,0,0,0,0,0,0,0,0,9],[9,0,0,0,0,0,0,0,0,0,9],[9,9,9,9,9,9,9,9,9,9,9]]
pr = False

def printif(*args):
    if pr:
        print(*args)

class Solution:

    def __init__(self, data=None):
        self.data = [[0]] if data is None else data
        self.cache = [[0]]
        self.cache_hits = 0

    def get(self, x, y) -> int:
        assert x >= 0
        assert y >= 0
        return self.data[y][x]

    def ge_from_cache(self, x, y) -> int:
        assert x >= 0
        assert y >= 0
        self.cache_hits += 1
        return self.cache[y][x]

    def get_unvisited_adjacent(self, x1, y1, visited, hi) -> List[Tuple[int, int]]:
        around_me = [(x1 - 1, y1), (x1, y1 - 1), (x1 + 1, y1), (x1, y1 + 1)]
        return [n for n in around_me if n not in visited]

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        '''
        >>> Solution().trapRainWater(test_data)
        14
        >>> Solution().trapRainWater(test_data_2)
        72
        '''
        self.data = heightMap
        self.cache = []
        for y, a in enumerate(self.data):
            a2 = [-1 if self.not_edge(x, y) else v for x, v in enumerate(a)]
            self.cache.append(a2)
        total = 0
        s = []
        grid = []
        for y in range(1, len(self.data) - 1):
            line = []
            for x in range(1, len(self.data[0]) - 1):
                capacity, chain = self.search(x, y)
                capacity -= self.get(x, y)
                line.append(capacity)
                assert capacity >= 0
                if capacity > 0:
                    s.append(f'capacity({x}, {y}) = {capacity}, chain={chain}')
                total += capacity
            grid.append(line)
        for t in s:
            printif(t)
        for line in grid:
            printif("  ", line, "=", sum(line))

        printif(f"cache_hits={self.cache_hits}")
        return total

    def not_edge(self, x, y):
        rv = 0 < x < len(self.data[0]) - 1 and 0 < y < len(self.data) - 1
        printif((x,y), "NOT EDGE" if rv else "EDGE")
        return rv

    def search(self, x, y, visited=None, hi=0) -> (int, List[int]):
        if visited is None:
            v = self.search(x, y, set())
            self.cache[y][x] = v[0]
            return v

        cached = self.ge_from_cache(x, y)
        if cached > -1:
            return cached, []

        my_height = self.get(x, y)
        hi = max(hi, my_height)
        visited.add((x, y))

        self.print_d(x, y, visited)
        adj = None
        if self.not_edge(x, y):
            adj = self.get_unvisited_adjacent(x, y, visited, hi)
            printif(x, y, " -> ", adj)
            rv = 10_000
        else:
            rv = my_height

        my_chain = [(my_height, x, y)]
        if adj:
            low = 20000
            low_chain = None
            for next_x, next_y in adj:
                cap, chain = self.search(next_x, next_y, visited.copy(), hi)
                if cap < low:
                    low = cap
                    low_chain = chain
            my_chain.append(low_chain)
            rv = max(my_height, low)
        return rv, my_chain

    def print_d(self, x: int, y: int, visited):
        if not pr:
            return
        print(f'adj to ({x}, {y}):')

        def _map(arg):
            _x, _v = arg
            s = "*" if _x == x and _y == y else " "
            s2 = "x" if arg in visited else " "
            return f"{s}{_v}{s2}"

        for _y, a in enumerate(self.data):
            print(list(map(_map, enumerate(a))))
        print("\n")


# v = get_volume()
# print(f'volume = {v}')


def t1(data=test_data_3):
    rv = Solution().trapRainWater(test_data_2)
    print(f'---- rv={rv}')
    for a in data[1:-1]:
        the_list = list(map(lambda x: 9 - x, a[1:-1]))
        print("  ", the_list, "=", sum(the_list))
    print()
    for a in data:
        print(a)
    return rv


def test_1(f_data1):
    rv = Solution().trapRainWater(f_data1)
    assert rv == 14


def se(x, y):
    return Solution(test_data_2).search(x,y)

