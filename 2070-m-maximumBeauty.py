import heapq
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x :x[0])
        query = [i for i in range(len(queries))]
        query.sort(key = lambda x : queries[x])
        #将queries的index 按照queries的大小排序
        #这样从小到大的查询就能不断的将item里面的美丽值添加到优先队列
        pq = []
        ans = [0] * len(queries)
        start = 0
        for i in query:#从查询的最小的那个开始依次递增
            while start <len(items) and queries[i] >= items[start][0]:
                #如果当前的item值小于当前的查询,那么就添加到优先队列,直到没有小于当前查询的item值
                heapq.heappush(pq,-items[start][1])
                start+=1
            #将当次查询的结果从优先队列队首取出来,结果填入当次查询在原queries数组的index中
            ans[i]= -pq[0] if len(pq)>0 else 0
        return ans