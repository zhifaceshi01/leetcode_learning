import math
from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(a + b)
            elif t == '-':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(b - a)
            elif t == '*':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(a * b)
            elif t == '/':
                a = stack.pop(-1)
                b = stack.pop(-1)
                value = b // a
                if b % a != 0 and value < 0:
                    value += 1
                stack.append(value)
            else:
                stack.append(int(t))
        return stack[-1]


if __name__ == '__main__':
    tokens =["4","-2","/","2","-3","-","-"]
    print(Solution().evalRPN(tokens))
