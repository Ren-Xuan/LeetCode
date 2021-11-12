class Solution:
    def minTime(self, time, m: int) -> int:
        def check(mid,time,m):
            help = 0
            cnt = 1
            n = len(time)
            i = 0
            curMax = -1
            total = 0
            while i <n:
                if time[i]>curMax:
                    curMax  = time[i]
                total +=time[i]
                if total>mid:
                    if help == 0:
                        help = 1
                        total -=curMax
                    else:
                        cnt+=1
                        help = 0
                        total = 0
                        curMax = -1
                        i-=1
                i+=1
            return cnt <= m
        
        l = 0
        r = max(time)
        while l < r:
            mid = (l+r)//2
            if check(mid,time,m):
                r = mid
            else:
                l = mid+1
        return r

def check(mid,time,m):
            help = 0
            cnt = 1
            n = len(time)
            i = 0
            curMax = -1
            total = 0
            while i <n:
                if time[i]>curMax:
                    curMax  = time[i]
                total +=time[i]
                if total>mid:
                    if help == 0:
                        help = 1
                        total -=curMax
                    else:
                        cnt+=1
                        help = 0
                        total = 0
                        curMax = -1
                        i-=1
                i+=1
            return cnt <= m
print(check(222,[999,999,999],3))
print(check(63,[82,35,6,53,37,75,69,69,53,18],4))
print(check(222,[999,999,999],3))
print("-"*10)
print(check(78,[82,35,6,53,37,75,69,69,53,18],4))
#print(check(488,[50,47,68,33,35,84,25,49,91,75],1))