class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if(dividend == -2147483648 and  divisor == -1):
            return 2147483647

        resultMark = 1
        if dividend < 0:
            if divisor < 0 :
                resultMark = 1
            elif divisor > 0:
                resultMark = -1
            else :
                return ZeroDivisionError()
        elif dividend > 0:
            if divisor < 0 :
                resultMark = -1
            elif divisor > 0:
                resultMark = 1
            else :
                return ZeroDivisionError()
        elif dividend == 0:
            return 0

        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0
        return (dividend//divisor)*resultMark
        i = 0
        while True:
            dividend -= divisor
            if dividend < divisor:
                return (i+1)*resultMark
            i +=1
        return pow(2,31) -1

s = Solution()
print(s.divide(10,3))
print(s.divide(-11,3))
print(s.divide(12,-3))
print(s.divide(13,3))