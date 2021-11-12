class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        visited = []
        for y in range(len(grid)):
            xArr = []
            for x in range(len(grid[0])):
                xArr.append(0)
            visited.append(xArr)
        visited[0][0] = -1
        def dfs(startX,startY,grid):
            #print(startX,startY,"\n",visited)
            if visited[0][0] == -2:
                return True
            if startX >= len(visited[0]) or startY >=len((visited)):
                return False
            if startX == len(visited[0])-1 and startY == len(visited)-1:
                return True
            val = grid[startY][startX]
            nextX1,nextY1 = 0,0
            nextX2,nextY2 = 0,0
            if val == 1:
                nextX1,nextY1,nextType1 = startX - 1 , startY,[1,4,6]
                nextX2,nextY2,nextType2 = startX + 1 , startY,[1,3,5]
            elif val == 2:
                nextX1,nextY1,nextType1 = startX , startY - 1,[2,3,4]
                nextX2,nextY2,nextType2 = startX , startY + 1,[2,5,6]
            elif val == 3:
                nextX1,nextY1,nextType1 = startX -1 , startY,[1,4,6]
                nextX2,nextY2,nextType2 = startX , startY + 1,[2,5,6]
                #下单元格 y = y+1 ,instead of y - 1
            elif val == 4:
                nextX1,nextY1,nextType1 = startX +1, startY,[1,3,5]
                nextX2,nextY2,nextType2 = startX , startY + 1,[2,5,6]
            elif val == 5:
                nextX1,nextY1,nextType1 = startX -1 , startY,[1,4,6]
                nextX2,nextY2,nextType2 = startX , startY - 1,[2,3,4]
            elif val == 6:
                nextX1,nextY1,nextType1 = startX +1 , startY,[1,3,5]
                nextX2,nextY2,nextType2 = startX , startY - 1 ,[2,3,4]
            #print("next:",nextX1,nextY1,nextType1,"next:",nextX2,nextY2,nextType2)
            if nextX1 < len(visited[0]) and nextX1>=0 and nextY1 < len((visited)) and nextY1 >=0:
                if visited[nextY1][nextX1] ==0:
                    if grid[nextY1][nextX1] in nextType1:
                        visited[nextY1][nextX1] = 1
                        res1 = dfs(nextX1,nextY1,grid)
                        if res1 == True:
                            hasRoad = True
                            #print(hasRoad)
                            visited[0][0] = -2
                            return  True
                        visited[nextY1][nextX1] = 0

            nextX1,nextY1,nextType1 = nextX2,nextY2,nextType2
            if nextX1 < len(visited[0]) and nextX1>=0 and nextY1 < len((visited)) and nextY1 >=0:
                if visited[nextY1][nextX1] ==0:
                    if grid[nextY1][nextX1] in nextType1:
                        visited[nextY1][nextX1] = 1
                        res1 = dfs(nextX1,nextY1,grid)
                        if res1 == True:
                            hasRoad = True
                            #print(hasRoad)
                            visited[0][0] = -2
                            return  True
                        visited[nextY1][nextX1] = 0
            return False
        res = dfs(0,0,grid)
        #print(visited)
        return res

s = Solution()
print(s.hasValidPath([[2,4,3],[6,5,2]]))
print("-"*10)
print(s.hasValidPath([[1,2,1],[1,2,1]]))
print("-"*10)
print(s.hasValidPath([[1,1,2]]))

print("-"*10)
print(s.hasValidPath([[2],[2],[2],[2],[2],[2],[6]]))
print("-"*10)
print(s.hasValidPath([[1,1,1,1,1,1,3]]))
print("-"*10)
print(s.hasValidPath( [[4,1],[6,1]] ))