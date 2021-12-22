from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        delta = [0] * 101   # 变化量
        offset = 1950   # 起始年份与起始下标之差
        for b, d in logs:
            delta[b-offset] += 1
            delta[d-offset] -= 1
        mx = 0   # 人口数量最大值
        res = 0   # 最大值对应的最小下标
        curr = 0   # 每一年的人口数量
        # 前缀和
        for i in range(101):
            curr += delta[i]
            if curr > mx:
                mx = curr
                res = i
        return res + offset   # 转回对应的年份
