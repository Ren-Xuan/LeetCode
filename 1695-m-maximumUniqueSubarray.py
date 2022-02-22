from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #typical slip window
        left = 0
        right = 0
        d = set()
        curSum = 0
        res = 0
        while right<len(nums) and left<len(nums):
            cur = nums[right]
            if cur not in d:
                d.add(cur)
                curSum +=cur
                res = max(res,curSum)
            else:
                while nums[left]!=cur:
                    curSum-=nums[left]
                    d.remove(nums[left])
                    left+=1
                d.add(cur)
                left+=1
            right+=1
        return res
