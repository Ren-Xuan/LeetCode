class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        a = nums
        n = len(a)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        anc = []
        has_anc = [[False]*n for _ in range(n)]
        s = [0]*n
        def _dfs(u, p):
            for v in anc:
                has_anc[u][v] = True
            anc.append(u)
            t = a[u]
            for v in adj[u]:
                if v == p: continue
                t ^= _dfs(v, u)
            s[u] = t
            anc.pop()
            return t
        _dfs(0, 0)

        def _score(*vals):
            return max(vals) - min(vals)

        r = float('inf')
        for u in range(1, n):
            for v in range(1, n):
                if u == v: continue
                if has_anc[u][v]:
                    r = min(r, _score(s[0]^s[v], s[v]^s[u], s[u]))
                elif has_anc[v][u]:
                    r = min(r, _score(s[0]^s[u], s[u]^s[v], s[v]))
                else:
                    r = min(r, _score(s[0]^s[u]^s[v], s[u], s[v]))
        return r