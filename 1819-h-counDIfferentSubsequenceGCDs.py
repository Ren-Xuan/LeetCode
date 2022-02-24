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

