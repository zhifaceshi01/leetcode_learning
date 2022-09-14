from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

# # 快速排序  超时  11 / 16
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         def dfs(nums):
#             if len(nums) == 0:
#                 return []
#             a = nums[0]
#             l = []
#             r = []
#             for n in nums[1:]:
#                 if n < a:
#                     l.append(n)
#                 else:
#                     r.append(n)
#             return dfs(l) +[a,] + dfs(r)
#         return dfs(nums)

# 归并排序  超时 15 / 16
class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(nums):
            if len(nums) == 0 or len(nums) == 1:
                return nums
            mid = len(nums) // 2

            a = sort(nums[:mid])
            b = sort(nums[mid:])
            c = merge(a, b)
            return c

        def merge(a:List, b: List):  # 可以优化
            ret = []
            while len(a) != 0 and len(b) != 0:
                if a[0] < b[0]:
                    v = a.pop(0)
                    ret.append(v)
                else:
                    v = b.pop(0)
                    ret.append(v)
            ret += a + b
            return ret
        return sort(nums)


# 归并排序  通过
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(nums):
            if len(nums) == 0 or len(nums) == 1:
                return nums
            mid = len(nums) // 2

            a = sort(nums[:mid])
            b = sort(nums[mid:])
            c = merge(a, b)
            return c

        def merge(a:List, b: List):  # 可以优化
            ret = []

            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    ret.append(a[i])
                    i += 1
                else:
                    ret.append(b[j])
                    j += 1

            return ret + a[i:] + b[j:]
        return sort(nums)






if __name__ == '__main__':
    nums = [5,2,3,1]
    print(Solution().sortArray(nums))
