class Solution:
    def decodeAtIndex2(self, s: str, k: int) -> str:
        stack, size = [], 0
        for char in s:
            if size>k:
                break
            size = size * int(char) if char.isdigit() else size + 1
            stack.append((size, stack[-1][1] if char.isdigit() else char))
        """
        stack[i]:
        如果当前扫描到的char为字符，则stack push进生成的（虚拟）字符串长度size和size所在的char
        如果扫描到的是数字，则（虚拟）字符串长度乘以 这个数字，然后字符串最后一位计为栈顶的字符
            (相当于把(虚拟)栈复制了一遍)
        如果（虚拟字符串）长度大于k则没有必要再增长字符串的长度了
        
        """
        while k % stack[-1][0]:
            k %= stack.pop()[0]
        return stack[-1][1]
    def decodeAtIndex(self, S, K):
        size = 0
        # Find size = length of decoded string
        """
        如果我们有一个像 appleappleappleappleappleapple 
        这样的解码字符串和一个像 K=24 这样的索引，那么如果 K=4，答案是相同的。

        一般来说，当解码的字符串等于某个长度为 size 的单词重复某些次数
        （例如 apple 与 size=5 组合重复6次）时，索引 K 的答案与索引 K % size 的答案相同。

        我们可以通过逆向工作，跟踪解码字符串的大小来使用这种洞察力。
        每当解码的字符串等于某些单词 word 重复 d 次时，
        我们就可以将 k 减少到 K % (Word.Length)。     
        """
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1

