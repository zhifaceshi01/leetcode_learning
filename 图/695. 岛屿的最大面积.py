from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j, visited):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if (i, j) in visited:
                return 0
            if grid[i][j] == 0:
                return 0
            visited.add((i, j))
            a = dfs(i - 1, j, visited)
            b = dfs(i + 1, j, visited)
            c = dfs(i, j - 1, visited)
            d = dfs(i, j + 1, visited)
            return 1 + sum([a,b,c,d])

        visited = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                if grid[i][j] == 1:

                    value = dfs(i, j, visited)
                    count = max(value, count)
        return count


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    print(Solution().maxAreaOfIsland(grid))
