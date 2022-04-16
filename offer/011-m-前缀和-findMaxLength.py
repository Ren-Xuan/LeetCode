from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:##转化为和为0的最大连续数组
        """
        本质还是前缀和，不过是进阶
        假如有 -1,-1,-1,1,1,1,-1,-1,-1
        当扫描前三个-1的时候cur_sum=3记录下标2
        扫描到最后一个-1即下标8的时候cur_sum又出现了3
        因此前缀和的概念说明从2到8的下标子数组和为0
        这样就能计算出长度8-2
        """
        pre_sum={0:-1}    ###### 存放前缀和的index
        for i in range(len(nums)):##  把0变为-1，1还是1
            if nums[i] == 0:
                nums[i] = -1
        cur_sum,res=0,0    ### 目前的和 结果
        for i in range(len(nums)): 
            cur_sum+=nums[i]
            if cur_sum in pre_sum:  ######## 只需要找到前缀和为cur_sum的最靠前的index
                res=max(res,i-pre_sum[cur_sum]) ##已经存在cur_sum了 没必要加入到pre_sum里面去
            else: 
                pre_sum[cur_sum]=i  ####之前不存在前缀和为cur_sum的，这是第一个。则加入进去
        return res
        