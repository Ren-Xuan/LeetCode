import heapq
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        num2position = {}
        to_search = []
        for y in range(len(forest)):
            for x in range(len(forest[0])):
                if forest[y][x] and forest[y][x] != 1:
                    num2position[forest[y][x]] = (y, x)
                    to_search.append(forest[y][x])
        to_search.sort()
        curr = (0, 0)
        ans = 0

        for target in to_search:
            dst = num2position[target]
            g = 0   # 从src到curr的距离 g
            y, x= curr
            visited = {}
            visited[curr] = -1
            prior_queue = []    # 优先f最小的，其次h最小的

            # 开始A*
            while curr != dst:   # 没到目的地
                for next_y, next_x in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                    if 0<=next_y<len(forest) and 0<=next_x<len(forest[0]) and forest[next_y][next_x] and visited.get((next_y, next_x), 10000) > g+1:  # 没来过或者需要更新g
                        h = abs(next_y-dst[0]) + abs(next_x-dst[1])   # 曼哈顿距离
                        f = g+1+h   # src到这个点的距离为g+1, dst到这个点的估计距离为h
                        visited[(next_y, next_x)] = g+1
                        heapq.heappush(prior_queue, (f, h, (next_y, next_x)))
                        
                if not prior_queue:
                    return -1
                new = heapq.heappop(prior_queue)
                g = new[0] - new[1]     # g = f-h
                curr = new[2]
                visited[curr] = -1    #不需要更新
                y, x = curr

            ans += g
        return ans