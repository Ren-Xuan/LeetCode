from functools import lru_cache
from typing import List


class Solution:
    def PredictTheWinner1(self, nums: List[int]) -> bool:
        #计算玩家在区间[l,r]中得分
        #玩家1最大化正分，玩家2最小化负分
        @lru_cache(None)
        def dfs(l,r,player1):
            if l == r:
                if player1:
                    return nums[l]
                else:
                    return -nums[l]
            if player1:
                return max(dfs(l+1,r,not player1)+nums[l],dfs(l,r-1,not player1)+nums[r])
            else:
                return min(dfs(l+1,r,not player1)-nums[l],dfs(l,r-1,not player1)-nums[r])
        return dfs(0,len(nums)-1,True) >=0
    def PredictTheWinner2(self, nums: List[int]) -> bool:
        """ 
        【状态定义】
        dp[i][j]表示在nums坐标[i, j]中，玩家1“先手”时能取到的最多分数。

        【状态转移】
        博弈论中的minmax思想：玩家1为了胜利总取max，玩家2为了阻碍玩家1胜利总取min
        dp[i][j]为以下两种情况的最大值：
        - 状态1： 
            玩家1“先手”取最左端的元素nums[i]，此时剩余元素坐标为[i+1, j]。
            玩家2“后手”为了阻碍玩家1的胜利，即使玩家1的得分最少，要在以下两种状态中取min：
                - 状态1.1：玩家2取元素nums[i+1]，导致在下一轮中玩家1最多得分dp[i+2][j]
                - 状态1.2：玩家2取元素nums[j]，导致在下一轮中玩家1最多得分dp[i+1][j-1]
            状态1 = nums[i] + min(状态1.1, 状态1.2)
        - 状态2： 
            玩家1“先手”取最右端的元素nums[j]，此时剩余元素坐标为[i, j-1]。
            玩家2“后手”为了阻碍玩家1的胜利，即使玩家1的得分最少，要在以下两种状态中取min：
                - 状态2.1：玩家2取元素nums[i]，导致在下一轮中玩家1最多得分dp[i+1][j-1]
                - 状态2.2：玩家2取元素nums[j-1]，导致在下一轮中玩家1最多得分dp[i][j-2]
            状态2 = nums[j] + min(状态2.1, 状态2.2)
        - 取最大值：
            玩家1为了胜利在所有状态中取max
            dp[i][j] = max(状态1，状态2)

        【初始值】
        当nums中只有一个元素时：
            dp[i][i] = nums[i]
        当nums中只有两个元素时：
            dp[i][i+1] = max(nums[i], nums[i+1])

        【返回值】
        玩家1在nums中能取到的最多分数是否大于等于玩家2的分数：
            dp[0][len(nums)-1] >= sum(nums) - dp[0][len(nums)-1]
        即是否大于等于总分数的一半：
            dp[0][len(nums)-1] >= sum(nums)/2
        """
        if not nums: return

        # 初始化
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for i in range(len(nums)-1):
            dp[i][i+1] = max(nums[i], nums[i+1])
        
        # 动态规划，从对角线递推（这里有点绕，可以边画矩阵边填数字）
        for x in range(2, len(nums)):  # 间距（至少相隔两个元素），i ~ i+x
            for i in range(len(nums)-x): # 0 ~ len(num)-x-1
                tmp1 = nums[i] + min(dp[i+2][i+x], dp[i+1][i+x-1]) 
                tmp2 = nums[i+x] + min(dp[i][i+x-2], dp[i+1][i+x-1])
                dp[i][i+x] = max(tmp1, tmp2)
        
        return dp[0][len(nums)-1] >= sum(nums)/2

    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        dp[l][r]表示当前对手在[l,r]区间内领先了几分，
        假如我选择了nums[l-1]或者nums[r+1]，
        那么我自己和对手的差值就剩nums[l-1] -dp[l][r] 或者nums[r+1]-dp[l][r]
        假如l==r那么就是等于nums[l]这个数，谁选到了l就可以多领先nums[l]分数
        假如nums[l-1] = 10,dp[l][r] = 5,nums[r+1] = 1
        就是说当前对手领先5分，但是我可以选择nums[l-1]或者nums[r+1]
        但是选择nums[l-1]得分可以更大的缩短了与对手的差值
        所以选择nums[l-1]
        归一化的写法：dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
        然后用三角动态规划
        """
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0
