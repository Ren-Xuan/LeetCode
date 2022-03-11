from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        @cache
        def dfs(x1, y1, x2, y2):
            if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0 or x1 >= n or y1 >= n or x2 >= n or y2 >= n:
                return -float('inf')
            if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                return -float('inf')
            if x1 == n - 1 and y1 == n - 1 and x2 == n - 1 and y2 == n - 1:
                return grid[x1][y1]
            res = 0
            if x1 == x2 and y1 == y2:
                res += grid[x1][y1]
            else:
                res += grid[x1][y1] + grid[x2][y2]
            res += max(dfs(x1+1, y1, x2 + 1, y2), dfs(x1+1, y1, x2, y2+1), dfs(x1, y1+1, x2 + 1, y2), dfs(x1, y1 + 1, x2, y2 + 1))
            return res
        return max(dfs(0, 0, 0, 0), 0)