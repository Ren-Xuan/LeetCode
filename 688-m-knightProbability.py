class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1
        dp = [[[1 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]
        moves = ((-1, -2), (-2, -1),(-2, 1), (-1, 2),(1, -2), (2, -1),(2, 1), (1, 2))
        tmp = 0
        for step in range(1,k+1):
            for i in range(n):
                for j in range(n):
                    tmp = 0
                    for move in moves:
                        nextI = i + move[0]
                        nextJ = j + move[1]
                        if nextI<0 or nextI>=n or nextJ<0 or nextJ>=n:
                            continue
                        tmp+=dp[nextI][nextJ][step-1]
                    dp[i][j][step] = tmp/8
        return dp[row][column][k]
        """
        位置（i，j）走k步留在棋盘上的概率，等于
        ：【从位置（i，j）开始，走一个日字所能到达的8个位置中，
        各位置走k-1步留在棋盘上的概率的均值】。
        8个位置包括棋盘外，因为走出棋盘外后棋子就不走了，
        可以认为棋盘外的位置走k-1步留在棋盘上的概率为0

        dp[i][j][k] = sum(dp[iNext][jNext][k-1])/8
        """