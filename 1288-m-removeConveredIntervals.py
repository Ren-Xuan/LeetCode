from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        res = 1
        maxval = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][1] > maxval:
                maxval = intervals[i][1]
                res+=1
        return res
    def removeCoveredIntervals2(self, intervals: List[List[int]]) -> int:
        end = dict()
        for e in intervals:
            if e[0] not in end:
                end[e[0]] = e[1]
            elif e[1]> end[e[0]]:
                end[e[0]] = e[1]
        intervals = [[e,end[e]] for e in end]
        result = []
        intervals.sort(key = lambda x : x[0])
        i = 0
        n = len(intervals)
        while i <n:
            if i+1<n and intervals[i][1]>=intervals[i+1][1]:
                intervals = intervals[:i+1]+intervals[i+2:]
                n-=1
            else:
                i+=1
        return len(intervals)