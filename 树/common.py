from typing import *
import bisect
from collections import *
from queue import PriorityQueue

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

def preorder(root):
    if root is None:
        return
    else:
        print(root.val ,end='\t')
        preorder(root.left)
        preorder(root.right)

class Codec:
    head = None
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        ret = []
        self._serialize(root, ret)
        return ret

    def _serialize(self, root, ret):
        if root is None:
            ret.append(None)
        else:
            ret.append(root.val)
            self._serialize(root.left, ret)
            self._serialize(root.right, ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """
        Codec.head = None
        self._deserialize(data)
        return Codec.head

    def _deserialize(self,data):
        if len(data) == 0:
            return None
        else:
            val = data.pop(0)
            if val is None:
                return None
            node = TreeNode(val)
            if Codec.head is None:
                Codec.head = node
            node.left = self._deserialize(data)
            node.right = self._deserialize(data)
            return node

def build_tree(lst):
    build_obj = Codec()
    root = build_obj.deserialize(lst)
    return root


build_obj = Codec()
head = build_obj.deserialize([5,3,2,None,None,4,None,None,6,None,7])
# head = build_obj.deserialize([3,1,None,2,4])
preorder(head)
print()
