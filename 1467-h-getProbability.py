from typing import List


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        # 球数， 颜色数
        n, c = sum(balls), len(balls)
        
        # 总方案数
        self.k = 0
        
        # 取到第i种球，1盒球数, 1盒颜色数, 2盒球数，2盒颜色数，方案数
        #@lru_cache(None) 
        def dfs(i, m1, c1, m2, c2, k):
            # 剪枝
            if m1 > n//2 or m2 > n//2:
                return 
            if i == c:
                if m1 == m2 and c1 == c2 :
                    self.k += k
                return     
            for dm in range(balls[i]+1):     
                dfs(i+1, m1 + dm, c1 + (dm != 0), m2 + balls[i] - dm, c2 + (dm != balls[i]), k*comb(balls[i], dm))
                
        dfs(0, 0, 0, 0, 0, 1)        
        return self.k/comb(n, n//2)