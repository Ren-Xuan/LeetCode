class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and popped and stack[-1] == popped[0]:
                stack.pop(-1)
                popped.pop(0)
        return len(stack) == 0 and len(popped) == 0