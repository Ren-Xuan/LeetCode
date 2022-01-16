class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 10**9+7
        a = 1
        e = 1
        i = 1
        o = 1
        u = 1
        for k in range(2,n+1):
            aa = (e+i+u)%M
            ee = (a+i)%M
            ii = (e+o)%M
            oo = i
            uu = (o+i)%M
            a = aa
            e = ee
            i = ii
            o = oo
            u = uu
        return (a+e+i+o+u)%M