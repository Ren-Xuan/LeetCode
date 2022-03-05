from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def LIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
    #递增不可以相等
    def LIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if not res or num>res[-1]:
                res.append(num)
            elif res:
                idx = bisect_left(res,num)
                res[idx] = num
        return len(res)
    #递增可以相等
    def LIS(nums: List[int]) -> int:
            res = []
            for num in nums:
                if not res or num>=res[-1]:
                    res.append(num)

                elif res:
                    idx = bisect_right(res,num)
                    res[idx] = num
            return len(res)