class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        result  = []
        #print(nums)
        for i in range(n):
            if nums[i]>0:
                result.append(i+1)
        return result