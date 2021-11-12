from typing import DefaultDict


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        self.cnt = 0
        self.m = 1e9
        self.used = set()
        # 预处理：如果桌面上某种球和手中的数量和小于3，则必然无法消除
        candidate = DefaultDict(int)
        boardcount = DefaultDict(int)
        for b in board:
            boardcount[b] += 1
        for h in hand:
            candidate[h] += 1
        for k in boardcount.keys():
            if boardcount[k]+candidate[k] < 3:
                print("defautk")
                return -1
        def change(s):

            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[i] == s[j]:
                    j += 1
                if j - i >= 3:
                    s = s[:i] + s[j:]
                    i = -1
                i += 1
            return s
        def traceback(res:str,candidate: set):
            self.used.add((res))
            #print(res)
            res = change(res)
            if len(res) == 0:
                if self.cnt<self.m:
                    self.m = self.cnt
                return
            if self.cnt>=self.m:
                return
            for e in candidate:
                for i in range(len(res)+1):
                    if i<len(res)-1 and res[i] == res[i+1] == candidate[e]:
                        continue
                    if 1<= i and i <len(res) and res[i-1] == res[i] == candidate[e]:
                        continue
                    if candidate[e]<=0:
                        break
                    if (res[:i]+e+res[i:]) in self.used:
                        continue
                    candidate[e]-=1
                    self.cnt+=1
                    traceback(res[:i]+e+res[i:],candidate)
                    self.cnt-=1
                    candidate[e]+=1
        traceback(board,candidate)
        if self.m>1e8:
            return -1
        return self.m