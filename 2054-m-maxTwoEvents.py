from heapq import heappush
from heapq import heappop
from typing import List


class Solution:
    def maxTwoEvents(self, E: List[List[int]]) -> int:
        maxv = ans = 0
        q = []
        for s, e, v in sorted(E):
            heappush(q, (e, v))
            while q[0][0] < s:
                maxv = max(maxv, heappop(q)[1])
            ans = max(ans, v + maxv)
        return ans