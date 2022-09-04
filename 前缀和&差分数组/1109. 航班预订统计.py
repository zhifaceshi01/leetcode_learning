from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        chafenshuzu = [0] * n
        for a, b, c in bookings:
            a -= 1
            b -= 1
            chafenshuzu[a] += c
            if b+1 < len(chafenshuzu):
                chafenshuzu[b+1] -= c
        count = 0
        ret_lst = []
        for v in chafenshuzu:
            count += v
            ret_lst.append(count)
        return ret_lst


if __name__ == '__main__':
    bookings = [[1,2,10],[2,2,15]]
    n = 2

    print(Solution().corpFlightBookings(bookings, n))
