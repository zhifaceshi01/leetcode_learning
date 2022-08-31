from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import TreeNode

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False
        if p.val != q.val:
            return False
        a = self.isSameTree(p.left, q.left)

        b  =self.isSameTree(p.right, q.right)
        return a and  b




if __name__ == '__main__':
    print(Solution().)
