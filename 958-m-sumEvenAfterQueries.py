class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []

        sumEven = 0
        for i in nums:
            if i%2 == 0:
                sumEven+=i

        for i in range(len(nums)):
            if nums[queries[i][1]]% 2 == 0:
                sumEven -= nums[queries[i][1]]
            nums[queries[i][1]]+= queries[i][0]
            if nums[queries[i][1]] % 2 == 0:
                sumEven += nums[queries[i][1]]

            result.append(sumEven)
        return result
    
s = Solution()
print(s.sumEvenAfterQueries([1,2,3,4],[[1,0],[-3,1],[-4,0],[2,3]]))