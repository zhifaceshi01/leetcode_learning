from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import *

MAXINF = float('inf')
MININF = -float('inf')

# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if root is None:
#             return root
#
#         q = [root]
#         while len(q) !=0:
#             length = len(q)
#             for t, n in zip(q[:-1], q[1:]):
#                 t.next = n
#             while length != 0:
#                 cur = q.pop(0)
#                 length -= 1
#                 if cur.left != None:
#                     q.append(cur.left)
#                 if cur.right != None:
#                     q.append(cur.right)
#         return root

# DFS算法
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        def dfs(node1, node2):
            if node1 is None or node2 is None:
                return None

            node1.next = node2
            dfs(node1.left, node1.right)
            dfs(node2.left, node2.right)
            dfs(node1.right, node2.left)

        dfs(root.left, root.right)
        return root



if __name__ == '__main__':
    build_obj = Codec()
    head = build_obj.deserialize([1,2,4,None,None,5,None,None,3,6,None,None,7])

    print(Solution().connect(head))
