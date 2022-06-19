class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        heapq.heapify(nums)   # 建立最小堆
        while k:
            k -= 1
            # 每次操作：弹出最小值，增加 1 并重新添加
            num = heapq.heappop(nums)
            heapq.heappush(nums, num + 1)
        res = 1
        for num in nums:
            res *= num
            res %= mod
        return res
