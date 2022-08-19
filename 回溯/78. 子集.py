from typing import *
import bisect
from collections import *
from queue import PriorityQueue
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(nums,  [], ret, 0)
        return ret
    def dfs(self, nums,  cur_lst, ret, step):
        if cur_lst not in ret:
            ret.append(cur_lst)
        for i in range(step, len(nums)):
            n = nums[i]
            self.dfs(nums,  cur_lst + [n], ret,  i+1)





if __name__ == '__main__':
    print(Solution().subsets([1,2,3]))
