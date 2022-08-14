from typing import *
import bisect
from collections import *
from queue import PriorityQueue
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0: return 0
        slow = 0
        fast = 0
        while fast != len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        print(nums)
        return slow


if __name__ == '__main__':
    m = [3,2,2,3]
    t = 3
    print(Solution().removeElement(m, t))
    m = [0,1,2,2,3,0,4,2]
    t = 2
    print(Solution().removeElement(m, t))
