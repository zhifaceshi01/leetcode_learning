from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s = [i for i in s if i != '']
        return ' '.join(s[::-1]).strip(' ')



