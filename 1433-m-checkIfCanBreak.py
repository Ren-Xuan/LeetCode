class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return any(all(x) for x in list(zip(*((a >= b, a <= b) for a, b in zip(sorted(s1), sorted(s2))))))
