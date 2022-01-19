from typing import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k and sum(map(lambda x: x % 2, Counter(s).values())) <= k
