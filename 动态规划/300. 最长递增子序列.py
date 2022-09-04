from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memory = defaultdict(int)
        def dfs(i):
            if i in memory:
                return memory[i]
            if i < 0:
                return 0
            if i == 0:
                return 1

            step = 1
            for k in range(1, len(nums)):
                if i - k >= 0 and nums[i] > nums[i-k]:
                    step = max(step, 1 + dfs(i-k))
            memory[i] = step
            return step
        [dfs(i) for i in range(len(nums))]
        return max([1,] + [w for w in memory.values()])


if __name__ == '__main__':
    nums = [0,1,2,3,4,0]
    print(Solution().lengthOfLIS(nums))
