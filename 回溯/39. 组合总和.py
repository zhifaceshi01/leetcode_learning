from typing import *
import bisect
from collections import *
from queue import PriorityQueue
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ret = []
        self.dfs(candidates, [], target,  0, ret)
        return ret

    def dfs(self, candidates, cur_lst, target,   start, ret):
        if target < 0:
            return
        if target == 0:
            # t = sorted(cur_lst)
            # if t not in ret:
            ret.append(cur_lst)

        for i in range(start, len(candidates)):
            v = candidates[i]
            self.dfs(candidates, cur_lst + [v,], target - v,  i, ret)




if __name__ == '__main__':
    c =[2,3,6,7]
    t = 7
    print(Solution().combinationSum(c, t))

    c =[100,200,4,12]
    t = 400
    print(Solution().combinationSum(c, t))
