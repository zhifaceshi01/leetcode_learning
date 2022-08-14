from typing import *
import bisect

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j += 1
        if i != len(s):
            return False
        return True



if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))
