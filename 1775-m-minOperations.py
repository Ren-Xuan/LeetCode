from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        # 确保nums1 是较大的那一个
        if sum1 < sum2: nums1, nums2 = nums2, nums1 
        thr = abs(sum1 - sum2)
        
        # 最大间隔计数数组
        res = [0]*6
        for i in nums1:
            res[i-1] += 1
        for i in nums2:
            res[6-i] += 1
        
        ans = 0
        #贪心
        for i in range(5, 0, -1):
            tmp = min(res[i], (thr+i-1)//i)
            ans += tmp
            thr -= i*tmp
            if thr <= 0: break
        if thr <= 0: return ans
        return -1
        """
        thr= sum(nums1) - sum(nums2)
        为了将 thr 变为 0 
        nums2 中的 6 和 nums1 中的 1 有相同的效果, 最多能将 d 减少 5
        因此, nums2 和 nums1 可以合并

        将 1~6 映射为 0~5, 方便数组存取, 且索引为该位置的贡献, 比如 res[5] 是 6 的个数, 一个 6 最多能将thr 降低 5
        所以最后问题简化为, 最多变化几个数字, 将正数thr 降为 0     

        换一种说法
        nums1和nums2数组中所有数字都是1到6的，而且两个数组长度可能不一样。我们可以先把两个数组的和做一个比较，
        我们需要将和更大的数组中的数字减小，或者把和更小的数组中的数字增大，来实现两个数组的和的一致。

            设nums1的和小于nums2的和，它们的差别为diff_total
            为了尽可能减少操作次数，nums1中所有元素都可以被增加到6，
            而且要优先处理那些能够尽快缩小两数组和的差距的。
            我们把nums1中所有元素与6的差距，以及nums2中所有元素与1的差距放在一个数组diff中
            每次选中diff中的数，都代表了一次操作，选中的数值代表了这次操作可以缩小它们之间的差距有多少。
            为了减少操作次数，我们将diff数组降序排列，优先使用数值比较大，
            直到diff中所有数字都被使用完，如果仍然无法满足两者差距为零，则说明无法实现，返回-1。
        """