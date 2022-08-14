from typing import *
import bisect

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        while l < r:
            mid = (l+r) // 2
            if nums[mid] != mid:
                r = mid
            else:
                l = mid + 1
        return l



if __name__ == '__main__':
    print(Solution().missingNumber([0,1,3]))
    print(Solution().missingNumber([0,1,2,3,4,5,6,7,9]))
