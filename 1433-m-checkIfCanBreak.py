class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return any(all(x) for x in list(zip(*((a >= b, a <= b) for a, b in zip(sorted(s1), sorted(s2))))))
        #or class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return any(all(x) for x in zip(*((a >= b, a <= b) for a, b in zip(sorted(s1), sorted(s2)))))
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return any(all(x) for x in zip(*((a >= b, a <= b) for a, b in zip(sorted(s1), sorted(s2)))))


    def checkIfCanBreak2(self, s1: str, s2: str) -> bool:
        s1, s2 = sorted(s1), sorted(s2)
        check = zip(*((a >= b, a <= b) for a, b in zip(s1, s2)))
        check = list(check)
        return all(check[0]) or all(check[1])