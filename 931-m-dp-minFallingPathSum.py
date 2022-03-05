class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for row in range(1,n):
            for col in range(n):
                if col == 0:
                    matrix[row][col] +=min(matrix[row-1][col],matrix[row-1][col+1])
                elif col == n-1:
                    matrix[row][col] +=min(matrix[row-1][col],matrix[row-1][col-1])
                else:
                    matrix[row][col] +=min(matrix[row-1][col],matrix[row-1][col-1],matrix[row-1][col+1])
        return min(matrix[n-1])