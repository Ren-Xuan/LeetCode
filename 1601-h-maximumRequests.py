from typing import List


class Solution:
    def maximumRequests1(self, n: int, requests: List[List[int]]) -> int:
        self.build = [0]*n
        self.origin = [0]*n
        self.ans = 0
        same = 0
        #找那些from==to的人,单独挑出来
        req = []
        for e in requests:
            if e[0] == e[1]:
                same+=1
            else:
                req.append(e)
        for e in requests:
            self.build[e[0]]+=1
            self.origin[e[0]]+=1
        def dfs(avail,surplus):
            if all(e1 == e2 for e1,e2 in zip(self.build,self.origin)):
                self.ans = max(self.ans,len(avail))
            for i,e in enumerate(surplus):
                self.build[e[0]]-=1
                self.build[e[1]]+=1
                dfs(avail+[e],surplus[i+1:])
                self.build[e[0]]+=1
                self.build[e[1]]-=1
        dfs([],req)
        return self.ans+same
    def maximumRequests2(self, n: int, requests: List[List[int]]) -> int:
        self.build = [0]*n
        self.ans = 0
        same = 0
        #找那些from==to的人,单独挑出来
        req = []
        for e in requests:
            if e[0] == e[1]:
                same+=1
            else:
                req.append(e)
        #回溯
        #复杂度n*pow(2,n)
        def dfs(avail,surplus):
            if all(e == 0 for e in self.build):
                self.ans = max(self.ans,avail)
            for i,e in enumerate(surplus):
                self.build[e[0]]-=1
                self.build[e[1]]+=1
                dfs(avail+1,surplus[i+1:])
                self.build[e[0]]+=1
                self.build[e[1]]-=1
        dfs(0,req)
        return self.ans+same
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        same = 0
        req = []
        #二进制枚举
        #复杂度n*pow(2,n)
        for e in requests:
            if e[0] == e[1]:
                same+=1
            else:
                req.append(e)
        for mask in range(1 << len(req)):
            cnt = mask.bit_count()
            if cnt <= ans:
                continue
            delta = [0] * n
            for i, (x, y) in enumerate(req):
                if mask & (1 << i):
                    delta[x] += 1
                    delta[y] -= 1
            if all(x == 0 for x in delta):
                ans = cnt
        return ans+same