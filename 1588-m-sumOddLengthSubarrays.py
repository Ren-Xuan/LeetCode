from typing import List


class Solution:
    def sumOddLengthSubarraysOn(self, arr: List[int]) -> int:
        sum = 0
        n = len(arr)
        for i, v in enumerate(arr):
            leftCount, rightCount = i, n - i - 1
            leftOdd = (leftCount + 1) // 2
            rightOdd = (rightCount + 1) // 2
            leftEven = leftCount // 2 + 1
            rightEven = rightCount // 2 + 1
            sum += v * (leftOdd * rightOdd + leftEven * rightEven)
        return sum
    def sumOddLengthSubarraysOn2(self, arr: List[int]) -> int:
        sum = 0
        n = len(arr)
        prefixSums = [0] * (n + 1)
        for i, v in enumerate(arr):
            prefixSums[i + 1] = prefixSums[i] + v
        for start in range(n):
            length = 1
            while start + length <= n:
                end = start + length - 1
                sum += prefixSums[end + 1] - prefixSums[start]
                length += 2
        return sum

    def sumOddLengthSubarraysOn3(self, arr: List[int]) -> int:
        result = 0
        n = len(arr)
        for k in range(1,n+1,2):
            for i in range(0,n-k+1):
                result+=sum(arr[i:i+k])
        return result
