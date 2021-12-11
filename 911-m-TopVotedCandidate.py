from typing import Counter, List
import heapq
class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        q = []
        self.res = []
        c = Counter()
        for i, j in zip(persons, times):
            c[i] += 1
            heapq.heappush(q, (-c[i], -j, i))
            self.res.append((q[0][2], -q[0][1]))



    def q(self, t: int) -> int:
        l, r = 1, len(self.res)
        while l < r:
            m = l + r >> 1
            if self.res[m][1] <= t:
                l = m + 1
            else:
                r = m
        return self.res[l - 1][0]