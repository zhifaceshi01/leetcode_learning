from typing import List

def g(piles, h, speed):
    r = 0
    for x in piles:
        y =  x // speed if (x%speed == 0) else (x // speed) + 1
        r += y
    return r <= h


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) + 1
        while l < r:
            m = (l+r)//2
            if g(piles, h, m):
                r = m
            else:
                l = m + 1
        return l

if __name__ == '__main__':

    print(Solution().minEatingSpeed([3,6,7,11], 8))
