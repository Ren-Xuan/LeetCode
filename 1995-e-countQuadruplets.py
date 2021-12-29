from typing import Counter, List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        在枚举前两个下标 a, b 时，
        我们可以先逆序枚举 b。
        在 b 减小的过程中，c 的取值范围是逐渐增大的：
        即从 b+1 减小到 b 时，c 的取值范围中多了 b+1这一项，
        而其余的项不变。
        因此我们只需要将所有满足 c=b+1 且 d> 的c,d 对应的 nums[d] - nums[c]加入哈希表即可。

        """
        n = len(nums)
        ans = 0
        cnt = Counter()
        for b in range(n - 3, 0, -1):
            for d in range(b + 2, n):
                cnt[nums[d] - nums[b + 1]] += 1
            for a in range(b):
                if (total := nums[a] + nums[b]) in cnt:
                    ans += cnt[total]
        return ans

