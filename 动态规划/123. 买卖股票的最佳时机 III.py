from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

from pprint import pprint

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        for i in range(len(prices)):
            t = [[0,0] for i in range(2+1)]
            dp.append(t)

        for i in range(0, len(prices)):
            for cishu in range(0, 3):
                if i == 0:
                    dp[i][cishu][1] = -prices[i]
                    continue
                if cishu == 0:
                    dp[i][cishu][1] = max(-prices[i], dp[i-1][cishu][1])  ## 这里需要重点考虑。刚开始没卖出，交易次数为0，持有的最小代价需要初始化一下。
                    continue
                dp[i][cishu][0] = max(dp[i-1][cishu][0], dp[i-1][cishu-1][1] + prices[i])
                dp[i][cishu][1] = max(dp[i-1][cishu][1], dp[i-1][cishu][0] - prices[i])

        return  max(dp[len(prices)-1][2][0],dp[len(prices)-1][2][1])




if __name__ == '__main__':
    print(Solution().maxProfit(
        [3, 3, 5, 0, 0, 3, 1, 4]
    ))
