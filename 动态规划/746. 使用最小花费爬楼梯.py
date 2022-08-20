from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @lru_cache(None)
        def dfs(i):
            if i >= len(cost):
                return 0
            a = cost[i] + dfs(i+1)
            b = cost[i] + dfs(i+2)
            return min(a, b)

        a = dfs(0)
        b = dfs(1)
        return min(a, b)





if __name__ == '__main__':
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(Solution().minCostClimbingStairs(cost))
