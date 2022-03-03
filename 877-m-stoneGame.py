from functools import lru_cache
from typing import List


class Solution:
    def stoneGame1(self, piles: List[int]) -> bool:
        #dfs算的还是差值(领先的分数)
        # dfs表示player1领先player2的分数
        # player1最大化领先的分数
        # 但是player2采用的负数，因此采用player2最小化领先的分数，
        @lru_cache(None)
        def dfs(l,r,player1):
            if l == r:
                if player1:
                    return piles[l]
                else:
                    return -piles[l]
            if player1:
                return max(dfs(l+1,r,not player1)+piles[l],dfs(l,r-1,not player1)+piles[r])
            else:
                return min(dfs(l+1,r,not player1)-piles[l],dfs(l,r-1,not player1)-piles[r])
        return dfs(0,len(piles)-1,True) >=0
    def stoneGame2(self, piles: List[int]) -> bool:
        """
        dp[l][r]表示当前对手在[l,r]区间内领先了几分，
        假如我选择了piles[l-1]或者piles[r+1]，
        那么我自己和对手的差值就剩piles[l-1] -dp[l][r] 或者piles[r+1]-dp[l][r]
        假如l==r那么就是等于piles[l]这个数，谁选到了l就可以多领先piles[l]分数
        假如piles[l-1] = 10,dp[l][r] = 5,piles[r+1] = 1
        就是说当前对手领先5分，但是我可以选择piles[l-1]或者piles[r+1]
        但是选择piles[l-1]得分可以更大的缩短了与对手的差值
        所以选择piles[l-1]
        归一化的写法：dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        
        然后用三角动态规划
        """
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, num in enumerate(piles):
            dp[i][i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0

    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [0] * length
        for i, pile in enumerate(piles):
            dp[i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[length - 1] > 0

