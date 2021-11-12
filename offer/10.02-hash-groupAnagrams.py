


from typing import Counter


class Solution:
    def groupAnagrams(self, strs) :
        
        def hashIt(s):
            d = dict(Counter(s))
            res = []
            for e in d:
                res.append(e)
            res = sorted(res)
            hashValue = ""
            for e in res:
                hashValue+=str(e)+"@"+str(d[e])
            return hashValue
        
        res = dict()
        for s in strs:
            hashValue = hashIt(s)
            if hashValue not in res:
                res[hashValue] = [s]
            else:
                res[hashValue].append(s)
        result = []
        for e in res:
            result.append(res[e])
        return result
    def groupAnagrams(self, strs) :

        res = dict()
        for s in strs:
            news = sorted([e for e in s])
            hashValue = ""
            for e in news:
                hashValue+=e
            if hashValue not in res:
                res[hashValue] = [s]
            else:
                res[hashValue].append(s)
        result = []
        for e in res:
            result.append(res[e])
        return result
            
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))