class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        dp[i][j]：最长为i棍子，左侧能看到j个

        dp[i]][j] = dp[i-1][j]#i排在当前最长的木棍的前面
        
        假如[1,3,2,4],[1,3,4,2]->[1,3,2,5,4],[1,3,5,2,4],[1,3,5,4,2]
        递推式来自于以下分析 从1... n n个数中看到k个，
        等价于以下两种情况排列数之和

        (i) 从2...n n -1个数中看到k个数，
        再把1插入排列，共有n-1 * dp[n-1][k]种排列。

        (ii)从1...n-1 n-1个数中看到k-1个数，
        再把n放在排列末尾。共有dp[n-1][k-1]种排列。
        dp[i][j] = (i-1) * dp[i-1][j] + dp[i-1][j-1]; 
        """
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[1][1] = 1
        M= 10**9+7
        for i in range(2,n+1):
            bound = min(k,i)
            for j in range(1,bound+1):
                dp[i][j] = dp[i-1][j-1]
                dp[i][j]+=dp[i-1][j]*(i-1)
                dp[i][j]%=M
        return dp[n][k]