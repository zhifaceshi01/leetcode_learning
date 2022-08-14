# leetcode submit region begin(Prohibit modification and deletion)
from typing import *



def get_total(matrix, num):
    m = len(matrix)
    n = len(matrix[0])
    count = 0
    for i in range(m):
        max_num = matrix[i][n-1]
        if num >= max_num:
            count += n
        else:
            for j in range(n):
                if matrix[i][j] <= num:
                    count += 1

        if matrix[i][0] > num:
            break
    return count

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = matrix[0][0]
        m = len(matrix)
        n = len(matrix[0])
        r = matrix[m - 1][n - 1]
        while l < r:
            mid = (l + r) // 2
            if get_total(matrix, mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l

if __name__ == '__main__':
    print(Solution().kthSmallest(
[[1, 5, 9], [10, 11, 13], [12, 13, 15]],
8
))