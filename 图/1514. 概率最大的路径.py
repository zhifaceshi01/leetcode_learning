import collections
from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dct = collections.defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            dct[a].append((b, prob))
            dct[b].append((a, prob))
        ret_lst = [MININF, ]

        def dfs(i, prob, visited):
            if i == end:
                ret_lst[0] = max(ret_lst[0], prob)
            for (b, p) in dct[i]:
                if b in visited:
                    continue
                dfs(b, prob * p, visited.union({b}))

        dfs(start, 1, set())
        return max(ret_lst[0], 0)




if __name__ == '__main__':
    n = 5
    edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
    succProb = [0.37,0.17,0.93,0.23,0.39,0.04]
    start = 3
    end = 4

    print(Solution().maxProbability(n, edges, succProb, start, end))
