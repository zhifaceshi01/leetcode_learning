from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxvalue = MININF
        while left < right:
            maxvalue = max(maxvalue, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxvalue


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))
