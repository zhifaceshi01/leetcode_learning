from typing import *
import bisect
from collections import *
from queue import PriorityQueue
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        self.dfs(n, k, [], ret, 1)
        return ret
    def dfs(self, n, k, cur_lst, ret, start):
        if len(cur_lst) == k:
            ret.append(cur_lst)
        for i in range(start, n+1):
            self.dfs(n, k, cur_lst + [i,], ret, i + 1)


if __name__ == '__main__':
    print(Solution().combine(4, 2))
