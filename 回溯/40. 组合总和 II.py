from typing import *
import bisect
from collections import *
from queue import PriorityQueue

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        if sum(candidates) == target:
            return [candidates]

        candidates = Counter(candidates)

        ret = []
        self.dfs(candidates, [], target,  set(), ret)
        return ret
    def dfs(self, candidates: Dict, cur_lst, target,  visited,ret):
        if target < 0:
            return
        if target == 0:
            cur_lst = sorted(cur_lst)
            if cur_lst not in ret:
                ret.append(list(cur_lst))
        for k, v in candidates.items():
            if k in visited:
                continue
            visited.add(k)
            for i in range(1, v+1):
                value = k * i
                candidates[k] -= value
                self.dfs(candidates, cur_lst + [k] * i, target - value, visited, ret)
                candidates[k] += value
            visited.remove(k)




if __name__ == '__main__':
    candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 30
    print(Solution().combinationSum2(candidates, target))

    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(Solution().combinationSum2(candidates, target))

    candidates = [2,5,2,1,2]
    target = 5
    print(Solution().combinationSum2(candidates, target))