import collections
from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

# 解法一，DFS超时了
class Solution1:
    flag = True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = collections.defaultdict(list)
        for a, b in prerequisites:
            path[a].append(b)

        def dfs(cur, visited):
            if cur in visited:
                return False
            flag = True
            for n in path[cur]:

                flag = flag and dfs(n , visited.union({cur}))
            return flag

        for k in range(numCourses):
            if not self.flag:
                return self.flag
            self.flag = self.flag and dfs(k, set())
        return self.flag

# BFS算法
class Solution:
    flag = True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = collections.defaultdict(list)
        rudu = {i: 0 for i in range(numCourses)}
        for a, b in prerequisites:
            path[a].append(b)
            rudu[b] += 1

        count = 0
        q = []

        for k, v in rudu.items():
            if v == 0:
                q.append(k)

        while len(q) != 0:
            cur = q.pop(0)
            count += 1
            for n in path[cur]:
                rudu[n] -= 1
                if rudu[n] == 0:
                    q.append(n)
        return numCourses == count



if __name__ == '__main__':
    print(Solution().canFinish(2,  [[1,0]]))
    print(Solution().canFinish(2,  [[1,0],[0,1]]))
