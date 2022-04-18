class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        presum = [0] * (n+1)
        for i in range(n):
            presum[i] += presum[i-1] + stoneValue[i]
        if n == 1:
            return 0

        @lru_cache(None)
        def dfs(i, j):
            if j - i == 0:
                return 0
            elif j - i == 1:
                return min(stoneValue[i], stoneValue[j])
            ret = 0
            for k in range(i, j):
                sum1 = presum[k] - presum[i-1]
                sum2 = presum[j] - presum[k]
                if sum1 < sum2:
                    if sum1 + sum1 > ret:#加速
                        ret = max(ret, sum1 + dfs(i, k))
                elif sum1 > sum2:
                    if sum2 + sum2 > ret:
                        ret = max(ret, sum2 + dfs(k+1, j))
                else:
                    ret = max(ret, sum1 + dfs(i, k), sum2 + dfs(k+1, j))
            return ret
        return dfs(0, n-1)