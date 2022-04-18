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

    def mergeStones2(self, stones: List[int], k: int) -> int:
        if (len(stones)-k)%(k-1) != 0: return -1

        pre_sum = [0]
        for n in stones:
            pre_sum.append(pre_sum[-1]+n)
        @lru_cache(None)
        def dfs(l, r):
            if r-l+1 < k:
                return 0
            tmp_sum = pre_sum[r+1] - pre_sum[l] if (r-l) % (k-1) == 0 else 0
            res = float('inf')

            for i in range(l, r, k-1):
                tmp1 = dfs(l,i)
                tmp2 = dfs(i+1,r)
                res = min(res, tmp1 + tmp2 + tmp_sum)
            return res
      
        return dfs(0, len(stones)-1)

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

        for delta in range(1,  n + 1):
            for L in range(1, n + 1 - delta):
                R = L + delta
                for mid in range(L, R, k - 1):
                    dp[L][R] = min(dp[L][R], dp[L][mid] + dp[mid+1][R])
                if delta % (k - 1) == 0:
                    dp[L][R] += (presum[R] - presum[L-1]);

        return dp[1][n]
