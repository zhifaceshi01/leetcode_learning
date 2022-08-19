from typing import *
import bisect
from collections import *
from queue import PriorityQueue
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(nums, set(), [], ret)
        return  ret
    def dfs(self, nums, visited, cur_lst,  ret):
        if len(cur_lst) == len(nums):
            ret.append(list(cur_lst))
        for v in nums:
            if v in visited:
                continue
            visited.add(v)

            self.dfs(nums, visited, cur_lst + [v,], ret)

            visited.remove(v)




if __name__ == '__main__':
    print(Solution().permute([1,2,3]))
