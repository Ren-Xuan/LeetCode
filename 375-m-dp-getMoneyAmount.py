class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]*(n+2) for _ in range(n+2)]
        """
        相似的题目有 887鸡蛋掉落 312戳气球 132分割回文串


        dp[i][j]表示从[i,j]中猜出正确数字所需要的最少花费金额.(dp[i][i] = 0)
        假设在范围[i,j]中选择x, 则选择x的最少花费金额为: max(dp[i][x-1], dp[x+1][j]) + x
        用max的原因是我们要计算最坏反馈情况下的最少花费金额(选了x之后, 正确数字落在花费更高的那侧)
        
        初始化为(n+2)*(n+2)数组的原因: 处理边界情况更加容易, 例如对于求解dp[1][n]时x如果等于1, 需要考虑dp[0][1](0不可能出现, dp[0][n]为0)
        而当x等于n时, 需要考虑dp[n+1][n+1](n+1也不可能出现, dp[n+1][n+1]为0)
        
        如何写出相应的代码更新dp矩阵, 递推式dp[i][j] = max(max(dp[i][x-1], dp[x+1][j]) + x), x~[i:j], 可以画出矩阵图协助理解, 可以发现
        dp[i][x-1]始终在dp[i][j]的左部, dp[x+1][j]始终在dp[i][j]的下部, 所以更新dp矩阵时i的次序应当遵循bottom到top的规则, j则相反, 由于
        i肯定小于等于j, 所以我们只需要遍历更新矩阵的一半即可(下半矩阵)
        """
        for i in range(n,0,-1):
            for j in range(i,n+1):
                if i == j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1e9
                    for x in range(i,j+1):
                        dp[i][j] = min(dp[i][j],max(dp[i][x-1],dp[x+1][j])+x)
        return dp[1][n]