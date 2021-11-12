class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        cur = 0
        m = len(nums)+1
        left = 0
        right = 0
        while right<len(nums):
            cur+=nums[right]
            while cur>=target:
                m = min(m,right-left+1)
                cur-=nums[left]
                left+=1
            right+=1
        return 0 if m == len(nums)+1 else m
    def minSubArrayLen2(self, s: int, nums) -> int:
        # 定义一个无限大的数
        res = float("inf")
        Sum = 0
        index = 0
        for i in range(len(nums)):
            Sum += nums[i]
            while Sum >= s:
                res = min(res, i-index+1)
                Sum -= nums[index]
                index += 1
        return 0 if res==float("inf") else res