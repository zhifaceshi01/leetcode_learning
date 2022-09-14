from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import TreeNode

MAXINF = float('inf')
MININF = -float('inf')



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(preorder, inorder):
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            a = preorder[1: index+1]
            b = preorder[index + 1: ]
            c = inorder[:index]
            d = inorder[index+1:]
            root.left = dfs(a, c)
            root.right = dfs(b, d)
            return root
        return dfs(preorder, inorder)




