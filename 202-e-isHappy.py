class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        def happy(n,cnt,d):
            if n in d:
                return -1
            else:
                d.add(n)
            if n == 0:
                return -1
            elif n == 1:
                return 1
            else:
                s = 0
                while n!=0:
                    s += (n%10)**2
                    n = n//10
                return happy(s,cnt+1,d)
        if happy(n,0,d)==1:
            return True
        else:
            return False
