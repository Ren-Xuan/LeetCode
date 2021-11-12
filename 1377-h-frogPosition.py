class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        visited = [False]*(n+1)
        visited[1]=True
        self.endPos = [[0]*(n+1) for _ in range(t+1)]
        self.end = -1
        pro = [1]*(n+1)
        pro[1] = 1
        g = dict()
        for e in edges:
            if e[0] not in g:
                g[e[0]] = [e[1]]
            else:
                g[e[0]].append(e[1])
            if e[1] not in g:
                g[e[1]] = [e[0]]
            else:
                g[e[1]].append(e[0])
        def bfs(start,g,pro,visited,target,T,t):
            if T >t:
                return
            cnt = 0
            vis = []
            for e in g[start]:
                if not visited[e]:
                    vis.append(e)
                    cnt+=1
                    self.endPos[T].append(e)
            #print(vis)
            if cnt == 0:#No way to visit
                self.endPos[T].append(start)
                visited[start] = False
                bfs(start,g,pro,visited,target,T+1,t)
                return
            for e in g[start]:
                if not visited[e]:
                    pro[e] = pro[start]*cnt
                    visited[e] = True
                    bfs(e,g,pro,visited,target,T+1,t)
        bfs(1,g,pro,visited,target,0,t)

        #print("visited")
        #print(self.endPos)
        if target not in self.endPos[t]:
            return 0.0
        return 1/pro[target]
"""
8
[[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]]
7
7

1
2\4\5\7
3\6\5\8
答案0.0

10
[[2,1],[3,2],[4,2],[5,2],[6,5],[7,1],[8,3],[9,1],[10,1]]
1
9

1
2 \7 \9 \10
3 4 5\ 7\ 9 \ 10 
答案0.25
7
[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
20
6

1
2\3\7
4 6\5\7
答案0.16667
"""