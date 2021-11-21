from typing import Deque, List


class Solution:
    def constrainedSubsetSum0(self, nums: List[int], k: int) -> int:

        dp = nums.copy()
        """
        dp[j] 表示最大下标为 j的子序列的最大值和
        dp[j] = max(dp[j-r]+nums[j] for r in range(k))
        """
        for j in range(len(nums)):
            dp[j] = max(*(dp[j-r]+nums[j] if j -r >=0 else -1e10 for r in range(1,k+1)),dp[j])
        #print(dp)
        return max(dp)
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = nums.copy()
        s = Deque()
        s.append((nums[0], 0))
        #单调队列
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], s[0][0] + nums[i])
            while s and s[-1][0] <= dp[i]:
                s.pop()
            s.append((dp[i], i))
            if s[0][1] <= i - k:
                s.popleft()
        return max(dp)
