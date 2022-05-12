import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if(len1+len2!=len3):
            return False
        """
        我们使用 dp[i][j]dp[i][j] 表示 s_1 的前 i 个字符和 s_2 的前 j 个字符是否能构成 s_3 的前 i+ji+j 个字符。
        首先，dp[0][0] 一定是 True
        

        """
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True
        for i in range(1,len1+1):
            dp[i][0]=(dp[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1,len2+1):
            dp[0][i]=(dp[0][i-1] and s2[i-1]==s3[i-1])
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]


    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        n3=len(s3)
        if n3!=n1+n2:
            return False
        @functools.lru_cache(maxsize=None)
        def dfs(i1, i2):
            i3 = i1 + i2
            if i1 == 0:
                return s3[:i2] == s2[:i2]
            if i2 == 0:
                return s3[:i1] == s1[:i1]
            a = dfs(i1 - 1, i2)
            aa = dfs(i1, i2 - 1)
            return (a and s1[i1-1]==s3[i3-1]) or (aa and s2[i2-1]==s3[i3-1])

        return dfs(n1, n2)