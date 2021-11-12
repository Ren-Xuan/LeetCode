class Solution:
    def maxProfitOvertime(self, prices) -> int:
        n = len(prices)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                if prices[j] > prices[i]:
                        dp[i][j] = prices[j] - prices[i]
        start = -1
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                start = i-1
                break

        for k in range(1):
            for i in range(start,n):       
                for j in range(i+4,n):
                    sale = -1
                    maxVal = prices[i]
                    for s in range(i+1,j-3+1):
                        if prices[s]>maxVal:
                            sale = s
                            break
                    if sale == -1:
                        continue
                    for s in range(sale,j-3+1):#卖

                        for t in range(s+2,j-1+1):#买
                        #for t in range(1):
                            dp[i][j] = max(dp[i][j],dp[i][s]+dp[t][j])
            maxVal = -1
        
        
        for i in range(n):
            for j in range(n):
                if dp[i][j]>maxVal:
                    maxVal = dp[i][j]

        return maxVal

    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp = [[0]*3 for _ in range(n)]
        #dp[i][x]第i天进入(处于)x状态（0.不持股，1.持股，2.冷冻期）
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0

        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][2])
            dp[i][1] = max(dp[i-1][0] - prices[i],dp[i-1][2])
            dp[i][2] = dp[i-1][1] +prices[i]
        return max(dp[n-1][0],dp[n-1][2])