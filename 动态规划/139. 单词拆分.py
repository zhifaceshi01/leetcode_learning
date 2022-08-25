from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dfs(i):
            if i > len(s):
                return False
            if i == len(s):
                return True
            lst = []
            for w in wordDict:
                if s[i:].startswith(w):
                    lst.append(dfs(i+len(w)))
                else:
                    lst.append(False)
            return any(lst)

        return dfs(0)

if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(Solution().wordBreak(s, wordDict))

    s = "catsandog"
    wordDict =  ["cats", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(s, wordDict))
