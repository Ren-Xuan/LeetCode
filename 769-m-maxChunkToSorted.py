from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        个区间内最大的数字，不应该大于这个区间最右边的index。
        因此我们从左向右遍历，如果已经观测到的最大值小于等于这个区间的index，则可以划分区间。
        
        """
        res, max_val = 0, arr[0]
        for i, num in enumerate(arr):
            if num > max_val:
                max_val = num
            if max_val == i:
                res += 1
        return res