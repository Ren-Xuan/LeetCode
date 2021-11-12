class Solution:
    def numOfSubarrays(self, arr) -> int:
        """
        odd[i]以arr[i]结尾的和为偶数的子数组数目
        even[i]以arr[i]结尾的和为奇数的子数组数目
        """
        even = [0]*len(arr)
        odd = [0]*len(arr)
        if arr[0]%2 ==0:
            odd[0] = 1
        else:
            even[0] = 1
        for i in range(1,len(arr)):
            if arr[i] %2 == 0:
                even[i] += even[i-1]
                odd[i]+=odd[i-1]+1
            else:# arr[i] %2 == 1:
                odd[i] +=  even[i-1]
                even[i]+=odd[i-1]+1
        return sum(even)%(1000000007)
    def numOfSubarrays2(self, arr) -> int:
        MODULO = 10**9 + 7
        odd, even = 0, 1
        subarrays = 0
        total = 0
        
        for x in arr:
            total += x
            subarrays += (odd if total % 2 == 0 else even)
            if total % 2 == 0:
                even += 1
            else:
                odd += 1
        
        return subarrays % MODULO

