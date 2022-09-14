from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import TreeNode

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root is None:
                return None

            if root in [p, q]:
                return root

            a = dfs(root.left)
            b = dfs(root.right)

            if a is not None and b is not None:
                return root

            return a or b

        return dfs(root)





if __name__ == '__main__':
    lst = [TreeNode(w) for w in [3,5,1,6,2,0,8,7,4]]
    lst[0].left = lst[1]
    lst[0].right = lst[2]
    lst[1].left = lst[3]
    lst[1].right = lst[4]
    lst[2].left = lst[5]
    lst[2].right = lst[6]
    lst[4].left = lst[7]
    lst[4].right = lst[8]
    print(Solution().lowestCommonAncestor(lst[0], lst[1], lst[8]))
