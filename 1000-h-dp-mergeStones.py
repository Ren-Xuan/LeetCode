from functools import lru_cache
from typing import List


class Solution:
    def mergeStones1(self, stones: List[int], k: int) -> int:
        #超时版本
        n = len(stones)
        if n == 1:
            return 0
        @lru_cache(None)
        def dfs(arr):
            if len(arr)<k:
                return 1e9
            elif len(arr) == k:
                return sum(arr)
            elif len(arr) == 0:
                return 0
            else:
                ret = 1e8
                for mid in range(0,len(arr)-k+1):
                    curSum = sum(arr[mid:mid+k])
                    ret = min(ret,dfs(tuple(arr[:mid]+(curSum,)+arr[mid+k:]))+curSum)
                return ret
        ret  = dfs(tuple(stones))
        return -1 if ret>10000000 else  ret

    def mergeStones1(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0: return -1
        dp = [[0]*n for _ in range(n)]
        preSum = [0]*(n+1)
        for x in range(len(stones)):
            preSum[x] = stones[x] + preSum[x-1]
        def dfs(i,j):
            if j< i+k-1:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            result = float("inf")
            for x in range(i,j,k-1):
                result = min(result,dfs(i,x) + dfs(x+1,j))
            if (j-i) % (k - 1) == 0:
                result += preSum[j]-preSum[i-1]
            dp[i][j] = result
            return dp[i][j]
        ans = dfs(0,n-1)
        #print(dp)
        return ans
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1) % (k-1) != 0:
            return -1
        presum = [0 for _ in range(n +1)]
        for i in range(n):
            presum[i+1] = presum[i] + stones[i]

        dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][i] = 0
        # dp[i][i] 代表区间内可以最大限度合并的最小成本
        for delta in range(1,  n + 1):
            for L in range(1, n + 1 - delta):
                R = L + delta
                for mid in range(L, R, k - 1):
                    dp[L][R] = min(dp[L][R], dp[L][mid] + dp[mid+1][R])
                if delta % (k - 1) == 0:
                    dp[L][R] += (presum[R] - presum[L-1])

        return dp[1][n]
