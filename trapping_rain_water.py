from collections import defaultdict, OrderedDict
from typing import List

class GoalPosts(object):

    def __init__(self):
        self.left = None
        self.right = None

    def append(self, pos: int):
        if not self.left:
            self.left = pos
        elif pos < self.left:
            if self.right:
                self.left = pos
            else:
                self.right, self.left = self.right, pos


class Solution1:

    def trap(self, height: List[int]) -> int:
        total = 0

        def def_val():
            return GoalPosts()

        heights_struct = defaultdict(def_val)
        for i, h in enumerate(height):
            heights_struct[h].append(i)
        heights_struct = OrderedDict(sorted(heights_struct))
        oddball = None

        for h, posts in heights_struct.items():
            if oddball:
                posts.append(oddball)
                oddball = None
            if not posts.right:
                oddball = posts.left
                continue
            for i in range(posts.left + 1, posts.right + 1):
                pass

        return 0


class Solution:

    def trap(self, height: List[int]) -> int:
        total = 0

        def def_val():
            return 0

        heights_struct = defaultdict(def_val)
        tallest = 0
        for h in height:
            for j in range(h + 1, tallest + 1):
                heights_struct[j] += 1
            for j in range(min(tallest, h), 0, -1):
                count = heights_struct[j]
                if count == 0:
                    break
                total += count
                heights_struct[j] = 0
            tallest = max(tallest, h)
            print(f"tallest={tallest}")
        print("total=", total)
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


    :return:
    """
    return 0