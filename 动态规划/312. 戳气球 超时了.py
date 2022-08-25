import collections
from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memory = collections.defaultdict(int)
        def dfs(nums):
            if nums in memory:
                return memory[nums]
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return nums[0]*nums[1] + max(nums[0], nums[1])
            value = MININF
            for i in range(0, len(nums)):
                if i == 0:
                    x = 1 * nums[i] * nums[i+1] + dfs(tuple(nums[:i] + nums[i+1:]))
                elif i == len(nums) - 1:
                    x = nums[i-1] * nums[i] * 1 + dfs(tuple(nums[:i] + nums[i+1:]))
                else:
                    x = nums[i] * nums[i-1] * nums[i+1] + dfs(tuple(nums[:i] + nums[i+1:]))
                value = max(value, x)
            memory[nums] = value
            return value
        a = dfs(tuple(nums))
        print(memory)
        return a



if __name__ == '__main__':
    nums = [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]
    print(Solution().maxCoins(nums))

    nums = [1,5]
    print(Solution().maxCoins(nums))

    nums = [2,3,7,9,1]
    print(Solution().maxCoins(nums))