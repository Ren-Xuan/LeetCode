class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mapper = {
            "a": 1,
            "e": 2,
            "i": 4,
            "o": 8,
            "u": 16
        }
        seen = {0: -1}
        res = cur = 0
        """
        aeiou每个元音用一个bit一共5个bit，32种奇偶次数组合状态，比如10101可以表示aiu出现奇数次数
        oe则出现偶数次数，每当遍历一个字符，就可以改变当前的aeiou出现的奇偶次数，也即是改变状态
        显然，如果两次出现了同样的状态，假设第一次出现在i处
        第二次出现在j处，那么i+1-j之间的字符串肯定是满足aeiou出现均为偶数次数的
        因为只有经历了偶数个aeiou，才能回到之前的状态，为了使得合理的字符串最长
        那么第一次出现此状态时，就需要记录到下标，然后下次遇到相同状态，计算最大长度
        
        """
        for i in range(len(s)):
            if s[i] in mapper:
                cur ^= mapper.get(s[i])
            # 全部奇偶性都相同，相减一定都是偶数
            if cur in seen:
                res = max(res, i - seen.get(cur))
            else:
                seen[cur] = i
        return res
