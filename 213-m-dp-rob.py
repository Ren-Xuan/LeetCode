from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return  max(nums)
        elif len(nums) == 3:
            return max(nums)
        elif len(nums) == 4:
            return max(nums[0]+nums[2],nums[1]+nums[3])
        #不抢第一家
        dp = [0] * len(nums)
        dp[1] = nums[1]
        dp[2] = max(nums[2], nums[1])
        for i in range(3, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        ans = dp[len(nums)-1]
        #抢第一家
        first = nums[0]
        for i in range(len(nums)):
            dp[i] = 0
        nums = nums[2:-1]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        ans = max(ans,dp[len(nums)-1]+first)
        return ans
