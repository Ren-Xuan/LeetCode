from typing import Counter, List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if freq[i]:
                ops = min(k, freq[i])
                ans += -i * ops * 2
                freq[i] -= ops
                freq[-i] += ops
                k -= ops
                if k == 0:
                    break
        
        if k > 0 and k % 2 == 1 and not freq[0]:
            for i in range(1, 101):
                if freq[i]:
                    ans -= i * 2
                    break
        
        return ans