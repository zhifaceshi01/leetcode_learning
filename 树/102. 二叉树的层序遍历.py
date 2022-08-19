from typing import *
import bisect
from collections import *
from queue import PriorityQueue

from 树.common import TreeNode, build_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        que = [root]
        ret = []
        while len(que) != 0:
            length = len(que)
            t = []
            while length != 0:
                cur = que.pop(0)
                t.append(cur.val)
                if cur.left != None:
                    que.append(cur.left)
                if cur.right != None:
                    que.append(cur.right)

                length -= 1
            ret.append(t)
        return ret


if __name__ == '__main__':
    root = build_tree([3,9,None,None,20,15,None,None,7])
    print(Solution().levelOrder(root))
