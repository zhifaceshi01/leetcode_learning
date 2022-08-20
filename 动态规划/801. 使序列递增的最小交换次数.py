from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache
MAXINF = float('inf')
MININF = -99
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:

        # 想了半天，还是先交换，再判断更容易一些
        @lru_cache(None)
        def dfs( i, min1, min2, pre1, pre2):
            if pre1 <= min1 or pre2 <= min2:
                return MAXINF

            if i == len(nums1):
                return 0

            n1 = nums1[i]
            n2 = nums2[i]

            # 不交换
            b = dfs(i + 1, max(min1, pre1), max(min2, pre2), n1, n2)
            # 交换
            a = 1 + dfs(i + 1, max(min1, pre1), max(min2, pre2), n2, n1)
            return min(a, b)

        nums1 = [MININF, ] + nums1
        nums2 = [MININF, ] + nums2
        return dfs(1, MININF, MININF, MININF+1, MININF+1)

if __name__ == '__main__':
    n1 =  [0,4,4,5,9]
    n2 = [0,1,6,8,10]
    print(Solution().minSwap(n1, n2))
