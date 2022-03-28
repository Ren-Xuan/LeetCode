class Solution:
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return min(n % 2 + 1 + self.minDays(n // 2), n % 3 + 1 + self.minDays(n // 3))

