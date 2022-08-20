from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)





if __name__ == '__main__':
    print(Solution().climbStairs(38))
