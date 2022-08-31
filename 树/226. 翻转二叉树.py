from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import TreeNode

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        a = self.invertTree(root.left)
        b = self.invertTree(root.right)
        root.left = b
        root.right = a
        return root



if __name__ == '__main__':
    print(Solution().)
