from typing import List


class Solution:
    def stoneGameIII1(self, stoneValue: List[int]) -> str:
        preSum = [0]*(len(stoneValue)+1)
        for i in range(len(stoneValue)):
            preSum[i] = preSum[i-1]+stoneValue[i]
        MAX=10**6
        @lru_cache(None)
        def dfs(l,player1):
            if player1:
                cur = -MAX
                for X in range(1,4):
                    if l+X>len(stoneValue)-1:
                        p = preSum[len(stoneValue)-1]-preSum[l-1]
                        cur = max(cur,p)
                        break
                    p = dfs(l+X,not player1)+preSum[l+X-1]-preSum[l-1]
                    cur = max(cur,p)
                return cur
            else:
                cur = MAX
                for X in range(1,4):
                    if l+X>len(stoneValue)-1:
                        p = -preSum[len(stoneValue)-1]+preSum[l-1]
                        cur = min(cur,p)
                        break
                    p = dfs(l+X,not player1)-preSum[l+X-1]+preSum[l-1]
                    cur = min(cur,p)
                return cur
        sub = dfs(0,True)#player1=True的时候领先的石子个数
        if sub == 0:
            return 'Tie'
        elif sub>0:
            return 'Alice'
        else:
            return 'Bob'

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        suffix_sum = [0] * (n - 1) + [stoneValue[-1]]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]
        
        # 边界情况，当没有石子时，分数为 0
        # 为了代码的可读性，显式声明
        f = [0] * n + [0]
        for i in range(n - 1, -1, -1):
            f[i] = suffix_sum[i] - min(f[i+1:i+4])
        
        total = sum(stoneValue)
        if f[0] * 2 == total:
            return "Tie"
        else:
            return "Alice" if f[0] * 2 > total else "Bob"
