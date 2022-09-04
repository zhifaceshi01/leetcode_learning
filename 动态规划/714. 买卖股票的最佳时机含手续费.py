from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0,0] for w in prices]
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return  max(dp[len(prices)-1][0],dp[len(prices)-1][1])


if __name__ == '__main__':
    print(Solution().maxProfit( [1, 3, 2, 8, 4, 9], 2))
