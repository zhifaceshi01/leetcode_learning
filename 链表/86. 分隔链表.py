from typing import *
import bisect
from collections import *

from 链表.listnode_tool import *


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_node1 = ListNode(0)
        dummy_node2 = ListNode(0)
        p1 = dummy_node1
        p2 = dummy_node2
        while head != None:
            value = head.val
            if value < x:
                p1.next = head
                head = head.next
                p1 = p1.next
                p1.next = None
            else:
                p2.next = head
                head = head.next
                p2 = p2.next
                p2.next = None

        if dummy_node1.next is None:
            return dummy_node2.next
        if dummy_node2.next is None:
            return dummy_node1.next
        p1.next = dummy_node2.next
        return dummy_node1.next




if __name__ == '__main__':

    n = construct_node([2,1])
    t = Solution().partition(n, 2)
    showList(t)

    n = construct_node([1,4,3,2,5,2])
    t = Solution().partition(n, 3)
    showList(t)


