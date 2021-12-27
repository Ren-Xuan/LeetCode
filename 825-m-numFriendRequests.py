from typing import List


class Solution:
    def numFriendRequests1(self, ages: List[int]) -> int:
        def binary_search_bigger_than(ages, target):
            left = 0
            right = len(ages)
            while left < right:
                mid = (left + right) // 2
                if ages[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        ages.sort()
        requests = 0
        for age in ages:
            if age > 14:
                lower = 0.5 * age + 7
                upper = age
                requests += binary_search_bigger_than(ages, upper) - binary_search_bigger_than(ages, lower) - 1
        return requests

    def numFriendRequests2(self, ages: List[int]) -> int:
        n = len(ages)
        ages.sort()
        left = right = ans = 0
        for age in ages:
            if age < 15:
                continue
            while ages[left] <= 0.5 * age + 7:
                left += 1
            while right + 1 < n and ages[right + 1] <= age:
                right += 1
            ans += right - left
        return ans
    def numFriendRequests(self, ages: List[int]) -> int:
        """
        桶排序+前缀和
        """
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1
        pre = [0] * 121
        for i in range(1, 121):
            pre[i] = pre[i - 1] + cnt[i]
        
        ans = 0
        for i in range(15, 121):
            if cnt[i] > 0:
                bound = int(i * 0.5 + 8)
                ans += cnt[i] * (pre[i] - pre[bound - 1] - 1)
        return ans


