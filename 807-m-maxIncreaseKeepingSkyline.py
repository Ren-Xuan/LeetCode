from typing import List
import copy

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        nroth = [max(e) for e in zip(*grid)]
        west = [max(e) for e in grid]
        #new = copy.deepcopy(grid)
        cnt = 0
        for i in range(n):
            for j in range(n):
                cnt+= min(nroth[j],west[i]) - grid[i][j]
        return cnt
    def maxIncreaseKeepingSkyline2(self, grid):
        m=len(grid)
        n=len(grid[0])
        h=[max(x) for x in grid]
        v=[max([x[j] for x in grid]) for j in range(n)]
        c=0
        for i in range(m):
            for j in range(n):
                c+=min(h[i],v[j])-grid[i][j]
        return c
