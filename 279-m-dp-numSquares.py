class Solution:
    def numSquares(self, n: int) -> int:
        s = [i**2 for i in range(1,n+1)]
        """
        dp[i] = min(dp[i],dp[i-e]+1)
        """
        dp = [10**4]*(n+1)
        dp[0] = 0
        for e in s:
            for i in range(e,n+1):
                dp[i] = min(dp[i],dp[i-e]+1)
        return dp[n]