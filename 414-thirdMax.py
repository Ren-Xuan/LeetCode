class Solution:
    def thirdMax(self, nums) -> int:
        
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        #situation:only contains two types of num
        first = -2147483649
        second = -2147483649
        third = -2147483649
        for e in nums:
            if e > first:
                first = e
        for e in nums:
            if e > second and e < first:
                second = e
        for e in nums:
            if e > third and e < second:
                third = e
        if third == -2147483649:
            return first
        return third



s = Solution()
o = s .thirdMax([1,-2,100,2,3,4,5,6,2,2,1,21])
print(o)
o = s .thirdMax([1141,-2,100,2,3,44,5,6,2,2,221,21])
print(o)
o = s .thirdMax([1,-2,100,2,1])
print(o)
o = s .thirdMax([2,1])
print(o)
o = s .thirdMax([1,2])
print(o)
o = s .thirdMax([3,2,1])
print(o)
o = s .thirdMax([1,2,3])
print(o)
o = s .thirdMax([2,2,3,1])
print(o)
o = s .thirdMax([1,1,2])
print(o)