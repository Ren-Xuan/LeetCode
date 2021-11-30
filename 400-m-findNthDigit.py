class Solution:
    def findNthDigit(self, n: int) -> int:
        digitCount = 1
        
        bottom, top = 0, 10
        while n > (top - bottom) * digitCount:
            n -= (top - bottom) * digitCount
            digitCount += 1
            bottom, top = top, top * 10
        num, r = divmod(n, digitCount)
        return int(str(num + bottom)[r])


        """
        分析:
        小于10，1~9，9个数字，9位
        小于100，10~99，90个数字，180位
        小于1000，100~999，900个数字，2700位

        各个区间的下限上限是[0,10),[10, 100),[100,1000)...位数是1，2，3...
        从第1个区间的上限开始进行比较，如果大于上限，将上下限*10，将n=n-(上限-下限)*位数 直至找到n所在的区间
        找到区间后，n/位数 找到所在的数字，然后n%位数，找到数字的第几位数字
        整除和求余运算能判定出指向的是哪一个数字，以及这个数字的第几个数位。
        假如n=200
        经过循环以后n=11，digitCount = 3 ，bottom = 100
        11/3 = 3得到是100以后的第三个长度为3的数，即100+3 = 103
        余2得到是103的第二位即0
        加入n = 9+180+2699，计算出来以后n = 2699，digitCount=3，bottom = 100
        2699/3 = 899位，即100以后的第899个三位数，即100+899 = 999 ，结果是9
        第k个d位数就从bottom加k因为第k个和第k-1个d位数只相差1！！！
        """