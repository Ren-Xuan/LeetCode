
class Solution:
    def sumFourDivisors0(self, nums) -> int:

        def factor(n):
            if n <=5:
                return []
            ans = set()
            #只需要找出两个就行了，因为1和它本身就是因数
            for i in range(2, int(n**0.5)+1):
                j, r = divmod(n, i)
                if r == 0:
                    ans = ans.union({i, j})
                if len(ans)>2:
                    return []
            return list(ans)

        factors = [(factor(n),n) for n in nums]
        ans = sum((sum(f[0])+1+f[1]) if len(f[0]) == 2 else 0 for f in factors)
        return ans
    def sumFourDivisors(self, nums) -> int:
        ans = 0
        for i in nums:
            t = int(i**.5)
            if t**2 == i: continue
            k, res, base = 1, 1 + i, 2
            while k >= 0 and base <= t: # 退出循环的条件是有多余一组因子以及因子的变化范围
                if i % base == 0:
                    k -= 1
                    res += base + i // base
                base += 1
            
            if k == 0: 
                ans += res # 正好是4因素
        return ans