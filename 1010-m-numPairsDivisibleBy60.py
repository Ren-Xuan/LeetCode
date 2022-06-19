class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0] * 60
        for t in time:
            arr[t % 60] += 1
        ans = (arr[0] * (arr[0] - 1) + arr[30] * (arr[30] - 1)) // 2
        for i in range(1, 30):
            ans += arr[i] * arr[60 - i]
        return ans