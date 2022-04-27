class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        pre, suf = [0] * n, [0] * n
        # left 记录 -> 最大值，right 记录 <- 最小值
        left, right = nums[0], nums[-1]

        # 从前往后记录 [0, i) 中的最大值
        # 从后往前记录 [i + 1, n) 中的最小值
        # 下标对应转换不要忘了
        for i in range(0, n):
            pre[i], suf[n - i - 1] = left, right
            left, right = max(left, nums[i]), min(right, nums[n - i - 1])        
        """
        就是找一个index,对于index前面的都要小于nums[index],对于index后面的都要大于nums[index]
        那就找一个前向序列pre,pre[i]表示i之前的最小值
        后向序列suf,suf[i]表示i之后的最大值
        """
        res = 0
        # 下标 0 和 n - 1 的美丽值一定是 0，剔除
        for i in range(1, n - 1):
            # 满足条件 1，优先级最高
            if nums[i] > pre[i] and nums[i] < suf[i]:
                res += 2
            # 满足条件 2
            elif nums[i] > nums[i - 1] and nums[i] < nums[i + 1]:
                res += 1
        
        return res