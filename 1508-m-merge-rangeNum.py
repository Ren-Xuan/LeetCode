
from heapq import heappop, heappush
from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        例. nums = [3, 4, 1, 2, 5, 6]
        这里会形成 6-路 升序数组，然后用归并排序合并。无需计算出全部数组，用 PriorityQueue 记录每一路当前的值以及下标即可。
        [3, 7, 8, 10, 15, 21]
        [4, 5, 7, 12, 18]
        [1, 3, 8, 14]
        [2, 7, 13]
        [5, 11]
        [6]

        """
        """
        
        查看378. 有序矩阵中第 K 小的元素、264. 丑数 II
        
        """
        mod = 10**9+7
        # 前缀和数组
        preSum = [0 for _ in range(n+1)]
        for i in range(n):
            preSum[i] = preSum[i-1] + nums[i]
        # 看作 以nums[i]为起点 的n个子数组序列 进行多路归并
        pq = []
        for i in range(n):
            # (val, i, idx)代表前缀和数值, 以第i个数为起点, 到第idx个数为终点即[i,idx)
            # 加入 每个元素 作为n个子数组序列的起始数组
            heappush(pq, (nums[i], i, i))
        res = 0
        for index in range(1, right+1):
            val, start, end = heappop(pq)
            if end + 1 < n:
                heappush(pq, (preSum[end+1] - preSum[start-1], start, end+1))
            if index >= left:
                res += val
        return res % mod


    def rangeSum2(self, nums: List[int], n: int, left: int, right: int) -> int:
        """暴力"""
        tmp = [e for e in nums]
        for i in range(len(nums)-1):
            cur = nums[i]
            for j in range(i+1,len(nums)):
                cur+=nums[j]
                tmp.append(cur)
        tmp.sort()
        ans = 0
        for i in range(left-1,right):
            ans+=tmp[i]
        return ans%(10**9+7)