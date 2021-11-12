class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]	# 多维费用问题的0-1背包问题。dp[i][j]表示使用i个0和j个1能表示的字符串的最大数量
        dic = dict()
        for s in strs:
            a,b= s.count('1'),s.count('0')
            dic[s] = (a,b)
        # 遍历物品
        for str in strs:
            ones = dic[str][0]
            zeros = dic[str][1]
            # 遍历背包容量且从后向前遍历！
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]