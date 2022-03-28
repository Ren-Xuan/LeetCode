class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        counter = Counter([0])                  # 空字符串，对应的mask是0，即所有位都是零
        mask, ans = 0, 0                        # 掩码和结果初始化为零

        for c in word:                          #
            mask ^= (1 << ord(c) - ord("a"))    # 翻转c位置在mask数组中的奇偶标志
            ans += counter[mask]                # 统计子串中各个字符出现次数全部是偶数的情况，因为一旦两个位置处对应的mask一样，则它们之间的子串各个位置出现次数一定是偶数
            for i in range(10):                 # 因为允许存在一个是奇数，而且word中包含从abcdefghij这几个字符
                mask_pre = mask ^ (1 << i)      # 逐个的更改mask在该字符处的奇偶性
                ans += counter[mask_pre]        # 加入到结果中
            counter[mask] += 1                  # 注意需要在以上步骤结束之后，更新计数器counter中的mask

        return ans