from typing import List
import heapq

class Solution:

    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        """
        计算吃苹果的最大数目分成两个阶段，第一阶段是第 0 天到第 n - 1 天，即天数在数组下标范围内，第二阶段是第 n天及以后，即天数在数组下标范围外。

        在第一阶段，由于每天树上都可能长出苹果，因此需要对每一天分别计算是否能吃到苹果，并更新优先队列。具体做法如下：
        在第二阶段，由于树上不会再长出苹果，因此只需要考虑能吃到的苹果数量。
        由于优先队列中的每个元素的数量可能很大，因此需要根据当前日期和优先队列的队首元素的腐烂日期和数量计算能吃到的苹果数量。

        假设当前日期是第 i 天，首先将优先队列中的所有腐烂日期小于等于 i 的元素取出，
        如果优先队列不为空，则根据优先队列的队首元素计算能吃到的苹果数量。
        假设优先队列的队首元素的腐烂日期是 x，数量是 y，其中 x > i，则有 y 个苹果，
        距离腐烂还有 x - i 天，因此能吃到的苹果数量是 curr = min(x - i, y)。
        将优先队列的队首元素 (x, y) 取出并将日期增加 curr，
        重复上述操作直到优先队列为空，即可得到吃苹果的最大数目。

        """
        ans = 0
        pq = []
        i = 0
        while i < len(apples):
            while pq and pq[0][0] <= i:
                heappop(pq)
            if apples[i]:
                heappush(pq, [i + days[i], apples[i]])
            if pq:
                pq[0][1] -= 1
                if pq[0][1] == 0:
                    heappop(pq)
                ans += 1
            i += 1
        while pq:
            while pq and pq[0][0] <= i:
                heappop(pq)
            if len(pq) == 0:
                break
            p = heappop(pq)
            num = min(p[0] - i, p[1])
            ans += num
            i += num
        return ans

