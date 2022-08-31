from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class MinStack:

    def __init__(self):
        self.stack = [MAXINF,]
        self.min_stack = [MAXINF,]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_stack[-1]:
            self.min_stack.append(val)



    def pop(self) -> None:
        value = self.stack.pop(-1)
        if value == self.min_stack[-1]:
            self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(0);
    minStack.push(0);
    minStack.push(0);
    print(minStack.getMin());
    # --> 返回 - 3.
    minStack.pop();
    # --> 返回
    # 0.
    print(minStack.getMin());
    # --> 返回 - 2.