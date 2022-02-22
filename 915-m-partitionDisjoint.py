from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        maxLeft<minRight
        """
        N = len(nums)
        maxleft = [None] * N
        minright = [None] * N

        m = nums[0]
        for i in range(N):
            m = max(m, nums[i])
            maxleft[i] = m

        m = nums[-1]
        for i in range(N-1, -1, -1):
            m = min(m, nums[i])
            minright[i] = m

        for i in range(1, N):
            if maxleft[i-1] <= minright[i]:
                return i
    def partitionDisjoint2(self, nums):

        # [0, pos]的最大值 也就是它是左边阵营的最大值
        lmaxv = nums[0]
        # [0, i]的最大值
        maxv = nums[0]
        pos = 0
        for i in range(1,len(nums)):
            maxv = max(maxv,nums[i])
            #如果当前元素小于还小于左边阵营的最大值，那当前元素可以收归麾下
            if nums[i]<lmaxv:
                #将当前阵地范围扩大并重新计算最大值（因为右边阵营的所有值都会大于左边阵营的所有值）
                lmaxv = maxv
                pos = i
        return pos + 1