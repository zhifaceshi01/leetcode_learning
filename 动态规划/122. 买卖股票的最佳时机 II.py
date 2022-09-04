from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
## 199/200 超时了
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         @lru_cache(None)
#         def dfs_have(i):
#             if i < 0:
#                 return MININF
#             if i == 0:
#                 return -prices[i]
#             value = MININF
#             for k in list(range(i))[::-1]:
#                 a = dfs_have(k)
#                 b = dfs_nohave(k)-prices[i]
#                 value = max(value, a, b)
#
#             return value
#
#         @lru_cache(None)
#         def dfs_nohave(i):
#             if i < 0:
#                 return MININF
#             if i == 0:
#                 return 0
#             value = MININF
#             for k in list(range(i))[::-1]:
#                 a = dfs_nohave(k)
#                 b = dfs_have(k) + prices[i]
#                 value = max(value, a, b)
#             return value
#         k = len(prices)-1
#         a = dfs_nohave(k)
#
#         return a


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0,0] for w in prices]
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return  max(dp[len(prices)-1][0],dp[len(prices)-1][1])






if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))
