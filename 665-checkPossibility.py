class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        n = len(nums)
        for i in range(0,n-1):
            if nums[i]>nums[i+1]:
                #find one reverse order pair
                cnt+=1

                if cnt == 2:
                    #more than one reverse order pair
                    return False
                # consider num[i] and nums[i+1]
                #i-1 i i+1 i+2
                # 1 2 1 1 T
                # 1 3 2 1 F
                # 3 5 2 4 F
                # 3 4 2 3 F
                # -1 4 2 3 T
                # when  a <= b <= d == False
                #   and a <= c <= d == False
                # return False
                if i != 0 and i != n-2:
                    if (nums[i-1]<= nums[i] and nums[i] <= nums[i+2]) == False and\
                        (nums[i-1]<= nums[i+1] and nums[i+1] <=nums[i+2]) == False:
                        return False
                
        return True

s = Solution()
a = [1,3,5,2,4]

print(s.checkPossibility(a))
print(s.checkPossibility([4,2,1]))
print(s.checkPossibility([3,4,2,3]))
print(s.checkPossibility([-1,4,2,3]))
print(s.checkPossibility([2,3,3,2,4]))
print(s.checkPossibility([2,3,2,4,5,4]))
print(s.checkPossibility([2,3,4,4,5,4]))
print(s.checkPossibility([1,2,1,1]))

print("-"*10)
print(s.checkPossibility([1,2,1,1]))
print(s.checkPossibility([1,3,2,1]))
print(s.checkPossibility([3,5,2,4]))
print(s.checkPossibility([3,4,2,3]))
print(s.checkPossibility([-1,4,2,3]))
