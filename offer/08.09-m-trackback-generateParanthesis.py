class Solution:
    def generateParenthesis2(self, n: int) :
        """超时解法，主要是递归回溯会遇到很多重复的情况"""
        self.res = set()
        def valid(s):
            return True
            """不必判断是不是符合括号的序列"""
            cur = 0
            for e in s:
                if e == '(':
                    cur+=1
                else:
                    cur-=1
                    if cur<0:
                        return False
            return cur == 0
        def traceback(candidate,n):
            if valid(candidate):
                if n == 1:
                    self.res.add(candidate)
                    return
                
                for i in range(len(candidate)+1):
                    traceback(candidate[:i]+"()"+candidate[i:],n-1)
            return
        traceback("()",n)
        
        return list(self.res)
    def generateParenthesis(self,n:int):
        level = set()
        level.add("()")
        for i in range(n-1):
            nextLevel = set()
            for e in level:
                for i in range(len(e)+1):
                    s = e[:i]+"()"+e[i:]
                    nextLevel.add(s)
            level = nextLevel
        return list(level)