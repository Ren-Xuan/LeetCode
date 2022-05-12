from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """滑动具有单调性，所以滑窗"""
        left, res, curProduct = 0, 0, 1
        for right, num in enumerate(nums):
            curProduct *= num
            while left <= right and curProduct >= k:
                curProduct /= nums[left]
                left += 1
            res += right - left + 1
        return res