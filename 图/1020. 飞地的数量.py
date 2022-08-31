from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = sum([sum(w) for w in grid])
        visited = set()

        def dfs(i,j,visited):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if (i, j) in visited:
                return
            if grid[i][j] == 0:
                return

            visited.add((i, j))

            dfs(i-1,j,visited)
            dfs(i+1,j,visited)
            dfs(i,j-1,visited)
            dfs(i,j+1,visited)

        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                if grid[i][j] == 1 and (i in [0, m -1] or j in [0, n -1]) :
                    dfs(i, j, visited)

        visited_cnt = len(visited)

        return count - visited_cnt






if __name__ == '__main__':

    grid = grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    print(Solution().numEnclaves(grid))


    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(Solution().numEnclaves(grid))
