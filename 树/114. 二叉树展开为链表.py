from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import *

MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ret_lst = []
        def dfs(root):
            if root is None:
                return
            ret_lst.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        for t,n in zip(ret_lst[:-1], ret_lst[1:]):
            t.left = None
            t.right = n

if __name__ == '__main__':
    build_obj = Codec()
    head = build_obj.deserialize([1,2,3,None,None,4,None,None,5,None,6])

    print(Solution().flatten(head))
    preorder(head)
