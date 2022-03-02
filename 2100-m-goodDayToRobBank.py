from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return [i for i in range(len(security))]
        left = [False]*len(security)
        right = [False]*len(security)
        k = 0
        for i in range(1,len(security)):
            if security[i-1] >= security[i]:
                k+=1
            else:
                k = 0
            if k >=time:
                left[i] = True
        k = 0
        for i in range(len(security)-2,-1,-1):
            if security[i+1] >= security[i]:
                k+=1
            else:
                k = 0
            if k >=time:
                right[i] = True
        ans = []
        for i in range(time,len(security)-time):
            if left[i] == True and right[i] == True:
                ans.append(i)
        return ans