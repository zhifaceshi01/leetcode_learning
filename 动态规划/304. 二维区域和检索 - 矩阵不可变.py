from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        array = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    array[i][j] = matrix[i][j]
                elif i == 0:
                    array[i][j] = array[i][j-1] + matrix[i][j]
                elif j == 0:
                    array[i][j] = array[i-1][j] + matrix[i][j]
                else:
                    array[i][j] = array[i][j-1] + array[i-1][j] - array[i-1][j-1] + matrix[i][j]
        self.array = array


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.array[row2][col2]
        b = self.array[row2][col1-1] if col1 - 1 >= 0 else 0
        c = self.array[row1-1][col2] if row1 - 1 >= 0 else 0
        d = self.array[row1-1][col1-1] if row1-1 >= 0 and col1 -1 >=0 else 0
        return a - b - c + d

# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
# [[[[-4,-5]]],[0,0,0,0],[0,0,0,1],[0,1,0,1]]

if __name__ == '__main__':
    a = NumMatrix(
        [[-4,-5]]
    )
    print(a.sumRegion(0,0,0,1))
    # print(a.sumRegion(1,1,2,2))
    # print(a.sumRegion(1,2,2,4))
