from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        pass
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(i, j, visited):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return False
            if grid[i][j] == 1:
                return False
            if (i, j) in visited:
                return False

            visited.add((i, j))

            a, b, c, d = [dfs(i - 1, j, visited), dfs(i + 1, j, visited), dfs(i, j - 1, visited), dfs(i, j + 1, visited)]
            if grid[i][j] == 0 and (i in [0, len(grid) -1] or j in [0, len(grid[0]) - 1]):
                return True

            return a or b or c or d

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                if (i, j) in visited:
                    continue
                a = dfs(i, j, visited)
                if not a:
                    count += 1

        return count


if __name__ == '__main__':
    grid = [[1,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,0,1,1,1],[1,0,1,0,0,0,1,0,1,0],[1,1,1,1,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,0],[0,0,0,0,1,1,0,0,0,0],[1,0,1,0,0,0,0,1,1,0],[1,1,0,0,1,1,0,0,0,0],[0,0,0,1,1,0,1,1,1,0],[1,1,0,1,0,1,0,0,1,0]]

    print(Solution().closedIsland(grid))
