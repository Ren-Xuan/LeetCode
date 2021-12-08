from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid

        self.grid2 = [[0 for _ in range(self.n)] for _ in range(self.m)]  #拷贝一份原始的网格，以便比较数字
        for i in range(self.m):
            for j in range(self.n):
                self.grid2[i][j] = self.grid[i][j]

        self.visit = set()   #记录走过的地方
        self.originColor = self.grid[row][col]
        self.targetColor = color
        self.dfs(row, col)
        return self.grid
    
    def dfs(self, row, col):
        count = 0   
        #如果上下左右四个方向的格子都是原始颜色，那么这个格子就不需要改变颜色，反之则改变颜色
        for (x, y) in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
            if 0 <= x < self.m and 0 <= y < self.n and self.grid2[x][y] == self.originColor:
                 count += 1
        if count != 4:
            self.grid[row][col] = self.targetColor

        #往上下左右四个方向找

        self.visit.add((row, col))
        for (x, y) in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
            if (x, y) not in self.visit and 0 <= x < self.m and 0 <= y < self.n and self.grid[x][y] == self.originColor:
                self.dfs(x, y)