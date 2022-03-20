class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        if n <=0 or n%4 != 0:
            return 0
        m = n // 4
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        if dic['Q']==m and dic['W']==m and dic['E']==m and dic['R']==m:     #已经平衡了
            return 0
        min_window_len = n                  #窗口内为多了的  窗口外为ok的  没超阈值的
        L = 0                               #L R 均为实指
        for R in range(n):
            dic[s[R]] -= 1
            while L <= R and dic['Q']<=m and dic['W']<=m and dic['E']<=m and dic['R']<=m:
                min_window_len = min(min_window_len, R - L + 1)
                dic[s[L]] += 1
                L += 1
        return min_window_len

