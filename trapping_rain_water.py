from collections import defaultdict, deque
from typing import List


def p(*argv):
    if False:
        print(argv)


class Solution2:

    def trap(self, height: List[int]) -> int:
        total = 0
        heights_struct = defaultdict(lambda: 0 )
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



class Solution:

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

    >>> Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    6
    >>> Solution().trap([4,2,0,3,2,5])
    9
    >>> Solution().trap([])
    0
    """
    import trapping_rain_water_data as d
    result = Solution().trap(d.test_data)
    print(result)


if __name__ == "__main__":
    test()