from bisect import bisect_left
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startArr = []
        dic = dict()
        ans = []
        for i,e in enumerate(intervals):
            startArr.append(e[0])
            dic[e[0]] = i
        startArr.sort()
        for start,end in intervals:
            index = bisect_left(startArr,end)
            if index>=len(startArr):
                ans.append(-1)
            else:
                ans.append(dic[startArr[index]])#
        return ans