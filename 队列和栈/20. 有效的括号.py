from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [""]
        for t in s:
            if t == '(':
                stack.append('(')
            else:
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
        if stack == [""]:
            return True
        return False

if __name__ == '__main__':
    print(Solution().)
