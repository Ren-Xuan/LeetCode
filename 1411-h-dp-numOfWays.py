class Solution:
    def numOfWays1(self, n: int) -> int:
        mod = 10**9 + 7
        # 预处理出所有满足条件的 type
        types = list()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k:
                        # 只要相邻的颜色不相同就行
                        # 将其以十进制的形式存储
                        types.append(i * 9 + j * 3 + k)
        type_cnt = len(types)
        # 预处理出所有可以作为相邻行的 type 对
        related = [[0] * type_cnt for _ in range(type_cnt)]
        for i, ti in enumerate(types):
            # 得到 types[i] 三个位置的颜色
            x1, x2, x3 = ti // 9, ti // 3 % 3, ti % 3
            for j, tj in enumerate(types):
                # 得到 types[j] 三个位置的颜色
                y1, y2, y3 = tj // 9, tj // 3 % 3, tj % 3
                # 对应位置不同色，才能作为相邻的行
                if x1 != y1 and x2 != y2 and x3 != y3:
                    related[i][j] = 1
        # 递推数组
        f = [[0] * type_cnt for _ in range(n + 1)]
        # 边界情况，第一行可以使用任何 type
        f[1] = [1] * type_cnt
        for i in range(2, n + 1):
            for j in range(type_cnt):
                for k in range(type_cnt):
                    # f[i][j] 等于所有 f[i - 1][k] 的和
                    # 其中 k 和 j 可以作为相邻的行
                    if related[k][j]:
                        f[i][j] += f[i - 1][k]
                        f[i][j] %= mod
        # 最终所有的 f[n][...] 之和即为答案
        ans = sum(f[n]) % mod
        return ans


    def numOfWays(self, n: int) -> int:
        """
        在第一层可以摆出6个ABA类型的和6个ABC类型的涂法。
        对于下面每一层，每一个ABA涂法可以拼接2个ABC涂法和3个ABA涂法，每一个ABC涂法可以拼接2个ABC涂法和2个ABA涂法。
        这样迭代可以算出第N层有几种ABA涂法和ABC涂法，相加就是答案。
        """
        aba=6
        abc=6

        for i in range(2,n+1):
            tmp=aba
            aba=abc*2+aba*3
            abc=abc*2+tmp*2
        
        
        return (aba+abc) %(10**9+7)