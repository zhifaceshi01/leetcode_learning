from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret_lst = []
        maxvalue = MININF
        for w in graph:
            maxvalue = max(maxvalue, max(w + [MININF]))
        def dfs(i, cur_lst):
            if i == maxvalue:
                ret_lst.append(list(cur_lst))
                return
            for n in graph[i]:
                dfs(n, cur_lst + [n,])
        dfs(0, [0,])
        return ret_lst



if __name__ == '__main__':
    graph = [[1,2],[3],[3],[]]
    print(Solution().allPathsSourceTarget(graph))

    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(Solution().allPathsSourceTarget(graph))

