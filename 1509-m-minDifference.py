class Solution:
    def minDifference(self, nums) -> int:
        """
        我们可以先将数组排序，然后修改最大或者最小的两端的元素，
        至于应该怎样修改，其实修改和删除是一样的，
        我们可以逆向思维，使用滑动窗口解决，只是窗口比较大，
        是尺寸固定为len(nums)-k的，
        确保窗口外部的左右两端多出来的元素和正好是3，
        其实窗口最右端就是剩余数组的最大值，
        窗口左端就是剩余数组的最小值，
        它们的差就是删除三个离群元素后的最小差，
        我们将窗口从左滑到右，记录下差的最小值。
        注意nums数组长度小于4的特殊情况要直接返回0。
        """
        nums.sort()
        k = 3
        return 0 if len(nums) <= k + 1 else min(nums[i+len(nums)-1-k]-nums[i]for i in range(k+1))