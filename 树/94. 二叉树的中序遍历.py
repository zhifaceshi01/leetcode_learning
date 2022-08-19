from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from 树.common import *
# class Solution:
#     def travers(self, root, ret):
#         if root is not None:
#             self.travers(root.left, ret)
#             ret.append(root.val)
#             self.travers(root.right, ret)
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ret = []
#         self.travers(root, ret)
#         return ret

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ret = []
        stack = []
        while len(stack) != 0 or root is not None:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ret.append(root.val)
            root = root.right
        return ret






        return ret

if __name__ == '__main__':
    root = build_tree([1, None, 2, 3])
    print(Solution().inorderTraversal(root))
