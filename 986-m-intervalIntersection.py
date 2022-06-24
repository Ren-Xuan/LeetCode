
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        #归并思想
        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []#暴力
        for AL,AR in firstList:
            for BL,BR in secondList:
                if AL<=BL<=BR<=AR:
                    ans.append([BL,BR])
                elif BL<AL<=AR<=BR:
                    ans.append([AL,AR])
                elif AL<=BL<=AR:#A在B左边并且有交集
                    ans.append([BL,AR])
                elif BL<=AL<=BR:
                    ans.append([AL,BR])
        return ans        
