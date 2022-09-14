from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import TreeNode

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 +max(self.maxDepth(root.left), self.maxDepth(root.right))




