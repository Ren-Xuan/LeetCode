class Solution:
    def kthLargestValue(self, matrix, k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prefix = [[0]*n for _ in range(m)]
        import queue
        q = queue.PriorityQueue()
        for i in range(m):
            line = matrix[i][0]
            for j in range(n):
                if j!=0:
                    line^=matrix[i][j]
                if i !=0:
                    prefix[i][j] = prefix[i-1][j]^line
                else:
                    prefix[i][j] = line
                q.put(- prefix[i][j])

        result = 0
        for i in range(k):
            result = -q.get()
        return result
    def kthLargestValue(self, matrix , k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prefix = [[0]*n for _ in range(m)]
        import heapq
        heap = []
        for i in range(m):
            line = matrix[i][0]
            for j in range(n):
                if j!=0:
                    line^=matrix[i][j]
                if i !=0:
                    prefix[i][j] = prefix[i-1][j]^line
                else:
                    prefix[i][j] = line
                heapq.heappush(heap,-prefix[i][j])
        print(prefix)
        result = 0
        for i in range(k):
            result = -heapq.heappop(heap)
        return result
