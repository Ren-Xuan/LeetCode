from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if all(arr[0] == arr[i] for i in range(len(arr))):
            return 1
        left ,right = 0,1
        ans =2
        while right<len(arr)-1:
            if arr[right-1]<arr[right]>arr[right+1]:
                right+=1
            elif arr[right-1]>arr[right]<arr[right+1]:
                right+=1
            else:
                left = right
                right+=1
            ans = max(ans,right-left+1)
        return ans