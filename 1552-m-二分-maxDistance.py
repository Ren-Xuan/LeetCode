class Solution:
    def maxDistance(self, position, m: int) -> int:
        l = 1
        r = sum(position)
        def check(mid,position,m):
            pre = position[0]
            cnt = 1
            n = len(position)
            for i in range(1,n):
                if position[i]-pre >=mid:
                    cnt+=1
                    pre = position[i]
            return cnt>=m
        while l<r:
            mid = (l+r)//2
            if check(mid,position,m):
                l = mid
            else:
                r = mid-1
        