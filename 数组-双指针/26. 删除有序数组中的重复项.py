from typing import *
import bisect
from collections import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        slow = 0
        fast = 0
        while fast != len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        # print(nums)
        return slow + 1



if __name__ == '__main__':
    nums =  [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))
