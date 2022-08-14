from typing import *
import bisect
from collections import *
from queue import PriorityQueue

# 使用双指针的方法，n^2的复杂度  🐂🍺
class Solution:

    def get_string(self,s, l, r):
        if s[l] != s[r]:
            return ""
        while r < len(s) and l > -1 and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1: r]

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        res = s[0]
        for i in range(len(s) - 1):
            s1 = self.get_string(s, i, i)
            s2 = self.get_string(s, i, i+1)
            res = sorted([res, s1, s2], key=lambda x: -len(x))[0]
        return res




if __name__ == '__main__':
    s = 'babad'
    print(Solution().longestPalindrome(s))
    s = 'cbbd'
    print(Solution().longestPalindrome(s))
