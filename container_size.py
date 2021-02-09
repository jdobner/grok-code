import itertools

class Solution2(object):
    @staticmethod
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_size = 0
        max_height = 0

        last = len(height) - 1

        for i, h in enumerate(height[0:last]):
            if h > max_height:
                max_height = h
                g = ((j, height[j]) for j in range(last, i, -1))
                for i2, h2 in g:
                    prefix = f"testing {i}/{h} - {i2}/{h2}"
                    distance = i2 - i
                    print(prefix, "distance=", distance)
                    if h * distance < max_size:
                        print(prefix, "break")
                        break
                    size = min(h, h2) * distance
                    print(prefix, "size=", size)
                    max_size = max(size, max_size)
            else:
                print(f"{h}@{i} too low")
        return max_size


class Solution(object):
    @staticmethod
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_size = 0
        left = 0
        right = len(height) - 1

        while right > left:
            left_height, right_height = height[left], height[right]
            size = min(left_height, right_height) * (right - left)
            #print(f"{left}/{left_height}--{right}/{right_height} size={size}")
            max_size = max(max_size, size)
            if left_height > right_height:
                right -= 1
            else:
                left += 1
        return max_size


args = list(itertools.chain(range(10001), range(10000, -1, -1)))
simple = [5,9,9,4,4,4,4,4,9,8,8,7,7,7,5]
the_answer = Solution.maxArea(simple)
print(the_answer)
the_answer = Solution.maxArea(args)
print(the_answer)
