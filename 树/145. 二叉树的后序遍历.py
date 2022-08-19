from typing import *
import bisect
from collections import *
from queue import PriorityQueue

from 树.common import TreeNode, build_tree

#
# class Solution:
#     def travers(self, root, ret):
#         if root is not None:
#             self.travers(root.left, ret)
#             self.travers(root.right, ret)
#             ret.append(root.val)
#
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ret = []
#         self.travers(root, ret)
#         return ret

################ 卧槽，后根遍历 牛逼 ###################
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ret = []
        stack = [root, ]
        while len(stack) != 0:
            cur = stack.pop()
            if cur is not None:
                ret.append(cur.val)
                stack.append(cur.left)
                stack.append(cur.right)
        return ret[::-1]

if __name__ == '__main__':
    root = build_tree([1, None, 2, 3])
    print(Solution().postorderTraversal(root))
