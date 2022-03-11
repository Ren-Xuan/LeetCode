from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        direction = [-1,0,1]
        @cache
        def dfs(x1, y1, x2, y2):
            if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0 or x1 >= m or y1 >= n or x2 >= m or y2 >= n:
                return -float('inf')
            if x1 == m - 1  and x2 == m - 1 :
                if y1 == y2:#
                    """
                    这里很重要
                    比如
                    [1,0,1]
                    [0,5,4]
                    如果不加以约束最后会返回错误值
                    """
                    return grid[x1][y1]
                else:
                    return grid[x1][y1]+grid[x2][y2]
            res = 0
            if x1 == x2 and y1 == y2:
                res += grid[x1][y1]
            else:
                res += grid[x1][y1] + grid[x2][y2]
            res += max(dfs(x1+1,y1+dy1,x2+1,y2+dy2)for dy1 in direction for dy2 in direction)
            return res
        return max(dfs(0, 0, 0, n-1),0)