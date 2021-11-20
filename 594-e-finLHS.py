
from typing import Counter


class Solution:
    def findLHS(self, nums) -> int:
        nums.sort()
        l = 0
        r = 0
        res = 0
        while r<len(nums):
            while nums[r] - nums[l]>1:
                l+=1
            if nums[r]-nums[l]==1:
                res = max(res,r-l+1)
            r+=1
        return res
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        ans = 0
        d = Counter(nums)
        for num in nums:
            if num + 1 in d:
                ans = max(ans, d[num] + d[num + 1])
        return ans