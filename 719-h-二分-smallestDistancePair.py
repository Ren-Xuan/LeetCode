from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        对于当前搜索的距离 mid，计算所有距离小于等于 mid 的数对数目 cnt，
        如果 cnt≥k，那么right=mid−1，否则 left=mid+1。
        当 left>right 时，终止搜索，那么第 k 小的数对距离为 left。
        """
        def check(dis):
            cnt = left = 0
            for i, x in enumerate(nums):
                #left = 0如果是这样搜索,由于nums已经是排了序的，而x是从小到大列举，所以left可以不从0开始
                while x - nums[left] > dis: left += 1
                cnt += i - left
            return cnt
        nums.sort()
        i, j = 0, nums[-1] - nums[0]
        while i < j:
            mid = i + j >> 1
            if check(mid) < k: i = mid + 1
            else: j = mid
        return j