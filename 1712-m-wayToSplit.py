class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        res,minSecondEndIdx,maxSecondEndIdx=0,0,0
        for i in range(len(nums)-2):
            first=prefix[i+1]
            minSecondEndIdx = max(minSecondEndIdx,i+1)
            while minSecondEndIdx<len(nums)-1 and prefix[minSecondEndIdx+1]-first<first:
                minSecondEndIdx+=1
            if minSecondEndIdx>=len(nums)-1:
                break
            if prefix[minSecondEndIdx+1]-first>prefix[-1]-prefix[minSecondEndIdx+1]:
                continue
            maxSecondEndIdx = max(maxSecondEndIdx,minSecondEndIdx)
            while maxSecondEndIdx+1<len(nums)-1 and \
                prefix[maxSecondEndIdx+2]-first<=prefix[-1]-prefix[maxSecondEndIdx+2]:
                    maxSecondEndIdx+=1
            res+=maxSecondEndIdx-minSecondEndIdx+1
        return res % (10**9+7)
