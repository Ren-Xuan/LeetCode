class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0]*(K+1) for _ in range(N+1)]
        #dp[i][j] 表示在i步用j个鸡蛋可以测出最大层数
        for i in range(1,N+1):
            for j in range(1,K+1):
                """
                // 鸡蛋没碎，数量不变，用了一步，dp[i - 1][j]（上层）
                // 鸡蛋碎了，数量减一，用了一步，dp[i - 1][j - 1]（下层）
                // 1（当前层）
                // 最大层数 = 上层 + 下层 + 当前层
                """
                dp[i][j] = dp[i-1][j]+dp[i-1][j-1]+1
                if dp[i][j]>=N:
                    return i
        return N
    def superEggDrop3(self, K: int, N: int) -> int:
        dp = [0] * (K + 1)
        m = 0
        #dp[k][m] 的含义是k个鸡蛋 移动m次最多能够确定多少楼层
        while dp[K] < N:
            m += 1
            for k in range(K, 0, -1):
                # print(m, k)
                dp[k] = dp[k - 1] + dp[k] + 1
        return m