from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        singleDic = set()
        visited = set()
        l = -1
        for e in intervals:
            if e[0] == e[1]:
                singleDic.add(e[0])
            if e[1]>l:
                l = e[1]
        arr = [0]*(l+1)
        for e in intervals:
            arr[e[0]]+=1
            arr[e[1]]-=1
        ans = []
        start = -1
        end = -1
        cur = 0
        cnt = False
        for i in range(len(arr)):
            cur+=arr[i]
            if cur!=0 and not cnt:
                start = i
                cnt = True
            if cnt:
                visited.add(i)
            if cur == 0 and cnt:
                end = i
                ans.append([start,end])
                start = -1
                end = -1
                cnt = False
        for e in singleDic:
            if e not in visited:
                ans.append([e,e])
        return ans