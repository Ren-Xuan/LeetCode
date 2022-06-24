class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n , m = len(nums) , len(multipliers)
        dp = [[0]*i for i in range(m+1,0,-1)]    #初始化一个二维数组后，有一半是用不上的
        res = float("-inf")
        for k in range(1,m+1):      #总的操作次数
            for i in range(k+1):
                if i == 0:          #都是从右边取
                    dp[0][k] = dp[0][k-1] + nums[n-k] * multipliers[k-1]
                elif i == k:        #都是从左边取
                    dp[i][0] = dp[i-1][0] + nums[i-1] * multipliers[k-1]
                else:
                    dp[i][k-i] = max(dp[i-1][k-i] + nums[i-1]*multipliers[k-1],dp[i][k-i-1] + nums[n-(k-i)]*multipliers[k-1])
                if k == m:
                    res = max(res,dp[i][k-i])
        return res
    def maximumScore2(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(len(multipliers))
        def dfs(left, right, idx) -> int:
            if idx >= len(multipliers):
                return 0
            multiplier = multipliers[idx]
            idx += 1
            return max(nums[left] * multiplier + dfs(left + 1, right, idx),
                       nums[right] * multiplier + dfs(left, right - 1, idx))

        return dfs(0, len(nums) - 1, 0)