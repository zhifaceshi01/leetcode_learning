from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            j = bisect.bisect_left(matrix[i], target)
            if j < len(matrix[i]) and matrix[i][j] == target:
                return True
        return False
if __name__ == '__main__':
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    target = 19

    print(Solution().searchMatrix(matrix, target))
