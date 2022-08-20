from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache
class Solution:


    def numTilings(self, n: int) -> int:
        ## 分别对应三种铺砖的方式
        @lru_cache(None)
        def dfs_0(i):
            if i <= 2:
                return i
            return dfs_0(i-1) + dfs_0(i-2) + dfs_1(i-1) + dfs_2(i-1)

        @lru_cache(None)
        def dfs_1(i):
            if i == 2:
                return 1
            return dfs_0(i-2) + dfs_2(i-1)

        @lru_cache(None)
        def dfs_2(i):
            if i == 2:
                return 1
            return dfs_0(i-2) + dfs_1(i-1)

        return dfs_0(n) %1000000007




if __name__ == '__main__':
    print(Solution().numTilings(30))
