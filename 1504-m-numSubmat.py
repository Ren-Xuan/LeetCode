class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        heights = [0] * (col + 1)
        ans = 0
        for i in range(row):
            stack = [-1]
            dp = [0] * col
            for j in range(col):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
                while stack and heights[stack[-1]] > heights[j]:
                    stack.pop()
                dp[j] += dp[stack[-1]] + (j - stack[-1]) * heights[j]
                stack.append(j)
            ans += sum(dp)
        return ans