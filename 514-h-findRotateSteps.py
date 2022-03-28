from collections import defaultdict
from functools import lru_cache


class Solution:
    def findRotateSteps1(self, ring: str, key: str) -> int:
        n, m = len(ring), len(key)
        pos = defaultdict(set)
        for idx, s in enumerate(ring):
            pos[s].add(idx)

        @lru_cache(None)
        def dfs(cur: int, i: int):
            """
            cur: 当前12点对应ring上的位置
            i：想要的字母的指针
            """
            if i == m:
                return 0
            res = float('inf')
            for p in pos[key[i]]:
                left = abs(p - cur) + 1 + dfs(p, i + 1)
                right = n - abs(p - cur) + 1 + dfs(p, i + 1)
                res = min(res, left, right)
            return res
        
        return dfs(0, 0)

    def findRotateSteps(self, ring: str, key: str) -> int:
        n=len(ring)
        m=len(key)
        dp=[[float('inf')]*n for _ in range(m)]
        #lookup 统计key中的各字符出现的位置
        lookup=collections.defaultdict(list)
        for i in range(n):
            lookup[ring[i]].append(i)
        #dp 初始化，
        for i in lookup[key[0]]:
            dp[0][i]=min(i,n-i)+1
        
        for i in range(1,m):
            for j in lookup[key[i]]:#key[i]字符出现的位置
                for k in lookup[key[i-1]]:#key[i-1]字符出现的位置
                    #t计算的是上一个字符原本位置是k的被移动到了12:00,
                    #那么当前字符位置是j的距离k的最短距离是多少
                    if j>k:
                        t=min(j-k,n-(j-k))
                    else:
                        t=min(k-j,n-(k-j))
                    dp[i][j]=min(dp[i][j],dp[i-1][k]+1+t)
        return min(dp[-1])            
        
        