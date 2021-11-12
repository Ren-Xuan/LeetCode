class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        def check(day,bloomDay,m,k):
            cnt = 0
            cur = k

            for e in bloomDay:
                if day>=e:
                    cur-=1
                    if cur == 0:
                        cnt+=1
                        cur = k
                else:#day < e
                    cur = k

            return cnt>=m
        r = max(bloomDay)
        l = 1
        while l < r:
            day = (r+l) // 2
            if check(day,bloomDay,m,k):
                r = day
            else:
                l = day +1
        if check(l,bloomDay,m,k):
            return l
        else :
            return -1
