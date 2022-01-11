from typing import List
from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], K: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        ans = float("-inf")
        for i in range(n):
            for j in range(i, n):
                pres = SortedList([0])
                pre = 0
                for k in range(m):
                    pre += matrix[k][j] - (0 if i == 0 else matrix[k][i - 1])
                    # 寻找小于等于 pre - k 的最大数。
                    # 为了达到这个目的，可以使用 bisect_left 来完成。（使用 bisect_right 不包含等号）
                    idx = pres.bisect_left(pre - K)
                    # 如果 i == len(pre) 表示无解
                    if idx < len(pres):
                        ans = max(ans, pre - pres[idx])
                    pres.add(pre)

        return ans
