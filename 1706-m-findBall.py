from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        ans = [None]*n
        for i in range(n):
            posCol = i
            for r in range(m):
                if grid[r][posCol] == 1:
                    if posCol+1 == n or grid[r][posCol+1] == -1 :
                        ans[i] = -1
                        break
                    else:
                        if r == m-1:
                            ans[i] = posCol+1
                            break
                        else:
                            posCol +=1
                elif grid[r][posCol] == -1:
                    if posCol-1 == -1 or grid[r][posCol-1] == 1 :
                        ans[i] = -1
                        break
                    else:
                        if r == m-1:
                            ans[i] = posCol-1
                            break
                        else:
                            posCol-=1
        return ans