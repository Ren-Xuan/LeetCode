class Solution:
    def countVowelSubstrings0(self, word: str) -> int:
        #超时
        num = 0        
        ss = set(['a','e','i','o','u'])
        for i in range(len(word)):
            for j in range(i):
                if set(word[j:i+1]) == ss:
                    num += 1
        return num
    def countVowelSubstrings(self, word: str) -> int:
            l = 0
            n = len(word)
            res = 0
            # l, r 分别记录当前元音字符串的边界
            for r in range(n):
                if word[r] not in 'aeiou': # 遇到辅音，重置左边界
                    l = r + 1
                    continue
                if r == n - 1 or word[r + 1] not in 'aeiou': # 已触达当前只包含元音的子字符串的最大右边界，计算该子字符串内有效的元音子字符串数目
                    # 滑动窗口
                    # 使用哈希记录当前窗口每个元音的出现次数
                    char_count = {'a':0,'e':0,'i':0,'o':0,'u':0}
                    # left, right 分别为当前窗口左右边界
                    left = l
                    for right in range(l, r + 1):
                        char_count[word[right]] += 1
                        while char_count[word[left]] > 1: # 收缩左边界，并保证不同元音的数量不下降
                            char_count[word[left]] -= 1
                            left += 1
                        if all(i >= 1 for i in char_count.values()): # 若当前窗口所有元音都存在，则当前窗口为有效的元音子字符串，且往左扩展的所有子字符串均为有效的元音子字符串
                            res += left - l + 1
            return res
