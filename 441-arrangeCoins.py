class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 1
        while True:
            n -= cnt
            if n==0:
                return cnt
            elif n < 0:
                return cnt-1
            cnt+=1



s= Solution()
print(s.arrangeCoins(1))
print(s.arrangeCoins(1+1))
print(s.arrangeCoins(1+2))
print(s.arrangeCoins(1+2+1))
print(s.arrangeCoins(1+2+2))
print(s.arrangeCoins(1+2+3))
print(s.arrangeCoins(1+2+3+1))
print(s.arrangeCoins(1+2+3+4))
print(s.arrangeCoins(1+2+3+4+1))