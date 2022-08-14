# leetcode submit region begin(Prohibit modification and deletion)
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n+1
        while l < r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m+1
        return l

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().firstBadVersion(5))