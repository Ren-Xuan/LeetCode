class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        #从尾部开始构造单调递减栈
        """
        比如当前单调栈为8、6、4
        插入7的时候，pop4、pop6然后变成8、7
        curmin记录为比当前元素小的最大元素6
        这样就满足了32条件
        只要再扫描到小于curmin的就满足了132模式的条件
        """
        _MIN = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < _MIN:
                return True
            while stack and nums[i] > stack[-1]:
                _MIN = stack.pop()
            stack.append(nums[i])
            
        return False