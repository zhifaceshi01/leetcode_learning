from typing import *
import bisect
from collections import *

from 链表.listnode_tool import *


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = head
        fast = head
        while fast != None and k != 0:
            k -= 1
            fast = fast.next
        while fast != None:
            fast = fast.next
            slow = slow.next
        return slow




if __name__ == '__main__':
    lst = [1,2,3,4,5,6]
    n = construct_node(lst)
    print(Solution().getKthFromEnd(n , 3))
