import collections
import math
from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = set(nums)
        c = max(nums)
        ans = 0
        #枚举1~max(nums)中所有的数字y，看y是不是nums某个子序列的最大公约数
        for y in range(1, c + 1):
            g = None
            #如果y是nums某个子序列的最大公约数，那么这个子序列都是y的整数倍
            #所以只需要列举y的所有整数倍x，如果x在nums中，求一下当前所列举的满足条件的的最大公约数g
            #不需要记住当前序列，因为最大公约数g一定是越来越大的
            for x in range(y, c + 1, y):
                if x in nums:
                    if not g:
                        g = x
                    else:
                        g = math.gcd(g, x)
                    if g == y:
                        ans += 1
                        break
        
        return ans


    def countDifferentSubsequenceGCDs2(self, nums: List[int]) -> int:
        d = collections.defaultdict(list)
        ma = max(nums)
        s = set(nums)
        #列举i是否是一个子序列的公约数
        for i in range(1, ma + 1):
            #如果i是公约数，那么i的整数倍n在nums中的话
            #那么以i作为公约数的list就记住n(即add(n))
            for n in range(i, ma + 1, i):
                if n in s:
                    d[i].append(n)
        #问题是现在我们的d是记住了所有的公约数，并没有体现最大这个东西
        #但是题目要求找的是所有
        #假如某一个长序列arr的公约数们有a、b、c且a<b<c最大公约数是c
        #则这个一定存在长序列arr的某个子序列subArr，它的最大公约数为c
        #只需要一个set就能统计最大公约数的数目
        return len(set((tuple(i) for i in d.values())))