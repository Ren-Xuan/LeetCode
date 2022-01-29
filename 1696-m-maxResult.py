class Solution:
    def maxResult2(self, nums: List[int], k: int) -> int:
        #维护当前最大值  方法1：最大堆  方法2:单调递减队列（队首）
        n = len(nums)
        maxHeap = []
        heapq.heapify(maxHeap)
        heapq.heappush(maxHeap, (-nums[0], 0) )
        res = nums[0]

        for i in range(1, n):
            while maxHeap and i - maxHeap[0][1] > k:    #index的距离太大，以后i越来越大，top()就没用了
                heapq.heappop(maxHeap)
            res = -maxHeap[0][0] + nums[i]
            heapq.heappush(maxHeap, (-res, i) )         #dp的思想
        return res
    def maxResult(self, nums: List[int], k: int) -> int:
        #维护当前最大值  方法1：最大堆  方法2:单调递减队列（队首）
        n = len(nums)
        pq = []
        pq.append((nums[0], 0) )
        res = nums[0]

        for i in range(1, n):
            while len(pq)>0 and i - pq[0][1] > k:    #index的距离太大，以后i越来越大，top()就没用了
                pq = pq[1:]
            res = pq[0][0] + nums[i]
            while len(pq)>0 and res>=pq[-1][0]:
                pq = pq[:-1]
            pq.append((res, i) )         #dp的思想
        return res