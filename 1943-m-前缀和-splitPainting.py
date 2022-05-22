from collections import defaultdict
from typing import List

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # 计算每个位置对应的颜色和改变量并用哈希表存储
        color = defaultdict(lambda: 0)
        for l, r, c in segments:
            color[l] += c
            color[r] -= c
        # 将哈希表转化为数组并按数轴坐标升序排序
        axis = sorted([[k, v] for k, v in color.items()])
        # 对数组求前缀和计算对应颜色和
        n = len(axis)
        for i in range(1, n):
            axis[i][1] += axis[i-1][1]
        # 遍历数组生成最终绘画结果
        res = []
        print(axis)
        for i in range(n - 1):
            if axis[i][1]:
                res.append([axis[i][0], axis[i+1][0], axis[i][1]])
        return res
