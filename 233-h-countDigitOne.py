class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        举个例子： n = 2304 。答案为四个部分之和：

        1. 所有小于等于2304的正整数中，个位出现1的次数.
        2. 所有小于等于2304的正整数中，十位出现1的次数.
        3. 所有小于等于2304的正整数中，百位出现1的次数.
        4. 所有小于等于2304的正整数中，千位出现1的次数.
        这四部分可以只考虑一部分，另外三部分就异曲同工了。用第二部分来举例，也就是计算所有小于等于2304的正整数中，十位出现1的次数：

        为了帮助理解，我们先想象有一个自行车密码锁（这个比喻来自@ryan0414），一共有四位，每一位可单独滚动。为了计算十位出现1的次数，我们考虑三种情况：

        1. n中的十位为0. 即 n = 2304。
        我们先锁住十位，强行让十位变成1，剩下三位可以随意滚动：XX1X。那么求十位出现一的个数也就是，我可以滚出多少种密码组合，使得该密码小于等于n（注意十位被锁定成了1，转不动）。

        不难发现，我们能滚出的最大数是：2219,

        我们能滚出的最小数是：0010。
        
        
        """
        # mulk 表示 10^k
        # 在下面的代码中，可以发现 k 并没有被直接使用到（都是使用 10^k）
        # 但为了让代码看起来更加直观，这里保留了 k
        k, mulk = 0, 1
        ans = 0
        while n >= mulk:
            ans += (n // (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0), mulk)
            k += 1
            mulk *= 10
        return ans