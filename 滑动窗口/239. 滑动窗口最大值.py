from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache
import heapq

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ret_lst = [-q[0][0]]
        for i in range(k, len(nums)):
            while len(q) != 0 and q[0][1] <= i -k:
                heapq.heappop(q)

            heapq.heappush(q, (-nums[i], i))
            ret_lst.append(-q[0][0])
        return ret_lst


if __name__ == '__main__':

    nums = [1,-1]
    k = 1
    print(Solution().maxSlidingWindow(nums, k))


    nums = [9,10,9,-7,-4,-8,2,-6]
    k = 5
    print(Solution().maxSlidingWindow(nums, k))



    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))

    nums =  [1]
    k = 1
    print(Solution().maxSlidingWindow(nums, k))