class Solution:
    def kSimilarity0(self, s1: str, s2: str) -> int:
        """Over time"""
        cnt=[0]
        arr1 = []
        arr2 = []
        for e in s1:
            arr1.append(e)
        for e in s2:
            arr2.append(e)
        m = [99999999]
        def traceBack(path,begin,end,des,cnt,m):
            #print(path,begin,end,des,cnt)
            if path == des:
                if cnt[0]<m[0]:
                    m[0] = cnt[0]
                return True
            for i in range(begin,end):
                if path[i] == path[begin] and i!=begin:
                    continue
                path[i],path[begin] = path[begin],path[i]
                if path[i] != path[begin]:
                    cnt[0]+=1
                traceBack(path,begin+1,end,des,cnt,m)
                path[i],path[begin] = path[begin],path[i]
                if path[i] != path[begin]:
                    cnt[0]-=1
        traceBack(arr1,0,len(s2),arr2,cnt,m)
        return m[0]


    def kSimilarity(self, s1: str, s2: str) -> int:
        cnt=[0]
        arr1 = []
        arr2 = []
        step = 0
        pairs = []
        for a,b in zip(s1,s2):
            if a==b:
                continue
            if (b,a) in pairs:
                """======================mostImportant======================"""
                """======================去重======================"""
                pairs.remove((b,a))
                step += 1
            else:
                pairs.append((a,b))
        for e in pairs:
            arr1.append(e[0])
            arr2.append(e[1])
        #print(arr1)
        m = [99999999]
        def traceBack(path,begin,end,des,cnt,m):
            #print(path,begin,end,des,cnt)
            if path == des:
                if cnt[0]<m[0]:
                    m[0] = cnt[0]
                return True
            for i in range(begin,end):
                """======================去重======================"""
                if path[i] == path[begin] and i!=begin:
                    continue
                """======================去重======================"""
                """======================去重======================"""
                """======================去重======================"""
                """======================去重======================"""
                if path[i]!=des[begin]:
                    continue
                path[i],path[begin] = path[begin],path[i]
                if path[i] != path[begin]:
                    cnt[0]+=1
                traceBack(path,begin+1,end,des,cnt,m)
                path[i],path[begin] = path[begin],path[i]
                if path[i] != path[begin]:
                    cnt[0]-=1
        traceBack(arr1,0,len(arr1),arr2,cnt,m)
        return m[0]+step

s = Solution()

print(s.kSimilarity("abc","bca"))
print(s.kSimilarity("aabc","abca"))
print(s.kSimilarity("abac","baca"))
print(s.kSimilarity("abcdefcb","fedcbacb"))

#print(s.kSimilarity("abccaacceecdeea","bcaacceeccdeaae"))
#print(s.kSimilarity("fffeaacbdbdafcfbbafb","abcbdfafffefabdbbafc"))
print(s.kSimilarity("accbadbbacadcdedaebc","caeacbbacddceacadbbd"))