class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 思路：滑动窗口
        # 技巧：本题list可直接判等
        m, n, ans = len(s), len(p), list()
        if m < n: return ans
        book_s, book_p = [0] * 26, [0] * 26
        for i in range(n):
            book_s[ord(s[i])-ord('a')] += 1
            book_p[ord(p[i])-ord('a')] += 1
        for i in range(n, m):
            if book_s == book_p: ans.append(i-n)
            book_s[ord(s[i-n])-ord('a')] -= 1
            book_s[ord(s[i])-ord('a')] += 1
        if book_s == book_p: ans.append(m-n)
        return ans