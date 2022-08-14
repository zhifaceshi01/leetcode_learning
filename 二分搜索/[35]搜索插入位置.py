from typing import *
import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if len(nums) == 0:
        #     return 0 if nums[0] == target else -1
        i = 0
        j = len(nums)
        while i < j:
            mid = (i+j) // 2
            if nums[mid] >= target:
                j = mid
            else:
                i = mid+1
        return i

if __name__ == '__main__':
    # nums = [1, 3, 5, 6]
    # target = 5
    # print(Solution().searchInsert(nums, target))
    nums = [1,3,5,6]
    target = 2
    print(Solution().searchInsert(nums, target))
    nums = [1,3,5,6]
    target = 7
    print(Solution().searchInsert(nums, target))