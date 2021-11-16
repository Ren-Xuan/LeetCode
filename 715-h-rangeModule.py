class RangeModule:

    def __init__(self):
        self.intervals = [] # 维护起点单调增的不相交的区间列表

    def addRange(self, left: int, right: int) -> None:
        self.intervals.append([left, right])
        self.intervals = sorted(self.intervals, key=lambda x : x[0])
        ans = []
        ans.append(self.intervals[0])
        for intv in self.intervals:
            if intv[0] > ans[-1][1]:
                ans.append(intv)
            elif intv[1] > ans[-1][1]:
                ans[-1][1] = intv[1]
        self.intervals = ans

    def queryRange(self, left: int, right: int) -> bool:
        for intv in self.intervals:
            if left >= intv[0] and right <= intv[1]:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        ans = []
        for intv in self.intervals:
            if intv[1] <= left or intv[0] >= right:
                ans.append(intv)
            else:
                inter =  [max(intv[0], left), min(intv[1], right)]
                if inter[0] == intv[0] and inter[1] == intv[1]:
                    pass
                elif inter[0] == intv[0]:
                    ans.append([inter[1], intv[1]])
                elif inter[1] == intv[1]:
                    ans.append([intv[0], inter[0]])
                else:
                    ans.append([intv[0], inter[0]])
                    ans.append([inter[1], intv[1]])
        self.intervals = ans