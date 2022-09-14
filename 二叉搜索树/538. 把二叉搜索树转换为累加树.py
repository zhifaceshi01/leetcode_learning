from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import TreeNode

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        count = 0
        def dfs(root ):
            nonlocal count
            if root is None:
                return 0
            dfs(root.right)
            root.val = root.val + count
            count = root.val
            dfs(root.left)
        dfs(root)
        return root


