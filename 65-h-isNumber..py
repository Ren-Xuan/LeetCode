class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            key=float(s)
            if 'nf' in s:
                return False
            return True
        except:
            return False