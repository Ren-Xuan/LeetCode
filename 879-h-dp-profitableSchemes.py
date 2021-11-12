class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group, profit) -> int:
        """
        dp[i][j] = 用i名员工,创造j利润的创造的计划
        dp[5] = [0]*n

        dp[i][j+profit] +=dp[i-group[k]][j]
        
        """
        dp = [[0]*(minProfit+1) for _ in range(n+1)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for k in range(len(group)):
            for i in range(n,-1,-1):
                if i < group[k]:
                    break
                for j in range(minProfit+1):
                    
                    if j+profit[k]> minProfit:
                        dp[i][minProfit] +=dp[i - group[k]][j]
                        dp[i][minProfit]%=1e9+7
                    else:
                        dp[i][j+profit[k]]+=dp[i-group[k]][j]
                        dp[i][j+profit[k]]%=1e9+7
        return int(dp[n][minProfit])