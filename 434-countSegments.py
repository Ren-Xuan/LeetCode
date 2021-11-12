class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

s = Solution()
s.countSegments("""\"Hello, my name is John\"""")
s.countSegments("""\"Hello,\"""")