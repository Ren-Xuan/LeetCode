from bisect import bisect_left


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """时间复杂度O(mlogmn)"""
        # 统计表中不大于mid的数的个数
        countNGT = lambda mid: sum(min(n, mid // row) for row in range(1, m + 1))
        return bisect_left(range(int(m * n + 10)), k, key=countNGT)