from typing import List


class Solution:
    def numFactoredBinaryTrees2(self, arr: List[int]) -> int:
        """
        dp[k] += (dp[i] * dp[j]) subject to arr[i]*arr[j] == arr[k]
        """
        arr.sort()
        dp = [1]*len(arr)
        for k in range(len(arr)):
            for i in range(k):
                for j in range(k):
                    if arr[i]*arr[j] == arr[k]:
                        dp[k] += (dp[i]*dp[j])
        return sum(dp)%(10**9+7)
    def numFactoredBinaryTrees(self, arr):
        MOD = 10 ** 9 + 7
        N = len(arr)
        arr.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0: #arr[j] will be left child
                    right = x / arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD
