class UFS():
    def __init__(self, N):
        self.p = [i for i in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        ufs = UFS(20000)
        for x,y in stones:
            ufs.union(x,y+10000)
        return len(stones)-len({ufs.find(x) for x,y in stones})