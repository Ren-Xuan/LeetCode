class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        self.target = n
        self.Queen(0, [], [], [])
        return self.ans

    def Queen(self, n, col, diag1, diag2):  #diag1为左上到左下，diag2为右上到右下
        if n == self.target:
            self.ans += 1
        else:
            for i in range(self.target):
                if (i not in col) and (i-n not in diag1) and (self.target - i - n not in diag2):
                    self.Queen(n + 1, col + [i], diag1 + [i-n], diag2 + [self.target - i - n])