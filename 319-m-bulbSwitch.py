class Solution:
    def bulbSwitch0(self, n: int) -> int:
        #模拟
        """
        reverse 1^1 = 0   0^1 = 1翻转
                1^0 = 1   0^0 = 0保持不变
        so mask = 1
        """
        if n <=1:
            return n
        
        def mask(k,n):
            """0..k-1个0..10..k-1个0..10..n-1个0..1"""
            result = 0
            start = (1<<n%k)
            
            for i in range(n//k):
                result |=start
                start<<=k
            """
            bin(mask(3,10))->0b10010010
            """
            return result
        result = pow(2,n)-1
        for i in range(2,n+1):
            result^=mask(i,n)
        
        return bin(result).count('1')
    def bulbSwitch(self, n: int) -> int:
        """
        第i个灯泡的反转次数等于它所有因子（包括1和i）的个数，
        一开始的状态的灭的，只有反转奇数次才会变成亮的，
        所以只有因子个数为奇数的灯泡序号才会亮，
        只有平方数的因子数为奇数
        （比如6=1*6,2*3，它们的因子总是成对出现的，
        而4=1*4,2*2，只有平方数的平方根因子会只出现1次），
        所以最终答案等于n以内（包括n和1）的平方数数量，
        只要计算sqrt(n)即可
        """
        import math
        return int(math.sqrt(n + 0.5))
