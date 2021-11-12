class Solution:
    def minimumSize2(self, nums: List[int], maxOperations: int) -> int:

        def search(nums,cnt):
            if cnt == 0:
                return max(nums)
            maxVal = nums[0]
            maxIndex = 0
            for i,e in enumerate(nums):
                if e > maxVal:
                    maxIndex = i
                    maxVal = e
            if maxVal == 1:
                return 0
            minCnt = 10**10
            for e in range(1,maxVal):
                k = max(search(nums[:maxIndex]+[e],cnt-1),search([maxVal - e]+nums[maxIndex+1:],cnt-2))
                if minCnt == -1:
                    minCnt = k
                elif minCnt>k:
                    minCnt = k
            return minCnt
    
        return search(nums,maxOperations)
    

    def check(self, nums, x, maxOperations):
        ans=0
        for b in nums:
            if b%x==0:
                ans+=int(b/x)-1
            else:
                ans+=int(b/x)
        return ans<=maxOperations

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l=1
        r=1e9
        while l<=r:
            mid=int((l+r)/2)
            if self.check(nums,mid,maxOperations):
                r=mid-1
            else:
                l=mid+1
        return l
