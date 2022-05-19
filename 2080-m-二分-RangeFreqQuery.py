class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        #超时
        self.dic = dict()
        for i,e in enumerate(arr):
            if e not in self.dic:
                self.dic[e] = []
            self.dic[e].append(i)
        l = [0]*(len(arr)+1)
        for e in self.dic:
            left = [0]*(len(arr)+1)
            cur = 0
            for i in self.dic[e]:
                left[i] = 1
            for i in range(1,len(left)-1):
                if left[i]==0:
                    left[i] = left[i-1]
                else:
                    left[i] = left[i-1]+1
            self.dic[e] = left
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.dic:
            return 0
        return self.dic[value][right] - self.dic[value][left-1]

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.dic = dict()#dic[val] contains left[index]
        for i,e in enumerate(arr):
            if e not in self.dic:
                self.dic[e] = []
            self.dic[e].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.dic:
            return 0
        return bisect_right(self.dic[value],right) - bisect_left(self.dic[value],left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)