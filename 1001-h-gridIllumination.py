from typing import DefaultDict
from typing import List

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 八皇后问题，check是否在一条直线上的应用而已

        Row, Col = n, n
        row_dic = DefaultDict(int)
        col_dic = DefaultDict(int)
        diag_dic = DefaultDict(int)
        anti_diag_dic = DefaultDict(int)
        lamp_set = set()
        for r, c in lamps:
            if (r, c) in lamp_set:      #很大一个坑！！！！！！！！！！！！！！！
                continue
            lamp_set.add((r, c))
            row_dic[r] += 1
            col_dic[c] += 1
            diag_dic[r-c] += 1
            anti_diag_dic[r+c] += 1

        res = []
        for r, c in queries:
            if row_dic[r] or col_dic[c] or diag_dic[r-c] or anti_diag_dic[r+c]:
                res.append(1)
            else:
                res.append(0)
            for nr,nc in ((r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1)):
                if (nr,nc) in lamp_set:
                    lamp_set.remove((nr,nc))
                    row_dic[nr] -= 1
                    col_dic[nc] -= 1
                    diag_dic[nr-nc] -= 1
                    anti_diag_dic[nr+nc] -= 1
        return res
