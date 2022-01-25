from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        cur = 0
        ans = 0
        nextPoint = dict()
        first = False
        second = False
        for a,b in edges:
            if a not in nextPoint:
                nextPoint[a] = set()
            if b not in nextPoint:
                nextPoint[b] = set()
            nextPoint[a].add(b)
            nextPoint[b].add(a)
        visited = [0]*(n+1)
        level = set()
        level.add(1)
        visited[1]+=1
        #除去最后一个n，其他的都不能访问两次以上
        while len(level)!=0:
            #print(level)
            nextLevel = set()
            for e in level:
                for i in nextPoint[e]:
                    if i ==n and not first :
                        first = True
                    if visited[i]<=2:
                        visited[i]+=1
                    else:
                        continue
                    nextLevel.add(i)
            #arrive
            cur+=time
            if first and not second:
                second = True
                first = False
            elif first and second:
                return cur
            #leave
            if cur//change%2 != 0:
                cur = (cur//change+1)*change
            level = nextLevel
        return cur