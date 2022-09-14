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
        ret_lst = []
        def dfs(root):
            if root is None:
                return
            if len(ret_lst) >= k:
                return
            dfs(root.left)
            ret_lst.append(root.val)
            dfs(root.right)
        dfs(root)
        return ret_lst[k-1]


if __name__ == '__main__':
    root = build_tree([3,1,4, None,None, None, 2])
    print(Solution().kthSmallest(root,1))