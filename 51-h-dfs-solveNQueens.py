import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        def valid(path,row,col):
            for i in range(row):
                r,c = i,path[i]
                if c == col or r+c == row+col or r+col == c + row:
                    return False
            return True
        def dfs(path,row):
            if row == n:
                self.ans.append(path)
                return
            for col in range(n):
                if valid(path,row,col):
                    path = path[:row]+(col,)+path[row+1:]
                    dfs(path,row+1)
        dfs((0,)*n,0)
        res = []
        init = ['.'*n for _ in range(n)]
        for e in self.ans:
            cur = copy.deepcopy(init)
            for row in range(n):
                r,c = row,e[row]
                cur[r] =cur[r][:c]+ 'Q'+cur[r][c+1:]
            res.append(cur)
        return res
