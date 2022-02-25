from typing import List


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # 0 <= blocked.length <= 200 说明只有这个限制是范围最小的 从这里入手
        # 判断 blocked是不是包住了source or target 由于200个block包住的最大范围是 200*199/2=19900, 我们只需要判断从原点（source or target）走19900步能不能逃出去即可

        # method1 dfs
        def dfs(x, y, target):
            if x==target[0] and y==target[1]:
                return True          
            vis[(x,y)] = 1
            if len(vis)>len(blocked)*(len(blocked)-1)//2:
                return True


            r = False
            path = []
            if x-1>=0 and (x-1, y) not in vis and [x-1, y] not in blocked:
                path.append([x-1,y])
            if x+1<=10**6-1 and (x+1, y) not in vis and [x+1, y] not in blocked:
                path.append([x+1, y])
            if y-1>=0 and (x, y-1) not in vis and [x, y-1] not in blocked:
                path.append([x, y-1])
            if y+1<=10**6-1 and (x, y+1) not in vis and [x, y+1] not in blocked:
                path.append([x, y+1])
            path.sort(key = lambda x : (x[0]-target[0])**2 + (x[1] - target[1])**2)
            for e in (path):#想用A*算法，但是好像没什么用
                r = r or dfs(e[0],e[1],target)
            return r
        vis = {}
        res1 = dfs(source[0], source[1], target)
        vis = {}
        res2 = dfs(target[0], target[1], source)
        if res1 and res2:
            return True
        else:
            return False
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        骚解法，适合于blocked的长度没有限制的时候，时间复杂度不解
        """
        if len(blocked) == True:
            return True
        self.dir = [[0,1],[1,0],[0,-1],[-1,0]]
        self.visited = set()
        self.visited.add((source[0],source[1]))
        self.rowDict = dict()
        for e in blocked:
            if e[0] not in self.rowDict:
                self.rowDict[e[0]] = []
            self.rowDict[e[0]].append(e[1])
        self.colDict = dict()
        for e in blocked:
            if e[1] not in self.colDict:
                self.colDict[e[1]] = []
            self.colDict[e[1]].append(e[0])
        for e in self.rowDict:
            self.rowDict[e].sort()
        for e in self.colDict:
            self.colDict[e].sort()
        self.blockedDic = set()
        self.ans = False
        for e in blocked:
            self.blockedDic.add((e[0],e[1]))
        n = 10**6
        def dfs(r,c,blocked = blocked,target = target,n = n):
            if self.ans:
                return
            #print(r,c)
            if r >=n or c >= n:
                return
            elif r<0 or c < 0:
                return
            if r == target[0] and c == target[1]:
                self.ans = True
            path = []
            if r in self.rowDict:
                if c < self.rowDict[r][0]:
                    p = (r,self.rowDict[r][0]-1)
                    if p not in self.visited: 
                        path.append(p)
                        self.visited.add(p)
                elif c > self.rowDict[r][-1]:
                    p = (r,self.rowDict[r][-1]+1)
                    if p not in self.visited:
                        self.visited.add(p)
                        path.append(p)
                else:
                    for i in range(1,len(self.rowDict[r])):
                        if self.rowDict[r][i-1] <c < self.rowDict[r][i]:
                            p = (r,self.rowDict[r][i-1]+1)
                            if p not in self.visited:
                                self.visited.add(p)
                                path.append(p)
                            p = (r,self.rowDict[r][i]-1)
                            if p not in self.visited:
                                self.visited.add(p)
                                path.append(p)
                            break
            else:
                p = (r,target[1])
                if p not in self.visited:
                    self.visited.add(p)
                    path.append(p)
            if c in self.colDict:
                if r < self.colDict[c][0]:
                    p =(self.colDict[c][0]-1,c)
                    if p not in self.visited:
                        self.visited.add(p)
                        path.append(p)
                elif r > self.colDict[c][-1]:
                    p = (self.colDict[c][-1]+1,c)
                    if p not in self.visited:
                        self.visited.add(p)
                        path.append(p)
                else:
                    for i in range(1,len(self.colDict[c])):
                        if self.colDict[c][i-1]<r<self.colDict[c][i]:
                            p = (self.colDict[c][i-1]+1,c)
                            if p not in self.visited:
                                self.visited.add(p)
                                path.append(p)
                            p = (self.colDict[c][i]-1,c)
                            if p not in self.visited:
                                self.visited.add(p)
                                path.append(p)
                            break
            else:
                p = (target[0],c)
                if p not in self.visited:
                    self.visited.add(p)
                    path.append(p)
            for i,j in self.dir:
                if 0<=r+i<n and 0<=c+j<n:
                    p = (r+i,c+j)
                    if p not in self.blockedDic:
                        if p not in self.visited:
                            path.append(p)
                            self.visited.add(p)
            if len(path) == 0:
                return
            path.sort(key = lambda r : (target[0] - r[0])**2 + (target[1] - r[1])**2)
            for e in path:
                #print(e[0],e[1])
                dfs(e[0],e[1])
        dfs(source[0],source[1])
        return self.ans