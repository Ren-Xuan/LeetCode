class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, n = 0, len(prices)
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                ans += diff
        return ans