from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        def make(array):  # 传入的array是arr从小到大或者从大到小排序后的索引值
            ans = [None] * n
            stack = []
            for i in array:
                while stack and i > stack[-1]:  # 保证stack内的元素是递减的
                    ans[stack.pop()] = i
                stack.append(i)
            return ans
        
        array = sorted(range(n), key = lambda i : arr[i])  # 按arr的值进行排序的索引值数组
        oddnext = make(array)
        array.sort(key = lambda i : -arr[i])
        evennext = make(array)

        odd = [False] * n
        even = [False] * n
        odd[n-1] = even[n-1] = True
        
        for i in range(n-2,-1,-1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i]:
                even[i] = odd[evennext[i]]

        return sum(odd)