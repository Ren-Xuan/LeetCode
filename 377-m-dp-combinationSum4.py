class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        dp[i][j]表示和为i,最大元素下标为i的组合元素个数
        """
        dp = [ 0 for _ in range(target+1)]
        for e in nums:
            if e<=target:
                dp[e] = 1
        for i in range(1,target+1):
            for e in nums:
                if e+i<=target:
                    dp[e+i] +=dp[i]
        return dp[target]
