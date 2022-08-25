from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = 999999999999999999999
MININF = -float('inf')
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(amount):
            if amount < 0:
                return MAXINF
            if amount == 0:
                return 0
            minsize = MAXINF
            for c in coins:
                a = 1 + dfs(amount - c)
                minsize = min(a, minsize)
            return minsize

        a =  dfs(amount)
        if a == MAXINF:
            return -1
        return a




if __name__ == '__main__':
    coins = [1,2,5]
    amount = 100
    print(Solution().coinChange(coins, amount))
    #
    # coins = [2]
    # amount = 3
    # print(Solution().coinChange(coins, amount))
    #
    # coins = [1]
    # amount = 0
    # print(Solution().coinChange(coins, amount))