from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        d = {}
        for i, x in enumerate(arr):
            if x in d:
                d[x].append(i)
            else:
                d[x] = [i]
        for v in d.values():
            m = len(v)
            s = sum(v)
            p = 0
            for i, x in enumerate(v):
                # (i * x - p) + ((s - p) - (m - i) * x)
                res[x] = s + x * (i * 2 - m) - p * 2
                p += x
        return res