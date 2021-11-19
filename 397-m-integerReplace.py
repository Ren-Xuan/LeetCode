class Solution:
    def integerReplacement0(self, n: int) -> int:
        if n==1:
            return 0
        else:
            if n%2==0:
                return 1+self.integerReplacement(n//2)
            else:
                return 1+min(self.integerReplacement(n+1),self.integerReplacement(n-1))
    def integerReplacement(self, n: int) -> int:
        ans=0
        # 奇数的话要么上要么下
        # 有两条路径可以走
        # 时间复杂度非常之高
        while n!=1:
            ans+=1
            if n&1==0:
                n>>=1
            else:
                if (n+1)%4==0 and n>4:
                    n+=1
                else:
                    n-=1
        return ans
    