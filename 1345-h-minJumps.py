from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        d = dict()
        for i,e in enumerate(arr):
            if e not in d:
                d[e] = []
            if i == 0 or i == n-1:
                d[e].append(i)
             # 连续出现相同值的区间只保留左右两个端点，起到搜索剪枝的作用
            elif arr[i-1]!= arr[i] or arr[i+1]!=arr[i]:
                d[e].append(i)
        visited = [False]*n
        level = set()
        cnt = 0
        level.add(0)
        visited[0] = True
        while True:
            cnt+=1
            nextlevel = set()
            for idx in level:
                for i in d[arr[idx]]:
                    if i == n-1:
                        return cnt
                    if not visited[i]:
                        nextlevel.add(i)
                        visited[i] = True
                d[arr[idx]] = []
                if idx+1<n and not visited[idx+1]:
                    if idx+1 == n-1:
                        return cnt
                    nextlevel.add(idx+1)
                    visited[idx+1] = True
                if idx-1>=0 and not visited[idx-1]:
                    if idx-1 == n-1:
                        return cnt
                    nextlevel.add(idx-1)
                    visited[idx-1] = True
            level = nextlevel
