from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.array = []
        count = 0
        for w in nums:
            count += w
            self.array.append(count)

    def sumRange(self, left: int, right: int) -> int:
        if left - 1 < 0:
            return self.array[right]
        else:
            return self.array[right] - self.array[left-1]


if __name__ == '__main__':
    a = NumArray([-2, 0, 3, -5, 2, -1])
    print(a.sumRange(,5))
