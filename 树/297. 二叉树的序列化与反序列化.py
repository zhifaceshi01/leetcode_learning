from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import TreeNode, preorder

MAXINF = float('inf')
MININF = -float('inf')


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret_lst = []
        def dfs(root):
            if root is None:
                ret_lst.append('#')
                return
            ret_lst.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(ret_lst)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(lst):
            if len(lst) == 0:
                return None
            a = lst.pop(0)
            if a == '#':
                return None
            val = int(a)
            node = TreeNode(val)
            a = dfs(lst)
            b = dfs(lst)
            node.left = a
            node.right = b
            return node
        return dfs(data.split(','))


if __name__ == '__main__':
    # a = TreeNode(1)
    # b = TreeNode(2)
    # c = TreeNode(3)
    # d = TreeNode(4)
    # e = TreeNode(5)
    # a.left = b
    # a.right = c
    # c.left = d
    # c.right = e
    #
    code = Codec()
    # print(code.serialize(a))

    s = "1,2,#,#,3,4,#,#,5,#,#"
    node = code.deserialize(s)
    preorder(node)

