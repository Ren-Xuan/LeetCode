
from typing import List


class Solution:
    def videoStitching1(self, clips: List[List[int]], time: int) -> int:
        dp = [0] + [float("inf")] * time
        for i in range(1, time + 1):
            for aj, bj in clips:
                if aj < i <= bj:
                    dp[i] = min(dp[i], dp[aj] + 1)
        
        return -1 if dp[time] == float("inf") else dp[time]


    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        maxn = [0] * time
        last = ret = pre = 0
        for a, b in clips:
            if a < time:
                maxn[a] = max(maxn[a], b)
        
        for i in range(time):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last
        
        return ret
