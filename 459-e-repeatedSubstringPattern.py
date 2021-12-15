class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        假设母串S是由子串s重复N次而成， 则 S+S则有子串s重复2N次， 那么现在有： S=Ns， S+S=2Ns， 其中N>=2。 
        如果条件成立， S+S=2Ns, 掐头去尾破坏2个s，S+S中还包含2*（N-1）s, 又因为N>=2, 因此S在(S+S)[1:-1]中必出现一次以上
        """
        return s in (s+s)[1:-1]
    def repeatedSubstringPattern2(self, s: str) -> bool:
        n = len(s)
        for k in range(n//2,0,-1):
            if (s[:k])*(n//k) == s:
                return True
        return False