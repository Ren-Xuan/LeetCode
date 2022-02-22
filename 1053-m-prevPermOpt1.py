from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i=next((x for x in range(len(arr)-2,-1,-1) if arr[x]>arr[x+1]),0)
        j=max((x for x in range(i,len(arr)) if arr[x]<arr[i]),key=lambda x:arr[x],default=0)
        arr[i],arr[j]=arr[j],arr[i]
        return arr