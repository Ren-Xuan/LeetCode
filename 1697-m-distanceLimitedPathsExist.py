from typing import List


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        f = list(range(n))
        def find(i):
            if f[i]!=i:
                f[i] = find(f[i])
            return f[i]
        
        def union(i, j):
            fi, fj = find(i), find(j)
            f[fj] = fi
        
        edgeList.sort(key=lambda x: x[2])
        q = [(queries[i], i) for i in range(len(queries))]
        q.sort(key=lambda x: x[0][2])
        ans = [False] * len(q)
        k = 0
        for t in q:
            while k < len(edgeList) and edgeList[k][2] < t[0][2]:
                union(edgeList[k][0], edgeList[k][1])
                k += 1
            if find(t[0][0]) == find(t[0][1]):
                ans[t[1]] = True
        return ans 

