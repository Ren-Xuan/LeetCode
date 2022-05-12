class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left = 0
        right = len(s)
        A = []
        for i in s:
            if i == 'I':
                A.append(left)
                left += 1
            else:
                A.append(right)
                right -= 1
        A.append(right)
        return A