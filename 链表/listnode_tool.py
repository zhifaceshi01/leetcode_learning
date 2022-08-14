import itertools
import collections
import math
import re
import sys

MAXINF = float('inf')
MININF = -float('inf')

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)
    # def __lt__(self, other): --- leetcode报错
    #     return self.val < other.val


def showList(node):
    while node != None:
        print(" " + str(node.val), end='')
        node = node.next
    print()


def construct_node(lst):
    head = None
    preNode = None
    for n in lst:
        node = ListNode(n)
        if head is None:
            head = node
        if preNode is not None:
            preNode.next = node
        preNode = node
    return head

def get_node(head, val):
    while head is not None and head.val != val:
        head = head.next
    return head

# if __name__ == '__main__':
#     n = ListNode(0)
#     m = ListNode(1)
#     print(n < m)