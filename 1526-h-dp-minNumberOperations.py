from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        dp = [0 for _ in range(len(target))]
        dp[0] = target[0]
        for i in range(1, len(target)):
            if target[i] <= target[i-1]:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + target[i] - target[i-1]
        return dp[-1]


    def minNumberOperations(self, target: List[int]) -> int:
        ans, n = 0, len(target)
        ans += target[0]
        for i in range(1, n):
            diff = target[i] - target[i-1]
            if diff > 0:
                ans += diff
        return ans