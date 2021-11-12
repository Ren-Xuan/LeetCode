

class binArr:
    def __init__(self,n,reverse = False) -> None:
        cnt = 0
        if n<=0:
            return []
        maxValue = pow(2,n)
        self.result = [0]*maxValue
        for i in range(maxValue):
            arr = [0]*n
            index = n-1
            begin = i
            while begin !=0:
                arr[index]=begin%2
                index-=1
                begin = begin //2
            self.result[i] = arr
        if reverse:
            self.result.reverse()
    def get(self):
        return self.result

    def permuteUnique(self,zero,one):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = [0]*zero+[1]*one
        if not nums:
            return []
        #nums.sort()

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


c = binArr(5,reverse= True)
print(c.get())
print("-"*10)
print(c.permuteUnique(2,3))
print(len(c.permuteUnique(10,8)))
"""
1 1 1 1
0 1 1 1 ,1 0 1 1 , 1 1 0 1 , 1 1 1 1



"""
