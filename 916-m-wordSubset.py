from typing import DefaultDict, List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        A = [None]*len(words1)
        for i,e in enumerate(words1):
            A[i] = DefaultDict(int)
            for c in e:
                A[i][c]+=1
        B = DefaultDict(int)
        for i,e in enumerate(words2):
            cur = DefaultDict(int)
            for c in e:
                cur[c]+=1
            for e in cur:
                if e in B:
                    if cur[e]>B[e]:
                        B[e] = cur[e]
                else:
                    B[e] = cur[e]
        #print(B)
        result = []
        for i,word in enumerate(words1):
            if all(A[i].get(c,0)>=B[c] for c in B):
                result.append(words1[i])
        return result
