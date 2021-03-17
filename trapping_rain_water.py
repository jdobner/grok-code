from collections import defaultdict, deque, namedtuple
from typing import List
from pprint import pprint


should_print = True


def p(*argv):
    if should_print:
        print(*argv)


def pp(*arg):
    if should_print:
        pprint(*arg)


class Slot:
    def __init__(self, height, effective_height):
        self.height = height
        self.effective_height = effective_height

    def __str__(self):
        return f"[{self.height}, {self.effective_height}]"

    def __repr__(self):
        return self.__str__()


Point = namedtuple('Point', ['x', 'y'])


class Solution:
    magic_height = 2001

    def __init__(self):
        self.hm = []
        self.trapped = 0
        self.len_x = 0
        self.len_y = 0

    def mapper(self, x, y, v):
        return Slot(v, None if 0 < x < self.len_y - 1 and 0 < y < self.len_x - 1 else v)

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        self.len_y = len(heightMap)
        self.len_x = len(heightMap[0])

        for y_pos, a in enumerate(heightMap):
            arr = [self.mapper(y_pos, n, k) for n, k in enumerate(a)]
            self.hm.append(arr)

        total = 0
        for y_pos in range(1, self.len_y - 1):
            for x_pos in range(1, self.len_x - 1):
                slot = self.calculate(Point(x_pos, y_pos))
                total += slot.effective_height - slot.height

        return total

    def get_slot(self, x: int, y: int) -> Slot:
        return self.hm[y][x]

    def calculate(self, point: Point) -> Slot:
        p(f'calculate({point})')
        visited = set()
        s = self.get_slot(*point)
        depth = 0

        def calc(pt: Point) -> int:
            nonlocal depth
            depth += 1
            print(f'{depth}:  calc({pt})')
            visited.add(pt)
            slot = self.get_slot(*pt)
            if slot.effective_height:
                return slot.effective_height
            x1, y1 = pt
            around_me = (Point(x1 - 1, y1),
                         Point(x1, y1 - 1),
                         Point(x1 + 1, y1),
                         Point(x1, y1 + 1))
            around_me = [it for it in around_me if it not in visited]
            p(f'{depth}: {pt}.around_me={around_me}')
            if not around_me:
                return slot.height
            effective_height = min(map(lambda d: calc(d), around_me))
            effective_height = max(effective_height, slot.height)
            return effective_height

        s.effective_height = calc(point)
        pp(self.hm)
        return s


class Solution2:
    magic_height = 2001

    def __init__(self):
        self.hm = []
        self.trapped = 0
        self.len_x = 0
        self.len_y = 0

    def mapper(self, x, y, v):
        return Slot(v, None if 0 < x < self.len_y - 1 and 0 < y < self.len_x - 1 else v)

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        self.len_y = len(heightMap)
        self.len_x = len(heightMap[0])

        for y_pos, a in enumerate(heightMap):
            arr = [self.mapper(y_pos, n, k) for n, k in enumerate(a)]
            self.hm.append(arr)

        total = 0
        for y_pos in range(1, self.len_y - 1):
            for x_pos in range(1, self.len_x - 1):
                slot = self.calculate(Point(x_pos, y_pos))
                total += slot.effective_height - slot.height

        return total

    def get_slot(self, x: int, y: int) -> Slot:
        return self.hm[y][x]

    def calculate(self, point: Point) -> Slot:
        p(f'calculate({point})')
        visited = set()
        s = self.get_slot(*point)
        depth = 0

        def calc(pt: Point) -> int:
            nonlocal depth
            depth += 1
            print(f'{depth}:  calc({pt})')
            visited.add(pt)
            slot = self.get_slot(*pt)
            if slot.effective_height:
                return slot.effective_height
            x1, y1 = pt
            around_me = (Point(x1 - 1, y1),
                         Point(x1, y1 - 1),
                         Point(x1 + 1, y1),
                         Point(x1, y1 + 1))
            around_me = [it for it in around_me if it not in visited]
            p(f'{depth}: {pt}.around_me={around_me}')
            if not around_me:
                return slot.height
            effective_height = min(map(lambda d: calc(d), around_me))
            effective_height = max(effective_height, slot.height)
            return effective_height

        s.effective_height = calc(point)
        pp(self.hm)
        return s


class Solution2:

    def trap(self, height: List[int]) -> int:
        total = 0
        heights_struct = defaultdict(lambda: 0)
        tallest = 0
        index = 0
        for h in height:
            index += 1
            for j in range(h + 1, tallest + 1):
                heights_struct[j] += 1
            for j in range(min(tallest, h), 0, -1):
                count = heights_struct[j]
                if count == 0:
                    break
                total += count
                heights_struct[j] = 0
            tallest = max(tallest, h)
            p(f"[{index} of {len(height)}] tallest={tallest}")
        p("total=", total)
        return total


class Solution1:

    def trap(self, height: List[int]) -> int:
        total = 0
        tallest = 0

        for i, h in enumerate(height):
            for j in range(i - 1, -1, -1):
                effective_height = min(h, tallest)
                if height[j] >= effective_height:
                    break
                else:
                    total += effective_height - height[j]
                    height[j] = effective_height
            tallest = max(tallest, h)
        return total


class Solution3:

    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size == 0:
            return 0
        total = 0
        left_max, right_max = deque(), deque()

        the_max = 0
        for i in range(0, size - 2):
            the_max = max(the_max, height[i])
            left_max.appendleft(the_max)

        the_max = 0
        for i in range(size - 1, 1, -1):
            the_max = max(the_max, height[i])
            right_max.append(the_max)

        # print(height)
        # print(left_max)
        # print(right_max)

        for h in height[1:size - 1]:
            # print(i, h, size, len(left_max), len(right_max))
            wall_height = min(left_max.pop(), right_max.pop())
            total += max(0, (wall_height - h))
        return total


def test():
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.

    see https://leetcode.com/problems/trapping-rain-water/

    >>> Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
    4
    >>> Solution().trapRainWater([4,2,0,3,2,5])
    9
    >>> Solution().trapRainWater([])
    0
    """
    import trapping_rain_water_data as d
    result = Solution().trap(d.test_data)
    print(result)


if __name__ == "__main__":
    # test()
    # r = Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
    # assert r == 4, f'expected {r} == 4'
    # data = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
    # r = Solution().trapRainWater(data)
    # pp(r)

    data = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
    pp(data)
    r = Solution().trapRainWater(data)
    assert r == 14, f'expected 14, received {r}'
