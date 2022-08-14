from typing import *


def check(weight, ability):
    count = 0
    t = 0
    for w in weight:
        t += w
        if t > ability:
            t = w
            count += 1
        elif t == ability:
            t = 0
            count += 1
        else:
            pass
    if t != 0:
        count += 1
    return count


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights) + 1
        while l < r:
            mid = (l+r) // 2
            if check(weights, mid) <= days:
                r = mid
            else:
                l = mid + 1
        return l



# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    weights = [1, 2, 3, 1,1]
    days = 4
    # weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # days = 5
    print(Solution().shipWithinDays(weights, days))