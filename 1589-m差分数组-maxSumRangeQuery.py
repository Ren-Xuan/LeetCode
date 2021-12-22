from typing import List
import heapq

class Solution:
    def maxSumRangeQuery2(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        countArr = [0]*len(nums)
        for e in requests:#复杂度太高
            for i in range(e[0],e[1]+1):
                countArr[i]+=1
        indexPq = []
        result  = 0
        for i,e in enumerate(countArr):
            heapq.heappush(indexPq,(-e,i))
        for i in range(len(indexPq)):
            result+=(-heapq.heappop(indexPq)[0])*nums[i]
        return result%(10**9+7)
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MODULO = 10**9 + 7
        length = len(nums)
        #差分数组
        counts = [0] * length
        for start, end in requests:
            counts[start] += 1
            if end + 1 < length:
                counts[end + 1] -= 1
        
        for i in range(1, length):
            counts[i] += counts[i - 1]

        counts.sort()
        nums.sort()
        
        total = sum(num * count for num, count in zip(nums, counts))
        return total % MODULO
