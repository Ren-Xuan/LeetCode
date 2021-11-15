class Solution:
    def splitString(self, s: str) -> bool:
        self.s = s
        self.flag = False
        def val(s):
            for i,e in enumerate(s):
                if e == 0:
                    i+=1
                else:
                    s = s[i:]
                    break
            return int(s)
        def dfs(pre,start,n,p):
            if start >= n and p:
                self.flag = True
                return
            for i in range(start,n):
                if pre - 1 == val(self.s[start:i+1]):
                    dfs(pre-1,i+1,n,True)
                elif pre ==-2:
                    dfs(val(self.s[start:i+1]),i+1,n,False)
        dfs(-2,0,len(s),False)
        return self.flag