from typing import List

# leetcode submit region begin(Prohibit modification and deletion)


def g(arr, mid):
    if arr[mid] >= arr[mid + 1]:
        return True
    else:
        return False


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = (l+r) // 2
            if g(arr, mid):
                r = mid
            else:
                l = mid + 1
        return l

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    arr = [24,69,100,99,79,78,67,36,26,19] # 2
    print(Solution().peakIndexInMountainArray(arr))
    arr = [0,1,0] # 1
    print(Solution().peakIndexInMountainArray(arr))
    arr = [0,2,1,0] # 1
    print(Solution().peakIndexInMountainArray(arr))
    arr = [0,10,5,2] # 1
    print(Solution().peakIndexInMountainArray(arr))
    arr = [3,4,5,1] # 2
    print(Solution().peakIndexInMountainArray(arr))