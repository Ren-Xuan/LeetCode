from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        pacific_visited = set()
        atlantic_visited = set()
        rows, cols = len(heights), len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(x, y, visited):
            if (x, y) in visited:
                return
                
            visited.add((x, y))
            for direction in directions:
                dx, dy = x + direction[0], y + direction[1]
                if 0 <= dx < rows and 0 <= dy < cols and heights[dx][dy] >= heights[x][y]:
                    dfs(dx, dy, visited)

        for row in range(rows):
            dfs(row, 0, pacific_visited)  # 左边
            dfs(row, cols - 1, atlantic_visited) # 右边

        for col in range(cols):
            dfs(0, col, pacific_visited)  # 上边
            dfs(rows - 1, col, atlantic_visited) # 下边

        return list(pacific_visited & atlantic_visited)