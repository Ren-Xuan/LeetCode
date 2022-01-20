import heapq
class Union():
    def __init__(self, n):
        self.n = n
        self.rank = [1]*n
        self.parent = list(range(n))
    def find(self, x):
        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def merge(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri == rj: return False  # 已经加入mst
        if self.rank[ri] < self.rank[rj]:
            ri, rj = rj, ri
        self.rank[ri] += self.rank[rj]
        self.parent[rj] = ri
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 没用并查集 把所有结点全部连通然后用prim算法
        graph = defaultdict(set)
        rank = defaultdict(dict)
        for i in range(len(points)):
            for j in range(len(points)):
                if j == i: continue
                graph[i].add(j)
                rank[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        n = len(points)
        shortest = {}
        visit = set()
        for i in range(1, n):
            shortest[i] = rank[0][i]
        ans = 0
        shortest[0] = 0
        while shortest:
            src = min(shortest, key=shortest.get)
            ans += shortest[src]
            visit.add(src)
            for v in graph[src]:
                if v not in visit:
                    if rank[src][v] < shortest[v]:
                        shortest[v] = rank[src][v]
            shortest.pop(src)
        return ans

        # prim 优化 不用构建边
        n = len(points)
        mst = set()
        convert = lambda x, y : abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        nodes = set(range(n))
        shorest = []
        heappush(shorest, (0, 0)) # (dis,src)
        ans = 0
        while nodes:
            dis, src = heappop(shorest)
            if src in mst: continue
            mst.add(src)
            ans += dis
            nodes.remove(src)
            for node in nodes:
                heappush(shorest, (convert(src, node), node))
        return ans

        # 并查集
        convert = lambda x, y : abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        n = len(points)
        un = Union(n)
        graph = []
        for i in range(n):
            for j in range(i+1, n):
                graph.append((convert(i, j), i, j))
        graph.sort(key=lambda x: x[0])
        ans = 0
        count = 1
        for dis, u, v in graph:
            if un.merge(u, v):
                ans += dis
                count += 1
            if count == n: break
        return ans
