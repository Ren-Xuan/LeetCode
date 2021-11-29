from typing import List
from itertools import combinations

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        if k==1:return [arr[0],arr[-1]]
        d={i/j:(i,j) for i,j in combinations(arr,2)}
        return d[sorted(d.keys())[k-1]]