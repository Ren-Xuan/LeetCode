class Solution:
    def maxScoreSightseeingPair(self, A):
        """
        拆分成 values[i]+i 和 values[j]−j 两部分，这样对于统计景点 j 答案的时候，
        由于 values[j]−j 是固定不变的

        """
        res = 0
        pre_max = A[0] + 0 #初始值
        for j in range(1, len(A)):
            res = max(res, pre_max + A[j] - j) #判断能否刷新res
            pre_max = max(pre_max, A[j] + j) #判断能否刷新pre_max， 得到更大的A[i] + i
                
        return res

