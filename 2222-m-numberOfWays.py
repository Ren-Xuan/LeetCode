class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        根据题意，只有两种情况：

        010：对每个 1，统计左边 0 的个数和右边 0 的个数；
        101：对每个 0，统计左边 1 的个数和右边 1 的个数。
        """
        n = len(s)
        n1 = s.count('1')   # s 中 '1' 的个数
        res = 0   # 两种子序列的个数总和
        cnt = 0   # 遍历到目前为止 '1' 的个数
        for i in range(n):
            if s[i] == '1':
                res += (i - cnt) * (n - n1 - i + cnt)
                cnt += 1
            else:
                res += cnt * (n1 - cnt)
        return res

