from functools import cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = min([dp[i][k] + dp[k+1][j] for k in range(i, j)])
        return dp[0][-1]

    def strangePrinter(self, s: str) -> int:
        @cache
        def dp(l,r):
            if l == r:return 1
            if s[l] == s[r]:return dp(l,r-1)
            return min(dp(l,i) + dp(i+1,r) for i in range(l,r))
        return dp(0,len(s)-1)