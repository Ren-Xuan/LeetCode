class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        dp[n][k] = dp[n - 1][k] + dp[n - 1][k - 1] + dp[n - 1][k - 2] + ... + dp[n - 1][k+1-n+1] + dp[n -1][k - n + 1]
        dp[n][k + 1] = dp[n - 1][k + 1] + dp[n - 1][k] + ... +dp[n - 1][k + 1 -n + 1]
 
        因此： dp[n][k + 1] = dp[n - 1][k + 1] + dp[n][k] - dp[n - 1][k - n + 1]
        """
        if k == 0:
            return 1
        if n == 1:
            return 0
        elif n == 2:
            if k == 1:
                return 1
            elif k >=2:
                return 0
        dp=[[0]*(k+1)for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i][0] = 1
        dp[2][1] = 1
        for i in range(3,n+1):
            for j in range(1,k+1):
                dp[i][j] += (dp[i-1][j]+dp[i][j-1])
                if j>=i:
                    dp[i][j] -=dp[i-1][j-i]
        return dp[n][k]%(10**9+7)