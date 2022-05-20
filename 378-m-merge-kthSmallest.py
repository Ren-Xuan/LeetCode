import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #多路归并，查看264. 丑数 II
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            val, row, col= heapq.heappop(pq)
            if col != n - 1:
                heapq.heappush(pq, (matrix[row][col + 1], row, col + 1))
        
        return heapq.heappop(pq)[0]
