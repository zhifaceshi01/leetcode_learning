from typing import *
import bisect
from collections import *
from queue import PriorityQueue

from 树.common import TreeNode, build_tree


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:return 0
        return self.travers(root)[1] - 1
    def travers(self, root: TreeNode):
        if root is None:
            return [0, 0]
        l0, l1 = self.travers(root.left)
        r0, r1 = self.travers(root.right)
        a = 1 + max(l0, r0)
        b = max(1 + l0 + r0, l1, r1)
        return [a, b]

if __name__ == '__main__':
    root = build_tree([1,2,4,None,None,5,None,None,3])
    print(Solution().diameterOfBinaryTree(root))
