from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(None)
        def dfs(word1, word2):
            if len(word1) == 0 or len(word2) == 0:
                return max(len(word1), len(word2))
            if word1[0] == word2[0]:
                return dfs(word1[1:], word2[1:])
            a = 1 + dfs(word1[1:], word2[1:])
            b = 1 + dfs(word1[1:], word2)
            c = 1 + dfs(word1, word2[1:])
            return min(a, b, c)

        return dfs(word1, word2)

if __name__ == '__main__':
    word1 = "intention"
    word2 = "execution"
    print(Solution().minDistance(word1, word2))
