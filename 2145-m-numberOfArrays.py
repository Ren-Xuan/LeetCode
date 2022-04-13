from itertools import accumulate
import random
from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        pre = list(accumulate([random.randint(1,100)]+differences))
        #第一个元素k放随机数都可以，因为只需要求出假设以k开头的数组中最大值和最小值之间的距离，这个距离就是可以k以后数组可以浮动的大小，结合股票k线图那样理解，就是一个固定趋势的k线图上下平移能平移多少
        return max(0, upper-lower-(max(pre)-min(pre))+1)