from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profile = 0
        minvalue = MAXINF
        for p in prices:
            minvalue = min(minvalue, p)
            profile = max(p - minvalue, profile)
        return profile

if __name__ == '__main__':
    nums = [7,1,5,3,6,4]
    print(Solution().maxProfit(nums))
