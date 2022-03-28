from collections import Counter


class Solution:
    def canMakePaliQueriesOverTime(self, s: str, queries) :
        def check(s,k):
            n = len(s)
            odd = True
            if n %2 == 0:
                odd = True
            else:
                odd = False
            """
            odd = true 如果s中的统计字符都是偶数，且剩余一个奇数，则return true
            odd = false如果s中的统计字符都是偶数，return true
            k的情况，可以容忍k个奇数次字符
            
            """
            d =dict(Counter(s))
            cnt = 0
            for e in d:
                if d[e]%2 == 0:
                    continue
                else:#d[e]是奇数
                    cnt+=1
            if (cnt/2 - k) <= 0 and odd == True:
                return True
            elif (cnt - 1)/2 - k <= 0 and odd == False:
                return True
            return False
        result = []
        for e in queries:
            result.append(check(s[e[0]:e[1]+1],e[2]))
        return result
    def canMakePaliQueries(self, s: str, queries) :
        dic = [[0]*26 for _ in range(len(s)+1)]
        for i in range(1,len(s)+1):
            dic[i] = dic[i-1].copy()
            dic[i][ord(s[i-1]) - ord('a')]+=1
        def check(s,k,d):
            n = len(s)
            odd = True
            if n %2 == 0:
                odd = True
            else:
                odd = False
            """
            odd = true 如果s中的统计字符都是偶数，且剩余一个奇数，则return true
            odd = false如果s中的统计字符都是偶数，return true
            k的情况，可以容忍k个奇数次字符
            
            """
            #d =dict(Counter(s))
            cnt = 0
            for i in range(26):
                if d[i]%2 == 0:
                    continue
                else:#d[e]是奇数
                    cnt+=1
            if (cnt/2 - k) <= 0 and odd == True:
                return True
            elif (cnt - 1)/2 - k <= 0 and odd == False:
                return True
            return False
        result = []
        for e in queries:
            if e[2]>13:
                result.append(True)
            else:
                d = [0 for _ in range(26)]
                for i in range(26):
                    d[i] = dic[e[1]+1][i] - dic[e[0]][i]
                result.append(check(s[e[0]:e[1]+1],e[2],d))
        return result
    def canMakePaliQueriesBit(self, s: str, queries) :
        res, box, last = [], [0], 0
        for i in range(len(s)):
            last ^= 1 << ord(s[i])-97
            box.append(last)
        for q in queries:
            if q[2] >= 13:
                res.append(True)
            else:
                c, d = 0, box[q[0]] ^ box[q[1]+1]
                while d:
                    d &= d-1
                    c += 1
                res.append(c // 2 <= q[2])
        return res
"""
目标，计算从 start到end出现次数为奇数次的字母的个数c ,如果 c <=2*k+1 则一定可以变成回文串 因为c最大是26，所以k如果>=13 则一定可以变成回文串

预处理s
把 ‘a’-'z' 看成一个26位的二进制数，如果某个字母出现了奇数次，记为1 如果出现了偶数次，记为0
这样 d[i] 表示到s 的第i个字符时，表示的数字

处理 queries

奇数-奇数 = 偶数
奇数-偶数 = 奇数
偶数-偶数 = 偶数
偶数-奇数 = 奇数

正是 异或 的结果



"""
"""

n&(n-1)消除数字n的二进制表示的最后一个1
例如 n = 110 经过上面运算 n就变成了100
应用
一个数如果是 22 的指数，那么它的二进制表示一定只含有一个 1
如果使用位运算技巧就很简单了（注意运算符优先级，括号不可以省略）：
"""
def isPowerOfTwo(n) :
    if n <= 0:
         return False
    return (n & (n - 1)) == 0


