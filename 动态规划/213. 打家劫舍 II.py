from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_list( nums: List[int]) -> int:
            if len(nums) == 0:
                return 0

            @lru_cache(None)
            def dfs(i):
                if i >= len(nums):
                    return 0
                a = nums[i] + dfs(i + 2)
                b = dfs(i + 1)
                return max(a, b)

            return dfs(0)
        a = rob_list(nums[:-1])
        b = rob_list(nums[1:])
        return max(a, b)




if __name__ == '__main__':
    nums = [1,2,3,1]
    print(Solution().rob(nums))
