class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        d = [0]*(n+1)
        d[1] = "1"
        d[2] = "11"
        def _countAndSay(arr):
            s = arr[0]
            res = ""
            cnt = 0
            for i,c in enumerate(arr):
                if s==c:
                    cnt+=1
                    s = c
                if i!=len(arr)-1 and arr[i+1]!=c:
                        res+=str(cnt)
                        res+=c
                        s = arr[i+1]
                        cnt = 0
            res+=str(cnt)
            res+=arr[-1]
            return res

        for i in range(3,n+1):
            d[i] = _countAndSay(d[i-1])
        
        return d[-1]

s = Solution()
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
print(s.countAndSay(6))
print(s.countAndSay(7))