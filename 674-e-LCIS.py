from bisect import bisect_right
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = 0
        right = 1
        ans = 1
        while right<len(nums):
            if nums[right] > nums[right-1]:
                right+=1
                ans = max(ans,right - left)
            else:
                left = right
                right +=1
        return ans
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if not res or num>res[-1]:
                res.append(num)
            elif res:
                idx = bisect_left(res,num)
                res[idx] = num
        return len(res)