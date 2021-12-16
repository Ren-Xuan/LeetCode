class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            nums[abs(i) - 1] *= -1
            if nums[abs(i)-1] > 0:
                res.append(abs(i))
        return res
        """
        对数组中出现的每个数，把它们对应的 index * -1。
        比如 [4,3,2,7,8,2,3,1]，首先出现的是4，那我们就将对应的index也就是（4-1）上的值乘以-1。
        这样只出现一次的数字的index上的值一定为负数，
        如果我们乘完-1发现对应index上的值为正数，那么该数字出现了两次。
        """