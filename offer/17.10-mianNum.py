


class Solution:
    def majorityElement(self, nums) -> int:
        m = nums[0]
        cnt = 1
        for e in nums[1:]:
            if e == m:
                cnt+=1
            else:
                cnt-=1
                if cnt<=0:
                    m = e
                    cnt = 0
        
        cnt = 0
        for i in nums:
            if i == m:
                cnt+=1
        if cnt<=len(nums)//2:
            return -1
        return m

        
s = Solution()
print(s.majorityElement([1,2,5,9,5,9,5,5,5]))
print(s.majorityElement([3,2]))
print(s.majorityElement([2,2]))
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2]))
print(s.majorityElement([2,2,1,1,1,2,2]))
print(s.majorityElement([9,8,8]))
print(s.majorityElement([1,2,3]))
print(s.majorityElement([3,3,4]))
print(s.majorityElement([87,78,87,78,87,78,87]))