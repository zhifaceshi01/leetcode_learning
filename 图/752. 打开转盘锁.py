from typing import *
import bisect
from collections import *
from queue import PriorityQueue


class Solution:
    def bodong(self, lst, i, action):
        value = int(lst[i])
        if action == 'left':
            value -= 1
            if value == -1:
                value = 9
        if action == 'right':
            value += 1
            if value == 10:
                value = 0
        lst = list(lst)
        lst[i] = str(value)
        return ''.join(lst)

    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        deadends = deadends
        queue = ['0000']
        step = 0
        visited = set()
        while len(queue) != 0:
            length = len(queue)
            while length != 0:
                cur = queue.pop(0)
                length -= 1

                if cur == target:
                    return step

                for i in range(4):
                    left = self.bodong(cur, i, 'left')
                    right = self.bodong(cur, i, 'right')

                    if left not in deadends and left not in visited:
                        visited.add(left)
                        queue.append(left)
                    if right not in deadends and right not in visited:
                        visited.add(right)
                        queue.append(right)

            step += 1

        return -1




if __name__ == '__main__':
    deadends = ["8888"]
    target = "0009"
    print(Solution().openLock(deadends, target))

    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(Solution().openLock(deadends, target))
