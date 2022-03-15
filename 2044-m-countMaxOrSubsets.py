from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        arr=[0]
        for i in range(len(nums)):
            arr+=[nums[i] | x for x in arr]
        return arr.count(max(arr))

    def countMaxOrSubsets1(self, nums: List[int]) -> int:
        T = nums[0]
        self.ans = 0
        for e in nums[1:]:
            T=T|e
        def dfs(cur,candidate):
            if cur == T:
                self.ans+=1
            for i,e in enumerate(candidate):
                dfs(cur|e,candidate[i+1:])
        dfs(0,nums)
        return self.ans