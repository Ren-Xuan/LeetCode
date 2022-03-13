from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """
        由于题目要求所有的子数组互不重叠，因此对于某个满足条件的子数组，
        如果其右端点是所有满足条件的子数组的右端点中最小的那一个，则该子数组一定会被选择。

        故可以使用贪心算法:从左到右遍历数组，
        一旦发现有某个以当前下标 i 为右端点的子数组和为 target，就给计数器的值加 1，
        并从数组 nums 的下标 i+1开始，进行下一次寻找。

        为了判断是否存在和为 target 的子数组，我们在遍历的过程中记录数组的前缀和，
        并将它们保存在哈希表中。如果位置 i 对应的前缀和为sum_i 
        而 sum_i-target已经存在于哈希表中，就说明找到了一个和为 target 的子数组。

        如果找到了一个符合条件的子数组，则接下来遍历时需要用一个新的哈希表，
        而不是使用原有的哈希表，因为要确保每次找到的子数组都与此前找到的不重合。
        """
        size = len(nums)
        ret = 0
        i = 0
        while i < size:
            s = {0}
            total = 0
            while i < size:
                total += nums[i]
                if total - target in s:
                    ret += 1
                    break
                else:
                    s.add(total)
                    i += 1
            i += 1
        return ret

