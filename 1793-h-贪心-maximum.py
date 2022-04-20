class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = k
        right = k
        ans = 0
        for val in range(nums[k],-1,-1):
            while left - 1>=0 and nums[left-1]>=val:
                left-=1
            while right + 1<n and nums[right+1]>=val:
                right+=1
            ans = max(ans,val*(right-left+1))
        return ans