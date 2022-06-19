from math import gcd

class Solution:
    def nthMagicalNumber(self, N: int, a: int, b: int) -> int:
        def check(n):
            return n // a + n // b - n // c >= N
        c = a * b // gcd(a, b)
        if a > b:
            a, b = b, a
        l, r = a * N // 2, a * N
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l % (10 ** 9 + 7)