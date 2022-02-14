class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mid = 0
        while l<r:
            mid= (l+r)//2
            if mid % 2 == 1:
                mid-=1
            if nums[mid] == nums[mid+1]:
                l = mid +2
            else:
                r = mid  
        return nums[l]
