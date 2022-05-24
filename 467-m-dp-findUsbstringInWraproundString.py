class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        """
        dp[i] = 以index i 结尾的最长连续字符串长度
        dp[i] = dp[i-1]+1 if (ord(p[i-1])+1)%26 == ord(p[i]) else 1
        找到所有字母为尾的最长连续子串，26个字母最长长度全部相加为结果。
        题目要求不同的子串个数，那么对于两个以同一个字符结尾的子串，长的那个子串必然包含短的那个。
        例如abcd和bcd均以d结尾，bcd是abcd的子串
        对于abcd的符合要求的个数为 d,cd,bcd,abcd

        """
        dp = [0]*len(p)
        dp[0] = 1
        for i in range(1,len(p)):
            dp[i] = dp[i-1]+1 if (ord(p[i-1])+1-ord('a'))%26 == ord(p[i])-ord('a') else 1
        alpha = [0]*26
        for i in range(len(dp)):
            index = ord(p[i])-ord('a')
            alpha[index] = max(alpha[index],dp[i])
        return sum(alpha)