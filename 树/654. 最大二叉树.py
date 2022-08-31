from typing import *
import bisect
from collections import *
from queue import PriorityQueue
from functools import lru_cache

from 树.common import *

MAXINF = float('inf')
MININF = -float('inf')


def find_index(nums):
    if len(nums) == 0:
        return None
    index = None
    maxvalue = MININF
    for i, v in enumerate(nums):
        if maxvalue <= v:
            maxvalue = v
            index = i
    return index

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:


        def dfs(nums):
            if len(nums) == 0:
                return None
            i = find_index(nums)
            if i is None:
                return None
            t = TreeNode(nums[i])
            t.left = dfs(nums[:i])
            t.right = dfs(nums[i+1:])
            return t

        return dfs(nums)



if __name__ == '__main__':
    nums = [3,2,1,6,0,5]
    t = (Solution().constructMaximumBinaryTree(nums))
    preorder(t)
