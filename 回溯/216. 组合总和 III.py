from typing import *
import bisect
from collections import *
from queue import PriorityQueue
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        lst = [i for i in range(1,10)]
        ret = []
        self.dfs(lst, [], 0, k, ret, n)
        return  ret
    def dfs(self, candidates, cur_lst, start, k, ret, n ):
        if k == 0 and n == 0:
            ret.append(list(cur_lst))
            return
        if k == 0:
            return
        if n < 0:
            return
        for i in range(start, len(candidates)):
            self.dfs(candidates, cur_lst + [candidates[i]], i+1, k-1, ret, n - candidates[i])

if __name__ == '__main__':
    print(Solution().combinationSum3(3,9))
