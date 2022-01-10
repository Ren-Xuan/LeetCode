class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.ans = False
        n = len(num)
        if n < 2:
            return False
        elif n == 3:
            return int(num[0])+int(num[1]) == int(num[2])

        def traceback(a,b,candidate):
            if self.ans:
                return
            if len(candidate) == 0:
                self.ans = True
            for i in range(1,len(candidate)+1):
                if candidate[0] == '0':
                    return
                c = int(candidate[:i])
                if a+b == c:
                    traceback(b,c,candidate[i:])
        for i in range(1,n-2):
            for j in range(i+1,n-1):
                if num[i] == '0' and j-i != 1:
                    #这里12012情况特殊
                    continue
                if i>=2 and num[0] == '0':
                    continue
                a = int(num[:i])
                b = int(num[i:j])
                traceback(a,b,num[j:])
        
        return self.ans