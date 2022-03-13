from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        前缀和
        最后的前缀和就类似于股票走势的K线图,最高点和最低点相差的值就是所求的答案
        """
        nums = [0] + nums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return max(nums) - min(nums)

    def maxAbsoluteSum2(self, nums: List[int]) -> int:
        curMax= 0
        ans = 0
        left = 0
        right = 0
        while right<len(nums):
            curMax+=nums[right]
            ans = max(ans,curMax)
            while left<=right and curMax<0:
                curMax-=nums[left]
                left+=1
            right+=1
        left = 0
        right = 0
        curMax = 0
        while right<len(nums):
            curMax+=nums[right]
            ans = max(ans,-curMax)
            while left<=right and curMax>0:
                curMax-=nums[left]
                left+=1
            right+=1
        
        return ans