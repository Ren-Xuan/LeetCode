from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        """
        对于一个元素nums[i]来说,移动到socre[k:k>=nums[i]]得一分,score[k:k<nums[i]]不得分
        对于nums[i],当移动k的时候,他的下标是 (i-k+n)%n
        当(i-k+n)%n>=nums[i]时候得一分,然后就等价于k<=(i-nums[i]+n)modn？？？？
        这里就可算出他的得分区间 
        i< nums[i]时候,i+1<=k<=i-nums[i]+n
        i>=nums[i]时候,k>=i+1或者k<=i-nums[i]
        然后就是差分数组，类似于人口统计这种题(给一批出生死亡年份,问什么时候人口最多)
        """

        n = len(nums)
        diffs = [0] * n
        for i, num in enumerate(nums):
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
        score, maxScore, idx = 0, 0, 0
        for i, diff in enumerate(diffs):
            score += diff
            if score > maxScore:
                maxScore, idx = score, i
        return idx


        