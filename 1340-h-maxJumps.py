from typing import List


class Solution:
    def maxJumps2(self, arr: List[int], d: int) -> int:
        """
        拓扑排序，但是java能过，python会超时
        """
        n = len(arr)
        graph = [[] for _ in range(n)]
        inDegree = [0]*n
        for i in range(n):
            for k in range(i-d,i+d+1):
                #注意这里要break；因为发现了某个k有arr[k]>arr[i]，则不能翻过arr[k]所以要break
                for k in range(i+1,i+d+1):
                    if k>=n or arr[k]>=arr[i]:
                        break
                    graph[i].append(k)
                    inDegree[k]+=1
                for k in range(i-1,i-d-1,-1):
                    if k<0 or arr[k]>=arr[i]:
                        break
                    graph[i].append(k)
                    inDegree[k]+=1
        #print(inDegree)
        depth = [0]*n
        q = []
        for i in range(n):
            if inDegree[i] ==0:
                depth[i] = 1
                q.append(i)
        while len(q)>0:
            i = q.pop(0)
            for k in graph[i]:
                inDegree[k]-=1
                if inDegree[k] == 0:
                    q.append(k)
                    depth[k] = depth[i]+1
        return max(depth)

    def maxJumps(self, arr: List[int], d: int) -> int:
        seen = dict()

        def dfs(pos):
            if pos in seen:
                return
            seen[pos] = 1

            i = pos - 1
            while i >= 0 and pos - i <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i -= 1
            i = pos + 1
            while i < len(arr) and i - pos <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i += 1
        for i in range(len(arr)):
            dfs(i)
        return max(seen.values())
    def maxJumps(self, arr: List[int], d: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def jump(index):
            left = max(0, index - d)
            right = min(len(arr) - 1, index + d)
            res = 0
            for i in range(index + 1, right + 1):
                if arr[i] < arr[index]:
                    res = max(res, jump(i))
                else: break
            for i in range(index - 1, left - 1, -1):
                if arr[i] < arr[index]:
                    res = max(res, jump(i))
                else: break
            return 1 + res
        res = 0
        for i in range(len(arr)):
            res = max(res, jump(i))
        return res
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        """
        1 stack是一个单调下降栈(基于元素值), 里面存的是下标, 不是元素值
        为什么是单调下降?
        比如柱子a和柱子b, a在左边, b在右边, 并且a的高度 < b的高度.
        如果右边来了一根柱子c, c的高度 > b的高度, 那么肯定是优先从c跳到b, 再从b跳到a.
        理由:

        因为b距离c更近, 如果c能够跳到a的话, 肯定也能够跳到b, 反之, 如果c能够跳到a, 就不一定
        能够跳到b了
        从c先跳到b, 比从c先跳到a可能多跳一下.
        a和b比较起来, 全面占了劣势, 因此, a被b淘汰.
        这就是证明了为什么stack设计为一个单调下降栈.

        2 dp是每根柱子的最多访问下标个数, 使用的是刷表法(元素值可能会多次更新)

        3 L是为了能够批量处理stack中的相同值的元素, 为什么要批量处理呢?
        为了保证在j左边, 并且比arr[j]大的元素, 能够更新dp值.

        
        """
        # 在最右侧添加一个无穷大高的柱子, 目的是为了让原先的元素全部出栈
        dp = [1] * (n + 1) 
        stack = []
        for i, a in enumerate(arr + [float("inf")]):
            while stack and arr[stack[-1]] < a:
                L = [stack.pop()]
                while stack and arr[stack[-1]] == arr[L[0]]:
                    L.append(stack.pop())
                for j in L:
                    # j被弹出来的时候, 更新右边i的dp
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                        
                    # j被弹出来的时候, 更新左边的元素的dp
                    if stack and j - stack[-1] <= d:
                        # 为什么只更新了stack[-1]的dp? stack[-2]以及更左边的dp, 怎么办?
                        # 不用担心, 当stack[-1]被弹出里的时候, 会更新stack[-2]的dp.
                        # stack[-2]被弹出来的时候, 会更新stack[-3]
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
            stack.append(i)
        return max(dp[:-1])

