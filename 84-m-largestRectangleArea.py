class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        看了别人的答案想了半天才明白……其实可以把这个想象成锯木板，
        如果木板都是递增的那我很开心，如果突然遇到一块木板i矮了一截，
        那我就先找之前最戳出来的一块（其实就是第i-1块），
        计算一下这个木板单独的面积，然后把它锯成次高的，
        这是因为我之后的计算都再也用不着这块木板本身的高度了。
        再然后如果发觉次高的仍然比现在这个i木板高，
        那我继续单独计算这个次高木板的面积（应该是第i-1和i-2块），
        再把它俩锯短。直到发觉不需要锯就比第i块矮了
        ，那我继续开开心心往右找更高的。当然为了避免到了最后一直都是递增的，
        所以可以在最后加一块高度为0的木板。

        这个算法的关键点是把那些戳出来的木板早点单独拎出来计算，然后就用不着这个值了
        """
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        
        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
        
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
