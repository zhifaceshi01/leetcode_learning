from typing import *
import bisect
from collections import *
from queue import PriorityQueue


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        self.dfs(n, set(), [], ret, 0)
        return ret

    def dfs(self, n, visited, cur_lst, ret, hangshu):
        if len(cur_lst) == n:
            ret.append(self.construct(cur_lst, n))
        for i in range(hangshu, n):
            for j in range(n):
                c = (i, j)
                if  self.is_bad(c, visited):
                    continue
                visited.add(c)
                self.dfs(n, visited, cur_lst + [c,], ret, hangshu + 1)
                visited.remove(c)

    def construct(self, lst, n):
        ret = [['.'] * n for i in range(n)]
        for x, y in lst:
            ret[x][y] = 'Q'
        t = []
        for i in range(n):
            t.append("".join(ret[i]))
        return t

    def is_bad(self, c, visited):
        a, b = c
        for x, y in visited:
            if abs(x - a) == abs(y - b):
                return True
            if x - a == 0 or y - b == 0:
                return True
        return False

if __name__ == '__main__':
    print(Solution().solveNQueens(8))
