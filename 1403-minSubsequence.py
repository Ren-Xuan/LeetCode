class Solution(object):
    def minSubsequence1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums,reverse=True)
        for i in range(0,len(nums)):
            if sum(nums[:i+1]) > sum(nums[i+1:]):
                return nums[:i+1]
    def minSubsequence2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums,reverse=True)
        right = sum(nums)
        left = 0
        for i in range(0,len(nums)):
            if left > right:
                return nums[:i]
            else:
                left += nums[i]
                right -=nums[i]
        return nums
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums,reverse=True)
        right = sum(nums)
        left = 0
        for i in range(0,len(nums)):
            if left > right//2:
                return nums[:i]
            else:
                left += nums[i]

        return nums
s = Solution()
print(s.minSubsequence([4,3,10,9,8]))
print(s.minSubsequence([4,4,7,6,7]))
print(s.minSubsequence([6]))
print(s.minSubsequence([1,1,1]))