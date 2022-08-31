from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        grid = board
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i <0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] in ( 'X', 'Y'):
                return
            grid[i][j] = 'Y'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                if grid[i][j] == 'Y':
                    grid[i][j] = 'O'





if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

    print(Solution().solve(board))
    print(board)
