class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        changedIndex = -1
        n = 0
        res = 1
        contain1 = False
        for right in range(len(nums)):
            if nums[right] == 1:
                n+=1
                contain1 = True
                if n>res:
                    res = n
            else:
                #print(left,right,changedIndex)
                left = changedIndex+1
                #find the frist 1
                changedIndex = right
                n = right - left +1
        res-=1
        if res == 0 and contain1:
            return 1
        return res