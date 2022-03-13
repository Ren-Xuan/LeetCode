class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """节省空间复杂度"""
        if len(s) == 1:
            return 0
        record = 0
        ans = 0
        cnt = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cnt+=1
            else:
                ans +=min(cnt,record)
                #比如11100,能组成的就只有1100 和10,所以是min(3,2)
                record = cnt
                cnt = 1
        ans+=min(cnt,record)
        return ans
    def countBinarySubstrings2(self, s: str) -> int:
        if len(s) == 1:
            return 0
        d = []
        cnt = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cnt+=1
            else:
                d.append(cnt)
                cnt = 1
        d.append(cnt)
        ans = 0
        for i in range(1,len(d)):
            ans+=min(d[i],d[i-1])
            #比如11100,能组成的就只有1100 和10,所以是min(3,2)
        return ans