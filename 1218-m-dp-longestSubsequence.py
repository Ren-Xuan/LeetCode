class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        d = {}
        for a in arr:
            d[a] = d.get(a - difference, 0) + 1
        return max(d.values())