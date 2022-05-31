from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        # 建立前缀和数组
        preSum = [0]
        for x in nums:
            preSum.append(preSum[-1] + x)

        ans, q = float('inf'), deque() # q中存储格式：(i, sum_i)
        for i, sum_i in enumerate(preSum):

            # 将deque末尾比sum_i大的值都pop，保持递增的deque
            # 前面的sum都被sum_i小，才能保证将sum_i有的比
            while q and sum_i <= q[-1][1]:
                q.pop()

            # 如果队尾减队首大于等于k，那么队首就找到了以他开始的最短的子数组，队首就可以退位了
            # 如果符合就把第一个扔掉，找到第一个不符合的，那么就是距离最近的
            while q and sum_i - q[0][1] >= k:
                ans = min(ans, i - q.popleft()[0])

            q.append((i, sum_i))

        return ans if ans != float('inf') else -1
