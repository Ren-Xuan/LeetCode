class Solution(object):

    def findDiagonalOrder(self, nums):
        """
        Over time
        """
        maxRow = len(nums)
        maxCol = -1
        for e in nums:
            if len(e)>maxCol:
                maxCol = len(e)

        def northEast(startRow,startCol,nums,maxRow,maxCol):
            res = []
            while True:
                if startRow<0:
                    return res
                try:
                    if nums[startRow][startCol]:
                        res.append(nums[startRow][startCol])
                except IndexError:

                    pass
                startRow-=1
                startCol+=1
                
        res = []
        for row in range(maxRow):
            res.extend(northEast(row,0,nums,maxRow,maxCol))
        for col in range(1,maxCol):
            res.extend(northEast(maxRow-1,col,nums,maxRow,maxCol))
        return res

    def findDiagonalOrder(self, nums: list) -> list:
        """
        对角线遍历 II
        每一条对角线上的 i + j 的值都是相同的
        """
        num_list = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                num_list.append((i + j, j, nums[i][j]))

        num_list.sort()
        return [i[2] for i in num_list]
s = Solution()
print(s.findDiagonalOrder( [[1,2,3],[4,5,6],[7,8,9]]))
print(s.findDiagonalOrder( [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
print(s.findDiagonalOrder([[1,2,3],[4],[5,6,7,8,9,8,9,9,9,9,9,5],[8],[9,10,11]]))
print(s.findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]]))