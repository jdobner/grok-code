from collections import defaultdict
from re import search
from typing import Tuple, List, Set
import typing

test_data = [[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]
test_data_2 = [[9,9,9,9,9,9],[9,2,1,1,2,9],[9,2,8,8,2,9],[9,2,3,3,2,9],[9,9,9,9,9,9]]
pr = True

def printif(*args):
    if pr:
        print(*args)

class Solution:

    def __init__(self, data=None):
        self.data = [[]] if data is None else data

    def get(self, x, y) -> int:
        return self.data[y][x]

    def get_unvisited_adjacent(self, x1, y1, visited, hi) -> List[Tuple[int, int]]:
        around_me = ((x1 - 1, y1),
                     (x1, y1 - 1),
                     (x1 + 1, y1),
                     (x1, y1 + 1))
        return [r for r in around_me if visited[r] > hi]

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        '''
        >>> Solution().trapRainWater(test_data)
        14
        >>> Solution().trapRainWater(test_data_2)
        57
        '''
        self.data = heightMap
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

        return total

    def not_edge(self, x, y):
        rv = 0 < x < len(self.data[0]) - 1 and 0 < y < len(self.data) - 1
        printif((x,y), "NOT EDGE" if rv else "EDGE")
        return rv

    def search(self, x, y, visited=None, hi=0) -> (int, List[int]):
        if visited is None:
            visited = defaultdict(lambda: 10_000)

        my_height = self.get(x, y)
        hi = max(hi, my_height)
        visited[(x, y)] = hi

        self.print_d(x, y, visited)
        adj = self.get_unvisited_adjacent(x, y, visited, hi)
        printif(x, y, " -> ", adj)

        if self.not_edge(x, y) and adj:
            low = 20000
            the_chain = []
            for next_x, next_y in adj:
                cap, chain = self.search(next_x, next_y, visited, hi)
                if cap < low:
                    low = cap
                    the_chain = chain
            the_chain.insert(0, (x, y))
            return max(my_height, low), the_chain
        else:
            return my_height, [(x, y)]

    def print_d(self, x: int, y: int, visited):
        if not pr:
            return
        print(f'adj to ({x}, {y}):')

        def _map(arg):
            _x, _v = arg
            s = "*" if _x == x and _y == y else " "
            i = visited[arg]
            s2 = "  " if i == 10_000 else f"x{i}"
            return f"{s}{_v}{s2}"

        for _y, a in enumerate(self.data):
            print(list(map(_map, enumerate(a))))
        print("\n")


# v = get_volume()
# print(f'volume = {v}')


def test():
    rv = Solution().trapRainWater(test_data_2)
    print(f'---- rv={rv}')
    for a in test_data_2[1:-1]:
        the_list = list(map(lambda x: 9 - x, a[1:-1]))
        print("  ", the_list, "=", sum(the_list))
    print()
    for a in test_data_2:
        print(a)

# test()


def se(x, y):
    return Solution(test_data_2).search(x,y)
