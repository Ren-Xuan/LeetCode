class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)   # 解决[i-n]之间的题目的最高分数
        for i in range(n - 1, -1, -1):
            #解决第i道题目，那么我们只能选择i+brainpower[i]以后的题目
            dp[i] = max(dp[i + 1], questions[i][0] + dp[min(n, i + questions[i][1] + 1)])
        return dp[0]

