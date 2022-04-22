class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        if n!=len(t):
            return False
        count = [0]*len(s)
        dic = dict()
        for i in range(n):
            if s[i]!=t[i]:
                diff =  (ord(t[i]) - ord(s[i]))
                if diff<0:
                    count[i] = 26+diff
                else:
                    count[i] = diff
                if count[i] in dic:
                    times = dic[count[i]]
                    dic[count[i]]+=1
                    count[i]+=26*times
                else:
                    dic[count[i]] = 1
                if count[i]>k:
                    return False
        return True

    def canConvertString2(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        if n!=len(t):
            return False
        dic = dict()
        for i in range(n):
            if s[i]!=t[i]:
                diff =  (ord(t[i]) - ord(s[i]))
                if diff<0:
                    diff = 26+diff
                else:
                    diff = diff
                if diff in dic:
                    times = dic[diff]
                    dic[diff]+=1
                    diff+=26*times
                else:
                    dic[diff] = 1
                if diff>k:
                    return False
        return True