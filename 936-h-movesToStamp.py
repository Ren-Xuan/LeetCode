
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """
        target: aabcaca, sub: abca, replacement: XXXX
        replaced target: aXXXXca, ans: 1
        target: aXXXXca, sub: XXca, replacement: XXXX
        replaced target: aXXXXXX, ans: 1 3
        target: aXXXXXX, sub: aXXX, replacement: XXXX
        replaced target: XXXXXXX, ans: 1 3 0
        found: false, s: XXXXXXX
        """
        m, n, s, t, res = len(stamp), len(target), list(stamp), list(target), []
        change = True

        def check(i):
            change = False
            for j in range(m):
                if t[i + j] == "?": continue
                if t[i + j] != s[j]: return False
                change = True
            if change:
                t[i:i + m] = ["?"] * m
                res.append(i)
            return change

        while change:
            change = False
            for i in range(n - m + 1):
                change |= check(i)
        return res[::-1] if t.count("?") == n else []