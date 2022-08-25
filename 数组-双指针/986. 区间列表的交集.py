from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        overlap_lst = []
        while i < len(firstList) and j < len(secondList):
            s_1, e_1 = firstList[i]
            s_2, e_2 = secondList[j]
            if e_1 < e_2:
                if e_1 < s_2:
                    pass
                else:
                    if s_1 >= s_2:
                        overlap_lst.append([s_1, e_1])
                    else:
                        overlap_lst.append([s_2, e_1])
                i += 1
            else:
                if e_2 < s_1:
                    pass
                else:
                    if s_2 >= s_1:
                        overlap_lst.append([s_2, e_2])
                    else:
                        overlap_lst.append([s_1, e_2])
                j += 1

        return overlap_lst
if __name__ == '__main__':

    firstList = [[3,10]]
    secondList = [[5,10]]

    print(Solution().intervalIntersection(firstList, secondList))


    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]

    print(Solution().intervalIntersection(firstList, secondList))
    firstList =  [[1,3],[5,9]]
    secondList = []

    print(Solution().intervalIntersection(firstList, secondList))
    firstList =  []
    secondList =  [[4,8],[10,12]]

    print(Solution().intervalIntersection(firstList, secondList))
    firstList =[[1,7]]
    secondList = [[3,10]]

    print(Solution().intervalIntersection(firstList, secondList))
