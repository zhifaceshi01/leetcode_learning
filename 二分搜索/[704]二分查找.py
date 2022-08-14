from typing import *
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums,target)
        if i == len(nums) or nums[i] != target:
            return -1
        return i


if __name__ == '__main__':
    print(Solution().search)
