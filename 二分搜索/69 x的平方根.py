
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x + 1
        while l < r:
            m = (l+r)//2
            if m ** 2 > x:
                r= m
            else:
                l = m + 1
        return l - 1
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))