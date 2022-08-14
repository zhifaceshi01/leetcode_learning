from queue import PriorityQueue

from 链表.listnode_tool import ListNode

tsq = q = PriorityQueue()

# 示例3
tsq.put_nowait((0, ListNode(0)))  # tuple包含两个元素，第一个是优先级，第二个是数据
tsq.put_nowait((1, ListNode(1)))
while not tsq.empty():
    print(tsq.get())