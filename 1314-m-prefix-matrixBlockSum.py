class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        presum = [[0] * (n + 1) for _ in range(m + 1)] 
        for i in range(1,m+1):
            for j in range(1,n+1):
                presum[i][j] = presum[i-1][j]+presum[i][j-1]-presum[i-1][j-1] +mat[i-1][j-1]
        # 任意矩形和
        def get(x1,y1,x2,y2):
            return presum[x2][y2] - presum[x2][y1-1] - presum[x1-1][y2] + presum[x1-1][y1-1]

        # 计算基于i,j的区域和
        res = []
        for i in range(1,m+1):
            tmp = []
            for j in range(1,n+1):
                q = get(max(i-k,1),max(j-k,1),min(i+k,m),min(j+k,n))
                tmp.append(q)
            res.append(tmp)
        return res
