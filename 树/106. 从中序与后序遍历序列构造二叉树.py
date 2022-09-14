from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import TreeNode

MAXINF = float('inf')
MININF = -float('inf')

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(inorder, postorder):
            if len(inorder) == 0 or len(postorder) == 0:
                return None
            root = TreeNode(postorder[-1])
            index = inorder.index(postorder[-1])
            a = postorder[: index]
            b = postorder[index: -1]
            c = inorder[:index]
            d = inorder[index+1:]
            assert len(a) ==  len(c)
            assert len(b) ==  len(d)

            root.left = dfs(c, a)
            root.right = dfs(d, b)
            return root
        return dfs(inorder, postorder)


if __name__ == '__main__':
    a = [9, 3, 15, 20, 7]
    b = [9, 15, 7, 20, 3]
    print(Solution().buildTree(a, b))