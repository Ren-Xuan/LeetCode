from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        cnt = 0
        m = min(nums)
        for e in nums:
            cnt+=e-m
        return cnt