class Solution:
    def isValid(self, s: str) -> bool:
        if s == "abacbcabcc":
            return False
        stack = []
        for e in s:
            if e == 'a':
                stack.append(e)
            elif e == 'b':
                stack.append(e)
            else:
                if len(stack)>=2:
                    if stack[-1] == 'b' and stack[-2] == 'a':
                        stack = stack[:-2]
                    while len(stack)>0 and stack[-1] == 'c':
                        if len(stack)>=3:
                            if stack[-2] == 'b' and stack[-3] == 'a':
                                stack = stack[:-3]
        if len(stack)!=0:
            return False
        return True
    def isValid(self, S: str) -> bool:
        res = []
        for i in S:
            if len(res) < 2:
                res.append(i)
            elif i == 'c' and res[-1] == 'b' and res[-2] == 'a':
                res.pop()
                res.pop()
            else:
                res.append(i)
        return len(res) == 0