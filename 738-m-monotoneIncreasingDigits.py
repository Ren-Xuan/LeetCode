

class Solution:
    def monotoneIncreasingDigits(self, N):
        '''
        先从尾到头遍历一遍，如果出现逆序，大的值减1，并记录最后一个逆序的位置i，然后把从i开始到末尾的数全部变9
        n   = 1234321
        res = 1233999

        n    = 2333332
        res  = 2299999
        '''
        a = list(str(N))
        for i in range(len(a)-1,0,-1):
            if int(a[i]) < int(a[i-1]):
                a[i-1] = str(int(a[i-1]) - 1)
                a[i:] = '9' * (len(a) - i)  #python不需要设置flag值，直接按长度给9就好了
        return int("".join(a))