class Solution:
    def largestSumOfAverages(self, nums, k: int) -> float:
        n = len(nums)
        presum = [0]*(n+1)

        dp = [[0]*(k+1) for _ in range(n+1)]
        for i in range(n):
            presum[i+1] = presum[i]+nums[i]
            dp[i+1][1] = presum[i+1]/(i+1)
        for i in range(1,n+1):
            for j in range(2,min(k,i)+1):
                for t in range(i):
                    dp[i][j] = max(dp[i][j],dp[t][j-1]+(presum[i] - presum[t])/(i-t))
        return dp[n][k]


