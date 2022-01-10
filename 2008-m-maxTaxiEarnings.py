
from typing import DefaultDict, List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rn = len(rides)
        rides.sort(key = lambda x: x[1])
        dp = [0 for _ in range(rn)]
        for i in range(rn):
            #--------当前可获得的利润
            cur = rides[i][1] - rides[i][0] + rides[i][2]

            #--------若是接当前的单
            #--二分-最右
            l = -1
            r = i - 1
            while l < r:
                mid = (l + r + 1) // 2
                if rides[mid][1] <= rides[i][0]:
                    l = mid
                else:
                    r = mid - 1
            if 0 <= l:
                cur += dp[l]
            dp[i] = max(dp[i], cur)
            #--------如果不接当前的单
            if 0 < i:
                dp[i] = max(dp[i - 1], dp[i])

        return dp[rn - 1]
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        end_start_tip = DefaultDict(list)
        for start, end, tip in rides:
            start -= 1
            end -= 1
            end_start_tip[end].append((start, end - start + tip))
            
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            dp[i] = max(dp[i], dp[i - 1])
            for ss, tt in end_start_tip[i]:
                dp[i] = max(dp[i], dp[ss] + tt)
        return dp[n - 1]
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        """
        超时
        dp[i] 表示到i最大盈利
        dp[j] = max(dp[i]+pay[i,j])        
        """
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            for e in rides:
                dp[e[1]] = max(dp[e[1]],dp[e[0]]+e[1]-e[0]+e[2])
        return max(dp)
