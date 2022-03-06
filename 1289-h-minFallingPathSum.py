from typing import List


class Solution:
    def minFallingPathSum1(self, arr: List[List[int]]) -> int:
        for i in range(len(arr) - 2, -1, -1):
            for j in range(len(arr[0])):
                arr[i][j] += min(arr[i + 1][: j] + arr[i + 1][j + 1: ])
        return min(arr[0])

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        first_sum, first_pos, second_sum = 0, -1, 0
        for i in range(n):
            fs, fp, ss = 10**9, -1, 10**9
            for j in range(n):
                cur_sum = (first_sum if first_pos != j else second_sum) + arr[i][j]
                if cur_sum < fs:
                    fs, fp, ss = cur_sum, j, fs
                elif cur_sum < ss:
                    ss = cur_sum
            first_sum, first_pos, second_sum = fs, fp, ss
        return first_sum
