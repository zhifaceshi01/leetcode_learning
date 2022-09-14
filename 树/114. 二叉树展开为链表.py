from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import *

MAXINF = float('inf')
MININF = -float('inf')
# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         ret_lst = []
#         def dfs(root):
#             if root is None:
#                 return
#             ret_lst.append(root)
#             dfs(root.left)
#             dfs(root.right)
#         dfs(root)
#         for t,n in zip(ret_lst[:-1], ret_lst[1:]):
#             t.left = None
#             t.right = n

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None

        def dfs(root: TreeNode):
            if root is None:
                return None

            left = dfs(root.left)
            right = dfs(root.right)

            if left is None:
                return root
            if right is None:
                root.left = None
                root.right = left
                return root

            root.left = None
            root.right = left
            p = left
            while p.right is not None:
                p = p.right
            p.right = right
            return root

        dfs(root)





if __name__ == '__main__':
    build_obj = Codec()
    head = build_obj.deserialize([1,2,3,None,None,4,None,None,5,None,6])

    print(Solution().flatten(head))
    preorder(head)
