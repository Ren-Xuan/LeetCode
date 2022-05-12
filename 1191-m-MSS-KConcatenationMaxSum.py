class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9+7
        def MSS(arr):#最大连续子数组和
            ans = arr[0]
            curMax = arr[0]
            for i in range(1,len(arr)):
                if curMax>=0:
                    curMax +=arr[i]
                else:
                    curMax = arr[i]
                if curMax>ans:
                    ans = curMax
            return ans if ans >=0 else 0
        if all(e<=0 for e in arr):
            return 0
        elif k == 1:#最大连续子数组和
            return MSS(arr)%MOD
        elif k == 2:#两个最大连续数组相连最大子数组和
            return MSS(arr+arr)%MOD
        else:#三个以上
            tot = sum(arr)
            if tot>0:#和大于0且k>=3，那么出去最最右两个数组，中间的直接乘起来,左右的要特别考虑
                #比如[-1,2],k = 3的时候是[-1,2,-1,2,-1,2]最大的应该是[2,-1,2,-1,2]
                #考虑左边的[-1,2]和最右边的[-1,2]应该取[-1,{2,-1,2}]所以是[left]+[right]相连的最大子数组和+中间数组和*(k-2)
                return (tot*(k-2)+MSS(arr+arr))%MOD
            return MSS(arr+arr+arr)%MOD#超过三个最多就是三个数组相连
