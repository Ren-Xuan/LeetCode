from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = set()
        @lru_cache(None)
        def dfs(dic,curSum,curMax,cnt):
            if curSum == n and cnt == k:
                self.ans.add(dic)
                return
            elif cnt>k:
                return
            for nextI in range(curMax,9):
                if curSum+nextI+1<=n:
                    nextDic = dic|(1<<nextI)#把某一位置1
                    dfs(nextDic,curSum+nextI+1,nextI+1,cnt+1)
        def dicToArr(dic):
            arr = []
            for i in range(9):
                if dic&(1<<i) == (1<<i):#判断某一位是不是1如果i==1则称为判断第1位是不是1
                    arr.append(i+1)
            return arr

        for i in range(9):
            dfs(1<<i,i+1,i+1,1)#从第0位开始
        return [dicToArr(e) for e in self.ans]
