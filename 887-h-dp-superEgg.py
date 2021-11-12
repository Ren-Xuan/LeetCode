class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0]*(K+1) for _ in range(N+1)]
        #dp[i][j] 表示在i步用j个鸡蛋可以测出最大层数
        for i in range(1,N+1):
            for j in range(1,K+1):
                dp[i][j] = dp[i-1][j]+dp[i-1][j-1]+1
                if dp[i][j]>=N:
                    return i
        return N
    def superEggDrop3(self, K: int, N: int) -> int:
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            m += 1
            for k in range(K, 0, -1):
                # print(m, k)
                dp[k] = dp[k - 1] + dp[k] + 1
        return m