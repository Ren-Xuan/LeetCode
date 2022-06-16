import bisect
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        diff = sum(abs(nums1[i] - nums2[i]) for i in range(n))
        if not diff:
            return 0
        ans = 10**6
        sl = sorted(nums1)
        for i, num in enumerate(nums2):
            idx = bisect.bisect_left(sl, num)
            # idx > 0 尝试用idx-1替换当前值
            if idx:
                ans = min(ans,  - abs(nums1[i] - nums2[i]) + abs(sl[idx-1] - nums2[i]))
            # idx < n 尝试用idx替换当前值
            if idx < n:
                ans = min(ans, - abs(nums1[i] - nums2[i]) + abs(sl[idx] - nums2[i]))
        return (ans+diff) % (10 ** 9 + 7)

