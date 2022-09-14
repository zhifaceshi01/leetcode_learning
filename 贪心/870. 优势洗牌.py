from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t = sorted([(i, w) for i, w in enumerate(nums2)],key=lambda x: x[1],reverse=True)
        nums1 = sorted(nums1, reverse=True)


        j = len(nums1) - 1
        i = 0
        ret_lst = [0] * len(nums1)
        for index, n in t:
            if nums1[i] > n:
                ret_lst[index] = (nums1[i])
                i += 1
            else:
                ret_lst[index] = (nums1[j])
                j -= 1

        return ret_lst







if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    print(Solution().advantageCount(nums1, nums2))
