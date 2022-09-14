from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Element():
    def __init__(self, value, index):
        self.value = value
        self.index = index
    def __repr__(self):
        return f"({self.value},{self.index})"


# 没想到是一个通过归并排序解决的问题
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:


        nums = [Element(v, i) for i, v in enumerate(nums)]
        ret_array = [0] * len(nums)

        def sort(nums):
            if len(nums) == 0 or len(nums) == 1:
                return nums
            mid = len(nums) // 2

            a = sort(nums[:mid])
            b = sort(nums[mid:])
            c = merge(a, b)
            return c

        def merge(a:List, b: List):
            ret = []

            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if a[i].value <= b[j].value:
                    ret_array[a[i].index] += j
                    ret.append(a[i])
                    i += 1
                else:
                    ret.append(b[j])
                    j += 1
            k = i
            while k < len(a):
                ret_array[a[k].index] += j
                k += 1

            return ret + a[i:] + b[j:]
        sort(nums)
        return ret_array


if __name__ == '__main__':
    nums = [5,2,6,1]
    print(Solution().countSmaller(nums))
