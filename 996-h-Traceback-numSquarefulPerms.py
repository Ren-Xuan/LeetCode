class Solution(object):
    def numSquarefulPermsEnum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        def permuteUnique(nums):
            if not nums:
                return []

            nums.sort()

            def _per(nums, beg, end, res):
                if beg == end - 1:
                    res.append(nums[:])  # appen copy

                for i in range(beg, end):
                    if nums[i] not in nums[beg:i]:
                        nums[i], nums[beg] = nums[beg], nums[i]
                        _per(nums, beg + 1, end, res)
                        nums[i], nums[beg] = nums[beg], nums[i]

            res = []
            _per(nums, 0, len(nums), res)
            return res
        import math
        def isValid(a,b):
            n = int(math.sqrt(a+b))
            return (a+b) == n*n
        def isValidArr(arr):
            for i in range(len(arr)-1):
                if not isValid(arr[i],arr[i+1]):
                    return False
            return True
        nums = permuteUnique(nums)
        cnt = 0
        for e in nums:
            if isValidArr(e):
                print(e)
                cnt+=1
        return cnt
    """
                        over time when take [2,2,2,2,2,2,2,2,2]like this
    """
    def numSquarefulPermsWithoutPruning(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        def isValid(a,b):
            n = int(math.sqrt(a+b))
            return (a+b) == n*n
        def isValidArr(arr):
            if len(arr) == 0:
                return True
            for i in range(len(arr)-1):
                if not isValid(arr[i],arr[i+1]):
                    return False
            return True
        result = []
        n = len(nums)
        used = [False]*n
        def generate(path,begin,end,used):
            #print(path,begin,end,isValidArr(path),used)
            if len(path) == n:# begin + 1 == end
                if path in result:
                    return
                if isValidArr(path):
                    result.append(path[:])
                
                return
            
            if isValidArr(path):
                for i in range(0,end):
                    if used[i]:
                        continue
                    if i!=0 and nums[i] == nums[i-1]:
                        continue
                    used[i] = True 
                    generate(path+[nums[i]],begin+1,end,used)
                    used[i] = False

        generate([],0,n,used)
        return len(result)

    def numSquarefulPerms(self, A):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import math
        nums = A
        nums.sort()
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                # 去重
                if i and nums[i]==nums[i-1]:
                    continue
                # 剪枝
                if not tmp or math.sqrt(tmp[-1]+nums[i]) % 1 == 0:
                    backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return len(res)


s = Solution()
print(s.numSquarefulPerms([89,72,71,44,50,72,89,72,71,44,50,72]))
print(s.numSquarefulPerms([65,44,5,11]))
print(s.numSquarefulPerms([1,17,8]))
print(s.numSquarefulPerms([2,2,2,2,2,2,2,2]))