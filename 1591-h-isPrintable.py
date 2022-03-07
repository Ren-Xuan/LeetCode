import collections
from typing import List


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        # 遍历所有点，计算出每个值矩阵的范围
        dic = {}
        for i in range(len(targetGrid)):
            for j in range(len(targetGrid[0])):
                cur = targetGrid[i][j]
                if not cur in dic:
                    dic[cur] = [i, i, j, j] # i最小值，i最大值，j最小值，j最大值
                else:
                    dic[cur] = [min(i, dic[cur][0]), max(i, dic[cur][1]), min(j, dic[cur][2]), max(j, dic[cur][3])]
        
        # 遍历每个数字的矩阵范围内包含的其他数字
        dic2 = collections.defaultdict(set)
        for k, v in dic.items():
            for i in range(v[0], v[1]+1):
                for j in range(v[2], v[3]+1):
                    if targetGrid[i][j] != k:
                        dic2[k].add(targetGrid[i][j])

        # bfs判断是否有环
        queue = [[k] for k in list(dic2.keys())]
        while queue:
            cur = queue.pop(0)
            if cur[-1] in dic2:
                for v in dic2[cur[-1]]:
                    if not v in cur:
                        queue.append(cur + [v])
                    else:
                        return False
        return True

