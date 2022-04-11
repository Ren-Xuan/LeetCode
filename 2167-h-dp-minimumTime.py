class Solution:
    def minimumTime(self, s: str) -> int:
        n, min_time, pre = len(s), len(s), 0
        for index, char in enumerate(s):
            if char == '1':
                pre = min(pre + 2, index + 1)
            min_time = min(min_time, pre + n - index - 1)
        return min_time