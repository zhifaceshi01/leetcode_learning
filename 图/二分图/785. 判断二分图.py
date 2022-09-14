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
    def isBipartite(self, graph: List[List[int]]) -> bool:
        path = collections.defaultdict(list)

        for i, lst in enumerate(graph):
            for n in lst:
                if n not in path[i]:
                    path[i].append(n)
                if i not in path[n]:
                    path[n].append(i)

        def dfs(cur_node, color, visited):
            if self.flag is False:
                return
            if cur_node in visited.keys():
                if color != visited[cur_node]:
                    self.flag = False
                return
            visited[cur_node] = color
            for n in path[cur_node]:
                dfs(n, ~color, visited)


        for i in range(len(graph)):
            if self.flag is False:
                return self.flag
            dfs(i, True, dict())
        return self.flag






if __name__ == '__main__':
    graph = [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]
    print(Solution().isBipartite(graph))
    graph = [[1,3],[0,2],[1,3],[0,2]]
    print(Solution().isBipartite(graph))
