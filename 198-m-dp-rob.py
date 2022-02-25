from typing import List


class Solution:
    def rob1(self, nums: List[int]) -> int:
        self.ans = 0
        self.nums = nums
        def dfs(start,cur):
            #start 已经盗窃的
            if start == len(self.nums)-1 or start ==len(self.nums) -2:
                self.ans = max(self.ans,cur)
                return
            for i in range(start+2,len(self.nums)):
                dfs(i,cur+self.nums[i])
        for i in range(len(nums)):
            dfs(i,self.nums[i])
        return self.ans
    def rob2(self, nums: List[int]) -> int:
        """
        dp[k] = max(dp[i]+nums[k] for k in range(0,k-1))
        """
        dp = nums.copy()
        for k in range(len(nums)):
            for i in range(k-1):
                dp[k] = max(dp[k],dp[i]+nums[k])
        return max(dp)
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        dp = nums.copy()
        dp[1] = max(dp[1],dp[0])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[size - 1]
