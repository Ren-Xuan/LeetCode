class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        """
        a、 a + 1、 a + 2、 ... 、a + b - 1 一共b个数

        (2a + b - 1) * b / 2 == n

        a = ((2n / b) - b + 1) / 2

        故b是2n的约数
            且2n > b * (b - 1)
        """
        res = 0
        b = 1
        while b*(b-1)<2*n:
            if (2*n) %b == 0 and ((2*n/b)-b+1)%2 == 0:
                res+=1
            b+=1
        return res 