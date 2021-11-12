class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        #weights = sorted(weights)
        def check(m,weight,days):
            cnt = 1
            cur = m
            for e in weight:
                if cur >= e:
                    cur -=e
                else:
                    cnt+=1
                    if cnt>days:
                        return False
                    cur = m
                    cur -=e
                    if cur<0:
                        return False
            return True
        
        if len(weights)<=days:
            r = max(weights)
        else:
            r = sum(weights)
        l = weights[0]
        while l < r:
            if l >=r:
                break
            print(l,r)
            m = (l+r)//2
            if check(m,weights,days):
                r = m
            else:
                l = m+1
        return l


