class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sDict = dict()
        tDict = dict()
        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]] = sDict[s[i]]+1
            else:
                sDict[s[i]] = 1

            if t[i] in tDict:
                tDict[t[i]] = tDict[t[i]]+1
            else:
                tDict[t[i]] = 1

        return sDict == tDict

solution = Solution()
s = "anagram"
t = "nagaram"
print(solution.isAnagram(s,t))
s = "anagram"
t = "nagacam"
print(solution.isAnagram(s,t))