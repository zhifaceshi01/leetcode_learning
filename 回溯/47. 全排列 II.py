from typing import *
import bisect
from collections import *
from queue import PriorityQueue
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(nums, set(), [], ret)
        return ret

    def dfs(self, nums, visited, cur_lst, ret):
        if len(cur_lst) == len(nums):
            if cur_lst not in ret:
                ret.append(list(cur_lst))
        for i, v  in enumerate(nums):
            if i in visited:
                continue
            self.dfs(nums, visited.union({i}), cur_lst + [v, ], ret)



if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
