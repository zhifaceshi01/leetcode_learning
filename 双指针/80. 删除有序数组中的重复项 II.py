from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        q = []
        while r < len(nums):
            a, b = nums[l], nums[r]
            q.append(b)
            if len(q) == 2:
                nums[l], nums[l+1] = q[0], q[1]
                l += 2
                while r < len(nums) and nums[r] == nums[q[1]]:
                    r += 1
                r -= 1
                q = []
            r += 1

        if len(q) != 0:
            nums[l] = q[0]
            l += 1

        return l


if __name__ == '__main__':

    nums =  [1,1,1,1,2,2,2,4]
    print(Solution().removeDuplicates(nums))  # 5
    print(nums)


    nums =  [0,0,1,1,1,1,2,3,3]
    print(Solution().removeDuplicates(nums)) # 7
    print(nums)
