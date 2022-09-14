import random
from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

class RandomizedSet:

    def __init__(self):
        self.hash_index = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hash_index:
            return False
        length = len(self.array)
        self.hash_index[val] = length
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_index:
            return False
        if len(self.array) == 1:
            self.hash_index = {}
            self.array = []
            return True


        index = self.hash_index[val]
        last_index = len(self.array) - 1
        last_val   = self.array[last_index]
        self.hash_index[last_val] = index
        self.array[index] = last_val
        self.array.pop()
        del self.hash_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


if __name__ == '__main__':
    # a = RandomizedSet()
    # print(a.insert(1))
    # print(a.remove(2))
    # print(a.insert(2))
    # print(a.getRandom())
    # print(a.remove(1))
    # print(a.insert(2))
    # print(a.getRandom())


    # a = RandomizedSet()
    # print(a.remove(0))
    # print(a.remove(0))
    # print(a.insert(0))
    # print(a.getRandom())
    # print(a.remove(0))
    # print(a.insert(0))
    #
    a = RandomizedSet()
    print(a.insert(0))
    print(a.insert(1))
    print(a.remove(0))
    print(a.insert(2))
    print(a.remove(1))
    print(a.getRandom())