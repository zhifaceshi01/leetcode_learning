import collections
from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')



class Solution:
    flag = True
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        path = collections.defaultdict(list)
        for i, j in dislikes:
            path[i].append(j)
            path[j].append(i)

        coloring = [None] * (n+1)
        def dfs(cur_node,  color):
            if coloring[cur_node] is not None:
                if coloring[cur_node] != color:
                    self.flag = False
                return
            coloring[cur_node] = color
            for n in path[cur_node]:
                dfs(n,  not color)
        count = 0
        for k in range(1, n+1):
            if coloring[k] is not None:
                continue
            if not self.flag:
                return self.flag
            count += 1
            dfs(k, True)
        return self.flag






if __name__ == '__main__':
    n = 4
    dislikes = [[1,2],[1,3],[2,4]]
    print(Solution().possibleBipartition(n, dislikes))

    n = 3
    dislikes = [[1,2],[1,3],[2,3]]
    print(Solution().possibleBipartition(n, dislikes))

    n = 5
    dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    print(Solution().possibleBipartition(n, dislikes))

