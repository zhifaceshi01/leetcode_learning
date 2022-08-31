from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j, visited):
            if i <0 or i >= m or j < 0 or j >= n:
                return
            if (i,j) in visited:
                return
            if grid[i][j] == '0':
                return
            visited.add((i,j))
            dfs(i-1,j,visited)
            dfs(i+1,j,visited)
            dfs(i,j-1,visited)
            dfs(i,j+1,visited)

        visited = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j, visited)
        return count

if __name__ == '__main__':
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


    print(Solution().numIslands(grid))
