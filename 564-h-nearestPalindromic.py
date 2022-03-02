class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if int(n)<10 or int(n[::-1])==1:
            return str(int(n)-1)
        if n=='11':
            return '9'
        if set(n)=={'9'}:
            return str(int(n)+2)
        ans = set()
        if n[0] == '1':
            ans.add('9'*(len(n)-1))
        elif n[0] == '9':
            ans.add('1'+(len(n)-2)*'0'+'1')
        """
        如果数组的字符串长度 == 1，数字n - 1
        开头为1，9**9为一个候选答案        例：100000，答案为99999
        开头为9, 10**01为一个候选答案       例：99999，答案为100001
        如果本身对称，则把最中间的一个（或两个）位数减（如果0则加）一
            例：123321，答案为122221
            例：120021，答案为121121
        如果不对称：
            把前半部分逆序替换掉后半部分       例：1223，答案为1221
            把最中间的一个（或两个）位数加一   例：1283，答案为1331，而非1221
            把最中间的一个（或两个）位数减一   例：1800，答案为1771，而非1881
        --------------------- 
        """
        if n[:len(n)//2] == n[::-1][:len(n)//2]:
            if len(n)%2 ==1:
                if n[len(n)//2] == '0':
                    ans.add(n[:len(n)//2]+'9'+n[:len(n)//2][::-1])
                    ans.add(n[:len(n)//2]+'1'+n[:len(n)//2][::-1])
                elif n[len(n)//2] == '9':
                    ans.add(n[:len(n)//2]+'0'+n[:len(n)//2][::-1])
                    ans.add(n[:len(n)//2]+'8'+n[:len(n)//2][::-1])
                else:
                    ans.add(n[:len(n)//2]+str(int(n[len(n)//2])+1)+n[:len(n)//2][::-1])
                    ans.add(n[:len(n)//2]+str(int(n[len(n)//2])-1)+n[:len(n)//2][::-1])
            else:
                if n[len(n)//2-1] == '0':
                    ans.add(n[:len(n)//2-1]+'99'+n[:len(n)//2-1][::-1])
                    ans.add(n[:len(n)//2-1]+'11'+n[:len(n)//2-1][::-1])
                elif n[len(n)//2-1] == '9':
                    ans.add(n[:len(n)//2-1]+'00'+n[:len(n)//2-1][::-1])
                    ans.add(n[:len(n)//2-1]+'88'+n[:len(n)//2-1][::-1])
                else:
                    ans.add(n[:len(n)//2-1]+2*str(int(n[len(n)//2])+1)+n[:len(n)//2-1][::-1])
                    ans.add(n[:len(n)//2-1]+2*str(int(n[len(n)//2])-1)+n[:len(n)//2-1][::-1])
        else:
            if len(n)% 2 ==1:
                ans.add(n[:len(n)//2+1]+n[:len(n)//2][::-1])
                if n[len(n)//2] == '0':
                    ans.add(n[:len(n)//2]+'9'+n[:len(n)//2][::-1])
                    ans.add(n[:len(n)//2]+'1'+n[:len(n)//2][::-1])
                elif n[len(n)//2] == '9':
                    ans.add(n[:len(n)//2]+'0'+n[:len(n)//2][::-1])
                    ans.add(n[:len(n)//2]+'8'+n[:len(n)//2][::-1])
                else:
                    ans.add(n[:len(n)//2]+str(int(n[len(n)//2])+1)+n[:len(n)//2][::-1])
                    ans.add(n[:len(n)//2]+str(int(n[len(n)//2])-1)+n[:len(n)//2][::-1])
            else:
                ans.add(n[:len(n)//2]+n[:len(n)//2][::-1])
                if n[len(n)//2-1] == '0':
                    ans.add(n[:len(n)//2-1]+'99'+n[:len(n)//2-1][::-1])
                    ans.add(n[:len(n)//2-1]+'11'+n[:len(n)//2-1][::-1])
                elif n[len(n)//2-1] == '9':
                    ans.add(n[:len(n)//2-1]+'00'+n[:len(n)//2-1][::-1])
                    ans.add(n[:len(n)//2-1]+'88'+n[:len(n)//2-1][::-1])
                else:
                    ans.add(n[:len(n)//2-1]+2*str(int(n[len(n)//2-1])+1)+n[:len(n)//2-1][::-1])
                    ans.add(n[:len(n)//2-1]+2*str(int(n[len(n)//2-1])-1)+n[:len(n)//2-1][::-1])
        res = set()
        curMin = 10**9
        for e in ans:
            if abs(int(e) - int(n)) == curMin:
                res.add(e)
            elif abs(int(e) - int(n))<curMin:
                curMin = abs(int(e) - int(n))
                res = set()
                res.add(e)
        return min(res,key = lambda x : int(x))