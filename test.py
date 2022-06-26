
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i+j == n:
                    if grid[i][j] == 0:
                        
                        print(grid[i][j])
                        return False
                elif grid[i][j] !=0:
                    print(grid[i][j])
                    return False
        return True
s = Solution()
s.checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]])