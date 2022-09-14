from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import *

MAXINF = float('inf')
MININF = -float('inf')



class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        value = 0
        def dfs(root):
            nonlocal value
            if root is None:
                return 0
            count1 = dfs(root.right)

            value += root.val
            root.val = value
            count2 = dfs(root.left)

        dfs(root)
        return root










