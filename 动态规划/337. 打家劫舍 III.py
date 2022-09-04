from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import *

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memory = {}
        def dfs(root, state):
            if root is None:
                return 0
            if (root, state) in memory:
                return memory[(root, state)]
            if state == 1:
                a =  max(0,
                           max(dfs(root.left, 0), dfs(root.left, 1)) + max(dfs(root.right, 0), dfs(root.right, 1)),
                           dfs(root.left, 0) + dfs(root.right, 0) + root.val,
                )
                memory[(root, state)] = a
                return a
            else:
                b = max(dfs(root.left, 0), dfs(root.left, 1)) + max(dfs(root.right, 0), dfs(root.right, 1))
                memory[(root, state)] = b
                return b

        return max(dfs(root,1), dfs(root, 0))


if __name__ == '__main__':
    root = build_tree([3,2,None,3,None,None,3,None,1])

    print(Solution().rob(root))

    root = build_tree([3,4,1,None,None,3,None,None,5,None,1])

    print(Solution().rob(root))