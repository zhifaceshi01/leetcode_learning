from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):
                return 0
            a = nums[i] + dfs(i+2)
            b = dfs(i+1)
            return max(a, b)

        return dfs(0)

if __name__ == '__main__':
    print(Solution().rob([2,7,9,3,1]))
