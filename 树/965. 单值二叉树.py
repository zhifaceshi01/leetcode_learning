from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import TreeNode

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        value = root.val

        def dfs(root):
            if root is None:
                return True
            if root.val != value:
                return False
            return dfs(root.left) and dfs(root.right)

        return dfs(root)


if __name__ == '__main__':
    print(Solution().)
