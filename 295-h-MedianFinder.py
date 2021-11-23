import heapq
class MedianFinder:

    def __init__(self):
        self.left = []#maxheap
        self.right = []#minheap
        """
        维护一对最大最小堆，
        左边最大堆，右边最小堆
        因此两个堆顶就是中位数:
        偶数数组长度时候，两个中位数分别大于左边的那部分，同时小于右边那部分，且左右两边那部分长度相同
        奇数数组长度的时候，一个中位数正好把数组切成两份长度一样的set，且中位数大于左边的每一个元素，小于右边的每一个元素
        """

    def addNum(self, num: int) -> None:
        if len(self.right) == 0 or num>= self.right[0]:
            heapq.heappush(self.right,num)
        elif len(self.left) == 0 or  num<=-self.left[0]:
            heapq.heappush(self.left,-num) 
        else:
            heapq.heappush(self.right,num)
        if len(self.left) == len(self.right) +2:
            heapq.heappush(self.right,-heapq.heappop(self.left))
        elif len(self.left)+2 == len(self.right):
            heapq.heappush(self.left,-heapq.heappop(self.right))
    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0]+self.right[0])/2.0
        elif len(self.left) == len(self.right)+1:
            return -self.left[0]
        elif len(self.left)+1 == len(self.right):
            return self.right[0]
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()