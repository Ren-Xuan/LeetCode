class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
         dp[i][j] 表示text1[0~i-1]和text2[0~j-1]的最长公共子序列长度 
         dp[0][0]等于0，等于dp数组总体往后挪了一个，免去了判断出界 
         转移方程： 
         text1[i-1] == text2[j-1] 当前位置匹配上了: dp[i][j]=dp[i-1][j-1]+1 
         text1[i-1] ！= text2[j-1] 当前位置没匹配上了 ：dp[i][j]=max(dp[i-1][j],dp[i][j-1]); 
         basecase: 任何一个字符串为0时都是零，初始化时候就完成了basecase是赋值
        """
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n1][n2]

