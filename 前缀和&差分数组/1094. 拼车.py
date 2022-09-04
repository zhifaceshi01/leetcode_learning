from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for a, b, c in trips:
            n = max(n, b, c)
        array = [0]*(n+1)
        for c, a, b in trips:
            array[a] += c
            array[b] -= c
        ret_lst = []
        count = 0
        for n in array:
            count += n
            ret_lst.append(count)

        return capacity >= max(ret_lst)



if __name__ == '__main__':
    trips = [[2,1,5],[3,3,7]]
    capacity = 5
    print(Solution().carPooling(trips, capacity))
