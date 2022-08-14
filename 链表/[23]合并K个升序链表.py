from typing import *
import bisect
from collections import *

from 链表.listnode_tool import *



from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if all([w is None for w in lists]):
            return None

        dummy_node = ListNode(0)
        p = dummy_node
        q = PriorityQueue()
        for head in lists:
            if head is None:
                continue
            value = head.val

            q.put_nowait((value, { head}))  # tuple包含两个元素，第一个是优先级，第二个是数据

        while not q.empty():
            cur = q.get()[1].pop()
            p.next = cur
            p = p.next
            if cur.next is not None:
                q.put_nowait((cur.next.val, { cur.next}))

        return dummy_node.next





if __name__ == '__main__':
    lists = [[], [1]]
    ret = []
    for l in lists:
        n = construct_node(l)
        ret.append(n)
    x = (Solution().mergeKLists(ret))
    showList(x)
