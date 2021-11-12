class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        dp = [10**30]*(amount+1)
        #dp[i]  = min(dp[j],dp[j-coin]+1)
        for coin in coins:
            if coin<=amount:
                dp[coin] = 1
        for coin in coins:
            for i in range(coin,amount+1):
                if i - coin<0:
                    continue
                dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[amount]>10**29:
            return -1
        return dp[amount]