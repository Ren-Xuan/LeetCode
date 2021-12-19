from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        单调栈
        维护一个递增的单调栈，
        栈内元素为数组下标，
        从栈顶到栈底的下标对应价格严格递减。
        
        入栈时，如果栈不为空，
        则比较栈顶元素对应的价格和当前的价格如果【当前的价格 ≤ 栈顶的价格】，
        将栈顶元素移除，并将其对应的价格修改为prices[st.pop()] - prices[i]，
        重复上述操作直到栈为空或者栈顶元素对应的价格严格小于当前的价格，然后当前的索引 i 进栈。

        """
        stack = []
        res = list(prices)
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                res[stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop(-1)
            stack.append(i)
        return res

