from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(tmp, cur, index):
            if cur > target:
                return
            if cur == target:
                res.append(tmp)
                return
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(tmp + [candidates[i]], cur + candidates[i], i + 1)
        
        res = []
        pre = []
        contain = False
        for e in candidates:
            if e<target:
                pre.append(e)
            elif e == target:
                contain = True
        if contain:
            res.append([target])
        candidates = pre
        n = len(candidates)
        candidates.sort()
        backtrack([], 0, 0)
        return res

