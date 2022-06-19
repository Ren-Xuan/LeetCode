class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        """
        把数放入哈希表set中，去重，遍历set中的每一个数，
        若当前遍历的数减一已经存在set中，则此数开头的序列必不可能最长，
        直接跳过进行下一次遍历，若此数减一不存在set中，
        则进行加一，再次判断是否在set中，直至跳出循环，更新长度
        """
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

