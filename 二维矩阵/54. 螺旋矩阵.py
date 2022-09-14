from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def traverse(x_1, y_1, x_2, y_2):
            if x_1 > x_2 or y_1 > y_2:
                return []
            ret_lst = []
            if x_1 == x_2:
                for j in range(y_1, y_2 + 1):
                    ret_lst.append ((x_1, j))
                return ret_lst
            if y_1 == y_2:
                for x in range(x_1, x_2 + 1):
                    ret_lst.append ((x, y_2))
                return ret_lst

            for j in range(y_1, y_2+1):
                ret_lst.append ((x_1, j))

            for x in range(x_1+1, x_2+1):
                ret_lst.append ((x, y_2))

            for j in range(y_2-1, y_1-1, -1):
                ret_lst.append ((x_2, j))

            for x in range(x_2-1, x_1, -1):
                ret_lst.append((x, y_1))

            return ret_lst + traverse(x_1 + 1, y_1 + 1, x_2 - 1, y_2 - 1)

        ret_lst = []
        x_1 = 0
        y_1=0
        x_2 = len(matrix) - 1
        y_2=len(matrix[0]) - 1

        for (a, b) in traverse(x_1, y_1, x_2, y_2):
            ret_lst.append(matrix[a][b])


        return ret_lst


if __name__ == '__main__':
    matrix = [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
    print(Solution().spiralOrder(matrix))
