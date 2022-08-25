from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        @lru_cache(None)
        def dfs(i, j):
            if i == len(grid) -1 and j == len(grid[0]) - 1:
                return grid[i][j]
            if i >= len(grid) or j >= len(grid[0]):
                return MAXINF
            return grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))

        return dfs(0, 0)




if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))

    grid = [[1,2,3],[4,5,6]]
    print(Solution().minPathSum(grid))
