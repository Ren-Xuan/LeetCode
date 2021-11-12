class DSU:
    def __init__(self,n: int):
        self.p = [i for i in range(n)]
    
    def find(self,x: int) -> int:
        if x != self.p[x]: self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def merge(self,x: int,y: int):
        rx , ry = self.find(x) , self.find(y)
        if rx == ry: return 
        self.p[rx] = ry
        return 


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n+1)
        for i in range(1,n+1):
            for j in range(1,i):
                if i % j == 0 and j > threshold:
                    dsu.merge(j,i)
        m = len(queries)
        res = []
        for a, b in queries:
            res.append(dsu.find(a) == dsu.find(b))
        return res