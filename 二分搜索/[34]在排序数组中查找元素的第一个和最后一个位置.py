from typing import *
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect.bisect_left(nums, target)
        if i == len(nums) or nums[i] != target:
            return [-1,-1]
        j = i
        while j < len(nums):
            if nums[j] == target:
                j += 1
            else:
                break
        return [i,j-1]



if __name__ == '__main__':
    nums = [
        5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))
