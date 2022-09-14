from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache
import collections

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = collections.defaultdict(list)
        rudu = {i: 0 for i in range(numCourses)}
        for a, b in prerequisites:
            path[a].append(b)
            rudu[b] += 1
        ret_lst = []
        count = 0
        q = []

        for k, v in rudu.items():
            if v == 0:
                q.append(k)

        while len(q) != 0:
            cur = q.pop(0)
            count += 1
            ret_lst.append(cur)
            for n in path[cur]:
                rudu[n] -= 1
                if rudu[n] == 0:
                    q.append(n)
        if numCourses != count:
            return []
        return ret_lst[::-1]





if __name__ == '__main__':
    print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
