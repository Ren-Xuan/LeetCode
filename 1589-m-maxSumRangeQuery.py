from typing import List
import heapq

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        countArr = [0]*len(nums)
        for e in requests:
            for i in range(e[0],e[1]+1):
                countArr[i]+=1
        indexPq = []
        result  = 0
        for i,e in enumerate(countArr):
            heapq.heappush(indexPq,(-e,i))
        for i in range(len(indexPq)):
            result+=(-heapq.heappop(indexPq)[0])*nums[i]
        return result%(10**9+7)