class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        cnt = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration >= timeSeries[i+1]:
                cnt+=(timeSeries[i+1] - timeSeries[i])
            else:
                cnt+=duration
        cnt+=duration
        return cnt

s = Solution()
print(s.findPoisonedDuration([1,4,9],3))
print(s.findPoisonedDuration([1,2,9],3))
print(s.findPoisonedDuration([1,2,3,4,10],3))