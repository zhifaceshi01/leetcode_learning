from typing import *
import bisect
from collections import *

from 链表.listnode_tool import *


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_node = ListNode(0)
        pre1 = list1
        pre2 = list2
        p = dummy_node

        while pre1 is not None and pre2 is not None:
            if pre1.val <= pre2.val:
                p.next = pre1
                pre1 = pre1.next
                p = p.next
            else:
                p.next = pre2
                pre2 = pre2.next
                p = p.next
        if pre2 is not None:
            p.next = pre2
        if pre1 is not None:
            p.next = pre1
        return dummy_node.next



if __name__ == '__main__':
    l1 = construct_node([1,2,4])
    l2 = construct_node([1,3,4])
    a = (Solution().mergeTwoLists(l1, l2))
    showList(a)

    l1 = construct_node([])
    l2 = construct_node([1,3,4])
    a = (Solution().mergeTwoLists(l1, l2))
    showList(a)