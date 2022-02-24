from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(set(arr))
        d = {}
        for i, v in enumerate(a, 1):
            d[v] = i
        return [d[i] for i in arr]