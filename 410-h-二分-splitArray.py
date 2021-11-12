class Solution:
    def splitArray(self, nums, m: int) -> int:
        right = sum(nums)
        left = 0
        def check(nums,m,mid):
            if mid<max(nums):
                return False
            cnt = 1
            cur = mid
            for e in nums:
                #print(cur,e,cnt)
                if cur - e>=0:
                    cur-=e
                else:
                    cnt+=1
                    cur = mid
                    cur -=e
            #print(cnt,m)
            return cnt<=m
        while left < right:
            mid = (right+left)//2
            #print(left,right,mid)
            if check(nums,m,mid):
                right = mid
            else:
                left = mid+1

        return left
   