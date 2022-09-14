from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import TreeNode

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = root
        l_cnt = 0
        while l is not None:
            l_cnt += 1
            l = l.left

        r = root
        r_cnt = 0
        while r is not None:
            r_cnt += 1
            r = r.right

        if l_cnt == r_cnt:
            return 2 ** l_cnt - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
