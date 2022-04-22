from typing import List


class Solution:
    def maxSatisfaction1(self, satisfaction: List[int]) -> int:
        import functools
        satisfaction.sort()
        
        @functools.lru_cache(None)
        def dfs(i, cur):
            if i == len(satisfaction):
                return 0
            return max(dfs(i + 1, cur), satisfaction[i] * cur + dfs(i + 1, cur + 1))
        
        return dfs(0, 1)

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        以示例1（satisfaction = [-1,-8,0,5,-9]）为例：
        排序后：satisfaction = [-9,-8,-1,0,5]
        会有如下几个值：
        5×1=5
        5×2+0×1=10
        5×3+0×2+(-1)×1=14
        5×4+0×3+(-1)×2+(-8)×1=10
        5×5+0×4+(-1)×3+(-8)×2+(-9)×1=-3
        最后取最大值，为14。
        """
        satisfaction.sort(reverse=True)
        ans, s = 0, 0
        for num in satisfaction:
            s += num
            if s > 0:
                ans += s
        return ans

