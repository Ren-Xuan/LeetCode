class Solution:
    def mostCompetitive1(self, nums: List[int], k: int) -> List[int]:
        #找k个最小的
        self.ans = []
        MAX = 10**10
        def find(start,res):
            if res>=len(nums) - start:
                for i in range(start,len(nums)):
                    self.ans.append(nums[i])
                return
            curIndex = -1
            curMin = MAX
            for index in range(start,len(nums)-res+1):
                if nums[index]<curMin:
                        curMin,curIndex = nums[index],index
            self.ans.append(nums[curIndex])
            if res>1:
                find(curIndex+1,res-1)
        find(0,k)
        return self.ans

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        #找k个最小的
        cnt = len(nums) - k  # 需要删除的元素个数
        stack = []               # 非严格单调递增栈
        for num in nums:
            while cnt and stack and num < stack[-1]:
                cnt -= 1
                stack.pop()
            stack.append(num)
        return stack[:k]
    def mostCompetitive2(self,nums,k):
        def drop_encoder(input_data:torch.Tensor,kth):
            #找到第k个最小值，低于k的都丢弃
            lower_bound = torch.kthvalue(input_data,kth).values
            mask = input_data<=lower_bound
            return input_data.mul(mask)
        res = drop_encoder(Tensor(nums),k).numpy().tolist()
        return list(filter(int(e)!=0,res))