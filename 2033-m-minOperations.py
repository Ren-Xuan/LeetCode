from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 转成有序数组，并寻找中位数（偶数寻找中间偏小那个数）
        l = []
        for i in grid:
            l.extend(i)
        l.sort()
        n = len(l)
        middle = n // 2 - 1 + n % 2
        # 1*1矩阵直接返回0
        if n == 1:
            return 0
        # 计算相邻两数相减的值（0不计入其内）
        l1 = []
        for i in range(1, n):
            if l[i]-l[i-1] > 0:
                l1.append(l[i]-l[i-1])
        # 如果l1不存在，说明全相等。如果l1最小值比x小，说明无法计算
        if l1:
            if min(l1) < x:
                return -1
        else:
            return 0
        # 计算次数，如果有一个数和中位数的间隔不能整除x，说明无法计算
        num = 0
        for i in l:
            dt = abs(i-l[middle])/x
            if dt % 1 != 0:
                return -1
            num += int(dt)
        return num