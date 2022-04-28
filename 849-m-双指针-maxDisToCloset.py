class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 0
        p1 = None
        for p2 in range(len(seats)):
            if seats[p2] == 1:
                if p1 is None:  # 考虑起始为0情况
                    res = max(res,p2)
                else:
                    res = max(res,int((p2-p1)/2))
                p1 = p2  
        if seats[p2] == 0:  # 考虑末尾为0情况
            res = max(res,p2-p1)
        return res