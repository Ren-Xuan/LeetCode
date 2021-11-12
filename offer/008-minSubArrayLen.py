class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        left, right, n = 0, 0, len(nums)
        s = 0
        minLen = float('inf')
        while left < n and right <= n:
            while right < n and s < target:  # 向右移动right指针，直至满足窗口内整数之和s>=target
                s += nums[right]
                right += 1
            if s >= target:
                minLen = min(minLen, right - left)  # 更新最小长度
                if minLen == 1:
                    return minLen  # 如果最小长度为1，不需要向后搜索了，1就是最小值
            s -= nums[left]  # 向右移动left指针
            left += 1
        return minLen if minLen <= n else 0

