from typing import *
import bisect
from collections import *
from queue import PriorityQueue
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(nums,  [], ret, 0)
        return ret
    def dfs(self, nums,  cur_lst, ret, step):
        t = sorted(cur_lst)
        if t  not in ret:
            ret.append(t )
        for i in range(step, len(nums)):
            n = nums[i]
            self.dfs(nums,  cur_lst + [n], ret,  i+1)





if __name__ == '__main__':
    print(Solution().subsetsWithDup([4,4,4,1,4]))
