from typing import List
from heapq import *

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        import bisect
        arr = []
        left = 0
        res = []
        for right in range(len(nums)):
            bisect.insort(arr, nums[right])
            while len(arr) > k:
                arr.pop(bisect.bisect_left(arr, nums[left]))
                left += 1
            if len(arr) == k:
                res.append((arr[k // 2] + arr[(k - 1) // 2]) / 2.0)
        return res


    def medianSlidingWindow2(self, nums: List[int], k: int) -> List[float]:
        minheap = []
        maxheap = []
        res = []
        for i in range(len(nums)):
            if i > k-1:
                remove = nums[i-k]
                if remove in minheap:
                    minheap.remove(remove)
                    heapify(minheap)
                else:
                    maxheap.remove(-remove)
                    heapify(maxheap)
            newnum = nums[i]
            heappush(minheap, newnum)
            heappush(maxheap, -heappop(minheap))
            while len(maxheap) > len(minheap):
                heappush(minheap, -heappop(maxheap))
            if i >= k-1:
                if len(minheap) > len(maxheap):
                    res.append(minheap[0])
                else:
                    res.append((minheap[0]-maxheap[0])/2)
        return res
