from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import *

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value = None
        flag = False
        count = 0
        def dfs(root:TreeNode):
            nonlocal flag
            nonlocal count
            nonlocal value
            if root is None or flag:
                return 0

            count1 = dfs(root.left)
            count += 1
            if count == k:
                flag = True
                value = root.val

            count2 = dfs(root.right)

        dfs(root)
        return value


if __name__ == '__main__':
    root = build_tree([1,None,2])
    print(Solution().kthSmallest(root,1))
