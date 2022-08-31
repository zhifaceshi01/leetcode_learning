from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])

        def dfs(i,j, visited):
            if i < 0 or j < 0 or i>=len(grid1) or j >= len(grid1[0]):
                return True
            if (i,j) in visited:
                return True
            visited.add((i,j))
            g1 = grid1[i][j]
            g2 = grid2[i][j]

            if g1 == 0 and g2 == 0:
                return True
            elif g1 == 0 and g2 == 1:
                a = dfs(i - 1, j, visited)
                b = dfs(i + 1, j, visited)
                c = dfs(i, j - 1, visited)
                d = dfs(i, j + 1, visited)
                return False
            elif g1 == 1 and g2 == 0:
                return True
            else:
                a = dfs(i - 1, j, visited)
                b = dfs(i + 1, j, visited)
                c = dfs(i, j - 1, visited)
                d = dfs(i, j + 1, visited)
                return a and b and c and d

        count = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i,j) in visited:
                    continue
                if grid2[i][j] == 0:
                    continue
                result = dfs(i,j,visited)
                if result:
                    print((i,j))
                    count += 1
        return count





if __name__ == '__main__':
    grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid2 = [
        [1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]

    print(Solution().countSubIslands(grid1, grid2))

    grid1 = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]
    grid2 = [
        [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]


    print(Solution().countSubIslands(grid1, grid2))
