from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def racecar(self, target: int) -> int:

        def dfs(position, speed):
            a = MAXINF
            b = MAXINF
            if position == target:
                return 1
            if position > target and speed > 0:
                b = 1 + dfs(position, 1 if speed < 0 else -1)
            elif position < target and speed < 0:
                b = 1 + dfs(position, 1 if speed < 0 else -1)
            else:
                a = 1 + dfs(position + speed, speed * 2)
                b = 1 + dfs(position, 1 if speed < 0 else -1)
            return min(a, b)

        return dfs(0, 1)





if __name__ == '__main__':
    print(Solution().racecar(3))
    # print(Solution().racecar(6))
