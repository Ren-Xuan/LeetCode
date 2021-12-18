from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.matrix = [[0]*n for _ in range(n)]
        self.cnt = 1
        def solve(startM,startN,N):
            #print(self.matrix)
            if startM>=1+len(self.matrix)//2:
                return
            for n in range(startN,startN+N):
                self.matrix[startM][n] = self.cnt
                self.cnt+=1
            for m in range(startM+1,startM+N):
                self.matrix[m][startN+N-1] = self.cnt
                self.cnt+=1
            for n in range(startN+N-2,startN-1,-1):
                self.matrix[startM+N-1][n] = self.cnt
                self.cnt+=1
            for m in range(startM+N-2,startM,-1):
                self.matrix[m][startN] = self.cnt
                self.cnt+=1
            solve(startM+1,startN+1,N-2)
        solve(0,0,n)
        return self.matrix