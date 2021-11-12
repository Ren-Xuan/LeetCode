class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 记录滑动窗口子串和，超过目标值，左指针移动，低于目标值，右指针移动。
        # 约束条件： 1）左指针移动小于数组长度-满足条件子串最大值
        # 找到一个最长的子序列 (right-left 最大) 满足：x = sum(nums) - sum(nums[left:right])
        # 蛮力法 O(n^2) n = 10^5 会超时
        # 这里保证都是正数的数组，所以可以排除不少 case
        # right - left 尽可能大，但如果直接使用 if 可能会漏掉 case， 输出 -1。所以中间使用 while, left 可以多减去一些。
        n = len(nums)
        val = sum(nums) - x

        if val < 0:
            return -1
        if val == 0:
            return n
        
        left, right = 0, 0
        cum_val = 0
        ans = 10**8
        while right < n:
            cum_val += nums[right]
            while cum_val > val:  # 这里 if 需要替换为 while, 可以一次多删几个，否则会漏解。不同于之前滑动窗口长度只变大不变小
                cum_val -= nums[left]
                left += 1
            if cum_val == val:
                ans = min(ans, n - (right - left + 1))
            right += 1

        return -1 if ans == 10**8 else ans
