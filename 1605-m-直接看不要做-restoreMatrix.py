class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = x = min(rowSum[i], colSum[j])
                rowSum[i] -= x
                colSum[j] -= x
        return res