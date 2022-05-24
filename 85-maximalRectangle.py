class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        每一层看作是柱状图，可以套用84题柱状图的最大面积。

        第一层柱状图的高度["1","0","1","0","0"]，最大面积为1；

        第二层柱状图的高度["2","0","2","1","1"]，最大面积为3；

        第三层柱状图的高度["3","1","3","2","2"]，最大面积为6；

        第四层柱状图的高度["4","0","0","3","0"]，最大面积为4；
        """
        if len(matrix) == 0:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] = heights[j] + 1
            res = max(res, self.largestRectangleArea(heights))
        return res

    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                s = stack.pop()
                res = max(res, heights[s] * ((i - stack[-1] - 1) if stack else i))
            stack.append(i)
        return res