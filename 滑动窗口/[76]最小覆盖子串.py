from typing import *
import bisect
from collections import *
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        target_dct = Counter(t)
        window= defaultdict(int)
        window_len = 0
        isvalid = 0
        word = None
        while r < len(s):
            c = s[r]
            window[c] += 1
            window_len += 1
            if window[c] == target_dct[c]:
                isvalid += 1
            r += 1
            while isvalid == len(target_dct):
                c = s[l]
                t_w = s[l: r]
                if word is None:
                    word = t_w
                elif len(word) >= len(t_w):
                    word = t_w


                if window[c] == target_dct[c]:
                    isvalid -= 1

                window[c] -= 1
                window_len -= 1
                l += 1
        return word if word is not None else ""


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    print(Solution().minWindow(s, t))
    s = 'a'
    t = 'aa'
    print(Solution().minWindow(s, t))