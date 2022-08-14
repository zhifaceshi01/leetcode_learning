from typing import *
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][len(matrix[i]) - 1] >= target:
                index = bisect.bisect_left(matrix[i], target)
                if index == len(matrix[i]) or matrix[i][index] != target:
                    return False
                return True
        return False

if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 10
    print(Solution().searchMatrix(matrix, target))
