class Solution:
    def shortestBridge(self, grid) -> int:
        def dfs(grid,i,j,M,N,mark,result):
            if i <0 or i>=M or j<0 or j >=N:
                return 
            if grid[i][j] ==1:
                grid[i][j] = mark
                result.add((i,j))
            else:
                return
            dfs(grid,i-1,j,M,N,mark,result)
            dfs(grid,i+1,j,M,N,mark,result)
            dfs(grid,i,j-1,M,N,mark,result)
            dfs(grid,i,j+1,M,N,mark,result)
        def isValid(i,j,M,N):
            if i <0 or i>=M or j<0 or j >=N:
                return False
            return True
        M = len(grid)
        N = len(grid[0])

        resultOne = set()
        resultTwo = set()
        cnt = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    #找到第一个岛的开始路线
                    if cnt == 0:
                        dfs(grid,i,j,M,N,2,resultOne)
                        cnt+=1
                    elif cnt == 1:
                        dfs(grid,i,j,M,N,3,resultTwo)
                        cnt+=1
                        break
            if cnt==2:
                break
        cnt = -1
        if len(resultOne) >len(resultTwo):
            while len(resultTwo)!=0:
                #print(resultTwo)
                nextLevel = set()
                cnt+=1
                for e in resultTwo:
                    m,n = e[0],e[1]
                    i,j = m-1,n
                    if isValid(i,j,M,N) :
                        if grid[i][j] == 0:
                            nextLevel.add((i,j))
                            grid[i][j] = 1
                        elif grid[i][j] == 2:
                            return cnt
                    i,j = m+1,n
                    if isValid(i,j,M,N) :
                        if grid[i][j] == 0:
                            nextLevel.add((i,j))
                            grid[i][j] = 1
                        elif grid[i][j] == 2:
                            return cnt
                    i,j = m,n-1
                    if isValid(i,j,M,N) :
                        if grid[i][j] == 0:
                            nextLevel.add((i,j))
                            grid[i][j] = 1
                        elif grid[i][j] == 2:
                            return cnt
                    i,j = m,n+1
                    if isValid(i,j,M,N) :
                        if grid[i][j] == 0:
                            nextLevel.add((i,j))
                            grid[i][j] = 1
                        elif grid[i][j] == 2:
                            return cnt
                resultTwo = nextLevel
        else:#cntOne[0] <=cntTwo[0]
            while len(resultOne)!=0:
                #print(resultOne)
                nextLevel = set()
                cnt+=1
                for e in resultOne:
                    m,n = e[0],e[1]
                    i,j = m-1,n
                    if isValid(i,j,M,N) :
                        if grid[i][j] == 0:
                            nextLevel.add((i,j))
                            grid[i][j] = 1
                        elif grid[i][j] == 3:
                            return cnt
                    i,j = m+1,n
                    if isValid(i,j,M,N) :
                        if grid[i][j] == 0:
                            nextLevel.add((i,j))
                            grid[i][j] = 1
                        elif grid[i][j] == 3:
                            return cnt
                    i,j = m,n-1
                    if isValid(i,j,M,N) :
                        if grid[i][j] == 0:
                            nextLevel.add((i,j))
                            grid[i][j] = 1
                        elif grid[i][j] == 3:
                            return cnt
                    i,j = m,n+1
                    if isValid(i,j,M,N) :
                        if grid[i][j] == 0:
                            nextLevel.add((i,j))
                            grid[i][j] = 1
                        elif grid[i][j] == 3:
                            return cnt
                resultOne = nextLevel
        