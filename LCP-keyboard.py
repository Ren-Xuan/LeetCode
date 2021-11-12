class Solution:
    def keyboard(self, K: int, N: int) -> int:
        mod = 1000000007
        C = [[0] * (N + 1) for _ in range(N + 1)]
        for m in range(N + 1):
            for n in range(m + 1):
                if n == 0 or n == m:
                    C[m][n] = 1
                else:
                    C[m][n] = (C[m - 1][n - 1] + C[m - 1][n]) % mod
        dp = [[0] * (N + 1) for _ in range(26)]
        for i in range(26):
            for n in range(N + 1):
                if n == 0:
                    dp[i][n] = 1
                elif i == 0:
                    if K >= n:
                        dp[i][n] = 1
                else:
                    for k in range(min(K + 1, n + 1)):
                        dp[i][n] = (dp[i][n] + C[n][k] * dp[i - 1][n - k]) % mod
        # print(dp)
        return dp[25][N]

    """
    dp[i][j] 表示使用 i 个字母，填充长度为 j 的序列，有多少种方法
    使用 dp[i-1][j-c] * combination(j, c) 的累加和来更新 dp[i][j]
    看少用一个字母的情况
    j 个空里取出 c 个来，用于填第 i 个字母


    """

    def keyboard(self, k: int, n: int) -> int:
        # 需要看多重背包，看闫氏DP分析法
        import math
        dp = [0]*(n+1)
        dp[0]=1
        c = lambda m,n:math.factorial(n)//(math.factorial(m)*math.factorial(n-m))
        for i in range(26):
            # 遍历背包容量，从大到小
            for j in range(n,0,-1):
                # 当前字母放入x个
                for x in range(1,k+1):
                    if x>j:
                        continue
                    # 每个dp[j-x]都表示之前已经填充了j-x的方案数，由于是按照每个字母顺序的方式，因此不会出现字母重复选择冲突情况
                    # c(x,j) 可以算出来x个字母填入j个空位的方案数，因为dp[j-x]已经把j-x个空位填满了，因此多出的x的这部
                    # 填充时可以先占据j个空位之中的x个，然后再将其他的字母放入到j-x个空位中
                    dp[j]+= c(x,j)*dp[j-x]
        return dp[-1]%1000000007
