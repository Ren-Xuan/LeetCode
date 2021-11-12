class NumMatrix:

    def __init__(self, matrix):
        """
        m rows
        n columns
        """
        print(matrix)
        m = len(matrix)
        n = len(matrix[0])
        m = 2
        self.presum0 = [[0 for _ in range(n+1)] for _ in range(m+1)]
        self.presum = [[0] * (n + 1) for _ in range(m + 1)]
        self.presum2 = [[0] * (n + 1)]*(m+1)


        print(self.presum0)
        print(self.presum)
        print(self.presum2)
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.presum[i][j] = self.presum[i-1][j]+self.presum[i][j-1]-self.presum[i-1][j-1] +matrix[i-1][j-1]
        print(self.presum0)
        print(self.presum)
        print(self.presum2)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(self.presum)
        return self.presum[row2+1][col2+1] - self.presum[row2+1][col1] - self.presum[row1][col2+1]+self.presum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
obj = NumMatrix([[3,0,1,4,2],[5,6,3,8,1],[1,2,0,9,5],[4,1,0,1,7],[1,2,3,0,5]])