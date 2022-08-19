from typing import *
import bisect
from collections import *
from queue import PriorityQueue

from 树.common import *


# class Solution:
#     def traver(self, root, ret):
#         if root is None:
#             return
#         ret.append(root.val)
#         self.traver(root.left, ret)
#         self.traver(root.right, ret)
#
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ret = []
#         self.traver(root, ret)
#         return ret

class Solution:


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ret = []
        stack = [root, ]
        while len(stack) != 0:
            cur = stack.pop()
            if cur != None:
                ret.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return ret







if __name__ == '__main__':
    root = build_tree([1, None, 2, 3])
    print(Solution().preorderTraversal(root))
