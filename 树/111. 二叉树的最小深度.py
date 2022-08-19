from typing import *
import bisect
from collections import *
from queue import PriorityQueue
#         self.right = right
from 树.common import build_tree, TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left is  None and root.right is  None:
            return 1
        elif root.right is None:
            a = self.minDepth(root.left)
            return a + 1
        elif root.left is None:
            b = self.minDepth(root.right)
            return b + 1
        else:
            a = self.minDepth(root.left)
            b = self.minDepth(root.right)
            val = 1 + min(a, b)
            return val


if __name__ == '__main__':
    root = build_tree([1, 2])
    print(Solution().minDepth(root))

    root = build_tree([2, None, 3, None, 4])
    print(Solution().minDepth(root))

    root = build_tree(([3,9,None,None,20,15,None,None,7]))
    print(Solution().minDepth(root))

