from functools import lru_cache
from typing import List


class Solution:
    def stoneGameII1(self, piles: List[int]) -> int:
        preSum = [0]*(len(piles)+1)
        for i in range(len(piles)):
            preSum[i] = preSum[i-1]+piles[i]
        MAX=10**6
        @lru_cache(None)
        def dfs(l,M,player1):
            if player1:
                cur = -MAX
                for X in range(1,2*M+1):
                    if l+X>len(piles)-1:
                        p = preSum[len(piles)-1]-preSum[l-1]
                        cur = max(cur,p)
                        break
                    p = dfs(l+X,max(X,M),not player1)+preSum[l+X-1]-preSum[l-1]
                    cur = max(cur,p)
                return cur
            else:
                cur = MAX
                for X in range(1,2*M+1):
                    if l+X>len(piles)-1:
                        p = -preSum[len(piles)-1]+preSum[l-1]
                        cur = min(cur,p)
                        break
                    p = dfs(l+X,max(X,M),not player1)-preSum[l+X-1]+preSum[l-1]
                    cur = min(cur,p)
                return cur
        sub = dfs(0,1,True)#player1=True的时候领先的石子个数
        return (preSum[len(piles)-1] + sub)//2

    def stoneGameII2(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i+1]
        @lru_cache(None)
        def f(i, M):
            #当前剩余可选的piles已经小于2*M，所以可以直接选了
            if n - i <= 2 * M:
                return piles[i]
            return max(piles[i] - f(i+j, max(M, j)) for j in range(1, 2*M+1))
        return f(0, 1)

    def stoneGameII(self, piles: List[int]) -> int:
        if len(piles) == 1:
            return piles[0]
        length = len(piles)
        total = 0
        dp = [[0] * (length+1) for _ in range(length+1)]
        for i in range(length - 1, -1, -1):
            total +=piles[i]
            for j in range(1,length):
                if i+j*2 >=length:
                    dp[i][j] = total
                else:
                    dp[i][j] = total - min([dp[i+x][max(x,j)] for x in range(1,2*j+1)])
        return dp[0][1]
