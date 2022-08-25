from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:return
        index = len(nums1) - 1
        i = m - 1
        j = n - 1
        while index >= 0:
            a, b = nums1[i], nums2[j]
            if a > b:
                nums1[index] = a
                i -= 1
            else:
                nums1[index] = b
                j -= 1

            if i < 0 or j < 0:
                break

            index -= 1

        for k in range(j+1):
            nums1[k] = nums2[k]





if __name__ == '__main__':
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    # print(Solution().merge(nums1, m, nums2, n))
    # print(nums1)

    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    print(Solution().merge(nums1, m, nums2, n))
    print(nums1)
