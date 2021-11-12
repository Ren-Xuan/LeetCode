class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s)<=10:
            return []
        arr = []
        for i in range(len(s)-10):
            if s[i:i+10] in s[i+1:]:
                if s[i:i+10] in arr:
                    continue
                arr.append(s[i:i+10])
        return arr
s = Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(s.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))