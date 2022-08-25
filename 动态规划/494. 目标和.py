from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def dfs(i, target):
            if i == len(nums):
                if target == 0:
                    return 1
                else:
                    return 0

            value = nums[i]
            return dfs(i+1, target - value) + dfs(i+1, target + value)

        return dfs(0, target)




if __name__ == '__main__':
    nums = [1, ]
    target = 1
    print(Solution().findTargetSumWays(nums, target))
