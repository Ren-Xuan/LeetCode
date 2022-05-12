import collections
from typing import List


class Solution(object):
    def minSwapsCouples1(self, row):
        """
        每两个座位成一对，假定左边的人都是合法的不变，如果TA右边的人与TA匹配则
        跳过，不匹配则找到TA的匹配对象的与TA右边的人交换。
        """
        def find_another(n):
            if n % 2 == 0:
                return n + 1
            else:
                return n - 1

        c = 0
        for i in range(0, len(row), 2):
            p1 = row[i]
            p2 = find_another(p1)
            if row[i+1] != p2:
                j = row.index(p2)
                row[i+1], row[j] = row[j], row[i+1]
                c += 1

        return c

    """"
    首先，我们总是以「情侣对」为单位进行设想：

    当有两对情侣相互坐错了位置，ta们两对之间形成了一个环。需要进行一次交换，使得每队情侣独立（相互牵手）

    如果三对情侣相互坐错了位置，ta们三对之间形成了一个环，需要进行两次交换，使得每队情侣独立（相互牵手）

    如果四对情侣相互坐错了位置，ta们四对之间形成了一个环，需要进行三次交换，使得每队情侣独立（相互牵手）

    也就是说，如果我们有 k 对情侣形成了错误环，需要交换 k - 1 次才能让情侣牵手。


    """
    def minSwapsCouples2(self, row: List[int]) -> int:
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # def union(x, y):    # 普通union
        #     parent[find(x)] = find(y)     # 简单地将x的父节点并到y的父节点上

        def union(x, y):    # 按照秩次union
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return

            if rank[rootx] <= rank[rooty]:
                parent[rootx] = rooty
                rank[rooty] += rank[rootx]
            else:
                parent[rooty] = rootx
                rank[rootx] += rank[rooty]
        
        
        
        n = len(row)
        m = n // 2
        parent = [0] * m
        for i in range(m):
            parent[i] = i
        
        rank = [1] * m      # 初始时刻，每个集合大小为1

        for i in range(0,n,2):
            union(row[i] // 2, row[i+1] // 2)   # 构造连通片
        
        cnt = 0             
        for i in range(m):
            if parent[i] == i:
                cnt += 1
        
        return m - cnt


    def minSwapsCouples2(self, row: List[int]) -> int:
        
        n = len(row)
        m = n//2
        
        graph = [[] * m for _ in range(m)]
        for i in range(0, n, 2):
            u = row[i] // 2
            v = row[i+1] // 2
            if u!=v:#这里可加可不加
                graph[u].append(v)  # 无向图【或者认为是双向图】
                graph[v].append(u)
        
        visited = [False] * m
        
        cnt = 0
        for i in range(m):
            if visited[i]:
                continue
            deque = collections.deque([i])
            visited[i] = True
            while deque:
                u = deque.popleft()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        deque.append(v)
            cnt += 1
        
        return m - cnt

    def minSwapsCouples(self, row: List[int]) -> int:
        
        n = len(row)
        m = n//2
        
        graph = [[] * m for _ in range(m)]
        for i in range(0, n, 2):
            u = row[i] // 2
            v = row[i+1] // 2
            if u!=v:#这里可加可不加
                graph[u].append(v)  # 无向图【或者认为是双向图】
                graph[v].append(u)
        
        visited = [False] * m
        
        cnt = 0
        for i in range(m):
            if visited[i]:
                continue
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            cnt += 1
        
        return m - cnt
