class Solution(object):
    """
    
    **如果求组合数就是外层for循环遍历物品，内层for遍历背包**。

    **如果求排列数就是外层for遍历背包，内层for循环遍历物品**。
    """
    def changeTraceback(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        result = []
        def traceback(res,n,amount,coins):
            if amount == 0:
                res.sort()
                if res not in result:
                    result.append(res)
                return
            if amount < 0:
                return
            for e in coins:
                traceback(res+[e],n,amount -e ,coins)

        traceback([],0,amount,coins)
        return len(result)
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        """
        凑成总金额j的货币组合数为dp[j]
        """
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:# 遍历物品
            # 记录每添加一种面额的零钱，总金额j的变化
            for i in range(coin,amount+ 1):# 遍历背包
                dp[i] = dp[i] + dp[i - coin]
                """
                =====================================================
                因为加入了coin这种币
                i元的凑法个数dp[i]应该加上 凑成i - coin 元的可能组合个数
                加入i = 100，coins = [1,5]
                第一次coin = 1的时候
                dp[100] = 0 + dp[99] = 1就是用100/coin个coin凑
                第二次coin = 5的时候
                dp[100] = 1 + dp[95] 
                qp[95]就是在95的凑法
                (现在dp[95]的凑法已经加上了可选币coin = 5的情况)
                因为只需要在dp[95]的每一种凑法加上一枚coin=5的币就可以凑成100的新凑法 
                =====================================================
                """
        return dp[amount]
s = Solution()

print(s.change(5,[1,2,5]))
print(s.change(3,[2]))
print(s.change(10,[10]))
print(s.change(10,[1]))
print(s.change(500,[1,2,5]))