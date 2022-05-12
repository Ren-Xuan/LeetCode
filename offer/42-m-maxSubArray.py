from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = 0
        ans = -10**9+7
        for i in range(len(nums)):
            curMax = max(curMax+nums[i],nums[i])
            ans = max(ans,curMax)
        return ans