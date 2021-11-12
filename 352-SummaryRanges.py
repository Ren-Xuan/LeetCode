class SummaryRanges:

    def __init__(self):
        #self.arr =[]
        self.result = []
        self.resultSet = set()

    def addNum(self, val: int) -> None:
        if val not in self.resultSet:
            self.insertArr(val)
            self.resultSet.add(val)
            i = 0
            while i < len(self.result) - 1:
                if self.result[i][1] + 1 == self.result[i+1][0]:
                    #Union
                    self.result[i][1] = self.result[i+1][1]
                    self.result.remove([self.result[i+1][0],self.result[i+1][1]])
                    i -= 1
                i+=1
            #print(self.result,"in")


    def getIntervals(self):
#        print(self.result)
        return self.result

    def insertArr(self,val):
        if len(self.result) == 0:
            self.result.append([val,val])
            return
        elif len(self.result) == 1:
            if val < self.result[0][0]:
                self.result.insert(0,[val,val])
            elif val > self.result[0][1]:
                self.result.append([val,val])
            return
        i = 0
        n = len(self.result)
        if val < self.result[i][0]:
            #insert to the head
            self.result.insert(0,[val,val])
            return
        elif val < self.result[i][1] and val > self.result[i][0]:
            return
        else:
            for i in range(1,n):
                if val < self.result[i][1] and val > self.result[i][0]:
                    #the val is aready in result section

                    return
                elif val > self.result[i-1][1] and val < self.result[i][0]:
                    self.result.insert(i,[val,val])
                    return
        #insert to the tail
        self.result.append([val,val])
    
   

obj = SummaryRanges()
obj.addNum(1)
# param_2 = obj.getIntervals()
obj.addNum(2)
obj.addNum(1)
obj.addNum(6)
obj.addNum(4)
obj = SummaryRanges()
print("----"*4)
summaryRanges =SummaryRanges()
summaryRanges.addNum(1)
summaryRanges.getIntervals()
summaryRanges.addNum(3)
summaryRanges.getIntervals()
summaryRanges.addNum(7)
summaryRanges.getIntervals()
summaryRanges.addNum(2)
summaryRanges.getIntervals()
summaryRanges.addNum(6)
summaryRanges.getIntervals()

max([1,2,3])