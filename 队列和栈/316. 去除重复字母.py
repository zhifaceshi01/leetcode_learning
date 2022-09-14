import collections
from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')





class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        stack = []

        for c in s:

            counter[c] -= 1
            if len(stack) == 0:
                stack.append(c)
            elif c in stack:
                continue
            else:
                while len(stack) > 0 and stack[-1] > c and counter[stack[-1]] > 0:
                    stack.pop()
                if c not in stack:
                    stack.append(c)

        return ''.join(stack)



if __name__ == '__main__':


    s =  "abacb"
    print(Solution().removeDuplicateLetters(s))

    s =  "edebbed"
    print(Solution().removeDuplicateLetters(s))

    s =  "cbacdcbc"
    print(Solution().removeDuplicateLetters(s))

    s =  "bcabc"
    print(Solution().removeDuplicateLetters(s))