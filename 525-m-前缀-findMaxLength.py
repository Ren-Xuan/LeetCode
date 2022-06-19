class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt, prev, ans = {}, 0, 0
        for i in range(len(nums)):
            prev += 1 if nums[i] else -1
            if prev == 0:
                ans = max(ans, i + 1)
            elif prev not in cnt:
                cnt[prev] = i
            else:
                ans = max(ans, i - cnt[prev])
        return ans