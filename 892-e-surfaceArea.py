class Solution:
    def surfaceArea0(self, grid: List[List[int]]) -> int:
        n = len(grid)
        s= 0
        updown = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]!=0:
                    updown+=1
                for l in range(1,grid[i][j]+1):
                    cnt = 0
                    for k in [(0,-1),(0,1),(1,0),(-1,0)]:
                        if 0<=i+k[0]<n and 0<=j+k[1]<n:
                            if grid[i+k[0]][j+k[1]] >=l:
                                cnt+=1
                    s+=4-cnt
        return s+updown*2
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans