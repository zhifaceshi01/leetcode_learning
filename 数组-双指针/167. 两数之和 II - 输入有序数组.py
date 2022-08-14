from typing import *
import bisect
from collections import *
from queue import PriorityQueue

### 解法一：使用二分查找的方法，nlogn复杂度
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             red = target - numbers[i]
#
#             t = bisect.bisect_right(numbers,red)
#             if numbers[t-1] == red:
#                 return [i+1, t]
class Solution:
## 解法二：使用两边指针的方式，n的复杂度
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    numbers = [2,3,4]
    target = 6
    print(Solution().twoSum(numbers, target))
    numbers = [2,7,11,15]
    target = 9
    print(Solution().twoSum(numbers, target))
    numbers = [0,0,3,4]
    target = 0
    print(Solution().twoSum(numbers, target))