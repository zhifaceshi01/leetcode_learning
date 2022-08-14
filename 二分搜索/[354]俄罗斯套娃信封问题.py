from typing import *
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sorted_envelopes = sorted(envelopes, key=lambda x: [x[0], -x[1]])
        print(sorted_envelopes)
        # 300 最长递增子序列


if __name__ == '__main__':
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    print(Solution().maxEnvelopes(envelopes))
