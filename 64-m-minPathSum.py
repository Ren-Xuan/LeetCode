from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        MAX = 10**5
        dp = [[MAX]*len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        m , n = len(grid),len(grid[0])
        for c in range(1,n):
            dp[0][c]=dp[0][c-1]+grid[0][c]
        for r in range(1,m):
            dp[r][0]=dp[r-1][0]+grid[r][0]
        for row in range(1,m):
            for col in range(1,n):
                dp[row][col] = min(dp[row-1][col],dp[row][col-1])+grid[row][col]
        return dp[-1][-1]