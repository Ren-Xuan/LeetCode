import bisect
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = bisect.bisect_left(nums, target)
        hi = bisect.bisect_right(nums, target)
        return [lo, hi-1] if lo != hi else [-1, -1]
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1,-1]
        result = []
        left = 0
        right = n-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid+1
            else:#nums[mid]>=target
                right = mid
        result.append(left)
        left = 0
        right = n-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<=target:
                left = mid+1
            else:#nums[mid]>target
                right = mid
        if nums[left]!=target:
            result.append(left-1)
        else:
            result.append(left)
        if nums[result[0]]!=target:
            return [-1,-1]
        return result
    
