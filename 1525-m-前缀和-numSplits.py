from collections import defaultdict


class Solution:
    def numSplits(self, s: str) -> int:
        leftdict = defaultdict(int)
        rightdict = defaultdict(int)
        for e in s:
            rightdict[e]+=1
        cnt = 0
        def check(leftdict,rightdict):
            tot = 0
            for e in leftdict:
                if leftdict[e]!=0:
                    tot+=1
            for e in rightdict:
                if rightdict[e]!=0:
                    tot-=1
            return tot == 0
        for i in range(0,len(s)):
            leftdict[s[i]]+=1
            rightdict[s[i]]-=1
            if check(leftdict,rightdict):
                cnt+=1
        return cnt