from typing import List


class Solution:
    def minSumOfLengthsError(self, arr: List[int], target: int) -> int:
        """
        1546. 和为目标值且不重叠的非空子数组的最大数目解法：

        由于题目要求所有的子数组互不重叠，因此对于某个满足条件的子数组，
        如果其右端点是所有满足条件的子数组的右端点中最小的那一个，则该子数组一定会被选择。

        故可以使用贪心算法:从左到右遍历数组，
        一旦发现有某个以当前下标 i 为右端点的子数组和为 target，就给计数器的值加 1，
        并从数组 nums 的下标 i+1开始，进行下一次寻找。

        为了判断是否存在和为 target 的子数组，我们在遍历的过程中记录数组的前缀和，
        并将它们保存在哈希表中。如果位置 i 对应的前缀和为sum_i 
        而 sum_i-target已经存在于哈希表中，就说明找到了一个和为 target 的子数组。

        如果找到了一个符合条件的子数组，则接下来遍历时需要用一个新的哈希表，
        而不是使用原有的哈希表，因为要确保每次找到的子数组都与此前找到的不重合。
        
        但是假如arr = [4,1,1,2,2,1,1] target = 4
        如果继续采用《和为目标值且不重叠的非空子数组的最大数目解法》就只会求出
        [4][1,1,2][2,1,1]但是符合本题的答案是[4]和[2,2]所以那种解法错误
        """
        size = len(arr)
        i = 0
        ans = [10**5,10**5]
        while i < size:
            d = dict()
            d[0] = i
            total = 0
            while i < size:
                total += arr[i]
                if total - target in d:
                    cnt = i - d[total - target] +1
                    if cnt<ans[0]:
                        ans[0] = cnt
                    elif cnt<ans[1]:
                        ans[1] = cnt
                    break
                else:
                    d[total] = i
                    i += 1
            i += 1
        return ans[0]+ans[1] if ans[0]+ans[1]<=10**5 else -1

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        MAX = 10**6
        dp = [MAX] * (n + 1)
        ans = MAX

        l = win = 0
        for r in range(n):
            win += arr[r]
            while win > target:
                win -= arr[l]
                l += 1
            if win == target:
                width = r - l + 1
                ans = min(ans, dp[l] + width)
                dp[r + 1] = min(width, dp[r])
            else:
                dp[r + 1] = dp[r]

        return -1 if ans >len(arr) else ans